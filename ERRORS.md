This page is meant to document the errors I've come across while creating a
stack and the fixes for them.

---

- [Key not found](#key-not-found)

---

### Key not found
- Status Reason
  - `The key pair '<keyname>' does not exist`
- Explanation
  - The key referenced in the stack does not exist in the region. This happened to me when I tried to create a working stack in a new region without changing the keyname parameter or importing the existing key.
- Fix (either/or)
  - Generate the public key from the existing private key: `ssh-keygen -f main.pem -y > main.pub`
  - Log into an instance in the region where the key does exist, get the public key from `/home/ec2-user/.ssh/authorized-keys` and import that into the new region.
