# NOTE: Nested Functions


def atm_machine(pin):

    def withdraw(amount):
        print(f"₹{amount} dispensed! ✅")

    if pin == 1234:
        print("PIN correct!")
        withdraw(500)
    else:
        print("Invalid Pin")


atm_machine(1234)
# atm_machine(12345)

# TODO: Closure
