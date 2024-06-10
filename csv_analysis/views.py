from django.shortcuts import render, redirect, get_object_or_404
from .forms import CSVFileUploadForm
from .models import CSVFile

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def upload_csv(request):
    if request.method == 'POST':
        form = CSVFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            return redirect('csv_analysis:analyse_csv', pk=csv_file.pk)
    else:
        form = CSVFileUploadForm()
    return render(request, 'csv_analysis/upload.html', {'form':form})
    
def analyse_csv(request, pk):
    csv_file = get_object_or_404(CSVFile, pk=pk)
    try:
        data = pd.read_csv(csv_file.file.path)
    except UnicodeDecodeError as e:
        return render(request, 'csv_analysis/error.html', {'message': 'File encoding error. Please upload a valid CSV file.'})
    
    head = data.head().to_html()
    description = data.describe().to_html()
    missing_values = data.isnull().sum().to_frame('missing_values').to_html()

    histograms = []
    plot_dir = os.path.join('media', 'plots')
    os.makedirs(plot_dir, exist_ok=True)

    for column in data.select_dtypes(include=[np.number]).columns:
        plt.figure()
        sns.histplot(data[column].dropna(), kde=True)
        plot_path = os.path.join(plot_dir, f'{column}_histogram.png')
        plt.savefig(plot_path)
        plt.close()
        histograms.append(plot_path)

    context = {
        'head': head,
        'description': description,
        'missing_values': missing_values,
        'histograms': histograms,
    }
    return render(request, 'csv_analysis/results.html', context)