# Assignment 3

## <mark> 1) Explain broadcast receiver and their types. </mark>

### **Broadcast Receiver in Android**

A **Broadcast Receiver** is a component in Android that **listens for system-wide or custom broadcast messages**. These messages can be sent by the **system** (e.g., battery low, network change) or by **applications** (e.g., custom event notifications).

### **Types of Broadcast Receivers in Android**

1. **System Broadcast Receivers** – Receive **predefined system broadcasts** (e.g., battery low, boot completed).
2. **Custom Broadcast Receivers** – Apps send and receive **their own broadcasts** for internal communication.

### **1. System Broadcast Receivers**

These are sent by Android when certain **system events** occur.

| Event                | Intent Action                           |
| -------------------- | --------------------------------------- |
| Battery Low          | `Intent.ACTION_BATTERY_LOW`             |
| Boot Completed       | `Intent.ACTION_BOOT_COMPLETED`          |
| Airplane Mode Change | `Intent.ACTION_AIRPLANE_MODE_CHANGED`   |
| Wi-Fi State Change   | `WifiManager.WIFI_STATE_CHANGED_ACTION` |

#### **Example: Listening for Battery Low**

##### **1. Create a Broadcast Receiver (`BatteryReceiver.java`)**

```java
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class BatteryReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Toast.makeText(context, "Battery is low!", Toast.LENGTH_LONG).show();
    }
}
```

##### **2. Register the Receiver in `AndroidManifest.xml`**

```xml
<receiver android:name=".BatteryReceiver">
    <intent-filter>
        <action android:name="android.intent.action.BATTERY_LOW"/>
    </intent-filter>
</receiver>
```

### **2. Custom Broadcast Receivers**

Apps can **send and receive** their own broadcasts.

#### **Example: Sending and Receiving a Custom Broadcast**

##### **1. Create a Custom Receiver (`MyReceiver.java`)**

```java
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class MyReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Toast.makeText(context, "Custom Broadcast Received!", Toast.LENGTH_SHORT).show();
    }
}
```

##### **2. Register the Receiver in `AndroidManifest.xml`**

```xml
<receiver android:name=".MyReceiver">
    <intent-filter>
        <action android:name="com.example.CUSTOM_BROADCAST"/>
    </intent-filter>
</receiver>
```

##### **3. Send a Custom Broadcast from an Activity**

```java
Intent intent = new Intent("com.example.CUSTOM_BROADCAST");
sendBroadcast(intent);
```

### **Types of Broadcasts Based on Execution**

| Type                                                     | Description                                                                                      |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Ordered Broadcast**                                    | Delivered **one receiver at a time**, allowing modification before passing to the next receiver. |
| **Normal Broadcast**                                     | Delivered to **all receivers at once**, without modification.                                    |
| **Sticky Broadcast** _(Deprecated)_                      | Persists even after broadcast is received, useful for system updates.                            |
| **Local Broadcast** _(Replaced by LiveData or EventBus)_ | Broadcasts within an app only for efficiency.                                                    |

### **Use Cases of Broadcast Receivers**

✔ **Battery & Network Status Updates**  
✔ **Push Notifications**  
✔ **Alarm & Reminders**  
✔ **Custom Event Handling Between Components**

### **Conclusion**

Broadcast Receivers **allow apps to listen for system and custom events**, improving communication between components. They can be **statically registered in the manifest** or **dynamically registered in Java** for better control.

## <mark> 2) Explain services with their types. </mark>

### **Services in Android**

A **Service** in Android is a **background component** that performs **long-running operations** without needing a **user interface (UI)**. It allows tasks like **playing music, fetching data, or handling network requests** to run in the background.

### **Types of Services in Android**

Android provides **three main types of services** based on how they operate:

1. **Foreground Service** – Runs in the background **with a visible notification**.
2. **Background Service** – Runs in the background **without user interaction**.
3. **Bound Service** – Allows **components (Activities, Fragments, etc.)** to bind and interact with it.

### **Diagram: Service Lifecycle in Android**

```
              ┌───────────────────┐
              |    onCreate()      | → Service is created
              └───────────────────┘
                      ↓
              ┌───────────────────┐
              | onStartCommand()   | → Service starts running
              └───────────────────┘
                      ↓
        ┌──────────────────────────┐
        | Service is Running       |
        | (Foreground/Background)  |
        └──────────────────────────┘
                      ↓
              ┌───────────────────┐
              |    onDestroy()     | → Service stops
              └───────────────────┘
```

### **1. Foreground Service**

✔ Runs **in the background** but remains **visible** via a **persistent notification**.  
✔ Used for **music players, tracking apps, or ongoing processes**.  
✔ Requires **startForeground()** method.

