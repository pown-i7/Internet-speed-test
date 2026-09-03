"""khoya ah code swlni 3elih ama README la ghir nsa dkchi krbo ghir AI 3etit lih code oglt lih i9ad liya README code mchi chihaja ghir tyhsb liya sor3a deyl wifi li3ndk fach ghadi thtaj code m3erftch ml9it mydar o ana nktb had code """

import sys

try:
    import speedtest
except ImportError:
    print("The speedtest-cli library is required. Install it with: python -m pip install speedtest-cli")
    sys.exit(1)


def run_speed_test():
    """Execute an internet speed test and display results.
    
    Performs a speed test by:
    1. Connecting to the best available Speedtest.net server
    2. Measuring download speed
    3. Measuring upload speed
    4. Recording ping latency
    
    Handles network errors gracefully with informative error messages.
    Results are printed to stdout in a formatted table.
    
    Raises:
        No exceptions are raised; errors are caught and printed instead.
    """
    try:
        st = speedtest.Speedtest()
    except speedtest.ConfigRetrievalError as exc:
        print("Failed to connect to Speedtest servers.")
        print("This usually means the service blocked the request or your network is preventing access.")
        print("Try upgrading speedtest-cli or using a different internet connection.")
        print("Error:", exc)
        return
    except Exception as exc:
        print("An unexpected error occurred while initializing the speed test:")
        print(exc)
        return

    print("Finding best server...")
    st.get_best_server()

    print("Testing download speed...")
    download_bps = st.download()
    print("Testing upload speed...")
    upload_bps = st.upload()

    ping_ms = st.results.ping

    download_mbps = download_bps / 1_000_000
    upload_mbps = upload_bps / 1_000_000

    print("\n=== Internet Speed Test Results ===")
    print(f"Ping:     {ping_ms:.2f} ms")
    print(f"Download: {download_mbps:.2f} Mbps")
    print(f"Upload:   {upload_mbps:.2f} Mbps")
    print(f"Server:   {st.results.server['sponsor']} - {st.results.server['name']}, {st.results.server['country']}")


if __name__ == "__main__":
    run_speed_test()
