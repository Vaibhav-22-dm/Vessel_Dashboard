from .models import *
from rest_framework.decorators import api_view, authentication_classes, parser_classes
from Vessel_Dashboard.auth import CustomAuthentication
from rest_framework.response import Response
import os
from tensorflow.keras.models import load_model
import pickle

MODEL_FILES_DIR = './Models/model_files/'

@api_view(['POST'])
@authentication_classes([CustomAuthentication])
def predict_trajectory(request):
    try:
        model_path = os.path.abspath(MODEL_FILES_DIR+'trajectory_lstm.h5')
        model = load_model(model_path)

        # Making predictions
        predictions = model.predict(request.data)
        return Response({
            'predictions': predictions
            }, status=200)

    except Exception as e:
        return Response({
            'error':str(e)
        }, status=400)

@api_view(['POST'])
@authentication_classes([CustomAuthentication])
def predict_fuel_consumption(request):
    try:
        values = [
            [
                request.data.get('cylinders'),
                request.data.get('displacement'),
                request.data.get('horsepower'),
                request.data.get('weight'),
                request.data.get('acceleration'), 
                request.data.get('model_year'), 
                request.data.get('origin')
            ]
        ]

        scaler_path = os.path.abspath(MODEL_FILES_DIR+'scaler.pkl')

        sc = None
        with open(scaler_path, 'rb') as f:
            sc = pickle.load(f)

        values = sc.transform(values)

        model_path = os.path.abspath(MODEL_FILES_DIR+'fuel_consumption_model.h5')
        model = load_model(model_path)

        # Making predictions
        predictions = model.predict(request.data)

        return Response({
            'predictions': predictions
            }, status=200)

    except Exception as e:
        return Response({
            'error':str(e)
        }, status=400)