#### **Example: Foreground Service with Notification**

```java
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.Service;
import android.content.Intent;
import android.os.Build;
import android.os.IBinder;
import androidx.core.app.NotificationCompat;

public class MyForegroundService extends Service {
    private static final String CHANNEL_ID = "ForegroundServiceChannel";

    @Override
    public void onCreate() {
        super.onCreate();
        createNotificationChannel();
        Notification notification = new NotificationCompat.Builder(this, CHANNEL_ID)
                .setContentTitle("Foreground Service")
                .setContentText("Running in the background")
                .setSmallIcon(R.drawable.ic_launcher_foreground)
                .build();
        startForeground(1, notification);
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        return START_STICKY;
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    private void createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(
                    CHANNEL_ID, "Foreground Service", NotificationManager.IMPORTANCE_LOW);
            NotificationManager manager = getSystemService(NotificationManager.class);
            manager.createNotificationChannel(channel);
        }
    }
}
```

✅ **Use Cases:** Music players, GPS tracking, file downloads.

### **2. Background Service**

✔ Runs in the background **without user interaction**.  
✔ Used for **short-term tasks** like **syncing data, sending notifications**.  
✔ Can be stopped by the system if **low on memory**.

#### **Example: Background Service**

```java
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.widget.Toast;

public class MyBackgroundService extends Service {
    @Override
    public void onCreate() {
        super.onCreate();
        Toast.makeText(this, "Background Service Started", Toast.LENGTH_SHORT).show();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        new Thread(() -> {
            // Perform background task here
        }).start();
        return START_STICKY;
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
```

✅ **Use Cases:** Syncing data, handling notifications, background computations.

### **3. Bound Service**

✔ Runs **only while components are bound** to it.  
✔ Allows **Activities, Fragments, or other components** to interact with it.  
✔ Uses **onBind()** method to return an **IBinder** for communication.

#### **Example: Bound Service**

```java
import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;

public class MyBoundService extends Service {
    private final IBinder binder = new LocalBinder();

    public class LocalBinder extends Binder {
        public MyBoundService getService() {
            return MyBoundService.this;
        }
    }

    @Override
    public IBinder onBind(Intent intent) {
        return binder;
    }

    public String getMessage() {
        return "Hello from Bound Service!";
    }
}
```

#### **Binding the Service in an Activity**

```java
MyBoundService myService;
boolean isBound = false;

private ServiceConnection connection = new ServiceConnection() {
    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
        MyBoundService.LocalBinder binder = (MyBoundService.LocalBinder) service;
        myService = binder.getService();
        isBound = true;
    }

    @Override
    public void onServiceDisconnected(ComponentName name) {
        isBound = false;
    }
};

// Bind the service
Intent intent = new Intent(this, MyBoundService.class);
bindService(intent, connection, Context.BIND_AUTO_CREATE);
```

✅ **Use Cases:** Streaming apps, live data fetching, inter-process communication.

### **Comparison of Android Services**

| Feature                       | Foreground Service         | Background Service           | Bound Service                  |
| ----------------------------- | -------------------------- | ---------------------------- | ------------------------------ |
| **Runs in Background**        | ✅ Yes                     | ✅ Yes                       | ✅ Yes                         |
| **User Interaction Needed?**  | ❌ No                      | ❌ No                        | ✅ Yes                         |
| **Requires Notification?**    | ✅ Yes                     | ❌ No                        | ❌ No                          |
| **Can Be Stopped by System?** | ❌ No                      | ✅ Yes                       | ✅ Yes (if all clients unbind) |
| **Example Use Cases**         | Music Player, GPS Tracking | Data Syncing, File Uploading | Live Chat, Streaming           |

### **Conclusion**

✔ **Foreground Service** – Runs **continuously** with a **notification** (e.g., **music player, tracking**).  
✔ **Background Service** – Runs in the background **without UI**, suitable for **short tasks** (e.g., **syncing, notifications**).  
✔ **Bound Service** – Allows **components to bind** to it and interact **(e.g., fetching live data)**.

Each service type is essential for **different app functionalities**, ensuring **efficient background processing**.

## <mark> 3) Explain alarm manager with the example of broadcast receiver. </mark>

### **AlarmManager in Android with BroadcastReceiver Example**

**AlarmManager** is a system service in Android that **schedules tasks** to run at a specified time, even if the app is **closed or the device is restarted**. It is commonly used for **reminders, notifications, and periodic background tasks**.

### **Steps to Implement AlarmManager with BroadcastReceiver**

To trigger an **alarm event** at a specific time, we use:

