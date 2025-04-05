#!/usr/bin/env python
"""
Simple loop demonstration script with proper exit handling and resource management.
"""
import time
import signal
import sys

# Global flag to control the loop
running = True

def signal_handler(sig, frame):
    """Handle keyboard interrupt (Ctrl+C) to gracefully exit the loop."""
    global running
    print('\nExiting loop gracefully...')
    running = False

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def main():
    """Main function to run the loop with proper resource management."""
    print("Starting loop (press Ctrl+C to exit)...")
    
    try:
        counter = 0
        while running:
            print(f'Loop iteration: {counter}')
            counter += 1
            # Sleep to reduce CPU usage
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Loop terminated.")

if __name__ == "__main__":
    main()