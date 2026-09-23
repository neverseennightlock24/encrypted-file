# encrypted-file
Demo of exporting sensitive data into an external unreadable file.

Demo uses race time score placements, but can be replaced with essentially anything. Note, that this information is not actually completely encrypted, a more precise term would be serialized and can be decrypted by external users if they so desire and dedicate time to doing so.

Also note that the file is saved with Python's `pickle` module, and loading a pickle file can run arbitrary code. Only load `.dat` files that you created yourself, never ones from an untrusted source.