1. **AlarmManager** – Schedules the alarm.
2. **PendingIntent** – Specifies the action (e.g., sending a broadcast).
3. **BroadcastReceiver** – Receives the alarm trigger and performs an action (e.g., showing a notification).

### **1. Set an Alarm Using AlarmManager (`MainActivity.java`)**

```java
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import java.util.Calendar;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button setAlarmButton = findViewById(R.id.setAlarmButton);
        setAlarmButton.setOnClickListener(v -> setAlarm());
    }

    private void setAlarm() {
        // Get AlarmManager instance
        AlarmManager alarmManager = (AlarmManager) getSystemService(Context.ALARM_SERVICE);

        // Intent to trigger the BroadcastReceiver
        Intent intent = new Intent(this, AlarmReceiver.class);
        PendingIntent pendingIntent = PendingIntent.getBroadcast(this, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);

        // Set the alarm time (5 seconds from now)
        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.SECOND, 5);

        // Schedule an exact alarm
        alarmManager.setExact(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
    }
}
```

### **2. Create a Broadcast Receiver (`AlarmReceiver.java`)**

```java
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class AlarmReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Toast.makeText(context, "Alarm Triggered!", Toast.LENGTH_LONG).show();
    }
}
```

### **3. Register the Receiver in `AndroidManifest.xml`**

```xml
<receiver android:name=".AlarmReceiver"/>
```

### **4. Running the App**

- Click the **"Set Alarm"** button.
- After **5 seconds**, the **AlarmReceiver** receives the broadcast and **shows a Toast message**.

### **Using AlarmManager for Repeating Alarms**

To **repeat the alarm every 10 minutes**, modify `setExact()` to `setRepeating()`:

```java
alarmManager.setRepeating(
    AlarmManager.RTC_WAKEUP,
    calendar.getTimeInMillis(),
    AlarmManager.INTERVAL_FIFTEEN_MINUTES / 1.5, // 10 minutes
    pendingIntent
);
```

### **Canceling an Alarm**

To cancel an alarm:

```java
alarmManager.cancel(pendingIntent);
```

### **Use Cases of AlarmManager with BroadcastReceiver**

✔ **Reminders and Notifications** (e.g., medication alerts).  
✔ **Periodic Background Tasks** (e.g., syncing data, checking updates).  
✔ **Task Scheduling** (e.g., alarms, scheduled reports).

### **Conclusion**

AlarmManager is a powerful tool for **scheduling background tasks**. When combined with a **BroadcastReceiver**, it allows apps to perform **timed operations even when the app is closed**, making it useful for **reminders, notifications, and periodic updates**.

## <mark> 4) Explain internal storage in Android with example. </mark>

### **Internal Storage in Android**

**Internal Storage** in Android is a **private storage space** allocated for an app, where files are stored within the device's internal memory. Data saved here is **only accessible to the app itself** and is **deleted when the app is uninstalled**.

### **Features of Internal Storage**

✔ **Private Storage** – Other apps cannot access the stored files.  
✔ **Automatically Deleted** – Files are removed when the app is uninstalled.  
✔ **No Permissions Required** – Unlike external storage, **no special permission is needed**.  
✔ **Secure and Fast** – Stored files are **sandboxed** and cannot be accessed by other apps.

### **Example: Writing and Reading a File in Internal Storage**

#### **1. Write Data to Internal Storage (`MainActivity.java`)**

```java
import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.io.FileOutputStream;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {
    private static final String FILE_NAME = "myfile.txt";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText editText = findViewById(R.id.editText);
        Button saveButton = findViewById(R.id.saveButton);

        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String text = editText.getText().toString();
                try (FileOutputStream fos = openFileOutput(FILE_NAME, Context.MODE_PRIVATE)) {
                    fos.write(text.getBytes());
                    Toast.makeText(MainActivity.this, "File Saved!", Toast.LENGTH_SHORT).show();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
    }
}
```

