<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body>
  
  <h1 style="font-size: 36px;">NeuroVisionAI-TumorMapperNet</h1>
  <hr><p>"NeuroVisionAI: TumorMapperNet" is an advanced deep learning model designed for precise detection and segmentation of brain tumors in MRI scans. Leveraging cutting-edge neural vision technology, the model accurately identifies tumor regions, aiding in early diagnosis and treatment planning. Its sophisticated architecture, combining convolutional and recurrent neural networks, ensures high accuracy and efficiency in tumor mapping.
</p>
  <br>
  <h2 style="font-size: 36px;">Network Architecture</h2>
  <hr>
 <p> This Model consists of two parts,first is Classification part and seciond is Segmentation part.</p><br>
  <p><h2 style="font-size: 36px;">Classification Part</h2><hr>
    <img src="https://github.com/jhaayush2004/NeuroVisionAI-TumorMapperNet/blob/main/imagesGit/cp.jpg" alt="Dataset Photo">
    This part comprises of the DenseNet121 architecture with freezed weights.After it, Average Pooling has been implemented followed by Flatten layer.Now ,four other neural Dense layers(256) has been added each with ReLU activation function and Dropout(0.3) between each two of them.Afterwards,"Softmax" activation has been added which gives output telling us whether provided MRI scan is tumor positive! 
  </p><br>
  <p><h2 style="font-size: 36px;">Segmentation Part</h2><hr>
    <img src="https://github.com/jhaayush2004/NeuroVisionAI-TumorMapperNet/blob/main/imagesGit/sp.jpg" alt="Dataset Photo">
    This part of our Network conssists of UNET architecture build using Resblocks.This consists of encoding part and decoding part as well as skip connections which enable the network to retain and transfer low-level features from earlier layers to later layers, aiding in the reconstruction of high-resolution feature maps in the decoding block.Finally a mask is produced as output and then it is overlayed on the input MRI scan image and pixel colors of that masked region are changed.
    <img src="https://github.com/jhaayush2004/NeuroVisionAI-TumorMapperNet/blob/main/imagesGit/fp.jpg" alt="Dataset Photo">
  </p><br>
   <p><h2 style="font-size: 36px;">Loss Functions</h2><hr>
  <ul>
    <li>Classification Part: Categorical Crossentropy</li>
    <li>Segmentation Part: Focal tversky Loss</li>
  </ul>
  </p><br>
  <p><h2 style="font-size: 36px;">Training Pipeline</h2><hr>
  Adam optimizer is used for training both Classification as well as Segmenattion branch.
    <ol>
      <li>We froze the weights for the DenseNet121 branch and trained our classification model branch for 90 epoches and attained val loss of 0.1573.</li>
     <li>we then trained our segmentation branch for 80 epochs by providing it MRI scans and masks as input.validation loss of 0.1644 has been acheived.</li> 
    </ol>
  </p><br>
  <p><h2 style="font-size: 36px;">Predictions</h2>
    <ul>
      <li>Classification Branch: <br>$nbsp<ol><li>1 --> Has Tumor</li>li><li>0 --> No Tumor</li>li></ol></li>
    </ul>
  </p>
  <p><h2 style="font-size: 36px;">Performance</h2>
  <hr>
   Model has Acheived Classification Accuracy of 98.31% and great f1-score.Segmentation accuracy of 91.24% has been acheived.<br>
    <center>Classification Branch</center>
   <img src="https://github.com/jhaayush2004/NeuroVisionAI-TumorMapperNet/blob/main/Visuals/Screenshot%202024-03-24%20204347.png" alt="Dataset Photo">
 <br><img src="https://github.com/jhaayush2004/NeuroVisionAI-TumorMapperNet/blob/main/imagesGit/fs.png" alt="Dataset Photo">
<center>Segmentation Branch</center>
    
  <img src="https://github.com/jhaayush2004/NeuroVisionAI-TumorMapperNet/blob/main/Visuals/Screenshot%202024-03-24%20204328.png" alt="Dataset Photo">
 
  </p>
  <h2 style="font-size: 36px;">Dataset</h2>
  <p>This dataset comprises brain MR images paired with manual FLAIR abnormality segmentation masks. The data is sourced from The Cancer Imaging Archive (TCIA) and involves 110 patients from The Cancer Genome Atlas (TCGA) lower-grade glioma collection. Each patient's data includes a FLAIR sequence and genomic cluster information. The tumor genomic clusters and patient data are provided in the <a href="https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation/download?datasetVersionNumber=2">data.csv file</a>.</p>

  <img src="https://github.com/jhaayush2004/NeuroVisionAI-TumorMapperNet/blob/main/imagesGit/ii.png" alt="Dataset Photo">
 <hr> <br>
 
</body>
</html>
