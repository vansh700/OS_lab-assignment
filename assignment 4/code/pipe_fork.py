import os

# Create pipe
r, w = os.pipe()

# Fork process
pid = os.fork()

if pid > 0:  # Parent process
    os.close(r)
    os.write(w, b"Hello from parent")
    os.close(w)
    os.wait()  # Wait for child to finish

else:  # Child process
    os.close(w)
    message = os.read(r, 1024)
    print("Child received:", message.decode())
    os.close(r)
