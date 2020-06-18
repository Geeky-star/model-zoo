#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import gdown

# import tensorflow as tf

class model_from_h5(object):
    
    def __init__(self, url, output = 'model.h5'):
        super().__init__()
        
        self.base_url = 'https://drive.google.com/uc?id='
        self.url_id = self.get_complete_url(url)
        self.output = output
        
    def get_complete_url(self, url):
        split_url = url.split('/')
        return self.base_url + split_url[5]
        
    def download_model(self):
        try:
            gdown.download(self.url_id, self.output, quiet=False)
        except:
            print("Some error occured")
            
    def load_model(self):
        pass
 
    