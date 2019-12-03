import matplotlib.pyplot as plt

x = []
for i in range(1,41):
    x.append(i)

y5 = []
for i in range(1,41):
    y5.append(5)

iaps_picture_code = [
    2101,    2230,    2830,    6020,
    7520,    7521,    9000,    9001,
    9280,    9440,    1441,    1604,
    1750,    5020,    5300,    5740,
    7006,    7026,    7492,    7530,
    1304,    1726,    2683,    2810,
    2900,    6260,    9630,    9925,
    9930,    9940,    2303,    2346,
    2488,    2489,    2605,    5410,
    7499,    7508,    8380,    8499
]

iaps_pictures = [
    "Man",
    "SadFace",
    "Woman",
    "ElectricChair",
    "Hospital",
    "Hospital",
    "Cemetery",
    "Cemetery",
    "Smoke",
    "Skulls",
    "PolarBears",
    "Butterfly",
    "Bunnies",
    "Flower",
    "Galaxy",
    "Plant",
    "Bowl",
    "PicnicTable",
    "Ferry",
    "House",
    "AttackDog",
    "Tiger",
    "War",
    "Boy",
    "CryingBoy",
    "AimedGun",
    "Bomb",
    "Fire",
    "ShipWave",
    "Explosion",
    "Children",
    "Kids",
    "Musician",
    "Musician",
    "Dance",
    "Violinist",
    "Concert",
    "FerrisWheel",
    "Athletes",
    "Rollercoaster"
]

normative_mean_valence = [
    4.48,    4.67,    5.09,    4.1,
    4.2,     4.37,    2.81,    3.41,
    2.96,    4.42,    7.71,    6.4,
    7.89,    6,       6.83,    5.07,
    4.65,    5.33,    7.27,    6.69,
    3.89,    5.34,    3.32,    4.56,
    2.76,    2.53,    2.96,    3.04,
    3.6,     1.91,    6.51,    7.09,
    5.48,    5.71,    6.04,    5.78,
    6.5,     7,       7.25,    7.51
]

experimental_mean_valence = [
    3.333333333,    3.566666667,    2.7,            2.833333333,
    3.333333333,    3.333333333,    3,              2.966666667,
    2.433333333,    3.466666667,    7.7,            6.333333333,
    6.733333333,    5.833333333,    7.133333333,    4.866666667,
    4.066666667,    5.366666667,    6.9,            7.166666667,
    2.7,            3.366666667,    2.433333333,    3.6,
    2.933333333,    2.933333333,    2.933333333,    2.933333333,
    3.5,            2.6,            6.8,            6.733333333,
    5.366666667,    5.766666667,    5.4,            5.633333333,
    6.866666667,    7.066666667,    7.266666667,    7.333333333
]

plt.plot(iaps_pictures,normative_mean_valence, label="Normative Mean Valence")
plt.plot(iaps_pictures,experimental_mean_valence, label="Experimental Mean Valence")

plt.plot(x,y5,dashes=[6, 2],label="Neutral Valence")

plt.xticks(x,iaps_pictures,rotation="vertical")

plt.xlabel("IAPS Pictures")
plt.ylabel("Mean Valence Ratings")

plt.title("Mean Valence Of IAPS Pictures (Normative Vs Experimental)")

plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)

plt.legend()

plt.show()