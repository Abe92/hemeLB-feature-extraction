# Feature extraction

The script to perform __manual feature extraction__ of hemeLB file

Note(s):

(1) The program __requires__ the hemeLB text file <br/>
(2) Use __hemeXtract__ to acquires the text file format of the hemeLB output file. <br/>
(3) Visit https://github.com/raar1/hemeXtract to get the __hemeXtract__


# IMPORTANT <br/>

__27th August 2016__ <br/>
The current code for manual feature extraction is not yet completed <br/>
Expected finish date on _6th September 2016_ <br/>

__28th August 2016__ <br/>
The script called __1238073-CLEANING.py__ is used to remove any white-spaces. <br/>
Currently bugged as per __18:37:50 pm BST__ due to some incorrect logic. <br/>
(It would be great if it is usable...)

# UPDATE(s) <br/>

__27th August 2016__ <br/>
The current code (__1238073-MAIN.py__) have been switched to only perform the followings: <br/>
(1) Convert the dimensionless __step__ into __time-step__ with seconds as its unit. <br/>
(2) Perform the calculation of __magnitudes__ from the available __velocities vector__ in the data. <br/>
(3) Create a __new flat file__ containings all of the modifications.

__29th August 2016__ <br/>
The Python script called __1238073-FEATURE_EXTRACTION.py__ main function is to manually extract the <br/>
interesting feature of the difference of velocity between adjacent lattices and use that difference as __filter__. <br/>
Currently in progress on building the __filter__ functionality as per __10.35 am BST__
