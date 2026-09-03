# Internet Speed Test

## Overview

A simple Python utility to measure your internet connection speed using the Speedtest.net service. This tool provides quick and accurate measurements of your download speed, upload speed, and network latency (ping).

## Why You Need This

- **Monitor Connection Performance**: Track your internet speed over time to ensure you're getting the service you're paying for
- **Troubleshoot Connectivity Issues**: Quickly identify if slow performance is due to your network or the service you're using
- **Simple & Reliable**: Uses the official Speedtest.net infrastructure for accurate measurements
- **Programmatic Speed Testing**: Automate speed tests and log results for analysis

## Features

- ✅ Download speed measurement (Mbps)
- ✅ Upload speed measurement (Mbps)
- ✅ Ping latency measurement (ms)
- ✅ Server information display (location, provider)
- ✅ Error handling for network failures
- ✅ Clean formatted output

## Requirements

- Python 3.6+
- `speedtest-cli` library

## Installation

1. **Clone or download this repository**

   ```bash
   git clone https://github.com/pown-i7/Internet-speed-test.git
   cd Internet-speed-test
   ```

2. **Install the required dependency**

   ```bash
   python -m pip install speedtest-cli
   ```

   Or use the requirements file (if available):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the speed test:

```bash
python internet_speed_test.py
```

### Example Output

```
Finding best server...
Testing download speed...
Testing upload speed...

=== Internet Speed Test Results ===
Ping:     15.25 ms
Download: 850.45 Mbps
Upload:   45.32 Mbps
Server:   ISP Provider - City Name, Country
```

## Code Quality

- Comprehensive error handling for network failures
- Detailed docstrings for maintainability
- Graceful failure messages for troubleshooting
- Clean, readable Python code

## Troubleshooting

### ImportError: No module named 'speedtest'

Install the speedtest-cli library:

```bash
python -m pip install speedtest-cli
```

### Connection Error

- Check your internet connection
- Try again in a few moments (Speedtest servers may be temporarily unavailable)
- Ensure your firewall isn't blocking the connection
- Try using a different network connection

## License

MIT License

## Author

pown-i7
