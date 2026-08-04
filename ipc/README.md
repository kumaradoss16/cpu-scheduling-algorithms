## Program Overview

This program demonstrates **Inter-Process Communication (IPC)** using a **Pipe** in Python's `multiprocessing` module.

There are **three processes** involved:

1. **Main Process** – Creates the pipe, reads user input, and starts the child processes.
2. **Sender Process** – Sends the message through the pipe.
3. **Receiver Process** – Receives the message from the pipe and displays it.

---

# Step 1: Import Required Modules

```python
from multiprocessing import Process, Pipe
```

### Explanation

This line imports two classes from the `multiprocessing` module.

### `Process`

Used to create a new process.

```python
Process(...)
```

A process is an independent program running in its own memory space.

---

### `Pipe`

Used for communication between two processes.

```python
Pipe()
```

It creates two connected communication endpoints.

---

## Step 2: Create the Sender Function

```python
def sender(conn, message):
```

### Explanation

This function is executed by the **Sender Process**.

It has two parameters:

* `conn` → One end of the pipe.
* `message` → The data to send.

---

## Step 3: Send the Message

```python
conn.send(message)
```

### Explanation

The `send()` method sends the message through the pipe.

Example:

```text
Sender Process
      │
      │ send("Hello")
      ▼
=========================
        PIPE
=========================
```

The message is stored inside the pipe until another process receives it.

---

## Step 4: Print Confirmation

```python
print("Sender: Message Sent")
```

Displays:

```text
Sender: Message Sent
```

This confirms that the message has been placed into the pipe.

---

## Step 5: Close the Connection

```python
conn.close()
```

Closes the sender's end of the pipe.

This releases system resources.

---

# Step 6: Create the Receiver Function

```python
def receiver(conn):
```

### Explanation

This function is executed by the **Receiver Process**.

It receives one parameter:

* `conn` → The other end of the pipe.

---

## Step 7: Receive the Message

```python
message = conn.recv()
```

### Explanation

`recv()` waits until a message arrives.

If no message has been sent yet, the receiver waits.

Diagram:

```text
Sender
   │
   │ send("Hello")
   ▼
========================
        Pipe
========================
   ▲
   │ recv()
Receiver
```

After receiving,

```python
message
```

contains:

```text
Hello
```

---

## Step 8: Display the Message

```python
print("Receiver: Message Received")
print("Message:", message)
```

Output

```text
Receiver: Message Received
Message: Hello
```

---

## Step 9: Close the Receiver Connection

```python
conn.close()
```

Closes the receiver's end of the pipe.

---

# Step 10: Main Program

```python
if __name__ == "__main__":
```

### Explanation

This ensures the code inside runs **only when the file is executed directly**.

Without it, Windows may repeatedly create child processes, leading to unexpected behavior or infinite process creation.

---

# Step 11: Create the Pipe

```python
parent_conn, child_conn = Pipe()
```

### Explanation

`Pipe()` creates two connected endpoints.

```text
parent_conn <====================> child_conn
```

Think of it as a telephone.

```text
Phone A <-----------------> Phone B
```

Whatever is sent from one end can be received at the other.

---

## Step 12: Read User Input

```python
message = input("Enter a message: ")
```

### Explanation

The **Main Process** reads the user's message.

Example:

```text
Enter a message: Hello IPC
```

The variable

```python
message
```

stores

```text
Hello IPC
```

---

## Step 13: Create the Sender Process

```python
p1 = Process(target=sender,
             args=(parent_conn, message))
```

### Explanation

Creates a new process.

* **Target function**

```python
sender
```

* **Arguments**

```python
(parent_conn, message)
```

Equivalent to:

```python
sender(parent_conn, message)
```

But it executes in a **new process**.

---

## Step 14: Create the Receiver Process

```python
p2 = Process(target=receiver,
             args=(child_conn,))
```

Creates another process.

Equivalent to

```python
receiver(child_conn)
```

running independently.

---

# Step 15: Start the Sender

```python
p1.start()
```

### Explanation

Starts the Sender Process.

The sender executes:

```python
sender(parent_conn, message)
```

It sends the message into the pipe.

---

# Step 16: Start the Receiver

```python
p2.start()
```

Starts the Receiver Process.

It executes:

```python
receiver(child_conn)
```

The receiver waits for data.

Once data arrives, it prints it.

---

# Step 17: Wait for the Sender

```python
p1.join()
```

### Explanation

The Main Process waits until the Sender Process finishes.

Without `join()`, the main process might exit before the sender completes.

---

# Step 18: Wait for the Receiver

```python
p2.join()
```

The Main Process waits until the Receiver Process finishes.

After both child processes complete, the program exits.

---

# Complete Process Flow

```text
                 Main Process
                      │
                      │
          Read User Input
                      │
                      ▼
             "Hello IPC"
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
 Sender Process              Receiver Process
        │                           ▲
        │ send()                    │ recv()
        ▼                           │
==================== PIPE ====================
        │                           ▲
        └────────── Message ─────────┘
```

---

# Execution Sequence

```text
1. Main Process starts
        │
2. Pipe is created
        │
3. User enters a message
        │
4. Sender Process is created
        │
5. Receiver Process is created
        │
6. Sender starts
        │
7. Sender sends the message
        │
8. Receiver starts
        │
9. Receiver receives the message
        │
10. Sender closes the pipe
        │
11. Receiver closes the pipe
        │
12. Main Process waits using join()
        │
13. Program ends
```

---

# Sample Output

```text
Enter a message: Hello IPC

Sender: Message Sent
Receiver: Message Received
Message: Hello IPC
```

---

# Key Concepts Used

| Concept                      | Explanation                                                                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `Process`                    | Creates a new independent process.                                                                                                            |
| `Pipe()`                     | Creates two connected communication endpoints.                                                                                                |
| `parent_conn`                | One end of the pipe, used by the sender.                                                                                                      |
| `child_conn`                 | The other end of the pipe, used by the receiver.                                                                                              |
| `send()`                     | Sends data through the pipe.                                                                                                                  |
| `recv()`                     | Receives data from the pipe.                                                                                                                  |
| `start()`                    | Starts a child process.                                                                                                                       |
| `join()`                     | Waits for a child process to finish.                                                                                                          |
| `close()`                    | Closes a pipe connection and releases resources.                                                                                              |
| `if __name__ == "__main__":` | Ensures the main code runs only when the script is executed directly, preventing unintended child process creation on platforms like Windows. |
