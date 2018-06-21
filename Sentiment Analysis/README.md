#### Sentiment analysis done to classify the text </br>
=======================================
</br>
</br>
In this Project I have implemented and evaluated the naive Bayes algorithm for text classification.  I have 
trained models on a IMDB movie review dataset of positive  and  negative  movie reviews and predicted  accuracy  on a test set.  
The code here in imdb.py reads  the  data  into  a document-term matrix  using scipy’s csr matrix format.
I have worked with log probabilities instead  of multiplying them  directly  to avoid the  possibility  of floating  point underflow.</br>
NaiveBayes.Train  = Train the model</br>
NaiveBayes.PredictLabel = Predicts the label</br>
Alpha values = 0.1, 0.5, 1.0, 5.0. 10.0</br>
</br>
Evaluation metrics :- </br>
ACcuracy</br>
Precision</br>
Recall</br>

NaiveBayes.PredictProb = this piece of code evaluates by precision/recall curves for the data, by adjusting the probability 
threshold for determining whether a review is classified as positive or negative.
</br>
IMPROVEMENT YET TO BE DONE </br>
Planning for an improvement where the 20 most positive and 20 most negative words in the vocabulary can be identified sorted by
their weight according to the model 
