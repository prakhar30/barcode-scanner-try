from mcr12_serial import BarcodeScanner


if __name__ == '__main__':
    while True:
        bcd = BarcodeScanner("/dev/tty.PhilipsBT50-SerialPort", baudrate=9600)

        barcode1 = bcd.scan()  # Same as bcd.scan(0)
    # The scanner will start scanning indefinitely until a barcode is
    # scanned.

        barcode2 = bcd.scan(5000)
    # The scanner will start scanning. If after 5000 milliseconds no
    # barcode has been scanned, a TimeoutError is raised.

#    bcd.stop()
    # Stop scanning. Not really useful here as the scanner stops scanning
    # automatically after a barcode has been scanned or after the timeout
    # has expired. However it may be useful if you call the scan() method
    # asynchronously or if you need to handle a KeyboardInterrupt to stop
    # scanning after calling the scan() method.

 #   bcd.config("013300")
    # Edit the scanner configuration. "013300" must be replaced with a
    # configuration code.
