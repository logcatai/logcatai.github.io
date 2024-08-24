import random
from datetime import datetime, timedelta

def generate_logcat_logs(num_lines=1000):
    log_levels = ['V', 'D', 'I', 'W', 'E']
    tags = [
        'MainActivity', 'NetworkManager', 'DatabaseHelper', 'ServiceManager',
        'NotificationManager', 'UIThread', 'BackgroundTask', 'AuthService',
        'PaymentProcessor', 'LocationService'
    ]
    messages = [
        'onCreate: Activity is being created.',
        'initView: Initializing views.',
        'onResume: Activity is now resumed.',
        'onPause: Activity is being paused.',
        'onError: An unexpected error occurred.',
        'loadData: Loading data from the server.',
        'fetchData: Fetching data from https://example.com/api/data',
        'onResponse: Response received with status code 200.',
        'insertData: Data inserted into the database.',
        'updateUI: UI updated with the latest data.',
        'onLowMemory: System is running low on memory.',
        'onDestroy: Activity is being destroyed.',
        'onStop: Activity has stopped.',
        'startService: Starting background service.',
        'onStartCommand: Service command received.',
        'performTask: Performing background task.',
        'showNotification: Notification displayed to the user.',
        'onError: Network error occurred, retrying request.',
        'onFailure: Failed to connect to server, giving up.',
        'onDestroy: Background service is being destroyed.',
        'onRestart: Activity is being restarted.',
        'authenticateUser: User authentication successful.',
        'processPayment: Payment processed successfully.',
        'updateLocation: User location updated.',
        'syncData: Data synchronization completed.',
        'cacheData: Data cached locally.',
        'handleIntent: Handling intent action.',
        'validateInput: User input validated successfully.',
        'parseResponse: Server response parsed.',
        'connectDatabase: Database connection established.',
        'disconnectDatabase: Database connection closed.',
        'encryptData: Data encryption completed.',
        'decryptData: Data decryption completed.',
        'compressData: Data compression completed.',
        'decompressData: Data decompression completed.',
        'resizeImage: Image resized successfully.',
        'loadImage: Image loaded into view.',
        'animateView: View animation started.',
        'stopAnimation: View animation stopped.',
        'registerReceiver: Broadcast receiver registered.',
        'unregisterReceiver: Broadcast receiver unregistered.'
    ]

    start_time = datetime.now()
    logs = []
    for _ in range(num_lines):
        # Increment time by random milliseconds
        delta = timedelta(milliseconds=random.randint(1, 100))
        start_time += delta
        timestamp = start_time.strftime("%m-%d %H:%M:%S.") + f"{int(start_time.microsecond / 1000):03d}"
        pid = random.randint(1000, 9999)
        tid = random.randint(1000, 9999)
        level = random.choice(log_levels)
        tag = random.choice(tags)
        message = random.choice(messages)
        log_entry = f"{timestamp} {pid:5d} {tid:5d} {level} {tag}: {message}"
        logs.append(log_entry)
    return logs

# Generate the logs
log_entries = generate_logcat_logs(1000)

# Optionally, write to a file
with open('dummy_logcat_logs.txt', 'w') as file:
    for log in log_entries:
        file.write(log + '\n')

# Or print to console (commented out to avoid clutter)
# for log in log_entries:
#     print(log)

