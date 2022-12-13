# This is the automated growth algo
# Each Dendrite will begin under the same precise conditions
# Trait packages will be chosen randomly and combined to create unique crystals
# Each Dendrite will be assigned a combination of trait packages in a random order each lasting for a random duration of time
# packages will be designed to blend

# Start Conditions
# set substrate temp to -12.2ºC
# set the heat exchanger temp to -12ºC
# set the air flow at ~250ccm

# Hexagonal Plate Package (HPP)
# Substrate Temp Lowered to -12.5ºC
# to grow large hexagonal plate substrate Temp must be slowly lowered to -10ºC

#  Branching, Wrinkles, & Spikes Package (BWS)
# Preceeded by HPP
# Temp lowered to -15ºC
# BWS includes a wider range of potential temps and supersats to produces a wide variety of branch structures

# Induced Sidebranching Package (ISP)
# Package combining BWS and HPP
# Induced after BWS
# Lower supersat to produces faceted tip geometry
# quickly increase supersat to induce sidebranching on facets

# Induced Rib Structures Package (IRP)
# Promote ESI with high supersat @ -15ºC
# Reduce supersat to stunt edge expantion
# Increase supersat to restore ESI

# Imports
import random as rand
import matplotlib.pyplot as plt
import numpy as np

# Example Eth Contact Address + Token ID: 0xC7CC3e8C6B69dc272ccf64cbfF4b7503Cbf7C1C5 + 40100010001

# Let's start with converting the Ethereum Token ID to randomized tempurature and supersaturation levels
# Supersaturation should be between 0.15 and 0.30
# Temperature should be between -20 and -10
# The time for making the Dendrite will be between 30 and 50 minutes

# Seed the random number generator from hexadecimal string
def temp_plot(token_id):
    print(token_id)
    rand.seed(token_id)

    rand_steps = rand.randrange(3, 15)
    n_increments = 3600 // rand_steps
    t_list, temp_list = [], np.empty((rand_steps, n_increments))

    print(f"# of steps ==> {rand_steps}")
    for i in range(0, rand_steps):
        t_list.append(round(rand.uniform(-20.0, -10.0), 2))

    for i in range(len(t_list)):
        if i == (len(t_list) - 1):
            temp_list[i] = t_list[i]
            break
        else:
            temp_list[i] = np.linspace(t_list[i], t_list[i + 1], n_increments)

    x = np.arange(rand_steps * n_increments)
    y = np.array(temp_list).flatten()
    print(y)
    plt.plot(x, y, color="blue", alpha=0.3)

    plt.grid(axis="x", color="0.95")
    plt.title("Temperature Graph")
    plt.show()


def air_plot(token_id):
    print(token_id)
    back_portion = token_id[2:]
    back_portion = back_portion[::-1]
    token_id = "0x" + back_portion
    print(token_id)

    rand.seed(token_id)

    rand_steps = rand.randrange(3, 15)
    n_increments = 3600 // rand_steps
    a_list, air_list = [], np.empty((rand_steps, n_increments))

    print(f"# of steps ==> {rand_steps}")
    for i in range(0, rand_steps):
        a_list.append(round(rand.uniform(200.0, 300.0), 2))

    for i in range(len(a_list)):
        if i == (len(a_list) - 1):
            air_list[i] = a_list[i]
            break
        else:
            air_list[i] = np.linspace(a_list[i], a_list[i + 1], n_increments)

    x = np.arange(rand_steps * n_increments)
    y = np.array(air_list).flatten()
    print(y)
    plt.plot(x, y, color="blue", alpha=0.3)

    plt.grid(axis="x", color="0.95")
    plt.title("Air Graph")
    plt.show()

    rand.randrange(200.0, 300.0)

    plt.step(x, y, where="post", label="post")
    plt.plot(x, y, "o--", color="grey", alpha=0.3)

    plt.grid(axis="x", color="0.95")
    plt.legend(title="Parameter where:")
    plt.title("plt.step(where=...)")
    plt.show()


if __name__ == "__main__":
    # Token ID to test with
    token_id = "0xC7CC3e8C6B69dc272ccf64cbfF4b7503Cbf7C1C540100010001"
    # Seed the random number generator
    # temp_plot(token_id)
    air_plot(token_id)
