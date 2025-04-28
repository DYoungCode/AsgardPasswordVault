The original intention of AsgardPassworVault was to create a password vault that could create, retrieve, rotate, and delete the password.  The primary benefit was working with the Python cryptography library to learn how to encrypt and decrypt data.  While I was successful in implementing the cryptography library, I felt the overall design was missing several peices of functionality.  Rather than try to band-aid the fixes in, I plan to write a version 2 that includes:

- adding the ability to store the username, not just the password
- adding support for multiple usernames and passwords
- a menu system for the user to view what accounts they can retrieve the password for

- optional: add an authentication mechanism to can access to the password vault (this will teach implementation for hashing and salting).
