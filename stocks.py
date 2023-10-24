# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bcs = pd.read_csv("BCS_ann.csv")
bp = pd.read_csv("BP_ann.csv")
tsco = pd.read_csv("TSCO_ann.csv")
vod = pd.read_csv("VOD_ann.csv")

plt.figure()

plt.subplot(2, 2, 1)
plt.hist(bcs["ann_return"], label="Barclays")


plt.legend()
plt.ylabel("N")
plt.xlabel("returns (%)")

plt.subplot(2, 2, 2)
plt.hist(bp["ann_return"], label="BP")

plt.legend()
plt.ylabel("N")
plt.xlabel("returns (%)")

plt.subplot(2, 2, 3)
plt.hist(tsco["ann_return"], label="Tesco")

plt.legend()
plt.ylabel("N")
plt.xlabel("returns (%)")


plt.subplot(2, 2, 4)
plt.hist(vod["ann_return"], label="Vodafone")

plt.legend()
plt.ylabel("N")
plt.xlabel("returns (%)")
plt.show()

plt.figure()
plt.hist(tsco["ann_return"], label="Tesco", alpha=0.7, density=True)
plt.hist(vod["ann_return"], label="Vodafone", alpha=0.7, density=True)
plt.show()



plt.boxplot([bcs["ann_return"], bp["ann_return"], tsco["ann_return"],vod["ann_return"]], labels=["Barclays", "BP","Tesco","Vodafone"])


cap = np.array([33367, 68785, 20979, 29741])
stocks = ["Barclays", "BP", "Tesco", "Vodaphone"]

ftse = 1814000
cap = cap/ftse

plt.figure()
plt.pie(cap, labels=stocks, normalize=True)
plt.show()


