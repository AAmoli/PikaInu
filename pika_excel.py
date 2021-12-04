import pandas as pd
import numpy as np


df = pd.DataFrame()
df["Background"] = [np.nan] * 100000
df["Body"] = [np.nan] * 100000
df["Eyes"] = [np.nan] * 100000
df["Clothing"] = [np.nan] * 100000
df["Watch"] = [np.nan] * 100000
df["Necklace"] = [np.nan] * 100000
df["Mouth"] = [np.nan] * 100000
df["Head"] = [np.nan] * 100000


#%%
zahl = 0

for eye in ["Sweet", "Cry Baby", "Stoned", "VR", "Sweet Eye Patch", "Stoned Eye Patch", "3D", "Sunglasses"]:


    for clothing in ["None", "Blue Jacket", "Blue Pants", "Pink Jacket", "Pink Pants", "Grey Jacket", "Grey Pants"]:


        for watch in ["None", "Silver Watch 3", "Silver Watch 9", "Golden Watch 3", "Golden Watch 9"]:

            for kette in ["None", "Silver Necklace USD", "Silver Necklace EUR", "Silver Necklace BTC", "Silver Necklace ETH",
                         "Golden Necklace USD", "Golden Necklace EUR", "Golden Necklace BTC", "Golden Necklace ETH"]:

                for mouth in ["Happy", "Happy Tongue", "Sad", "Cold", "Dirty", "Joint", "Cigarette", "Pipe"]:

                    for head in ["None", "Chinese Hat", "Headband", "Nippon Headband"]:

                        background = ["Turquois", "Pink", "Purple", "Green", "Blue"]
                        background_nummer = np.random.randint(0,5)
                        df.loc[zahl ,"Background"] = background[background_nummer]

                        fuellung = ["Yellow", "Yellow", "Yellow", "Yellow", "Yellow",
                                    "Yellow", "Yellow", "Yellow", "Orange", "Beige"]
                        fuellung_nummer = np.random.randint(0,10)
                        df.loc[zahl ,"Body"] = fuellung[fuellung_nummer]

                        df.loc[zahl ,"Eyes"] = eye

                        df.loc[zahl, "Clothing"] = clothing

                        df.loc[zahl, "Watch"] = watch

                        df.loc[zahl, "Necklace"] = kette

                        df.loc[zahl, "Mouth"] = mouth

                        df.loc[zahl, "Head"] = head

                        zahl = zahl + 1


#%%

df.to_excel("pika.xlsx", index = False)




