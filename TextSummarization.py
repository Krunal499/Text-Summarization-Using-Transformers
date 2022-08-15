from transformers import pipeline
import pickle

summarizer = pipeline('summarization')
pickle.dump(summarizer, open('summarize_model.pkl','wb'))
