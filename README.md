# Machine Learning POC

This model is a POC to predict best time to user read a message.

<!-- https://chat.openai.com/share/0720efcc-5095-48ee-836d-5ffba01a2654 -->

## how to run

```sh
make container-debug 
pip install -r requirements.txt 
python main.py 
```

output:

```log
building model
number of readtAt:  146
model built in 0.04669809341430664 seconds
Accuracy: 0.9666666666666667
Best time to send a message at 2024-05-17 14:23 (Fri) is next: 16:00
Best time to send a message at 2024-05-17 10:23 (Fri) is next: 10:00
Best time to send a message at 2024-05-17 15:23 (Fri) is next: 16:00
Best time to send a message at 2024-05-17 01:23 (Fri) is next: 8:00
Best time to send a message at 2024-05-19 14:23 (Sun) is next: 14:00
Best time to send a message at 2024-05-20 14:23 (Mon) is next: 16:00
```
