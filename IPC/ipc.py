import socket
from multiprocessing import Process, Pipe

# Sender Process
def sender(conn, message):
    conn.send(message)  # Send data through the pipe
    print("Sender: Message Sent")
    conn.close()


# Receiver Process
def  receiver(conn):
    message = conn.recv()  # Receive data from the pipe
    
    print("Receiver: Message Received")
    print(f"Message: {message}")
    conn.close()


# Main Program
if __name__ == "__main__":
    # Create two ends of the pipe
    parent_conn, child_conn = Pipe()
    message = input("Enter a message: ")
    # Create Processes
    p1 = Process(target=sender, args=(parent_conn,message))
    p2 = Process(target=receiver, args=(child_conn,))


    # Start Process
    p1.start()
    p2.start()

    # Wait for Completion
    p1.join()
    p2.join()




"""
Output:
Enter a message: Hello IPC
Sender: Message Sent
Receiver: Message Received
Message: Hello IPC
"""

