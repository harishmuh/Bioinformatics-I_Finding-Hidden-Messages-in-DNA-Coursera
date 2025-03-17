# Week 5: Bioinformatics Application Challenge

### The instructions of the test challenge can be seen as below:

Mycobacterium tuberculosis (MTB) can persist in a latent state in humans for many years before causing disease. Latency has been found to be linked to hypoxia (lack  of oxygen) in the host. You suspect that genes that are activated in  hypoxia are regulated by a common transcription factor, so you collect  the upstream sequences for all of the MTB genes that are upregulated in  hypoxia, looking for the motif that corresponds to the binding site for  the transcription factor regulating these genes. Your biologist  colleague tells you that you should look at the 250 bp upstream region  of each gene (which have been conveniently compiled for you in a 
FASTA, file named upstream250.txt. Your colleague also tells you that the motif is probably about 20 bp long.

We will first work with [MEME](https://meme-suite.org/meme/tools/meme) (Bailey and Elkan, 1994). Upload upstream250.txt, and tell MEME to find 1 motif instead of 3. Then click on advanced options and change the minimum width to 20 and the maximum width to 20. After submitting the process, click on "MEME html output". Notice that the motif logo has been generated under "Discovered Motifs". Click the down arrow under "more" to see the starting positions of motifs. To download the motif logo, click the right arrow above the logo, navigate to the "Download-logo" tab, and click "Download".
If the queue on the MEME server is too long, you can use alternate instance. 

![MEME interface](https://github.com/harishmuh/Bioinformatics-I_Finding-Hidden-Messages-in-DNA-Coursera/blob/main/exam/MEME%20find%20motifs.PNG?raw=true)

* **Indicate the starting positions of the substrings of length 20 identified by MEME**
Answer: 57 139 107 172 114 136 159 143 155 186 178 200 118 137 173 201 160 62 216 165 45 204

In order to visualize the information contained in these sequences, we will copy them into [WebLogo](http://weblogo.threeplusone.com) to generate a motif logo.

* **Upload the image file obtained after generating this motif logo (with default parameters)**

![Motif default](https://github.com/harishmuh/Bioinformatics-I_Finding-Hidden-Messages-in-DNA-Coursera/blob/main/exam/Motif_AGGGSCGWARGTCCYCAABB_upstream25.png?raw=true)

Although your biologist colleague told you that the motif is probably about 20 bp long, you are skeptical, so you decide to run a motif finding program that finds a motif over a wide range of different lengths.
Run [MEME](https://meme-suite.org/meme/tools/meme) again on upstream250.txt, but this time, use the default parameters for minimum width (6) and maximum width (50). Note: this process may take a few minutes to run.

* **(a) How long is the motif produced by MEME?**

Answer: The motif has length 20.

* **(b) Is the motif logo produced by MEME similar to the one produced before for a motif of length 20?**

Answer: This motif is the same as the previous motif, except that it has been shifted over by a single letter.

* **When using motif software with fixed motif lengths, is it better to start with short motifs or long motifs? Why?**

Answer: Its better to start with shorter motifs. There are few reasons that consist :
  * Shorter motifs reduce search space as searching for long motifs increase the combinatorial complexity that maks harder to find statistically significant patterns
  * Shorter motifs are more likely to appear in multiple sequences. Starts with long motif may be too specific and fail to match across differenet sequences due to natural variations
  * Easier to extend short motifs than to trim long ones. If you start too, you may include unnecessary regions that do not contribute to motif function


To evaluate the statistical significance of an identified motif, we need to ensure that a motif with the same or even larger score is unlikely to occur in a collection of "typical" DNA strings (of the same length).

* **How would you generate these strings? Justify your answer**

Answer: I believe we can generate random DNA strings with uniform nucleotide distribution. The method can be explained as Generate sequences where each nucleotide (A, C, G, T) is chosen randomly and independently with equal probability (25% each).

The justification:
  * The method serves as a baseline model assuming no sequence bias.
  * It Helps determine whether the motif score is significantly higher than what would occur by chance.
  * However, real DNA sequences often do not have equal nucleotide frequencies, making this method too simplistic.

We have begun to confirm our colleague's suspicion that we should consider motifs of length about 20. However, thus far, we have only analyzed the 250 bp regions upstream of each gene. This makes us wonder whether we will identify the same motif for upstream regions of different lengths. First, we will consider upstream regions of length 25 bp (upstream25.txt).

* **Upload the motif logo obtained by running MEME on upstream25.txt. (You should specify that we are finding a single motif of length 20, as we did before.)**

![Motif upstream25](https://github.com/harishmuh/Bioinformatics-I_Finding-Hidden-Messages-in-DNA-Coursera/blob/main/exam/Motif_TMCGCCCMHKCVANGRRGAY_upstream25.png?raw=true)

Next, we will consider upstream regions of length 100 bp (upstream100.txt).

* **Upload the motif logo obtained by running MEME on upstream100.txt. (Remember to specify in the options that we are looking for a single motif of length 20.)**

![Motif upstream100](https://github.com/harishmuh/Bioinformatics-I_Finding-Hidden-Messages-in-DNA-Coursera/blob/main/exam/Motif_CVRYTRGGGACYDWMGBCCC_upstream100.png?raw=true)

Next, we will consider upstream regions of length 500 bp (upstream500.txt).

* **Upload the motif logo obtained by running MEME on upstream500.txt. (Remember to specify in the options that we are looking for a single motif of length 20.)**

![Motif upstream500](https://github.com/harishmuh/Bioinformatics-I_Finding-Hidden-Messages-in-DNA-Coursera/blob/main/exam/Motif_SGGNTAGGGMCNAAAGTCCC_upstream500.png?raw=true)

Finally, we will consider upstream regions of length 1000 bp (upstream1000.txt).

* **Upload the motif logo obtained by running MEME on upstream1000.txt. (Remember to specify in the options that we are looking for a single motif of length 20.)**

![Motif upstream1000](https://github.com/harishmuh/Bioinformatics-I_Finding-Hidden-Messages-in-DNA-Coursera/blob/main/exam/Motif_GBTRGGGMCNRAMGTCCCCN_upstream1000.png?raw=true)

We will now compare the different motif logos generated from varying the length of upstream regions.

* **Which of the motif logos that you created are similar to the motif logo generated from upstream250.txt?**

Answer: The motifs produced by upstream100, upstream500, and upstream1000 are  all similar to the motif produced by upstream250, but the motifs  produced by upstream25 does not resemble the others.





