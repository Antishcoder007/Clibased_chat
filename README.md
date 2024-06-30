# clibasedchat

## Overview

`clibasedchat` is a simple command-line interface (CLI) based chat application using UDP sockets. It allows sending and receiving messages along with timestamp information.

## Files

- `sender.py`: Script for sending messages.
- `receiver.py`: Script for receiving messages and displaying the sender's IP address along with the date and time the message was received and also stores data which is receive in a seprated file `Data.txt`.

## Usage

1. Run `receiver.py` to start the receiver:
    ```
    python receiver.py
    ```

2. Run `sender.py` to send messages:
    ```
    python sender.py
    ```

## Requirements

- Python 3.x
