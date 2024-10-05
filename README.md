# Alt Listener for Nerd Dictation

This script provides a keyboard listener that controls nerd-dictation based on the left Alt key state.

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/dotdevdotdev/alt-listener.git
   ```

2. Move the project to the `/opt` directory:

   ```
   sudo mv alt-listener /opt/
   ```

3. Install the required Python packages:

   ```
   pip install pynput
   ```

4. Copy the service file to the systemd directory:

   ```
   sudo cp /opt/alt-listener/alt-listener.service /etc/systemd/system/
   ```

5. Edit the service file to set your username:

   ```
   sudo nano /etc/systemd/system/alt-listener.service
   ```

   Replace `YOUR_USERNAME` with your actual username.

6. Reload the systemd manager configuration:

   ```
   sudo systemctl daemon-reload
   ```

7. Enable the service to start on boot:

   ```
   sudo systemctl enable alt-listener.service
   ```

8. Start the service:
   ```
   sudo systemctl start alt-listener.service
   ```

## Usage

Once installed and started, the script will run in the background. It will start nerd-dictation when you press the left Alt key and suspend it when you release the key.

## Troubleshooting

- To check the status of the service:

  ```
  sudo systemctl status alt-listener.service
  ```

- To view the logs:
  ```
  journalctl -u alt-listener.service
  ```

## Uninstallation

1. Stop and disable the service:

   ```
   sudo systemctl stop alt-listener.service
   sudo systemctl disable alt-listener.service
   ```

2. Remove the service file:

   ```
   sudo rm /etc/systemd/system/alt-listener.service
   ```

3. Remove the project directory:

   ```
   sudo rm -rf /opt/alt-listener
   ```

4. Reload the systemd manager configuration:
   ```
   sudo systemctl daemon-reload
   ```