#### **2. Read Data from Internal Storage (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import java.io.FileInputStream;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {
    private static final String FILE_NAME = "myfile.txt";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView textView = findViewById(R.id.textView);
        Button loadButton = findViewById(R.id.loadButton);

        loadButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try (FileInputStream fis = openFileInput(FILE_NAME)) {
                    int size;
                    StringBuilder stringBuilder = new StringBuilder();
                    while ((size = fis.read()) != -1) {
                        stringBuilder.append((char) size);
                    }
                    textView.setText(stringBuilder.toString());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
    }
}
```

### **File Storage Location in Internal Storage**

Files are stored in:  
📂 **`/data/data/com.example.myapp/files/myfile.txt`**  
(Apps cannot access each other’s storage due to Android's **sandboxing**.)

### **Deleting a File from Internal Storage**

```java
boolean deleted = deleteFile("myfile.txt");
if (deleted) {
    Toast.makeText(this, "File Deleted!", Toast.LENGTH_SHORT).show();
}
```

### **Use Cases of Internal Storage**

✔ **Saving User Preferences** (e.g., settings, user profile data).  
✔ **Storing Application Data** (e.g., cache files, logs).  
✔ **Keeping Private Files** (e.g., authentication tokens).

### **Comparison: Internal Storage vs. External Storage**

| Feature                  | Internal Storage                    | External Storage                 |
| ------------------------ | ----------------------------------- | -------------------------------- |
| **Access Level**         | Private to the app                  | Accessible by other apps         |
| **Permission Required?** | No                                  | Yes (`WRITE_EXTERNAL_STORAGE`)   |
| **Data Deletion**        | Deleted when the app is uninstalled | Persists even after uninstalling |
| **Security**             | High (sandboxed)                    | Lower (other apps can access)    |

### **Conclusion**

Internal Storage in Android provides **a secure and private way to store app-specific files**. It is useful for **storing personal user data, settings, and cache files**. Unlike external storage, **it does not require permissions and is automatically deleted when the app is uninstalled**.

## <mark> 5) Explain SQLite Database with example. </mark>

### **SQLite Database in Android**

**SQLite** is a lightweight, embedded **relational database** used in Android for **storing structured data locally**. It does not require a separate server and provides efficient storage for **offline applications**.

### **Features of SQLite in Android**

✔ **Lightweight & Embedded** – No external setup needed.  
✔ **Uses SQL Queries** – Supports **CRUD operations** (`Create, Read, Update, Delete`).  
✔ **Local Storage** – Stores data in a **single file** on the device.  
✔ **Efficient & Fast** – Ideal for **small to medium-sized applications**.

### **Steps to Implement SQLite Database in Android**

#### **1. Create a Database Helper Class (`DatabaseHelper.java`)**

```java
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "students.db";
    private static final int DATABASE_VERSION = 1;

    private static final String CREATE_TABLE =
            "CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(CREATE_TABLE); // Create students table
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS students");
        onCreate(db);
    }
}
```

#### **2. Insert Data into SQLite (`MainActivity.java`)**

```java
import android.content.ContentValues;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        DatabaseHelper dbHelper = new DatabaseHelper(this);
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        ContentValues values = new ContentValues();
        values.put("name", "John Doe");
        values.put("age", 25);

        long result = db.insert("students", null, values);
        db.close();

        if (result != -1) {
            Toast.makeText(this, "Data Inserted Successfully!", Toast.LENGTH_SHORT).show();
        }
    }
}
```

#### **3. Retrieve Data from SQLite (`MainActivity.java`)**

```java
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        DatabaseHelper dbHelper = new DatabaseHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        Cursor cursor = db.rawQuery("SELECT * FROM students", null);

        if (cursor.moveToFirst()) {
            do {
                String name = cursor.getString(cursor.getColumnIndex("name"));
                int age = cursor.getInt(cursor.getColumnIndex("age"));

                Toast.makeText(this, "Name: " + name + ", Age: " + age, Toast.LENGTH_SHORT).show();
            } while (cursor.moveToNext());
        }

        cursor.close();
        db.close();
    }
}
```

#### **4. Update Data in SQLite (`MainActivity.java`)**

```java
SQLiteDatabase db = new DatabaseHelper(this).getWritableDatabase();
ContentValues values = new ContentValues();
values.put("age", 30);

int rowsAffected = db.update("students", values, "name=?", new String[]{"John Doe"});
db.close();

if (rowsAffected > 0) {
    Toast.makeText(this, "Data Updated Successfully!", Toast.LENGTH_SHORT).show();
}
```

#### **5. Delete Data from SQLite (`MainActivity.java`)**

```java
SQLiteDatabase db = new DatabaseHelper(this).getWritableDatabase();
int rowsDeleted = db.delete("students", "name=?", new String[]{"John Doe"});
db.close();

if (rowsDeleted > 0) {
    Toast.makeText(this, "Data Deleted Successfully!", Toast.LENGTH_SHORT).show();
}
```

### **Use Cases of SQLite**

✔ **Offline Applications** – Stores data locally without internet.  
✔ **User Data Storage** – Saves **preferences, settings, and history**.  
✔ **Small to Medium Databases** – Efficient for **mobile apps**.

### **Conclusion**

SQLite in Android provides **a powerful, local database** for storing structured data. It supports **CRUD operations** and is widely used for **offline applications, user data storage, and local caching**.
