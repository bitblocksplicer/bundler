# Bundler
Bundler is a script written in Python, in order to bundle **codes**.

## The Main Idea
You can simply think like we have a text file with categories containing one or more codes. This is the input file.
We will have 2 output files, one includes the bundles of codes of each category, another one includes the rest of the file that script didn't touch. The main file will never be modified.

## Examples
Let's imagine we have some codes looks like this in a .txt file:
```markdown
Red Gloves: A98FE24N-ZRFZVB65-XPKUJB74-4LWC4HJH-RTVCDAWB
Red Gloves: YTJUK64P-8FVBKWKA-F2S4CECA-HU88F59H-ETTL8BQ4
Red Gloves: 7AD2VRM5-AVL55U89-C77WW5N6-33Z2S59C-W8TMNJFT

Green Pants: NNQ94PKY-U9NQV9SV-A2RWBAFD-WW3PXMD5-QC5M3MT7
Green Pants: F459UM6Y-6RQ5X3GJ-B37DVWME-7UN8XN3Z-8NJ66FKL
Green Pants: AKJRV5MJ-XMFAA8BH-BZC8CN3V-NAH99A6C-U9N9GE65
Green Pants: NCAA3CHG-7LDUQUDY-UY9E28VB-7PTDD976-CJACYTM8

Black Shoes: EWD46ZFU-4JD5VZSU-EG3KXDPM-575S2KWT-GRZMNBK6
Black Shoes: FJWC3L99-LU42AYAC-4LXGFW8Z-UMAEWNWB-CG35L7DC
Black Shoes: KNUW6ACV-PZVQWEQ2-76QK5ZMC-VAMCUUFC-6L8D5VHH
Black Shoes: MXE3AY8N-4QX27Y47-F2LCKR9B-6BM4QK7F-K8K6N8VD
Black Shoes: AWEHXD4W-3Z2EUZAQ-VDAYW62D-H6P2LCC6-8T59M6CS
Black Shoes: DXC8TG5Z-HGJYB4YY-MZBRPS5A-NNLCHMRX-87JEG26V
Black Shoes: PSENP85L-QWTXXYQD-QHP9T5KN-MBXPHJ9B-Q2TQE9ZA
Black Shoes: 8QU23W6P-NQPUYMDN-NHZW28UF-H23YMKG3-KKNDVVLT

Sunglasses: ZEW5M525-CBSDA59D-JB54H446-3DE5AEZD-DCDCC48P
```
We have 3 Gloves, 4 Pants, 8 Shoes and a Sunglasses codes. We want to bundle them, which means to get maximum number of bundles that can be created.
### With Default Settings
If you don't change anything, default settings of the script creates a bundle like this:
```markdown
Red Gloves: A98FE24N-ZRFZVB65-XPKUJB74-4LWC4HJH-RTVCDAWB
Green Pants: NNQ94PKY-U9NQV9SV-A2RWBAFD-WW3PXMD5-QC5M3MT7
Black Shoes: EWD46ZFU-4JD5VZSU-EG3KXDPM-575S2KWT-GRZMNBK6
Sunglasses: ZEW5M525-CBSDA59D-JB54H446-3DE5AEZD-DCDCC48P
```
The script created only 1 bundle because the category with the minimum number of codes was the _sunglasses_ category. Since it contains only one code, only one package can be created by obtaining one code from each category. It saves bundled codes as a .txt file to the script directory. 

The remaining codes which aren't bundled also be saved the same directory, like this:
```markdown
Red Gloves: YTJUK64P-8FVBKWKA-F2S4CECA-HU88F59H-ETTL8BQ4
Red Gloves: 7AD2VRM5-AVL55U89-C77WW5N6-33Z2S59C-W8TMNJFT

Green Pants: F459UM6Y-6RQ5X3GJ-B37DVWME-7UN8XN3Z-8NJ66FKL
Green Pants: AKJRV5MJ-XMFAA8BH-BZC8CN3V-NAH99A6C-U9N9GE65
Green Pants: NCAA3CHG-7LDUQUDY-UY9E28VB-7PTDD976-CJACYTM8

Black Shoes: FJWC3L99-LU42AYAC-4LXGFW8Z-UMAEWNWB-CG35L7DC
Black Shoes: KNUW6ACV-PZVQWEQ2-76QK5ZMC-VAMCUUFC-6L8D5VHH
Black Shoes: MXE3AY8N-4QX27Y47-F2LCKR9B-6BM4QK7F-K8K6N8VD
Black Shoes: AWEHXD4W-3Z2EUZAQ-VDAYW62D-H6P2LCC6-8T59M6CS
Black Shoes: DXC8TG5Z-HGJYB4YY-MZBRPS5A-NNLCHMRX-87JEG26V
Black Shoes: PSENP85L-QWTXXYQD-QHP9T5KN-MBXPHJ9B-Q2TQE9ZA
Black Shoes: 8QU23W6P-NQPUYMDN-NHZW28UF-H23YMKG3-KKNDVVLT
```
—
### With Custom Settings
You can determine how many codes from which category each package will contain.
If you don't want to contain sunglasses category, one each of the red gloves, two each of the green pants and four each of the black shoes, the bundled output file would be:
```markdown
--
Red Gloves: A98FE24N-ZRFZVB65-XPKUJB74-4LWC4HJH-RTVCDAWB
Green Pants: NNQ94PKY-U9NQV9SV-A2RWBAFD-WW3PXMD5-QC5M3MT7
Green Pants: F459UM6Y-6RQ5X3GJ-B37DVWME-7UN8XN3Z-8NJ66FKL
Black Shoes: EWD46ZFU-4JD5VZSU-EG3KXDPM-575S2KWT-GRZMNBK6
Black Shoes: FJWC3L99-LU42AYAC-4LXGFW8Z-UMAEWNWB-CG35L7DC
Black Shoes: KNUW6ACV-PZVQWEQ2-76QK5ZMC-VAMCUUFC-6L8D5VHH
Black Shoes: MXE3AY8N-4QX27Y47-F2LCKR9B-6BM4QK7F-K8K6N8VD

--
Red Gloves: YTJUK64P-8FVBKWKA-F2S4CECA-HU88F59H-ETTL8BQ4
Green Pants: AKJRV5MJ-XMFAA8BH-BZC8CN3V-NAH99A6C-U9N9GE65
Green Pants: NCAA3CHG-7LDUQUDY-UY9E28VB-7PTDD976-CJACYTM8
Black Shoes: AWEHXD4W-3Z2EUZAQ-VDAYW62D-H6P2LCC6-8T59M6CS
Black Shoes: DXC8TG5Z-HGJYB4YY-MZBRPS5A-NNLCHMRX-87JEG26V
Black Shoes: PSENP85L-QWTXXYQD-QHP9T5KN-MBXPHJ9B-Q2TQE9ZA
Black Shoes: 8QU23W6P-NQPUYMDN-NHZW28UF-H23YMKG3-KKNDVVLT

--
```
Unbundled output file:
```markdown
Red Gloves: 7AD2VRM5-AVL55U89-C77WW5N6-33Z2S59C-W8TMNJFT
Sunglasses: ZEW5M525-CBSDA59D-JB54H446-3DE5AEZD-DCDCC48P
```