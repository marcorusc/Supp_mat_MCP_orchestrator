# Chat Summary

**User Request:**

You are my multiscale modelling assistant. Together we are creating a mutliscale multicellular model of cancer cell fate in response to TNF. In order to chieve this we are going to use NeKo, MaBoSS and PhysiCell to create a simulation where an initial group of cancer cell will grow while TNF diffuses in the microenvironment. When the cells sense the TNF they will activate the input nodes of their boolean network. According to the final state of the network, they will perform behaviors such as die for apoptosis or proliferte. Those are he steps to follow: 1) create a network using Omnipath that describes cancer cell fates in response to tnf. This network should contains TNF sensing receptr as well asgenes responsible for proliferation and apoptosis. Once create the network we have to remove the bimodal interactions and check the connectivity. If the network is connected,  export it in bnet file. After that  generate the maboss file (.bnd and .cfg), create a simulation and select some nodes to identify the output, to represent apoptotic state and proliferative state. Once set those nodes as output, we run the maboss simulation, get the results and study the outcome (does the network make sense? are the states biologically feasible?).
This is the first part. In the second part we will build the PhysiCell simulation and add maboss to the cancer cell type. Is everything clear?

**GitHub Copilot Response:**

Yes—clear plan.

Before I start, please confirm a few defaults:

- Network build (NeKo/OmniPath)

  - Seed genes: TNF, TNFRSF1A/TNFR1, TRADD, TRAF2, RIPK1, FADD, CASP8, CFLAR, BCL2, BAX, MCL1, XIAP, BIRC2/3, IKBKB, NFKBIA, RELA, MAP3K7, JNK (MAPK8), JUN/FOS (AP1), PI3K, AKT1, PTEN, mTOR, CCND1, CDK4/6, E2F1, MYC, TP53, CDKN1A(p21), CASP3, CASP9, APAF1. Include necroptosis (RIPK3/MLKL)? yes/no
  - Path completion: max_len=2, algorithm=bfs, only_signed=true, consensus=true. OK?
  - Remove bimodal interactions, then check connectivity. If connected, export .bnet.
- MaBoSS

  - Inputs: TNF node ON/OFF driven later by PhysiCell.
  - Outputs to track: Apoptosis = CASP3 (and/or CASP8); Proliferation = E2F1 (and/or CCND1/CDK4-6). Which do you prefer?
  - Params: time_tick=0.1, max_time=50, sample_count=10000. OK?
- Workspace

  - Use existing scenario folders or create a new one (e.g., ./Sonnet4/Scenario_4)?

Reply “proceed with defaults” or specify changes, and I’ll build the network, export .bnet, generate .bnd/.cfg, set outputs, run MaBoSS, and report results.

**User Request:**

proceed with defaults, for the workspace, use gpt_5/scenario_1

**Tool Output:**

**Network created successfully!**

- **Initial genes:** TNF, TNFRSF1A, TRADD, TRAF2, RIPK1, FADD, CASP8, CFLAR, BCL2, BAX, MCL1, XIAP, BIRC2, BIRC3, IKBKB, NFKBIA, RELA, MAP3K7, MAPK8, JUN, FOS, PIK3CA, AKT1, PTEN, MTOR, CCND1, CDK4, E2F1, MYC, TP53, CDKN1A, CASP3, CASP9, APAF1
- **Total nodes:** 200
- **Total interactions:** 2356

**Preview of interactions (first 100 rows):**

source    target    Effect
TNFRSF1A  MAP4K4    stimulation
MAP4K4    TNF       inhibition
TNF       TNFRSF1A  stimulation
TRADD     TRAF1     stimulation
TRAF1     TNF       inhibition
TNF       TRADD     inhibition
TRAF2     TRAF1     stimulation
TRADD     TRAF2     bimodal
RIPK1     MAP4K4    stimulation
TRADD     RIPK1     stimulation
FADD      MYD88     inhibition
MYD88     TNF       stimulation
TRADD     FADD      stimulation
CASP8     TRAF1     bimodal
TNF       CASP8     stimulation
CFLAR     TNF       inhibition
TNF       MAPK8     stimulation
MAPK8     CFLAR     inhibition
BCL2      MYC       stimulation
MYC       TNF       stimulation
TNF       MAPK3     stimulation
MAPK3     BCL2      bimodal
MAPK8     BAX       stimulation
MAPK3     MCL1      stimulation
XIAP      PTEN      stimulation
PTEN      TNF       inhibition
TNF       RELA      stimulation
RELA      XIAP      stimulation
BIRC2     CFLAR     inhibition
TRADD     BIRC2     stimulation
BIRC3     MAP4K4    stimulation
TNF       CSF3      stimulation
CSF3      BIRC3     stimulation
IKBKB     CYLD      bimodal
CYLD      TNF       inhibition
TNF       IKBKB     stimulation
NFKBIA    IL23A     stimulation
IL23A     TNF       stimulation
TNF       NFKBIA    inhibition
RELA      PPARA     inhibition
PPARA     TNF       inhibition
MAP3K7    MAP2K3    stimulation
MAP2K3    TNF       inhibition
TNF       IL1A      stimulation
IL1A      MAP3K7    stimulation
MAPK8     INS       inhibition
INS       TNF       inhibition
JUN       LPL       inhibition
LPL       TNF       stimulation
TNF       JUN       stimulation
FOS       TNF       stimulation
MAPK3     FOS       stimulation
PIK3CA    MAPK11    inhibition
MAPK11    TNF       inhibition
TNF       BDNF      stimulation
BDNF      PIK3CA    stimulation
AKT1      RXRA      stimulation
RXRA      TNF       stimulation
TNF       AKT1      stimulation
TNF       TGFB1     inhibition
TGFB1     PTEN      stimulation
MTOR      IFNG      stimulation
IFNG      TNF       stimulation
TNF       CXCL8     stimulation
CXCL8     MTOR      stimulation
CCND1     TNF       inhibition
MAPK3     CCND1     stimulation
CDK4      RB1       bimodal
RB1       TNF       stimulation
MAPK3     CDK4      stimulation
E2F1      MYC       stimulation
MAPK3     E2F1      stimulation
MAPK3     MYC       stimulation
TP53      PTEN      stimulation
MAPK3     TP53      stimulation
CDKN1A    CCND1     inhibition
TNF       CDK6      inhibition
CDK6      CDKN1A    inhibition
CASP3     PTEN      stimulation
TNF       CASP3     stimulation
MAPK3     CASP9     inhibition
TNF       SUCLA2    stimulation
SUCLA2    APAF1     stimulation
TRADD     MAPK1     inhibition
MAPK1     TNFRSF1A  inhibition
TNFRSF1A  TRADD     stimulation
TNFRSF1A  TRAF2     stimulation
RIPK1     FASLG     stimulation
FASLG     TNFRSF1A  stimulation
TNFRSF1A  RIPK1     stimulation
FADD      MAPK1     stimulation
TNFRSF1A  FADD      stimulation
CASP8     CASP7     stimulation
CASP7     TNFRSF1A  bimodal
TNFRSF1A  CASP8     stimulation
TNFRSF1A  MAPK3     stimulation
TNFRSF1A  BID       stimulation
BID       BAX       stimulation
XIAP      CASP7     inhibition
TNFRSF1A  RELA      stimulation

**Tool Output:**

{
  "result": "**Network created successfully!**\n\n- **Initial genes:** TNF, TNFRSF1A, TRADD, TRAF2, RIPK1, FADD, CASP8, CFLAR, BCL2, BAX, MCL1, XIAP, BIRC2, BIRC3, IKBKB, NFKBIA, RELA, MAP3K7, MAPK8, JUN, FOS, PIK3CA, AKT1, PTEN, MTOR, CCND1, CDK4, E2F1, MYC, TP53, CDKN1A, CASP3, CASP9, APAF1\n- **Total nodes:** 200\n- **Total interactions:** 2356\n\n**Preview of interactions (first 100 rows):**\n\nsource    target    Effect\nTNFRSF1A  MAP4K4    stimulation\nMAP4K4    TNF       inhibition\nTNF       TNFRSF1A  stimulation\nTRADD     TRAF1     stimulation\nTRAF1     TNF       inhibition\nTNF       TRADD     inhibition\nTRAF2     TRAF1     stimulation\nTRADD     TRAF2     bimodal\nRIPK1     MAP4K4    stimulation\nTRADD     RIPK1     stimulation\nFADD      MYD88     inhibition\nMYD88     TNF       stimulation\nTRADD     FADD      stimulation\nCASP8     TRAF1     bimodal\nTNF       CASP8     stimulation\nCFLAR     TNF       inhibition\nTNF       MAPK8     stimulation\nMAPK8     CFLAR     inhibition\nBCL2      MYC       stimulation\nMYC       TNF       stimulation\nTNF       MAPK3     stimulation\nMAPK3     BCL2      bimodal\nMAPK8     BAX       stimulation\nMAPK3     MCL1      stimulation\nXIAP      PTEN      stimulation\nPTEN      TNF       inhibition\nTNF       RELA      stimulation\nRELA      XIAP      stimulation\nBIRC2     CFLAR     inhibition\nTRADD     BIRC2     stimulation\nBIRC3     MAP4K4    stimulation\nTNF       CSF3      stimulation\nCSF3      BIRC3     stimulation\nIKBKB     CYLD      bimodal\nCYLD      TNF       inhibition\nTNF       IKBKB     stimulation\nNFKBIA    IL23A     stimulation\nIL23A     TNF       stimulation\nTNF       NFKBIA    inhibition\nRELA      PPARA     inhibition\nPPARA     TNF       inhibition\nMAP3K7    MAP2K3    stimulation\nMAP2K3    TNF       inhibition\nTNF       IL1A      stimulation\nIL1A      MAP3K7    stimulation\nMAPK8     INS       inhibition\nINS       TNF       inhibition\nJUN       LPL       inhibition\nLPL       TNF       stimulation\nTNF       JUN       stimulation\nFOS       TNF       stimulation\nMAPK3     FOS       stimulation\nPIK3CA    MAPK11    inhibition\nMAPK11    TNF       inhibition\nTNF       BDNF      stimulation\nBDNF      PIK3CA    stimulation\nAKT1      RXRA      stimulation\nRXRA      TNF       stimulation\nTNF       AKT1      stimulation\nTNF       TGFB1     inhibition\nTGFB1     PTEN      stimulation\nMTOR      IFNG      stimulation\nIFNG      TNF       stimulation\nTNF       CXCL8     stimulation\nCXCL8     MTOR      stimulation\nCCND1     TNF       inhibition\nMAPK3     CCND1     stimulation\nCDK4      RB1       bimodal\nRB1       TNF       stimulation\nMAPK3     CDK4      stimulation\nE2F1      MYC       stimulation\nMAPK3     E2F1      stimulation\nMAPK3     MYC       stimulation\nTP53      PTEN      stimulation\nMAPK3     TP53      stimulation\nCDKN1A    CCND1     inhibition\nTNF       CDK6      inhibition\nCDK6      CDKN1A    inhibition\nCASP3     PTEN      stimulation\nTNF       CASP3     stimulation\nMAPK3     CASP9     inhibition\nTNF       SUCLA2    stimulation\nSUCLA2    APAF1     stimulation\nTRADD     MAPK1     inhibition\nMAPK1     TNFRSF1A  inhibition\nTNFRSF1A  TRADD     stimulation\nTNFRSF1A  TRAF2     stimulation\nRIPK1     FASLG     stimulation\nFASLG     TNFRSF1A  stimulation\nTNFRSF1A  RIPK1     stimulation\nFADD      MAPK1     stimulation\nTNFRSF1A  FADD      stimulation\nCASP8     CASP7     stimulation\nCASP7     TNFRSF1A  bimodal\nTNFRSF1A  CASP8     stimulation\nTNFRSF1A  MAPK3     stimulation\nTNFRSF1A  BID       stimulation\nBID       BAX       stimulation\nXIAP      CASP7     inhibition\nTNFRSF1A  RELA      stimulation"
}

**Tool Output:**

Removed 160 bimodal interactions from the network.

**Tool Output:**

{
  "result": "Removed 160 bimodal interactions from the network."
}

**Tool Output:**

All nodes are connected.

**Tool Output:**

{
  "result": "All nodes are connected."
}

**Tool Output:**

**Exported to** `Network_1.bnet`

_Preview (first 100 lines) of the BNET file:_

gene       expression
TNF        (MYD88 | MYC | IL23A | LPL | FOS | RXRA | IFNG | RB1 | TNFAIP3 | CREB1 | COMPLEX_P19838_Q04206 | IL12B) & !(MAP4K4 | TRAF1 | CFLAR | PTEN | CYLD | PPARA | MAP2K3 | INS | MAPK11 | CCND1 | CSF3 | S100B | MAPK14 | APEX1 | SP1 | CSF2)
TNFRSF1A   (TNF | FASLG | IL2 | TNFAIP3 | TNFRSF1B) & !(MAPK1 | CYLD | S100B)
TRADD      (TNFRSF1A | TNFRSF10B) & !(TNF | CFLAR | CYLD | KRT18 | S100B)
TRAF2      (TNFRSF1A | RELA | TRAF1 | CASP2 | NFKB2 | TNFRSF1B) & !(CYLD | STAT1 | FLNA | PPP2CA | S100B | TNFAIP3)
RIPK1      (TRADD | TNFRSF1A | TRAF2 | FADD | BIRC2 | BIRC3 | SQSTM1 | TICAM1 | HSP90AA1 | CASP2 | TNFRSF10B) & !(CASP8 | CFLAR | OTUD7B | RNF11 | TNFAIP3 | S100B | CASP10)
FADD       (TRADD | TNFRSF1A | TP53 | STAT1 | MYD88 | TNFRSF10B) & !(MAP2K7 | BIRC2 | MAP3K1 | S100B | RIPK2)
CASP8      (TNF | TNFRSF1A | TRADD | TRAF2 | E2F1 | FADD | TP53 | EDN1 | CASP2 | IFNG | TNFRSF10B) & !(RELA | BCL2 | CFLAR | BIRC2 | BIRC3 | MAPK3 | MAPK1 | NFKB1 | S100B | MAPK14 | CDK1)
CFLAR      (MAPK14 | AR | TP53 | DDB2) & !(MAPK8 | BIRC2 | BIRC3 | AKT1 | MYC | CBL | ATM)
BCL2       (RELA | MAP2K1 | NFKB1 | MTOR | CREB1 | E2F2 | BAG1 | STAT1 | PPP2CA | NFKB2 | HSP90AA1 | EIF4G2 | CTNNB1 | IL6 | BCL2L1 | VEGFA) & !(CASP3 | TP53 | IRS1 | IL5 | CDK6 | MAPK14 | ATM | BCL2L11 | PPP2R5C)
BAX        (MAPK8 | BID | TP73 | TP53 | CASP3 | TP63 | SP1 | RPS6KB1 | MYC | BCL2L11) & !(BCL2 | MCL1 | RELA | AKT1 | UBB | PRKCZ | PRNP | AKT3 | BCL2L1)
MCL1       (MAPK3 | MAPK1 | MAP2K1 | CSF2 | AKT1 | HIF1A | IL6 | VEGFA) & !(CASP3 | E2F1 | TFDP1 | BCL2L11 | CDK1)
XIAP       (RELA | TP53 | NFKB1 | EIF4G2 | AKT3 | AKT1 | AKT2 | BIRC5 | NFKB2 | ELK1) & !(HTRA2)
BIRC2      (TRADD | TNFRSF1B | TRAF2 | RELA | NFKB1 | EIF4G2 | BIRC3 | ELK1 | CD40LG | NFKB2) & !(HTRA2)
BIRC3      (CSF3 | RELA | TRAF2 | NFKBIA | NFKB1 | NFKB2 | ELK1) & !(TP53 | HTRA2 | S100B)
IKBKB      (TNF | MAP3K5 | TRADD | TRAF2 | RIPK1 | FADD | CASP8 | MAP3K7 | RIPK2 | AKT1 | FASLG | AKT2 | MAP4K4 | MYD88 | CHUK | TNFRSF10B | FLNA | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | AKT3 | IKBKG | IRAK1 | NGFR) & !(CASP3)
NFKBIA     (TRAF2 | ATM | CASP3 | IKBKG | RXRA | IL12B | TRAF1 | IL23A | NFKB1 | TRAF6 | MAP3K1) & !(TNF | TNFRSF1A | RELA | MAPK3 | JUN | RPS6KA2 | CUL1 | PPARA | MAPK1 | TNFAIP3 | MAPK14 | PRKCZ | SP1 | PRKCD | HSPB1)
RELA       (TNF | TNFRSF1A | TRADD | RIPK1 | TRAF2 | PIK3CA | E2F1 | IKBKB | IKBKG | IL23A | MAPK3 | IL1B | CUL1 | RAC1 | TRAF1 | MAPK1 | CHUK | NFKB1 | MAPK14 | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | IRAK1 | NGFR | IL12B | RPS6KA2 | PRKCD) & !(CASP3 | STAT1 | TSC22D3 | PPP2CA | SIRT1)
MAP3K7     (IL1A | TRAF2 | TRAF6 | MYD88 | XIAP | RIPK2 | IRAK1 | LAT | SMAD7 | GNAI1 | TRIM8 | MAP3K1 | MAP4K4 | CYLD | TGFB1 | EPHB2 | TICAM1 | BMP2) & !(MAPK11 | PPP2CA)
MAPK8      (TNF | MAPK3 | MAP3K5 | TRAF2 | MAP2K7 | MAP2K4 | MAP3K7 | PIK3CA | XIAP | RIPK2 | NGFR | IL2 | SH3RF1 | PTK2B | RAC1 | ROCK1 | LYN | MAP2K3 | BDNF | TGFB1 | MAP2K1 | TRAF6 | PRKCZ | MAP3K1 | EDN1 | CD40LG | IL1B | GNAI1 | PRKCD | ILK | CDC42) & !(AKT2 | MAPK1)
JUN        (TNF | RELA | MAPK9 | NFKB1 | PAK2 | MAPK8 | COMPLEX_P19838_Q04206 | IL2 | FOS | ILK | AKT1 | AKT2 | MEF2D | AR | CDK3 | ARHGDIB | MAPK11 | BDNF | RB1 | MAPK1 | MAPK14 | MAP3K1 | AKT3 | ELK1) & !(NOTCH1 | VDR | LYN)
FOS        (MAPK3 | RELA | NFKB1 | APEX1 | MAPK8 | SMAD4 | AKT1 | AKT2 | HNRNPR | MRTFA | MAPK11 | MAPK1 | MAPK14 | CREB1 | AKT3 | ELK1 | IL12B | ILK) & !(NOTCH1 | VDR | PPP3CA | LYN)
PIK3CA     (BDNF | RAC1 | TRAF5 | EPHB2 | EGFR | CTNNB1 | FOXO3 | IL23A | ZAP70 | INS | FGR | IRS4 | VEGFA | FGFR2 | GNG2 | PTK2 | LAMB2 | LYN | TGFB1 | IFNG | IRS1 | IL5 | CD40LG | IL12B | LAT | GNAI1 | SHC1 | SOS1) & !(PTEN | CDKN2A | CDKN2A)
AKT1       (TNF | MAPK8 | TRAF6 | MTOR | ATM | FASLG | IL2 | TGFB1 | PELP1 | SIRT1 | COMPLEX_P20248_P24941 | EIF4E | INS | RAC1 | EDN1 | CD40LG | GNAI1 | SHC1 | ILK | LAMB2 | SOS1) & !(CASP3 | RALBP1 | PPP2CA | PRKCZ | PPP2R5C)
PTEN       (XIAP | TGFB1 | TP53 | CASP3 | CDC42 | EGR1 | HSP90AA1 | ROCK1) & !(RELA | BMP2 | AKT1 | JUN | FOS)
MTOR       (CXCL8 | CHUK | IKBKB | IL2 | SHC1 | PIK3CA | RHEB | SOS1 | TSC2 | EGFR | TGFB1 | CDC42)
CCND1      (MAPK3 | RELA | NFKB1 | COMPLEX_P19838_Q04206 | SMAD4 | JUN | FOS | PIK3CA | NOTCH1 | DDAH2 | MYC | EGFR | MAPK1 | RAC1 | STAT1 | NFKB2 | MAPK14 | CREB1 | TERT | SP1 | ELK1) & !(CDKN1A | BCL2 | CDKN2A | CDKN2A)
CDK4       (MAPK3 | MAPK1 | MYC | IL6 | FOS | JUN | CCND1 | CCND3) & !(CDKN2A | CDKN1A | CDKN2A | TGFB1)
E2F1       (MAPK3 | MAPK1 | PARP1 | PTEN | CUL1 | EGFR | ATM | SP1 | CDK1 | VEGFA | COMPLEX_P20248_P24941 | E2F3 | CCNE1) & !(CDKN1A | CCND3 | RB1 | SIRT1 | CDK3)
MYC        (BCL2 | E2F1 | MAPK3 | MAP3K5 | NFKB1 | MAPK8 | IL2 | PIK3CA | RPS6KB1 | E2F3 | SMAD4 | RAC1 | INS | MAPK11 | RXRA | MAPK1 | CHUK | MAPK9 | PPP2CA | MAPK14 | IL5 | CTNNB1 | CREB1 | E2F2) & !(RELA | JUN | RB1 | PPARA | PAK2)
TP53       (MAPK3 | NFKB1 | TRAF2 | TRAF6 | XIAP | MAPK8 | E2F1 | PSEN1 | DAXX | PARP1 | BAD | NGFR | EGR1 | TP53BP1 | PTK2B | CCNE1 | PPP2R5C | MAPK11 | BDNF | TGFB1 | MAPK1 | RAC1 | MAPK9 | MAPK14 | APEX1 | CREB1 | CD40LG | PRKCD | CDK1 | COMPLEX_P20248_P24941) & !(JUN | FOS | NOTCH1 | TRIM24 | XPO1 | HSP90AA1 | BAG1 | SIRT1 | BCL2L1 | HSPB1)
CDKN1A     (MAP3K5 | MAPK14 | CASP3 | EGR1 | MAPK8 | JUN | IL1B | NOTCH1 | E2F3 | SMAD4 | IL1A | TGFB1 | IFNG | RAC1 | STAT1 | AR | CREB1 | SP1 | HIF1A) & !(CDK6 | MYC | TP73 | DDB2 | TP63 | CDKN2A | CUL1 | CDKN2A)
CASP3      (TNF | TNFRSF1A | FADD | CASP8 | CASP10 | PRNP | CYCS | NFE2L2 | PRKCD | IFNG | E2F1 | VDR) & !(BIRC3 | MAPK14 | BIRC2 | XIAP | NAIP | HSPB1)
CASP9      (APAF1 | RARA | E2F1 | DIABLO | CYCS) & !(MAPK3 | BIRC2 | BIRC3 | MAPK1 | ALPI | BAD | BCL2L1 | CDK1 | BIRC5 | GSN | MAP2K1 | PRKCZ | AKT3 | NAIP)
APAF1      (SUCLA2 | CASP10 | BAX | COX5B | ACHE | TP53 | RAC1 | E2F1 | TFDP1 | EIF4G2 | DIABLO | CYCS) & !(BIRC2 | BIRC3 | BCL2 | XIAP | AKT1 | HSPA4 | HSP90AA1 | BIRC5)
MAP4K4     (TNFRSF1A | RIPK1 | BIRC3 | TNF | TRADD | FADD | TP53 | MYD88 | IL1A | MAP3K5 | CASP2 | EPHB2 | TRAF6 | CD40LG | IRAK1)
TRAF1      (TRADD | TRAF2 | RELA | TNFRSF1B | NFKB1 | NFKB2 | TICAM1) & !(MYC | CYLD | S100B)
MYD88      !(FADD | IL1B)
MAPK3      (TNF | TNFRSF1A | MAP3K7 | AKT1 | CSF3 | MAP2K3 | MAPK11 | BDNF | TGFB1 | SUCLA2 | MAPK1 | IL2 | NFKB1 | MAP2K7 | MAP2K1 | MAPK9 | EPHB2 | TRAF6 | MAP2K4 | PRKCZ | MAP3K1 | EDN1 | IL5 | CSF2 | IL6 | RIPK2 | IL1B | GNAI1 | PTK2B | LYN | VEGFA | PELP1) & !(PIK3CA | PPP2CA | MAPK14 | TSC22D3 | PRKCD)
CSF3       (TNF | IFNG) & !(CXCL8)
CYLD       CYLD
IL23A      (NFKBIA | TNF | RELA | JUN | NFKB1 | IL1B) & !(MAPK1)
PPARA      (MAPK8 | MAPK3 | RXRA | MAPK1) & !(RELA)
MAP2K3     (MAP3K7 | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | TGFB1 | MAPK1 | FASLG | MAP3K5 | RAC1 | TRAF6 | MAP3K1 | DAXX | IL1B | PTK2B | CDC42)
IL1A       (TNF | TP63 | IL6 | IL1B) & !(IFNG)
INS        !(MAPK8)
LPL        (TNF | TRAF2 | RXRA) & !(JUN | RELA | TGFB1 | IFNG | SP1)
MAPK11     (TRAF2 | MAP2K3 | IL2 | RAC1 | MAP2K7 | TRAF6 | MAP2K4 | MAP3K1 | PAK2 | CD40LG | ZAP70 | SHC1 | LYN | FGR | CDC42 | VEGFA | GNG2) & !(PIK3CA | DUSP4)
BDNF       (TNF | MAPK3)
RXRA       (AKT1 | MAP3K7 | AR | RARA | VDR | CDK1 | FGR) & !(MAPK9 | MAP2K4)
TGFB1      (RELA | MAP3K7 | JUN | FOS | IFNG | RB1 | NFKB1 | EPHB2 | EDN1 | RPS6KB1 | HIF1A | EGR1 | EIF4E) & !(TNF | AKT1 | MAP2K3 | IL2 | MAPK14 | DAXX | IRS1 | SMAD4 | HSPB1)
IFNG       (MTOR | JUN | FOS | MAPK3 | IL23A | LPL | MAPK1 | IL2 | NFKB1 | IL12B | NOTCH1) & !(TNF | TGFB1 | MAPK9 | PPP3CA)
CXCL8      (TNF | RELA | JUN | FOS | MYC | IL1A | TGFB1 | FASLG | RAC1 | NFKB1 | MAP2K1 | PPP2CA | EGFR | EDN1 | CTNNB1 | CSF2 | CD40LG | COMPLEX_P19838_Q04206 | IL1B | BCL2L1 | VEGFA) & !(MAPK3 | MAPK11 | IFNG | MAPK14 | HIF1A | EGR1)
RB1        (AKT1 | TP53 | TGFB1 | PPP2CA | SIRT1) & !(CASP3 | CDKN1A | SMAD7 | VEGFA)
CDK6       (CCND1 | MYC | TP73 | CREB1 | CCND3) & !(TNF)
SUCLA2     (TNF | TGFB1 | CD40LG | ACHE)
MAPK1      (FADD | TNF | IL1A | INS | BDNF | TGFB1 | SUCLA2 | IL2 | RAC1 | MAP2K7 | MAP2K1 | MAP2K4 | PRKCZ | MAP3K1 | EDN1 | CSF2 | IL1B | GNAI1 | BMP2 | SHC1 | FGR | CDC42 | VEGFA) & !(TRADD | PIK3CA | PPP2CA)
FASLG      (RIPK1 | MAPK8 | JUN | FOS | TP53 | IFNG | NFKB1 | STAT1 | IL12B | EGR1) & !(BIRC2 | BIRC3 | RIPK2 | SIRT1 | HSPB1)
CASP7      (CASP8 | CASP3 | CASP9 | APAF1 | FADD | FASLG | CASP2 | CASP10 | CYCS) & !(XIAP | BIRC2 | BIRC3 | RB1 | PAK2 | E2F2 | TFDP1 | BIRC5 | NAIP | E2F3)
BID        (TNFRSF1A | TRADD | TRAF2 | RIPK1 | FADD | BIRC3 | TNF | CASP8 | MAPK8 | E2F1 | TP53 | CASP3 | FASLG | MAP3K5 | CASP2 | DAXX | CASP10 | ATM) & !(BCL2 | HIF1A)
TNFRSF1B   (TNFRSF1A | TNF)
MAP3K5     (TNFRSF1A | TRADD | E2F1 | TNF | IFNG | MAPK1 | TRAF6 | DAXX) & !(AKT1 | RB1 | S100B | AKT3 | AKT2)
IL2        (JUN | FOS | IL1A | NFKB1 | IL5 | CREB1 | IL6 | IKBKG | IL1B) & !(MAP3K7 | CSF3 | CSF2 | CD40LG)
TNFAIP3    (RELA | TNF | TNFRSF1A | NFKB1)
RAC1       (TNFRSF1A | CDKN1A | PIK3CA | PTEN | EPHB2 | EGFR | EDN1 | NGFR | GNAI1 | SHC1 | PTK2B | LYN | VEGFA | GNG2 | PTK2 | LAMB2 | SOS1) & !(TP53)
CHUK       (TNFRSF1A | CASP8 | TNF | TRADD | TRAF2 | RIPK1 | FADD | MAP3K7 | AKT1 | MAP4K4 | MYD88 | MAPK3 | IL1A | FASLG | MAP3K5 | TNFRSF10B | FLNA | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | TP63 | AKT3 | AKT2 | IKBKG | RIPK2 | IRAK1 | NGFR | NOTCH1)
TRAF5      (TRADD | RELA | NFKB1 | NFKB2)
TNFRSF10B  (TP53 | FASLG | NFKB1 | NOTCH1)
NFKB1      (TRADD | FADD | MAP3K7 | TNF | TNFRSF1A | TRAF2 | RIPK1 | PIK3CA | AKT1 | TRAF1 | IL23A | BDNF | SUCLA2 | MAPK1 | RAC1 | MAPK14 | SQSTM1 | TRAF6 | TICAM1 | EGFR | PARP1 | PRKCZ | MAP3K1 | EDN1 | CASP10 | ATM | PRNP | CSF2 | IKBKG | RIPK2 | IRAK1 | NGFR | IL12B | PRKCD | LYN) & !(E2F1 | BAG1 | CDKN2A | CUL1 | TSC22D3 | HSPB1 | CDKN2A)
KRT18      (CASP3 | AR | CDK1)
MAP2K7     (TRAF2 | RIPK1 | CASP8 | BIRC3 | MAP3K7 | TNF | TNFRSF1A | TRADD | TRAF1 | FASLG | MAP3K5 | RAC1 | CASP2 | FLNA | MAP3K1 | DAXX | RIPK2 | SH3RF1 | CDC42)
MAP2K1     (TRAF2 | MAP3K7 | PIK3CA | IL2 | RAC1 | MAPK14 | EGFR | MAP3K1 | PAK2 | CSF2 | PRKCD | SHC1) & !(PPP2CA | CDK1)
CASP2      (CASP3 | TRADD | TP73 | CCND3) & !(BIRC2 | S100B | AR)
STAT1      (MAPK8 | CSF3 | IL23A | MAPK11 | IFNG | MAPK1 | IL2 | MAPK9 | EPHB2 | MAPK14 | EGFR | AR | IL6 | IL12B | PRKCD | LYN | FGFR2 | PTK2) & !(CCND1 | CYLD)
MAPK9      (TRAF2 | MAPK8 | MAP2K3 | BDNF | MAP3K5 | RAC1 | MAP2K7 | MAP2K1 | MAPK14 | TRAF6 | MAP2K4 | PRKCZ | CD40LG | NGFR | CDC42) & !(DUSP4)
EPHB2      (TRAF2 | TGFB1 | MAPK14 | LYN | FGR) & !(PPP2CA)
FLNA       (AKT1 | PRKCD) & !(PPP3CA)
PPP2CA     (CDK3 | PPP2R5C) & !(MTOR)
NFKB2      (TP53 | CUL1) & !(MYC | TSC22D3)
S100B      (IFNG) & !(TP53)
MAPK14     (RIPK1 | TNF | TRAF2 | MAP3K7 | MAPK8 | PIK3CA | MAP2K3 | MAPK11 | TGFB1 | MAP3K5 | IL2 | RAC1 | MAP2K7 | TRAF6 | MAP2K4 | MAP3K1 | EDN1 | PAK2 | RIPK2 | CD40LG | ZAP70 | GNAI1 | BMP2 | PTK2B | LYN | CDC42 | GNG2) & !(DUSP4)
SQSTM1     (IKBKB | CDK1)
OTUD7B     (MAP3K7 | CDK4 | AKT1 | CDK6 | MAPK1 | IRAK1)
TRAF6      (RELA | MYD88 | IL1A | TGFB1 | NFKB1 | NFKB2 | SQSTM1 | TICAM1 | ATM | IRAK1 | IL1B | HSPB1) & !(TNFAIP3 | PSEN1)
TICAM1     (PIK3CA | TRAF2) & !(TRAF1 | TNFAIP3)
EGFR       (TP53 | INS | TGFB1 | CXCL8 | FASLG | PPP2CA | AR | EDN1 | EGR1 | PTK2B | LYN | RARA | NOTCH1 | FGR | VEGFA) & !(RIPK1 | PTEN | MAPK11 | MAPK14 | TRAF6 | PRKCD | CDK1 | CDC42)
RNF11      !(AKT1)
PARP1      (INS | SUCLA2 | MAPK1 | ILK) & !(RIPK1 | BCL2 | CASP7)
HSP90AA1   (MYC | PPARA | IL2 | ZAP70) & !(IFNG)
MAP2K4     (FADD | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | BIRC3 | MAP3K7 | FASLG | MAP3K5 | RAC1 | MAP2K7 | MAP2K1 | FLNA | DAXX | CASP10 | CD40LG | SH3RF1 | ROCK1) & !(AKT1 | AKT3 | AKT2)
PRKCZ      (PIK3CA | INS | IL2 | SHC1 | ROCK1 | CDC42) & !(PPP2CA)
MAP3K1     (AKT1 | CASP3 | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | MAP4K4 | TRAF1 | MYD88 | IL1A | IFNG | CASP7 | TNFRSF1B | RAC1 | TNFRSF10B | TRAF6 | EGFR | PAK2 | CD40LG | IRAK1 | LAT | CDC42)
AR         (MAPK8 | RXRA | TGFB1 | MAPK14 | HSP90AA1 | MAP3K1 | EDN1 | SIRT1 | SMAD4 | CDK1 | TRIM24 | GSN) & !(CASP8 | PTEN | E2F1 | RELA | TP53 | CASP7 | DAXX | EGR1)
TP73       (CASP8 | E2F1 | TP53 | CASP3 | MAPK11 | MAPK14 | TFDP1 | PRKCD) & !(SIRT1 | CDK1)
EIF4G2     (CASP8 | CASP9 | CASP7 | CASP2 | CASP10 | CDK1)
EDN1       (JUN | FOS | TNF | PPARA | TGFB1 | CREB1 | HIF1A) & !(VEGFA)
PAK2       (CASP8 | CASP3 | TGFB1 | RAC1 | CDC42)
RALBP1     (CASP8)
PSEN1      (CASP8 | TNF | CASP3 | CASP7 | MAPK9 | PRKCZ) & !(ELK1)
ALPI       (CASP8 | CASP10) & !(NFKB1 | DIABLO)
CBL        (CDK4 | AKT1 | INS | IFNG | IL2 | PRKCZ | IRS1 | PRKCD | PTK2B | FGR)

**Warning:** The following gene/node names were modified to remove special characters: COMPLEX:P19838_Q04206, COMPLEX:P20248_P24941

**Tool Output:**

{
  "result": "**Exported to** `Network_1.bnet`\n\n_Preview (first 100 lines) of the BNET file:_\n\ngene       expression\nTNF        (MYD88 | MYC | IL23A | LPL | FOS | RXRA | IFNG | RB1 | TNFAIP3 | CREB1 | COMPLEX_P19838_Q04206 | IL12B) & !(MAP4K4 | TRAF1 | CFLAR | PTEN | CYLD | PPARA | MAP2K3 | INS | MAPK11 | CCND1 | CSF3 | S100B | MAPK14 | APEX1 | SP1 | CSF2)\nTNFRSF1A   (TNF | FASLG | IL2 | TNFAIP3 | TNFRSF1B) & !(MAPK1 | CYLD | S100B)\nTRADD      (TNFRSF1A | TNFRSF10B) & !(TNF | CFLAR | CYLD | KRT18 | S100B)\nTRAF2      (TNFRSF1A | RELA | TRAF1 | CASP2 | NFKB2 | TNFRSF1B) & !(CYLD | STAT1 | FLNA | PPP2CA | S100B | TNFAIP3)\nRIPK1      (TRADD | TNFRSF1A | TRAF2 | FADD | BIRC2 | BIRC3 | SQSTM1 | TICAM1 | HSP90AA1 | CASP2 | TNFRSF10B) & !(CASP8 | CFLAR | OTUD7B | RNF11 | TNFAIP3 | S100B | CASP10)\nFADD       (TRADD | TNFRSF1A | TP53 | STAT1 | MYD88 | TNFRSF10B) & !(MAP2K7 | BIRC2 | MAP3K1 | S100B | RIPK2)\nCASP8      (TNF | TNFRSF1A | TRADD | TRAF2 | E2F1 | FADD | TP53 | EDN1 | CASP2 | IFNG | TNFRSF10B) & !(RELA | BCL2 | CFLAR | BIRC2 | BIRC3 | MAPK3 | MAPK1 | NFKB1 | S100B | MAPK14 | CDK1)\nCFLAR      (MAPK14 | AR | TP53 | DDB2) & !(MAPK8 | BIRC2 | BIRC3 | AKT1 | MYC | CBL | ATM)\nBCL2       (RELA | MAP2K1 | NFKB1 | MTOR | CREB1 | E2F2 | BAG1 | STAT1 | PPP2CA | NFKB2 | HSP90AA1 | EIF4G2 | CTNNB1 | IL6 | BCL2L1 | VEGFA) & !(CASP3 | TP53 | IRS1 | IL5 | CDK6 | MAPK14 | ATM | BCL2L11 | PPP2R5C)\nBAX        (MAPK8 | BID | TP73 | TP53 | CASP3 | TP63 | SP1 | RPS6KB1 | MYC | BCL2L11) & !(BCL2 | MCL1 | RELA | AKT1 | UBB | PRKCZ | PRNP | AKT3 | BCL2L1)\nMCL1       (MAPK3 | MAPK1 | MAP2K1 | CSF2 | AKT1 | HIF1A | IL6 | VEGFA) & !(CASP3 | E2F1 | TFDP1 | BCL2L11 | CDK1)\nXIAP       (RELA | TP53 | NFKB1 | EIF4G2 | AKT3 | AKT1 | AKT2 | BIRC5 | NFKB2 | ELK1) & !(HTRA2)\nBIRC2      (TRADD | TNFRSF1B | TRAF2 | RELA | NFKB1 | EIF4G2 | BIRC3 | ELK1 | CD40LG | NFKB2) & !(HTRA2)\nBIRC3      (CSF3 | RELA | TRAF2 | NFKBIA | NFKB1 | NFKB2 | ELK1) & !(TP53 | HTRA2 | S100B)\nIKBKB      (TNF | MAP3K5 | TRADD | TRAF2 | RIPK1 | FADD | CASP8 | MAP3K7 | RIPK2 | AKT1 | FASLG | AKT2 | MAP4K4 | MYD88 | CHUK | TNFRSF10B | FLNA | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | AKT3 | IKBKG | IRAK1 | NGFR) & !(CASP3)\nNFKBIA     (TRAF2 | ATM | CASP3 | IKBKG | RXRA | IL12B | TRAF1 | IL23A | NFKB1 | TRAF6 | MAP3K1) & !(TNF | TNFRSF1A | RELA | MAPK3 | JUN | RPS6KA2 | CUL1 | PPARA | MAPK1 | TNFAIP3 | MAPK14 | PRKCZ | SP1 | PRKCD | HSPB1)\nRELA       (TNF | TNFRSF1A | TRADD | RIPK1 | TRAF2 | PIK3CA | E2F1 | IKBKB | IKBKG | IL23A | MAPK3 | IL1B | CUL1 | RAC1 | TRAF1 | MAPK1 | CHUK | NFKB1 | MAPK14 | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | IRAK1 | NGFR | IL12B | RPS6KA2 | PRKCD) & !(CASP3 | STAT1 | TSC22D3 | PPP2CA | SIRT1)\nMAP3K7     (IL1A | TRAF2 | TRAF6 | MYD88 | XIAP | RIPK2 | IRAK1 | LAT | SMAD7 | GNAI1 | TRIM8 | MAP3K1 | MAP4K4 | CYLD | TGFB1 | EPHB2 | TICAM1 | BMP2) & !(MAPK11 | PPP2CA)\nMAPK8      (TNF | MAPK3 | MAP3K5 | TRAF2 | MAP2K7 | MAP2K4 | MAP3K7 | PIK3CA | XIAP | RIPK2 | NGFR | IL2 | SH3RF1 | PTK2B | RAC1 | ROCK1 | LYN | MAP2K3 | BDNF | TGFB1 | MAP2K1 | TRAF6 | PRKCZ | MAP3K1 | EDN1 | CD40LG | IL1B | GNAI1 | PRKCD | ILK | CDC42) & !(AKT2 | MAPK1)\nJUN        (TNF | RELA | MAPK9 | NFKB1 | PAK2 | MAPK8 | COMPLEX_P19838_Q04206 | IL2 | FOS | ILK | AKT1 | AKT2 | MEF2D | AR | CDK3 | ARHGDIB | MAPK11 | BDNF | RB1 | MAPK1 | MAPK14 | MAP3K1 | AKT3 | ELK1) & !(NOTCH1 | VDR | LYN)\nFOS        (MAPK3 | RELA | NFKB1 | APEX1 | MAPK8 | SMAD4 | AKT1 | AKT2 | HNRNPR | MRTFA | MAPK11 | MAPK1 | MAPK14 | CREB1 | AKT3 | ELK1 | IL12B | ILK) & !(NOTCH1 | VDR | PPP3CA | LYN)\nPIK3CA     (BDNF | RAC1 | TRAF5 | EPHB2 | EGFR | CTNNB1 | FOXO3 | IL23A | ZAP70 | INS | FGR | IRS4 | VEGFA | FGFR2 | GNG2 | PTK2 | LAMB2 | LYN | TGFB1 | IFNG | IRS1 | IL5 | CD40LG | IL12B | LAT | GNAI1 | SHC1 | SOS1) & !(PTEN | CDKN2A | CDKN2A)\nAKT1       (TNF | MAPK8 | TRAF6 | MTOR | ATM | FASLG | IL2 | TGFB1 | PELP1 | SIRT1 | COMPLEX_P20248_P24941 | EIF4E | INS | RAC1 | EDN1 | CD40LG | GNAI1 | SHC1 | ILK | LAMB2 | SOS1) & !(CASP3 | RALBP1 | PPP2CA | PRKCZ | PPP2R5C)\nPTEN       (XIAP | TGFB1 | TP53 | CASP3 | CDC42 | EGR1 | HSP90AA1 | ROCK1) & !(RELA | BMP2 | AKT1 | JUN | FOS)\nMTOR       (CXCL8 | CHUK | IKBKB | IL2 | SHC1 | PIK3CA | RHEB | SOS1 | TSC2 | EGFR | TGFB1 | CDC42)\nCCND1      (MAPK3 | RELA | NFKB1 | COMPLEX_P19838_Q04206 | SMAD4 | JUN | FOS | PIK3CA | NOTCH1 | DDAH2 | MYC | EGFR | MAPK1 | RAC1 | STAT1 | NFKB2 | MAPK14 | CREB1 | TERT | SP1 | ELK1) & !(CDKN1A | BCL2 | CDKN2A | CDKN2A)\nCDK4       (MAPK3 | MAPK1 | MYC | IL6 | FOS | JUN | CCND1 | CCND3) & !(CDKN2A | CDKN1A | CDKN2A | TGFB1)\nE2F1       (MAPK3 | MAPK1 | PARP1 | PTEN | CUL1 | EGFR | ATM | SP1 | CDK1 | VEGFA | COMPLEX_P20248_P24941 | E2F3 | CCNE1) & !(CDKN1A | CCND3 | RB1 | SIRT1 | CDK3)\nMYC        (BCL2 | E2F1 | MAPK3 | MAP3K5 | NFKB1 | MAPK8 | IL2 | PIK3CA | RPS6KB1 | E2F3 | SMAD4 | RAC1 | INS | MAPK11 | RXRA | MAPK1 | CHUK | MAPK9 | PPP2CA | MAPK14 | IL5 | CTNNB1 | CREB1 | E2F2) & !(RELA | JUN | RB1 | PPARA | PAK2)\nTP53       (MAPK3 | NFKB1 | TRAF2 | TRAF6 | XIAP | MAPK8 | E2F1 | PSEN1 | DAXX | PARP1 | BAD | NGFR | EGR1 | TP53BP1 | PTK2B | CCNE1 | PPP2R5C | MAPK11 | BDNF | TGFB1 | MAPK1 | RAC1 | MAPK9 | MAPK14 | APEX1 | CREB1 | CD40LG | PRKCD | CDK1 | COMPLEX_P20248_P24941) & !(JUN | FOS | NOTCH1 | TRIM24 | XPO1 | HSP90AA1 | BAG1 | SIRT1 | BCL2L1 | HSPB1)\nCDKN1A     (MAP3K5 | MAPK14 | CASP3 | EGR1 | MAPK8 | JUN | IL1B | NOTCH1 | E2F3 | SMAD4 | IL1A | TGFB1 | IFNG | RAC1 | STAT1 | AR | CREB1 | SP1 | HIF1A) & !(CDK6 | MYC | TP73 | DDB2 | TP63 | CDKN2A | CUL1 | CDKN2A)\nCASP3      (TNF | TNFRSF1A | FADD | CASP8 | CASP10 | PRNP | CYCS | NFE2L2 | PRKCD | IFNG | E2F1 | VDR) & !(BIRC3 | MAPK14 | BIRC2 | XIAP | NAIP | HSPB1)\nCASP9      (APAF1 | RARA | E2F1 | DIABLO | CYCS) & !(MAPK3 | BIRC2 | BIRC3 | MAPK1 | ALPI | BAD | BCL2L1 | CDK1 | BIRC5 | GSN | MAP2K1 | PRKCZ | AKT3 | NAIP)\nAPAF1      (SUCLA2 | CASP10 | BAX | COX5B | ACHE | TP53 | RAC1 | E2F1 | TFDP1 | EIF4G2 | DIABLO | CYCS) & !(BIRC2 | BIRC3 | BCL2 | XIAP | AKT1 | HSPA4 | HSP90AA1 | BIRC5)\nMAP4K4     (TNFRSF1A | RIPK1 | BIRC3 | TNF | TRADD | FADD | TP53 | MYD88 | IL1A | MAP3K5 | CASP2 | EPHB2 | TRAF6 | CD40LG | IRAK1)\nTRAF1      (TRADD | TRAF2 | RELA | TNFRSF1B | NFKB1 | NFKB2 | TICAM1) & !(MYC | CYLD | S100B)\nMYD88      !(FADD | IL1B)\nMAPK3      (TNF | TNFRSF1A | MAP3K7 | AKT1 | CSF3 | MAP2K3 | MAPK11 | BDNF | TGFB1 | SUCLA2 | MAPK1 | IL2 | NFKB1 | MAP2K7 | MAP2K1 | MAPK9 | EPHB2 | TRAF6 | MAP2K4 | PRKCZ | MAP3K1 | EDN1 | IL5 | CSF2 | IL6 | RIPK2 | IL1B | GNAI1 | PTK2B | LYN | VEGFA | PELP1) & !(PIK3CA | PPP2CA | MAPK14 | TSC22D3 | PRKCD)\nCSF3       (TNF | IFNG) & !(CXCL8)\nCYLD       CYLD\nIL23A      (NFKBIA | TNF | RELA | JUN | NFKB1 | IL1B) & !(MAPK1)\nPPARA      (MAPK8 | MAPK3 | RXRA | MAPK1) & !(RELA)\nMAP2K3     (MAP3K7 | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | TGFB1 | MAPK1 | FASLG | MAP3K5 | RAC1 | TRAF6 | MAP3K1 | DAXX | IL1B | PTK2B | CDC42)\nIL1A       (TNF | TP63 | IL6 | IL1B) & !(IFNG)\nINS        !(MAPK8)\nLPL        (TNF | TRAF2 | RXRA) & !(JUN | RELA | TGFB1 | IFNG | SP1)\nMAPK11     (TRAF2 | MAP2K3 | IL2 | RAC1 | MAP2K7 | TRAF6 | MAP2K4 | MAP3K1 | PAK2 | CD40LG | ZAP70 | SHC1 | LYN | FGR | CDC42 | VEGFA | GNG2) & !(PIK3CA | DUSP4)\nBDNF       (TNF | MAPK3)\nRXRA       (AKT1 | MAP3K7 | AR | RARA | VDR | CDK1 | FGR) & !(MAPK9 | MAP2K4)\nTGFB1      (RELA | MAP3K7 | JUN | FOS | IFNG | RB1 | NFKB1 | EPHB2 | EDN1 | RPS6KB1 | HIF1A | EGR1 | EIF4E) & !(TNF | AKT1 | MAP2K3 | IL2 | MAPK14 | DAXX | IRS1 | SMAD4 | HSPB1)\nIFNG       (MTOR | JUN | FOS | MAPK3 | IL23A | LPL | MAPK1 | IL2 | NFKB1 | IL12B | NOTCH1) & !(TNF | TGFB1 | MAPK9 | PPP3CA)\nCXCL8      (TNF | RELA | JUN | FOS | MYC | IL1A | TGFB1 | FASLG | RAC1 | NFKB1 | MAP2K1 | PPP2CA | EGFR | EDN1 | CTNNB1 | CSF2 | CD40LG | COMPLEX_P19838_Q04206 | IL1B | BCL2L1 | VEGFA) & !(MAPK3 | MAPK11 | IFNG | MAPK14 | HIF1A | EGR1)\nRB1        (AKT1 | TP53 | TGFB1 | PPP2CA | SIRT1) & !(CASP3 | CDKN1A | SMAD7 | VEGFA)\nCDK6       (CCND1 | MYC | TP73 | CREB1 | CCND3) & !(TNF)\nSUCLA2     (TNF | TGFB1 | CD40LG | ACHE)\nMAPK1      (FADD | TNF | IL1A | INS | BDNF | TGFB1 | SUCLA2 | IL2 | RAC1 | MAP2K7 | MAP2K1 | MAP2K4 | PRKCZ | MAP3K1 | EDN1 | CSF2 | IL1B | GNAI1 | BMP2 | SHC1 | FGR | CDC42 | VEGFA) & !(TRADD | PIK3CA | PPP2CA)\nFASLG      (RIPK1 | MAPK8 | JUN | FOS | TP53 | IFNG | NFKB1 | STAT1 | IL12B | EGR1) & !(BIRC2 | BIRC3 | RIPK2 | SIRT1 | HSPB1)\nCASP7      (CASP8 | CASP3 | CASP9 | APAF1 | FADD | FASLG | CASP2 | CASP10 | CYCS) & !(XIAP | BIRC2 | BIRC3 | RB1 | PAK2 | E2F2 | TFDP1 | BIRC5 | NAIP | E2F3)\nBID        (TNFRSF1A | TRADD | TRAF2 | RIPK1 | FADD | BIRC3 | TNF | CASP8 | MAPK8 | E2F1 | TP53 | CASP3 | FASLG | MAP3K5 | CASP2 | DAXX | CASP10 | ATM) & !(BCL2 | HIF1A)\nTNFRSF1B   (TNFRSF1A | TNF)\nMAP3K5     (TNFRSF1A | TRADD | E2F1 | TNF | IFNG | MAPK1 | TRAF6 | DAXX) & !(AKT1 | RB1 | S100B | AKT3 | AKT2)\nIL2        (JUN | FOS | IL1A | NFKB1 | IL5 | CREB1 | IL6 | IKBKG | IL1B) & !(MAP3K7 | CSF3 | CSF2 | CD40LG)\nTNFAIP3    (RELA | TNF | TNFRSF1A | NFKB1)\nRAC1       (TNFRSF1A | CDKN1A | PIK3CA | PTEN | EPHB2 | EGFR | EDN1 | NGFR | GNAI1 | SHC1 | PTK2B | LYN | VEGFA | GNG2 | PTK2 | LAMB2 | SOS1) & !(TP53)\nCHUK       (TNFRSF1A | CASP8 | TNF | TRADD | TRAF2 | RIPK1 | FADD | MAP3K7 | AKT1 | MAP4K4 | MYD88 | MAPK3 | IL1A | FASLG | MAP3K5 | TNFRSF10B | FLNA | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | TP63 | AKT3 | AKT2 | IKBKG | RIPK2 | IRAK1 | NGFR | NOTCH1)\nTRAF5      (TRADD | RELA | NFKB1 | NFKB2)\nTNFRSF10B  (TP53 | FASLG | NFKB1 | NOTCH1)\nNFKB1      (TRADD | FADD | MAP3K7 | TNF | TNFRSF1A | TRAF2 | RIPK1 | PIK3CA | AKT1 | TRAF1 | IL23A | BDNF | SUCLA2 | MAPK1 | RAC1 | MAPK14 | SQSTM1 | TRAF6 | TICAM1 | EGFR | PARP1 | PRKCZ | MAP3K1 | EDN1 | CASP10 | ATM | PRNP | CSF2 | IKBKG | RIPK2 | IRAK1 | NGFR | IL12B | PRKCD | LYN) & !(E2F1 | BAG1 | CDKN2A | CUL1 | TSC22D3 | HSPB1 | CDKN2A)\nKRT18      (CASP3 | AR | CDK1)\nMAP2K7     (TRAF2 | RIPK1 | CASP8 | BIRC3 | MAP3K7 | TNF | TNFRSF1A | TRADD | TRAF1 | FASLG | MAP3K5 | RAC1 | CASP2 | FLNA | MAP3K1 | DAXX | RIPK2 | SH3RF1 | CDC42)\nMAP2K1     (TRAF2 | MAP3K7 | PIK3CA | IL2 | RAC1 | MAPK14 | EGFR | MAP3K1 | PAK2 | CSF2 | PRKCD | SHC1) & !(PPP2CA | CDK1)\nCASP2      (CASP3 | TRADD | TP73 | CCND3) & !(BIRC2 | S100B | AR)\nSTAT1      (MAPK8 | CSF3 | IL23A | MAPK11 | IFNG | MAPK1 | IL2 | MAPK9 | EPHB2 | MAPK14 | EGFR | AR | IL6 | IL12B | PRKCD | LYN | FGFR2 | PTK2) & !(CCND1 | CYLD)\nMAPK9      (TRAF2 | MAPK8 | MAP2K3 | BDNF | MAP3K5 | RAC1 | MAP2K7 | MAP2K1 | MAPK14 | TRAF6 | MAP2K4 | PRKCZ | CD40LG | NGFR | CDC42) & !(DUSP4)\nEPHB2      (TRAF2 | TGFB1 | MAPK14 | LYN | FGR) & !(PPP2CA)\nFLNA       (AKT1 | PRKCD) & !(PPP3CA)\nPPP2CA     (CDK3 | PPP2R5C) & !(MTOR)\nNFKB2      (TP53 | CUL1) & !(MYC | TSC22D3)\nS100B      (IFNG) & !(TP53)\nMAPK14     (RIPK1 | TNF | TRAF2 | MAP3K7 | MAPK8 | PIK3CA | MAP2K3 | MAPK11 | TGFB1 | MAP3K5 | IL2 | RAC1 | MAP2K7 | TRAF6 | MAP2K4 | MAP3K1 | EDN1 | PAK2 | RIPK2 | CD40LG | ZAP70 | GNAI1 | BMP2 | PTK2B | LYN | CDC42 | GNG2) & !(DUSP4)\nSQSTM1     (IKBKB | CDK1)\nOTUD7B     (MAP3K7 | CDK4 | AKT1 | CDK6 | MAPK1 | IRAK1)\nTRAF6      (RELA | MYD88 | IL1A | TGFB1 | NFKB1 | NFKB2 | SQSTM1 | TICAM1 | ATM | IRAK1 | IL1B | HSPB1) & !(TNFAIP3 | PSEN1)\nTICAM1     (PIK3CA | TRAF2) & !(TRAF1 | TNFAIP3)\nEGFR       (TP53 | INS | TGFB1 | CXCL8 | FASLG | PPP2CA | AR | EDN1 | EGR1 | PTK2B | LYN | RARA | NOTCH1 | FGR | VEGFA) & !(RIPK1 | PTEN | MAPK11 | MAPK14 | TRAF6 | PRKCD | CDK1 | CDC42)\nRNF11      !(AKT1)\nPARP1      (INS | SUCLA2 | MAPK1 | ILK) & !(RIPK1 | BCL2 | CASP7)\nHSP90AA1   (MYC | PPARA | IL2 | ZAP70) & !(IFNG)\nMAP2K4     (FADD | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | BIRC3 | MAP3K7 | FASLG | MAP3K5 | RAC1 | MAP2K7 | MAP2K1 | FLNA | DAXX | CASP10 | CD40LG | SH3RF1 | ROCK1) & !(AKT1 | AKT3 | AKT2)\nPRKCZ      (PIK3CA | INS | IL2 | SHC1 | ROCK1 | CDC42) & !(PPP2CA)\nMAP3K1     (AKT1 | CASP3 | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | MAP4K4 | TRAF1 | MYD88 | IL1A | IFNG | CASP7 | TNFRSF1B | RAC1 | TNFRSF10B | TRAF6 | EGFR | PAK2 | CD40LG | IRAK1 | LAT | CDC42)\nAR         (MAPK8 | RXRA | TGFB1 | MAPK14 | HSP90AA1 | MAP3K1 | EDN1 | SIRT1 | SMAD4 | CDK1 | TRIM24 | GSN) & !(CASP8 | PTEN | E2F1 | RELA | TP53 | CASP7 | DAXX | EGR1)\nTP73       (CASP8 | E2F1 | TP53 | CASP3 | MAPK11 | MAPK14 | TFDP1 | PRKCD) & !(SIRT1 | CDK1)\nEIF4G2     (CASP8 | CASP9 | CASP7 | CASP2 | CASP10 | CDK1)\nEDN1       (JUN | FOS | TNF | PPARA | TGFB1 | CREB1 | HIF1A) & !(VEGFA)\nPAK2       (CASP8 | CASP3 | TGFB1 | RAC1 | CDC42)\nRALBP1     (CASP8)\nPSEN1      (CASP8 | TNF | CASP3 | CASP7 | MAPK9 | PRKCZ) & !(ELK1)\nALPI       (CASP8 | CASP10) & !(NFKB1 | DIABLO)\nCBL        (CDK4 | AKT1 | INS | IFNG | IL2 | PRKCZ | IRS1 | PRKCD | PTK2B | FGR)\n\n**Warning:** The following gene/node names were modified to remove special characters: COMPLEX:P19838_Q04206, COMPLEX:P20248_P24941"
}

**Tool Output:**

source                 target                 Effect
TNFRSF1A               MAP4K4                 stimulation
MAP4K4                 TNF                    inhibition
TNF                    TNFRSF1A               stimulation
TRADD                  TRAF1                  stimulation
TRAF1                  TNF                    inhibition
TNF                    TRADD                  inhibition
TRAF2                  TRAF1                  stimulation
RIPK1                  MAP4K4                 stimulation
TRADD                  RIPK1                  stimulation
FADD                   MYD88                  inhibition
MYD88                  TNF                    stimulation
TRADD                  FADD                   stimulation
TNF                    CASP8                  stimulation
CFLAR                  TNF                    inhibition
TNF                    MAPK8                  stimulation
MAPK8                  CFLAR                  inhibition
BCL2                   MYC                    stimulation
MYC                    TNF                    stimulation
TNF                    MAPK3                  stimulation
MAPK8                  BAX                    stimulation
MAPK3                  MCL1                   stimulation
XIAP                   PTEN                   stimulation
PTEN                   TNF                    inhibition
TNF                    RELA                   stimulation
RELA                   XIAP                   stimulation
BIRC2                  CFLAR                  inhibition
TRADD                  BIRC2                  stimulation
BIRC3                  MAP4K4                 stimulation
TNF                    CSF3                   stimulation
CSF3                   BIRC3                  stimulation
CYLD                   TNF                    inhibition
TNF                    IKBKB                  stimulation
NFKBIA                 IL23A                  stimulation
IL23A                  TNF                    stimulation
TNF                    NFKBIA                 inhibition
RELA                   PPARA                  inhibition
PPARA                  TNF                    inhibition
MAP3K7                 MAP2K3                 stimulation
MAP2K3                 TNF                    inhibition
TNF                    IL1A                   stimulation
IL1A                   MAP3K7                 stimulation
MAPK8                  INS                    inhibition
INS                    TNF                    inhibition
JUN                    LPL                    inhibition
LPL                    TNF                    stimulation
TNF                    JUN                    stimulation
FOS                    TNF                    stimulation
MAPK3                  FOS                    stimulation
PIK3CA                 MAPK11                 inhibition
MAPK11                 TNF                    inhibition
TNF                    BDNF                   stimulation
BDNF                   PIK3CA                 stimulation
AKT1                   RXRA                   stimulation
RXRA                   TNF                    stimulation
TNF                    AKT1                   stimulation
TNF                    TGFB1                  inhibition
TGFB1                  PTEN                   stimulation
MTOR                   IFNG                   stimulation
IFNG                   TNF                    stimulation
TNF                    CXCL8                  stimulation
CXCL8                  MTOR                   stimulation
CCND1                  TNF                    inhibition
MAPK3                  CCND1                  stimulation
RB1                    TNF                    stimulation
MAPK3                  CDK4                   stimulation
E2F1                   MYC                    stimulation
MAPK3                  E2F1                   stimulation
MAPK3                  MYC                    stimulation
TP53                   PTEN                   stimulation
MAPK3                  TP53                   stimulation
CDKN1A                 CCND1                  inhibition
TNF                    CDK6                   inhibition
CDK6                   CDKN1A                 inhibition
CASP3                  PTEN                   stimulation
TNF                    CASP3                  stimulation
MAPK3                  CASP9                  inhibition
TNF                    SUCLA2                 stimulation
SUCLA2                 APAF1                  stimulation
TRADD                  MAPK1                  inhibition
MAPK1                  TNFRSF1A               inhibition
TNFRSF1A               TRADD                  stimulation
TNFRSF1A               TRAF2                  stimulation
RIPK1                  FASLG                  stimulation
FASLG                  TNFRSF1A               stimulation
TNFRSF1A               RIPK1                  stimulation
FADD                   MAPK1                  stimulation
TNFRSF1A               FADD                   stimulation
CASP8                  CASP7                  stimulation
TNFRSF1A               CASP8                  stimulation
TNFRSF1A               MAPK3                  stimulation
TNFRSF1A               BID                    stimulation
BID                    BAX                    stimulation
XIAP                   CASP7                  inhibition
TNFRSF1A               RELA                   stimulation
BIRC2                  FASLG                  inhibition
TNFRSF1A               TNFRSF1B               stimulation
TNFRSF1B               BIRC2                  stimulation
BIRC3                  FASLG                  inhibition
RELA                   BIRC3                  stimulation
CYLD                   TNFRSF1A               inhibition
TNFRSF1A               MAP3K5                 stimulation
MAP3K5                 IKBKB                  stimulation
IL2                    TNFRSF1A               stimulation
TNFRSF1A               NFKBIA                 inhibition
RELA                   TNFAIP3                stimulation
TNFAIP3                TNFRSF1A               stimulation
MAP3K7                 IL2                    inhibition
TRAF2                  MAP3K7                 stimulation
MAPK8                  FASLG                  stimulation
MAPK3                  MAPK8                  stimulation
JUN                    FASLG                  stimulation
RELA                   JUN                    stimulation
FOS                    FASLG                  stimulation
PIK3CA                 MAPK1                  inhibition
TNFRSF1A               RAC1                   stimulation
RAC1                   PIK3CA                 stimulation
TNFRSF1A               CASP3                  stimulation
CASP3                  AKT1                   inhibition
RELA                   PTEN                   inhibition
TNFRSF1A               CHUK                   stimulation
CHUK                   MTOR                   stimulation
TP53                   FASLG                  stimulation
MAP3K5                 CDKN1A                 stimulation
CASP3                  CASP7                  stimulation
CASP9                  CASP7                  stimulation
APAF1                  CASP7                  stimulation
TRADD                  CASP8                  stimulation
CFLAR                  TRADD                  inhibition
TRADD                  RELA                   stimulation
RELA                   BCL2                   stimulation
TRADD                  BID                    stimulation
MAPK1                  MCL1                   stimulation
BIRC3                  CFLAR                  inhibition
CYLD                   TRADD                  inhibition
TRADD                  IKBKB                  stimulation
TRADD                  MAP3K5                 stimulation
MAP3K5                 MAPK8                  stimulation
RELA                   FOS                    stimulation
TRADD                  TRAF5                  stimulation
TRAF5                  PIK3CA                 stimulation
AKT1                   CFLAR                  inhibition
IKBKB                  MTOR                   stimulation
RELA                   CCND1                  stimulation
MAPK1                  CDK4                   stimulation
MAPK1                  E2F1                   stimulation
MAP3K5                 MYC                    stimulation
TP53                   TNFRSF10B              stimulation
TNFRSF10B              TRADD                  stimulation
TRADD                  NFKB1                  stimulation
NFKB1                  TP53                   stimulation
CASP3                  KRT18                  stimulation
KRT18                  TRADD                  inhibition
FADD                   CASP3                  stimulation
BIRC2                  CASP9                  inhibition
BIRC2                  APAF1                  inhibition
RIPK1                  RELA                   stimulation
RELA                   TRAF2                  stimulation
TRAF2                  RIPK1                  stimulation
TRAF2                  MAP2K7                 stimulation
MAP2K7                 FADD                   inhibition
TRAF1                  TRAF2                  stimulation
TRAF2                  CASP8                  stimulation
TRAF2                  BIRC3                  stimulation
TRAF2                  MAP2K1                 stimulation
MAP2K1                 BCL2                   stimulation
TRAF2                  BID                    stimulation
MAP2K1                 MCL1                   stimulation
TRAF2                  TP53                   stimulation
TP53                   XIAP                   stimulation
BIRC2                  CASP2                  inhibition
CASP2                  TRAF2                  stimulation
TRAF2                  BIRC2                  stimulation
CYLD                   TRAF2                  inhibition
TRAF2                  IKBKB                  stimulation
TRAF2                  NFKBIA                 stimulation
TRAF2                  RELA                   stimulation
MAPK8                  STAT1                  stimulation
STAT1                  TRAF2                  inhibition
TRAF2                  MAPK8                  stimulation
TRAF2                  MAPK9                  stimulation
MAPK9                  JUN                    stimulation
PIK3CA                 RELA                   stimulation
TRAF2                  EPHB2                  stimulation
EPHB2                  PIK3CA                 stimulation
AKT1                   FLNA                   stimulation
FLNA                   TRAF2                  inhibition
MAPK8                  AKT1                   stimulation
MTOR                   PPP2CA                 inhibition
PPP2CA                 TRAF2                  inhibition
CCND1                  STAT1                  inhibition
E2F1                   RELA                   stimulation
MYC                    NFKB2                  inhibition
NFKB2                  TRAF2                  stimulation
TP53                   S100B                  inhibition
S100B                  TRAF2                  inhibition
CASP3                  CASP2                  stimulation
BIRC3                  CASP3                  inhibition
BIRC3                  CASP9                  inhibition
BIRC3                  APAF1                  inhibition
FADD                   RIPK1                  stimulation
RIPK1                  MAP2K7                 stimulation
CASP8                  RIPK1                  inhibition
RELA                   CASP8                  inhibition
CFLAR                  RIPK1                  inhibition
RIPK1                  MAPK14                 stimulation
MAPK14                 CFLAR                  stimulation
BCL2                   CASP8                  inhibition
RIPK1                  BID                    stimulation
BIRC2                  RIPK1                  stimulation
RELA                   BIRC2                  stimulation
BIRC3                  RIPK1                  stimulation
IKBKB                  SQSTM1                 stimulation
SQSTM1                 RIPK1                  stimulation
RIPK1                  IKBKB                  stimulation
NFKBIA                 BIRC3                  stimulation
MAP3K7                 OTUD7B                 stimulation
OTUD7B                 RIPK1                  inhibition
TRAF6                  MAP3K7                 stimulation
MAP2K7                 MAPK8                  stimulation
PIK3CA                 TICAM1                 stimulation
TICAM1                 RIPK1                  stimulation
RIPK1                  EGFR                   inhibition
EGFR                   PIK3CA                 stimulation
AKT1                   RNF11                  inhibition
RNF11                  RIPK1                  inhibition
TRAF6                  AKT1                   stimulation
CDK4                   OTUD7B                 stimulation
E2F1                   CASP8                  stimulation
RIPK1                  PARP1                  inhibition
PARP1                  E2F1                   stimulation
MYC                    HSP90AA1               stimulation
HSP90AA1               RIPK1                  stimulation
RELA                   MYC                    inhibition
TP53                   BIRC3                  inhibition
TRAF6                  TP53                   stimulation
MAPK14                 CDKN1A                 stimulation
CASP2                  RIPK1                  stimulation
MAPK14                 CASP3                  inhibition
CASP8                  MAP2K7                 stimulation
FADD                   CASP8                  stimulation
FADD                   NFKB1                  stimulation
NFKB1                  BCL2                   stimulation
FADD                   BID                    stimulation
CASP3                  MCL1                   inhibition
XIAP                   TP53                   stimulation
TP53                   FADD                   stimulation
NFKB1                  XIAP                   stimulation
BIRC2                  FADD                   inhibition
NFKB1                  BIRC2                  stimulation
BIRC3                  MAP2K7                 stimulation
NFKB1                  BIRC3                  stimulation
FADD                   IKBKB                  stimulation
IKBKB                  RELA                   stimulation
MAP3K7                 MAP2K7                 stimulation
MYD88                  MAP3K7                 stimulation
MAPK8                  TP53                   stimulation
FADD                   MAP2K4                 stimulation
MAP2K4                 MAPK8                  stimulation
JUN                    TP53                   inhibition
NFKB1                  JUN                    stimulation
FOS                    TP53                   inhibition
NFKB1                  FOS                    stimulation
PIK3CA                 PRKCZ                  stimulation
AKT1                   MAP3K1                 stimulation
MAP3K1                 FADD                   inhibition
STAT1                  FADD                   stimulation
NFKB1                  CCND1                  stimulation
E2F1                   TP53                   stimulation
MYC                    CFLAR                  inhibition
NFKB1                  MYC                    stimulation
CASP3                  CDKN1A                 stimulation
CASP3                  MAP3K1                 stimulation
MAPK1                  CASP9                  inhibition
CFLAR                  CASP8                  inhibition
CASP8                  AR                     inhibition
AR                     CFLAR                  stimulation
CASP8                  CASP3                  stimulation
CASP3                  BCL2                   inhibition
CASP8                  TP73                   stimulation
TP73                   BAX                    stimulation
TP53                   CASP8                  stimulation
CASP8                  EIF4G2                 stimulation
EIF4G2                 XIAP                   stimulation
BIRC2                  CASP8                  inhibition
EIF4G2                 BIRC2                  stimulation
BIRC3                  CASP8                  inhibition
CASP8                  IKBKB                  stimulation
MAP3K7                 MAPK3                  stimulation
MAPK3                  CASP8                  inhibition
JUN                    EDN1                   stimulation
EDN1                   CASP8                  stimulation
CASP8                  PAK2                   stimulation
PAK2                   JUN                    stimulation
FOS                    EDN1                   stimulation
PIK3CA                 MAPK3                  inhibition
CASP8                  RALBP1                 stimulation
RALBP1                 AKT1                   inhibition
MTOR                   BCL2                   stimulation
CASP8                  CHUK                   stimulation
CASP8                  PSEN1                  stimulation
PSEN1                  TP53                   stimulation
CDKN1A                 E2F1                   inhibition
CASP2                  CASP8                  stimulation
CASP8                  ALPI                   stimulation
ALPI                   CASP9                  inhibition
TP53                   CFLAR                  stimulation
MAP3K7                 MAPK8                  stimulation
PIK3CA                 MAPK8                  stimulation
PTEN                   AR                     inhibition
MTOR                   AKT1                   stimulation
CDK4                   CBL                    stimulation
CBL                    CFLAR                  inhibition
E2F1                   DDB2                   stimulation
DDB2                   CFLAR                  stimulation
CFLAR                  DAXX                   inhibition
DAXX                   TP53                   stimulation
CFLAR                  CASP10                 inhibition
CASP10                 CASP3                  stimulation
CASP10                 APAF1                  stimulation
BAX                    BAD                    inhibition
BCL2                   BAX                    inhibition
TP53                   BCL2                   inhibition
BIRC2                  CASP3                  inhibition
IKBKB                  IRS1                   inhibition
IRS1                   BCL2                   inhibition
BCL2                   ATM                    stimulation
ATM                    NFKBIA                 stimulation
JUN                    IL5                    stimulation
IL5                    BCL2                   inhibition
FOS                    IL5                    stimulation
BCL2                   APEX1                  stimulation
APEX1                  FOS                    stimulation
BCL2                   CTNNB1                 stimulation
CTNNB1                 PIK3CA                 stimulation
ATM                    AKT1                   stimulation
PTEN                   CREB1                  inhibition
CREB1                  BCL2                   stimulation
BCL2                   TERT                   stimulation
CCND1                  CDK6                   stimulation
CDK6                   BCL2                   inhibition
BCL2                   CCND1                  inhibition
CDK4                   E2F2                   inhibition
E2F2                   BCL2                   stimulation
MYC                    CDK4                   stimulation
BCL2                   PARP1                  inhibition
MYC                    BAG1                   stimulation
BAG1                   BCL2                   stimulation
PARP1                  TP53                   stimulation
MYC                    CDKN1A                 inhibition
BCL2                   PRNP                   stimulation
PRNP                   CASP3                  stimulation
BCL2                   APAF1                  inhibition
APAF1                  CASP9                  stimulation
MCL1                   BAX                    inhibition
TP53                   BAX                    stimulation
BAX                    DIABLO                 stimulation
CASP3                  BAX                    stimulation
BIRC3                  BID                    stimulation
IKBKB                  TP63                   stimulation
TP63                   BAX                    stimulation
RELA                   BAX                    inhibition
AKT1                   BAX                    inhibition
PTEN                   SP1                    inhibition
SP1                    BAX                    stimulation
MTOR                   RPS6KB1                stimulation
RPS6KB1                BAX                    stimulation
CDK4                   UBB                    stimulation
UBB                    BAX                    inhibition
E2F1                   TP73                   stimulation
MYC                    BAX                    stimulation
BAD                    TP53                   stimulation
BAX                    CYCS                   stimulation
CYCS                   CASP3                  stimulation
BAX                    APAF1                  stimulation
RELA                   CSF2                   inhibition
CSF2                   MCL1                   stimulation
JUN                    CSF2                   stimulation
FOS                    CSF2                   stimulation
AKT1                   MCL1                   stimulation
PTEN                   E2F1                   stimulation
E2F1                   MCL1                   inhibition
MTOR                   HIF1A                  stimulation
HIF1A                  MCL1                   stimulation
CCND1                  TFDP1                  inhibition
TFDP1                  MCL1                   inhibition
CDK4                   TFDP1                  inhibition
MYC                    BCL2L11                stimulation
BCL2L11                MCL1                   inhibition
CDKN1A                 TFDP1                  inhibition
BAD                    CASP9                  inhibition
MCL1                   COX5B                  inhibition
COX5B                  APAF1                  stimulation
XIAP                   MAP3K7                 stimulation
MAP3K7                 IKBKB                  stimulation
XIAP                   CASP3                  inhibition
CASP3                  NFKBIA                 stimulation
CASP3                  RELA                   inhibition
MAP3K7                 AKT3                   stimulation
AKT3                   XIAP                   stimulation
AKT1                   XIAP                   stimulation
XIAP                   MAPK8                  stimulation
MAPK8                  JUN                    stimulation
MAPK8                  FOS                    stimulation
PIK3CA                 AKT2                   stimulation
AKT2                   XIAP                   stimulation
PTEN                   PIK3CA                 inhibition
MTOR                   AKT2                   stimulation
XIAP                   IL6                    stimulation
IL6                    CDK4                   stimulation
MYC                    BIRC5                  stimulation
BIRC5                  XIAP                   stimulation
MAPK8                  MYC                    stimulation
CASP9                  EIF4G2                 stimulation
XIAP                   APAF1                  inhibition
BIRC3                  BIRC2                  stimulation
BIRC2                  IKBKG                  stimulation
IKBKG                  NFKBIA                 stimulation
IKBKG                  RELA                   stimulation
MAP3K7                 NFKB1                  stimulation
BIRC2                  RIPK2                  stimulation
RIPK2                  MAP3K7                 stimulation
MAPK8                  ELK1                   stimulation
ELK1                   BIRC2                  stimulation
RIPK2                  MAPK8                  stimulation
JUN                    CD40LG                 stimulation
CD40LG                 BIRC2                  stimulation
FOS                    CD40LG                 stimulation
AKT1                   HTRA2                  inhibition
HTRA2                  BIRC2                  inhibition
FASLG                  AKT1                   stimulation
NFKB2                  BIRC2                  stimulation
BIRC3                  RIPK2                  stimulation
RIPK2                  IKBKB                  stimulation
HTRA2                  BIRC3                  inhibition
NFKB2                  BIRC3                  stimulation
IKBKB                  IRAK1                  stimulation
IRAK1                  MAP3K7                 stimulation
AKT1                   IKBKB                  stimulation
IKBKB                  NGFR                   stimulation
NGFR                   MAPK8                  stimulation
FASLG                  IKBKB                  stimulation
AKT2                   IKBKB                  stimulation
IKBKB                  FOXO3                  inhibition
FOXO3                  PIK3CA                 stimulation
IKBKB                  CDKN2A                 inhibition
CDKN2A                 CCND1                  inhibition
CDKN2A                 CDK4                   inhibition
E2F1                   MAP3K5                 stimulation
NGFR                   TP53                   stimulation
CASP3                  IKBKB                  inhibition
IKBKB                  NFE2L2                 inhibition
NFE2L2                 CASP3                  stimulation
IKBKB                  BAD                    inhibition
RELA                   NFKBIA                 inhibition
IL23A                  RELA                   stimulation
MAPK3                  NFKBIA                 inhibition
RXRA                   NFKBIA                 stimulation
IL2                    MAPK8                  stimulation
JUN                    NFKBIA                 inhibition
COMPLEX:P19838_Q04206  JUN                    stimulation
FOS                    IL12B                  stimulation
IL12B                  NFKBIA                 stimulation
IL23A                  PIK3CA                 stimulation
IL2                    AKT1                   stimulation
MTOR                   RPS6KA2                stimulation
RPS6KA2                NFKBIA                 inhibition
IL2                    MTOR                   stimulation
COMPLEX:P19838_Q04206  CCND1                  stimulation
E2F1                   SIRT1                  stimulation
MYC                    CUL1                   stimulation
CUL1                   NFKBIA                 inhibition
IL2                    MYC                    stimulation
MAPK3                  RELA                   stimulation
STAT1                  RELA                   inhibition
JUN                    IL1B                   stimulation
IL1B                   RELA                   stimulation
FOS                    IL1B                   stimulation
AKT1                   TSC22D3                stimulation
TSC22D3                RELA                   inhibition
RELA                   TGFB1                  stimulation
TGFB1                  AKT1                   stimulation
PPP2CA                 RELA                   inhibition
RELA                   CXCL8                  stimulation
FOS                    CDK4                   stimulation
CUL1                   RELA                   stimulation
TP53                   RAC1                   inhibition
RAC1                   RELA                   stimulation
RELA                   EGR1                   stimulation
EGR1                   TP53                   stimulation
EGR1                   CDKN1A                 stimulation
MAPK8                  LAT                    inhibition
LAT                    MAP3K7                 stimulation
JUN                    SMAD7                  stimulation
SMAD7                  MAP3K7                 stimulation
IL2                    JUN                    stimulation
FOS                    SMAD7                  stimulation
MAPK11                 MAP3K7                 inhibition
MAP3K7                 ZAP70                  stimulation
ZAP70                  PIK3CA                 stimulation
AKT1                   GNAI1                  stimulation
GNAI1                  MAP3K7                 stimulation
MAP3K7                 BMP2                   inhibition
BMP2                   PTEN                   inhibition
PPP2CA                 MAP3K7                 inhibition
MYC                    TRIM8                  inhibition
TRIM8                  MAP3K7                 stimulation
MAPK8                  CDKN1A                 stimulation
MAP3K1                 MAP3K7                 stimulation
MAP3K7                 PRKCD                  stimulation
PRKCD                  CASP3                  stimulation
JUN                    IL2                    stimulation
FOS                    IL2                    stimulation
INS                    PIK3CA                 stimulation
AKT1                   SH3RF1                 inhibition
SH3RF1                 MAPK8                  stimulation
AKT1                   PTEN                   inhibition
AKT2                   MAPK8                  inhibition
MAPK8                  SHC1                   stimulation
SHC1                   MTOR                   stimulation
MAPK8                  SMAD4                  stimulation
SMAD4                  CCND1                  stimulation
CDKN1A                 CDK4                   inhibition
MYC                    PTK2B                  inhibition
PTK2B                  MAPK8                  stimulation
TP53                   DUSP4                  stimulation
CDKN1A                 RAC1                   stimulation
RAC1                   MAPK8                  stimulation
CASP3                  ROCK1                  stimulation
ROCK1                  MAPK8                  stimulation
MAPK8                  NAIP                   inhibition
NAIP                   CASP3                  inhibition
CASP9                  LYN                    inhibition
LYN                    MAPK8                  stimulation
MAPK8                  RARA                   stimulation
RARA                   CASP9                  stimulation
FOS                    JUN                    stimulation
JUN                    SMAD4                  stimulation
SMAD4                  FOS                    stimulation
PIK3CA                 ILK                    stimulation
ILK                    JUN                    stimulation
JUN                    PTEN                   inhibition
AKT1                   JUN                    stimulation
PTEN                   NOTCH1                 stimulation
NOTCH1                 JUN                    inhibition
AKT2                   JUN                    stimulation
JUN                    CCND1                  stimulation
CDK4                   MEF2D                  inhibition
MEF2D                  JUN                    stimulation
JUN                    CDK4                   stimulation
E2F1                   AR                     inhibition
AR                     JUN                    stimulation
JUN                    CCND3                  stimulation
CCND3                  E2F1                   inhibition
JUN                    MYC                    inhibition
TP53                   VDR                    stimulation
VDR                    JUN                    inhibition
CDKN1A                 CDK3                   inhibition
CDK3                   JUN                    stimulation
JUN                    CDKN1A                 stimulation
CASP3                  ARHGDIB                stimulation
ARHGDIB                JUN                    stimulation
JUN                    IFNG                   stimulation
IFNG                   CASP3                  stimulation
LYN                    JUN                    inhibition
JUN                    BCL2L1                 stimulation
BCL2L1                 CASP9                  inhibition
JUN                    ACHE                   stimulation
ACHE                   APAF1                  stimulation
FOS                    PTEN                   inhibition
AKT1                   FOS                    stimulation
NOTCH1                 FOS                    inhibition
AKT2                   FOS                    stimulation
FOS                    CCND1                  stimulation
CDK4                   SMAD4                  stimulation
MYC                    HNRNPR                 stimulation
HNRNPR                 FOS                    stimulation
VDR                    FOS                    inhibition
IL1B                   CDKN1A                 stimulation
CASP3                  PPP3CA                 stimulation
PPP3CA                 FOS                    inhibition
LYN                    FOS                    inhibition
FOS                    CDK1                   stimulation
CDK1                   CASP9                  inhibition
APAF1                  MRTFA                  stimulation
MRTFA                  FOS                    stimulation
TP53                   APAF1                  stimulation
AKT1                   FGR                    stimulation
FGR                    PIK3CA                 stimulation
PIK3CA                 CDC42                  stimulation
CDC42                  PTEN                   stimulation
MTOR                   IRS4                   inhibition
IRS4                   PIK3CA                 stimulation
PIK3CA                 MTOR                   stimulation
CCND1                  VEGFA                  inhibition
VEGFA                  PIK3CA                 stimulation
PIK3CA                 CCND1                  stimulation
E2F1                   FGFR2                  stimulation
FGFR2                  PIK3CA                 stimulation
MYC                    GNG2                   inhibition
GNG2                   PIK3CA                 stimulation
PIK3CA                 MYC                    stimulation
TP53                   PTK2                   inhibition
PTK2                   PIK3CA                 stimulation
CASP3                  LAMB2                  stimulation
LAMB2                  PIK3CA                 stimulation
PIK3CA                 PRKCD                  stimulation
LYN                    PIK3CA                 stimulation
PIK3CA                 RAC1                   stimulation
RAC1                   APAF1                  stimulation
AKT1                   RHEB                   stimulation
RHEB                   MTOR                   stimulation
CDK4                   PELP1                  stimulation
PELP1                  AKT1                   stimulation
SIRT1                  AKT1                   stimulation
AKT1                   TP53BP1                inhibition
TP53BP1                TP53                   stimulation
CDKN1A                 COMPLEX:P20248_P24941  inhibition
COMPLEX:P20248_P24941  AKT1                   stimulation
AKT1                   HSPB1                  inhibition
HSPB1                  CASP3                  inhibition
CASP9                  EIF4E                  stimulation
EIF4E                  AKT1                   stimulation
AKT1                   APAF1                  inhibition
PTEN                   SOS1                   inhibition
SOS1                   MTOR                   stimulation
NOTCH1                 CCND1                  stimulation
E2F1                   EGR1                   stimulation
EGR1                   PTEN                   stimulation
HSP90AA1               PTEN                   stimulation
NOTCH1                 TP53                   inhibition
NOTCH1                 CDKN1A                 stimulation
E2F1                   CASP9                  stimulation
E2F1                   APAF1                  stimulation
MYC                    TSC2                   inhibition
TSC2                   MTOR                   stimulation
RPS6KB1                MYC                    stimulation
TP53                   EGFR                   stimulation
EGFR                   MTOR                   stimulation
MTOR                   TRIM24                 stimulation
TRIM24                 TP53                   inhibition
CCND1                  CDK4                   stimulation
E2F1                   DDAH2                  stimulation
DDAH2                  CCND1                  stimulation
MYC                    CCND1                  stimulation
CCND1                  E2F3                   inhibition
E2F3                   MYC                    stimulation
EGFR                   CCND1                  stimulation
E2F3                   CDKN1A                 stimulation
TFDP1                  APAF1                  stimulation
CDKN2A                 CDK4                   inhibition
SMAD4                  MYC                    stimulation
CDK4                   XPO1                   stimulation
XPO1                   TP53                   inhibition
SMAD4                  CDKN1A                 stimulation
E2F1                   CASP3                  stimulation
CUL1                   E2F1                   stimulation
EGFR                   E2F1                   stimulation
TP73                   CDKN1A                 inhibition
RAC1                   MYC                    stimulation
PTK2B                  TP53                   stimulation
CASP3                  RB1                    inhibition
RB1                    MYC                    inhibition
BIRC5                  CASP9                  inhibition
MYC                    HSPA4                  stimulation
HSPA4                  APAF1                  inhibition
CDKN1A                 CCNE1                  inhibition
CCNE1                  TP53                   stimulation
CASP3                  PPP2R5C                inhibition
PPP2R5C                TP53                   stimulation
GSN                    CASP9                  inhibition
TNF                    MAP4K4                 stimulation
CSF3                   TNF                    inhibition
TNF                    IL23A                  stimulation
TNF                    MAP2K3                 stimulation
TNF                    LPL                    stimulation
TNF                    IFNG                   inhibition
TNF                    MAPK1                  stimulation
TNF                    BID                    stimulation
TNF                    TNFRSF1B               stimulation
TNF                    MAP3K5                 stimulation
TNF                    TNFAIP3                stimulation
TNFAIP3                TNF                    stimulation
TNF                    CHUK                   stimulation
TNF                    NFKB1                  stimulation
TNF                    MAP2K7                 stimulation
S100B                  TNF                    inhibition
TNF                    MAPK14                 stimulation
MAPK14                 TNF                    inhibition
TNF                    MAP2K4                 stimulation
TNF                    MAP3K1                 stimulation
TNF                    EDN1                   stimulation
TNF                    PSEN1                  stimulation
TNF                    IRS1                   stimulation
TNF                    ATM                    stimulation
APEX1                  TNF                    inhibition
CREB1                  TNF                    stimulation
SP1                    TNF                    inhibition
TNF                    RPS6KB1                stimulation
TNF                    CSF2                   stimulation
CSF2                   TNF                    inhibition
TNF                    IL6                    stimulation
TNF                    IKBKG                  stimulation
TNF                    NFE2L2                 stimulation
COMPLEX:P19838_Q04206  TNF                    stimulation
IL12B                  TNF                    stimulation
TNF                    IL1B                   stimulation
TNF                    FGR                    stimulation
TNF                    IRS4                   stimulation
TNF                    PTK2                   stimulation
TNFRSF1A               MAP2K3                 stimulation
TNFRSF1B               TNFRSF1A               stimulation
TNFRSF1A               TNFAIP3                stimulation
TNFRSF1A               NFKB1                  stimulation
TNFRSF1A               MAP2K7                 stimulation
S100B                  TNFRSF1A               inhibition
TNFRSF1A               MAP2K4                 stimulation
TNFRSF1A               MAP3K1                 stimulation
TNFRSF1A               DAXX                   stimulation
TNFRSF1A               IKBKG                  stimulation
TRADD                  MAP4K4                 stimulation
TRADD                  MAP2K3                 stimulation
TRADD                  CHUK                   stimulation
TRADD                  MAP2K7                 stimulation
TRADD                  CASP2                  stimulation
S100B                  TRADD                  inhibition
TRADD                  MAP2K4                 stimulation
TRADD                  MAP3K1                 stimulation
TRADD                  IKBKG                  stimulation
TRAF2                  MAP2K3                 stimulation
TRAF2                  LPL                    stimulation
TRAF2                  MAPK11                 stimulation
TNFRSF1B               TRAF2                  stimulation
TNFAIP3                TRAF2                  inhibition
TRAF2                  CHUK                   stimulation
TRAF2                  NFKB1                  stimulation
TRAF2                  MAPK14                 stimulation
TRAF2                  TICAM1                 stimulation
TRAF2                  MAP2K4                 stimulation
TRAF2                  MAP3K1                 stimulation
TRAF2                  IKBKG                  stimulation
RIPK1                  MAP2K3                 stimulation
TNFAIP3                RIPK1                  inhibition
RIPK1                  CHUK                   stimulation
TNFRSF10B              RIPK1                  stimulation
RIPK1                  NFKB1                  stimulation
S100B                  RIPK1                  inhibition
RIPK1                  MAP2K4                 stimulation
RIPK1                  MAP3K1                 stimulation
CASP10                 RIPK1                  inhibition
RIPK1                  IKBKG                  stimulation
FADD                   MAP4K4                 stimulation
MYD88                  FADD                   stimulation
FADD                   CASP7                  stimulation
FADD                   CHUK                   stimulation
TNFRSF10B              FADD                   stimulation
S100B                  FADD                   inhibition
FADD                   CASP10                 stimulation
FADD                   IKBKG                  stimulation
RIPK2                  FADD                   inhibition
IFNG                   CASP8                  stimulation
MAPK1                  CASP8                  inhibition
CASP8                  BID                    stimulation
TNFRSF10B              CASP8                  stimulation
NFKB1                  CASP8                  inhibition
S100B                  CASP8                  inhibition
MAPK14                 CASP8                  inhibition
CASP8                  CASP10                 inhibition
CASP8                  TP63                   stimulation
CASP8                  IKBKG                  stimulation
CDK1                   CASP8                  inhibition
CASP8                  EIF4E                  stimulation
ATM                    CFLAR                  inhibition
BCL2                   BID                    inhibition
STAT1                  BCL2                   stimulation
PPP2CA                 BCL2                   stimulation
NFKB2                  BCL2                   stimulation
MAPK14                 BCL2                   inhibition
HSP90AA1               BCL2                   stimulation
EIF4G2                 BCL2                   stimulation
ATM                    BCL2                   inhibition
CTNNB1                 BCL2                   stimulation
BCL2                   CYCS                   inhibition
BCL2L11                BCL2                   inhibition
BCL2                   COX5B                  inhibition
IL6                    BCL2                   stimulation
BCL2L1                 BCL2                   stimulation
VEGFA                  BCL2                   stimulation
PPP2R5C                BCL2                   inhibition
PRKCZ                  BAX                    inhibition
PRNP                   BAX                    inhibition
BCL2L11                BAX                    stimulation
BAX                    COX5B                  stimulation
AKT3                   BAX                    inhibition
BAX                    HTRA2                  stimulation
BCL2L1                 BAX                    inhibition
IL6                    MCL1                   stimulation
CDK1                   MCL1                   inhibition
VEGFA                  MCL1                   stimulation
NFKB2                  XIAP                   stimulation
XIAP                   RIPK2                  stimulation
ELK1                   XIAP                   stimulation
HTRA2                  XIAP                   inhibition
BIRC2                  CASP7                  inhibition
BIRC3                  CASP7                  inhibition
S100B                  BIRC3                  inhibition
BIRC3                  MAP2K4                 stimulation
ELK1                   BIRC3                  stimulation
MAP4K4                 IKBKB                  stimulation
MYD88                  IKBKB                  stimulation
CHUK                   IKBKB                  stimulation
TNFRSF10B              IKBKB                  stimulation
FLNA                   IKBKB                  stimulation
SQSTM1                 IKBKB                  stimulation
TRAF6                  IKBKB                  stimulation
PRKCZ                  IKBKB                  stimulation
MAP3K1                 IKBKB                  stimulation
AKT3                   IKBKB                  stimulation
IKBKG                  IKBKB                  stimulation
IRAK1                  IKBKB                  stimulation
NGFR                   IKBKB                  stimulation
IKBKB                  COMPLEX:P19838_Q04206  inhibition
IKBKB                  TSC22D3                stimulation
IKBKB                  IRS4                   inhibition
TRAF1                  NFKBIA                 stimulation
IL23A                  NFKBIA                 stimulation
PPARA                  NFKBIA                 inhibition
MAPK1                  NFKBIA                 inhibition
TNFAIP3                NFKBIA                 inhibition
NFKB1                  NFKBIA                 stimulation
MAPK14                 NFKBIA                 inhibition
TRAF6                  NFKBIA                 stimulation
PRKCZ                  NFKBIA                 inhibition
MAP3K1                 NFKBIA                 stimulation
SP1                    NFKBIA                 inhibition
PRKCD                  NFKBIA                 inhibition
HSPB1                  NFKBIA                 inhibition
RELA                   TRAF1                  stimulation
TRAF1                  RELA                   stimulation
RELA                   IL23A                  stimulation
RELA                   LPL                    inhibition
MAPK1                  RELA                   stimulation
CHUK                   RELA                   stimulation
RELA                   TRAF5                  stimulation
NFKB1                  RELA                   stimulation
MAPK14                 RELA                   stimulation
SQSTM1                 RELA                   stimulation
RELA                   TRAF6                  stimulation
TRAF6                  RELA                   stimulation
PRKCZ                  RELA                   stimulation
MAP3K1                 RELA                   stimulation
RELA                   AR                     inhibition
RELA                   SP1                    stimulation
RELA                   IL6                    stimulation
RELA                   BIRC5                  stimulation
IRAK1                  RELA                   stimulation
NGFR                   RELA                   stimulation
RELA                   IL12B                  stimulation
IL12B                  RELA                   stimulation
RPS6KA2                RELA                   stimulation
SIRT1                  RELA                   inhibition
PRKCD                  RELA                   stimulation
RELA                   BCL2L1                 stimulation
RELA                   VEGFA                  stimulation
MAP4K4                 MAP3K7                 stimulation
CYLD                   MAP3K7                 stimulation
MAP3K7                 RXRA                   stimulation
MAP3K7                 TGFB1                  stimulation
TGFB1                  MAP3K7                 stimulation
MAP3K7                 CHUK                   stimulation
MAP3K7                 MAP2K1                 stimulation
EPHB2                  MAP3K7                 stimulation
MAP3K7                 MAPK14                 stimulation
TICAM1                 MAP3K7                 stimulation
MAP3K7                 MAP2K4                 stimulation
MAP3K7                 DAXX                   stimulation
MAP3K7                 TERT                   inhibition
BMP2                   MAP3K7                 stimulation
MAPK8                  PPARA                  stimulation
MAP2K3                 MAPK8                  stimulation
BDNF                   MAPK8                  stimulation
TGFB1                  MAPK8                  stimulation
MAPK1                  MAPK8                  inhibition
MAPK8                  BID                    stimulation
MAP2K1                 MAPK8                  stimulation
MAPK8                  MAPK9                  stimulation
MAPK8                  MAPK14                 stimulation
TRAF6                  MAPK8                  stimulation
PRKCZ                  MAPK8                  stimulation
MAP3K1                 MAPK8                  stimulation
MAPK8                  AR                     stimulation
EDN1                   MAPK8                  stimulation
MAPK8                  CREB1                  stimulation
MAPK8                  SP1                    stimulation
MAPK8                  RPS6KB1                stimulation
MAPK8                  IL6                    stimulation
CD40LG                 MAPK8                  stimulation
MAPK8                  COMPLEX:P19838_Q04206  stimulation
MAPK8                  SIRT1                  stimulation
IL1B                   MAPK8                  stimulation
GNAI1                  MAPK8                  stimulation
PRKCD                  MAPK8                  stimulation
ILK                    MAPK8                  stimulation
MAPK8                  BCL2L1                 inhibition
CDC42                  MAPK8                  stimulation
MAPK8                  IRS4                   inhibition
MAPK8                  TRIM24                 stimulation
MAPK8                  XPO1                   stimulation
JUN                    IL23A                  stimulation
MAPK11                 JUN                    stimulation
BDNF                   JUN                    stimulation
JUN                    TGFB1                  stimulation
JUN                    CXCL8                  stimulation
RB1                    JUN                    stimulation
MAPK1                  JUN                    stimulation
MAPK14                 JUN                    stimulation
MAP3K1                 JUN                    stimulation
JUN                    CTNNB1                 stimulation
JUN                    CREB1                  stimulation
JUN                    TERT                   inhibition
JUN                    BCL2L11                stimulation
AKT3                   JUN                    stimulation
JUN                    IL6                    stimulation
ELK1                   JUN                    stimulation
JUN                    CDKN2A                 stimulation
JUN                    IL12B                  stimulation
JUN                    EGR1                   stimulation
JUN                    VEGFA                  stimulation
JUN                    CDKN2A                 stimulation
MAPK11                 FOS                    stimulation
FOS                    TGFB1                  stimulation
FOS                    IFNG                   stimulation
FOS                    CXCL8                  stimulation
MAPK1                  FOS                    stimulation
MAPK14                 FOS                    stimulation
CREB1                  FOS                    stimulation
FOS                    TERT                   inhibition
FOS                    BCL2L11                stimulation
AKT3                   FOS                    stimulation
FOS                    IL6                    stimulation
ELK1                   FOS                    stimulation
IL12B                  FOS                    stimulation
ILK                    FOS                    stimulation
FOS                    VEGFA                  stimulation
TGFB1                  PIK3CA                 stimulation
IFNG                   PIK3CA                 stimulation
PIK3CA                 NFKB1                  stimulation
PIK3CA                 MAP2K1                 stimulation
PIK3CA                 MAPK14                 stimulation
IRS1                   PIK3CA                 stimulation
IL5                    PIK3CA                 stimulation
PIK3CA                 CREB1                  stimulation
PIK3CA                 SP1                    stimulation
PIK3CA                 RPS6KB1                stimulation
PIK3CA                 AKT3                   stimulation
CD40LG                 PIK3CA                 stimulation
CDKN2A                 PIK3CA                 inhibition
IL12B                  PIK3CA                 stimulation
LAT                    PIK3CA                 stimulation
GNAI1                  PIK3CA                 stimulation
SHC1                   PIK3CA                 stimulation
PIK3CA                 PTK2B                  stimulation
PIK3CA                 CCND3                  stimulation
PIK3CA                 BCL2L1                 stimulation
PIK3CA                 SOS1                   stimulation
SOS1                   PIK3CA                 stimulation
PIK3CA                 DDAH2                  stimulation
CDKN2A                 PIK3CA                 inhibition
AKT1                   MAPK3                  stimulation
INS                    AKT1                   stimulation
AKT1                   TGFB1                  inhibition
AKT1                   RB1                    stimulation
AKT1                   MAP3K5                 inhibition
RAC1                   AKT1                   stimulation
AKT1                   CHUK                   stimulation
AKT1                   NFKB1                  stimulation
PPP2CA                 AKT1                   inhibition
AKT1                   OTUD7B                 stimulation
AKT1                   MAP2K4                 inhibition
PRKCZ                  AKT1                   inhibition
EDN1                   AKT1                   stimulation
AKT1                   CBL                    stimulation
AKT1                   IRS1                   stimulation
AKT1                   CTNNB1                 stimulation
AKT1                   CREB1                  stimulation
AKT1                   TERT                   stimulation
AKT1                   RPS6KB1                stimulation
AKT1                   HIF1A                  stimulation
AKT1                   BCL2L11                inhibition
AKT1                   AKT2                   inhibition
AKT1                   BIRC5                  stimulation
CD40LG                 AKT1                   stimulation
AKT1                   IRAK1                  inhibition
AKT1                   COMPLEX:P19838_Q04206  stimulation
GNAI1                  AKT1                   stimulation
AKT1                   PRKCD                  stimulation
SHC1                   AKT1                   stimulation
ILK                    AKT1                   stimulation
AKT1                   MEF2D                  stimulation
AKT1                   BCL2L1                 stimulation
LAMB2                  AKT1                   stimulation
SOS1                   AKT1                   stimulation
AKT1                   TSC2                   inhibition
PPP2R5C                AKT1                   inhibition
PTEN                   RAC1                   stimulation
PTEN                   EGFR                   inhibition
PTEN                   AKT2                   inhibition
PTEN                   SHC1                   inhibition
ROCK1                  PTEN                   stimulation
PTEN                   PTK2                   inhibition
TGFB1                  MTOR                   stimulation
MTOR                   IRS1                   inhibition
MTOR                   CYCS                   stimulation
MTOR                   AKT3                   stimulation
MTOR                   PPP3CA                 stimulation
CDC42                  MTOR                   stimulation
MTOR                   EIF4E                  inhibition
MAPK1                  CCND1                  stimulation
RAC1                   CCND1                  stimulation
STAT1                  CCND1                  stimulation
NFKB2                  CCND1                  stimulation
MAPK14                 CCND1                  stimulation
CREB1                  CCND1                  stimulation
TERT                   CCND1                  stimulation
CCND1                  E2F2                   inhibition
SP1                    CCND1                  stimulation
ELK1                   CCND1                  stimulation
CCND1                  DDAH2                  inhibition
CDKN2A                 CCND1                  inhibition
TGFB1                  CDK4                   inhibition
CCND3                  CDK4                   stimulation
CDK4                   E2F3                   inhibition
RB1                    E2F1                   inhibition
E2F1                   BID                    stimulation
E2F1                   NFKB1                  inhibition
ATM                    E2F1                   stimulation
E2F1                   CTNNB1                 inhibition
E2F1                   E2F2                   stimulation
SP1                    E2F1                   stimulation
E2F1                   CYCS                   stimulation
E2F1                   TFDP1                  stimulation
E2F1                   BCL2L11                stimulation
E2F1                   BIRC5                  stimulation
SIRT1                  E2F1                   inhibition
CDK3                   E2F1                   inhibition
CDK1                   E2F1                   stimulation
VEGFA                  E2F1                   stimulation
COMPLEX:P20248_P24941  E2F1                   stimulation
E2F3                   E2F1                   stimulation
CCNE1                  E2F1                   stimulation
MYC                    TRAF1                  inhibition
PPARA                  MYC                    inhibition
INS                    MYC                    stimulation
MAPK11                 MYC                    stimulation
RXRA                   MYC                    stimulation
MYC                    CXCL8                  stimulation
MYC                    CDK6                   stimulation
MAPK1                  MYC                    stimulation
CHUK                   MYC                    stimulation
MAPK9                  MYC                    stimulation
PPP2CA                 MYC                    stimulation
MAPK14                 MYC                    stimulation
PAK2                   MYC                    inhibition
IL5                    MYC                    stimulation
CTNNB1                 MYC                    stimulation
CREB1                  MYC                    stimulation
E2F2                   MYC                    stimulation
MYC                    SP1                    stimulation
MYC                    CYCS                   stimulation
MYC                    TFDP1                  stimulation
MYC                    VEGFA                  stimulation
MYC                    EIF4E                  stimulation
MYC                    CCNE1                  stimulation
TP53                   MAP4K4                 stimulation
MAPK11                 TP53                   stimulation
BDNF                   TP53                   stimulation
TGFB1                  TP53                   stimulation
TP53                   RB1                    stimulation
MAPK1                  TP53                   stimulation
TP53                   BID                    stimulation
RAC1                   TP53                   stimulation
MAPK9                  TP53                   stimulation
TP53                   NFKB2                  stimulation
MAPK14                 TP53                   stimulation
HSP90AA1               TP53                   inhibition
TP53                   AR                     inhibition
TP53                   TP73                   stimulation
TP53                   DDB2                   stimulation
TP53                   CASP10                 stimulation
APEX1                  TP53                   stimulation
CREB1                  TP53                   stimulation
TP53                   TERT                   inhibition
BAG1                   TP53                   inhibition
TP53                   TP63                   stimulation
TP53                   UBB                    stimulation
TP53                   BIRC5                  inhibition
CD40LG                 TP53                   stimulation
TP53                   NFE2L2                 inhibition
SIRT1                  TP53                   inhibition
PRKCD                  TP53                   stimulation
TP53                   BCL2L1                 inhibition
BCL2L1                 TP53                   inhibition
CDK1                   TP53                   stimulation
COMPLEX:P20248_P24941  TP53                   stimulation
HSPB1                  TP53                   inhibition
TP53                   EIF4E                  inhibition
TP53                   TSC2                   stimulation
IL1A                   CDKN1A                 stimulation
TGFB1                  CDKN1A                 stimulation
IFNG                   CDKN1A                 stimulation
CDKN1A                 RB1                    inhibition
RAC1                   CDKN1A                 stimulation
STAT1                  CDKN1A                 stimulation
AR                     CDKN1A                 stimulation
DDB2                   CDKN1A                 inhibition
CREB1                  CDKN1A                 stimulation
CDKN1A                 E2F2                   inhibition
TP63                   CDKN1A                 inhibition
SP1                    CDKN1A                 stimulation
HIF1A                  CDKN1A                 stimulation
CDKN2A                 CDKN1A                 inhibition
CUL1                   CDKN1A                 inhibition
CDKN1A                 CCND3                  inhibition
CDKN1A                 CDK1                   inhibition
CDKN1A                 DDAH2                  stimulation
CDKN2A                 CDKN1A                 inhibition
CASP3                  BID                    stimulation
CASP3                  TP73                   stimulation
CASP3                  PAK2                   stimulation
CASP3                  PSEN1                  stimulation
CASP3                  BAD                    stimulation
CASP3                  TERT                   stimulation
CASP3                  TP63                   stimulation
CASP3                  BCL2L11                stimulation
VDR                    CASP3                  stimulation
CASP3                  BCL2L1                 inhibition
CASP3                  PTK2                   inhibition
CASP3                  EIF4E                  stimulation
MAP2K1                 CASP9                  inhibition
PRKCZ                  CASP9                  inhibition
DIABLO                 CASP9                  stimulation
CYCS                   CASP9                  stimulation
AKT3                   CASP9                  inhibition
NAIP                   CASP9                  inhibition
HSP90AA1               APAF1                  inhibition
EIF4G2                 APAF1                  stimulation
DIABLO                 APAF1                  stimulation
CYCS                   APAF1                  stimulation
BIRC5                  APAF1                  inhibition
MYD88                  MAP4K4                 stimulation
IL1A                   MAP4K4                 stimulation
MAP3K5                 MAP4K4                 stimulation
MAP4K4                 CHUK                   stimulation
CASP2                  MAP4K4                 stimulation
EPHB2                  MAP4K4                 stimulation
TRAF6                  MAP4K4                 stimulation
MAP4K4                 MAP3K1                 stimulation
MAP4K4                 IKBKG                  stimulation
CD40LG                 MAP4K4                 stimulation
IRAK1                  MAP4K4                 stimulation
CYLD                   TRAF1                  inhibition
TNFRSF1B               TRAF1                  stimulation
TRAF1                  NFKB1                  stimulation
NFKB1                  TRAF1                  stimulation
TRAF1                  MAP2K7                 stimulation
NFKB2                  TRAF1                  stimulation
S100B                  TRAF1                  inhibition
TRAF1                  TICAM1                 inhibition
TICAM1                 TRAF1                  stimulation
TRAF1                  MAP3K1                 stimulation
MYD88                  CHUK                   stimulation
MYD88                  TRAF6                  stimulation
MYD88                  MAP3K1                 stimulation
MYD88                  IKBKG                  stimulation
MYD88                  RIPK2                  stimulation
MYD88                  IRAK1                  stimulation
MYD88                  NGFR                   stimulation
MYD88                  IL1B                   inhibition
IL1B                   MYD88                  inhibition
CSF3                   MAPK3                  stimulation
MAPK3                  PPARA                  stimulation
MAP2K3                 MAPK3                  stimulation
MAPK11                 MAPK3                  stimulation
MAPK3                  BDNF                   stimulation
BDNF                   MAPK3                  stimulation
TGFB1                  MAPK3                  stimulation
MAPK3                  IFNG                   stimulation
MAPK3                  CXCL8                  inhibition
SUCLA2                 MAPK3                  stimulation
MAPK1                  MAPK3                  stimulation
IL2                    MAPK3                  stimulation
MAPK3                  CHUK                   stimulation
NFKB1                  MAPK3                  stimulation
MAP2K7                 MAPK3                  stimulation
MAP2K1                 MAPK3                  stimulation
MAPK9                  MAPK3                  stimulation
EPHB2                  MAPK3                  stimulation
PPP2CA                 MAPK3                  inhibition
MAPK14                 MAPK3                  inhibition
TRAF6                  MAPK3                  stimulation
MAP2K4                 MAPK3                  stimulation
PRKCZ                  MAPK3                  stimulation
MAP3K1                 MAPK3                  stimulation
EDN1                   MAPK3                  stimulation
MAPK3                  BAD                    inhibition
MAPK3                  IRS1                   inhibition
IL5                    MAPK3                  stimulation
MAPK3                  CREB1                  stimulation
MAPK3                  TERT                   stimulation
MAPK3                  SP1                    stimulation
MAPK3                  RPS6KB1                stimulation
CSF2                   MAPK3                  stimulation
MAPK3                  HIF1A                  stimulation
MAPK3                  BCL2L11                inhibition
IL6                    MAPK3                  stimulation
RIPK2                  MAPK3                  stimulation
MAPK3                  ELK1                   stimulation
MAPK3                  FOXO3                  inhibition
MAPK3                  COMPLEX:P19838_Q04206  stimulation
MAPK3                  RPS6KA2                stimulation
IL1B                   MAPK3                  stimulation
TSC22D3                MAPK3                  inhibition
MAPK3                  EGR1                   stimulation
MAPK3                  LAT                    inhibition
GNAI1                  MAPK3                  stimulation
PRKCD                  MAPK3                  inhibition
MAPK3                  SHC1                   stimulation
PTK2B                  MAPK3                  stimulation
MAPK3                  ROCK1                  inhibition
LYN                    MAPK3                  stimulation
MAPK3                  RARA                   stimulation
MAPK3                  BCL2L1                 stimulation
MAPK3                  MRTFA                  inhibition
VEGFA                  MAPK3                  stimulation
MAPK3                  FGFR2                  inhibition
PELP1                  MAPK3                  stimulation
MAPK3                  TSC2                   inhibition
MAPK3                  PPP2R5C                inhibition
IFNG                   CSF3                   stimulation
CXCL8                  CSF3                   inhibition
CSF3                   IL2                    inhibition
CSF3                   STAT1                  stimulation
CSF3                   CSF2                   stimulation
CYLD                   STAT1                  inhibition
CYLD                   IKBKG                  inhibition
IL23A                  IFNG                   stimulation
MAPK1                  IL23A                  inhibition
IL23A                  NFKB1                  stimulation
NFKB1                  IL23A                  stimulation
IL23A                  STAT1                  stimulation
IL23A                  IL6                    stimulation
IL23A                  IL1B                   stimulation
IL1B                   IL23A                  stimulation
RXRA                   PPARA                  stimulation
MAPK1                  PPARA                  stimulation
PPARA                  HSP90AA1               stimulation
PPARA                  EDN1                   stimulation
PPARA                  RPS6KB1                inhibition
MAP2K3                 MAPK11                 stimulation
MAP2K3                 TGFB1                  inhibition
TGFB1                  MAP2K3                 stimulation
MAPK1                  MAP2K3                 stimulation
FASLG                  MAP2K3                 stimulation
MAP3K5                 MAP2K3                 stimulation
RAC1                   MAP2K3                 stimulation
MAP2K3                 MAPK9                  stimulation
MAP2K3                 MAPK14                 stimulation
TRAF6                  MAP2K3                 stimulation
MAP3K1                 MAP2K3                 stimulation
DAXX                   MAP2K3                 stimulation
IL1B                   MAP2K3                 stimulation
PTK2B                  MAP2K3                 stimulation
CDC42                  MAP2K3                 stimulation
IFNG                   IL1A                   inhibition
IL1A                   CXCL8                  stimulation
IL1A                   MAPK1                  stimulation
IL1A                   IL2                    stimulation
IL1A                   CHUK                   stimulation
IL1A                   TRAF6                  stimulation
IL1A                   MAP3K1                 stimulation
TP63                   IL1A                   stimulation
IL1A                   CSF2                   stimulation
IL1A                   IL6                    stimulation
IL6                    IL1A                   stimulation
IL1B                   IL1A                   stimulation
INS                    MAPK1                  stimulation
INS                    EGFR                   stimulation
INS                    PARP1                  stimulation
INS                    PRKCZ                  stimulation
INS                    CBL                    stimulation
INS                    IRS1                   stimulation
INS                    AKT2                   stimulation
INS                    SHC1                   stimulation
INS                    IRS4                   stimulation
INS                    FGFR2                  stimulation
INS                    SOS1                   stimulation
RXRA                   LPL                    stimulation
TGFB1                  LPL                    inhibition
LPL                    IFNG                   stimulation
IFNG                   LPL                    inhibition
SP1                    LPL                    inhibition
MAPK11                 CXCL8                  inhibition
IL2                    MAPK11                 stimulation
RAC1                   MAPK11                 stimulation
MAP2K7                 MAPK11                 stimulation
MAPK11                 STAT1                  stimulation
MAPK11                 MAPK14                 stimulation
TRAF6                  MAPK11                 stimulation
MAPK11                 EGFR                   inhibition
MAP2K4                 MAPK11                 stimulation
MAP3K1                 MAPK11                 stimulation
MAPK11                 TP73                   stimulation
PAK2                   MAPK11                 stimulation
MAPK11                 CREB1                  stimulation
MAPK11                 SP1                    stimulation
MAPK11                 HIF1A                  stimulation
MAPK11                 ELK1                   stimulation
CD40LG                 MAPK11                 stimulation
MAPK11                 NFE2L2                 inhibition
MAPK11                 IL1B                   inhibition
ZAP70                  MAPK11                 stimulation
SHC1                   MAPK11                 stimulation
DUSP4                  MAPK11                 inhibition
LYN                    MAPK11                 stimulation
MAPK11                 MEF2D                  stimulation
FGR                    MAPK11                 stimulation
CDC42                  MAPK11                 stimulation
VEGFA                  MAPK11                 stimulation
GNG2                   MAPK11                 stimulation
MAPK11                 TP53BP1                inhibition
MAPK11                 HSPB1                  stimulation
MAPK11                 EIF4E                  stimulation
MAPK11                 TSC2                   stimulation
BDNF                   MAPK1                  stimulation
BDNF                   NFKB1                  stimulation
BDNF                   MAPK9                  stimulation
BDNF                   CTNNB1                 stimulation
BDNF                   NGFR                   stimulation
BDNF                   SHC1                   stimulation
BDNF                   CDC42                  stimulation
BDNF                   SOS1                   stimulation
MAPK9                  RXRA                   inhibition
MAP2K4                 RXRA                   inhibition
RXRA                   AR                     stimulation
AR                     RXRA                   stimulation
RXRA                   CTNNB1                 inhibition
RXRA                   RPS6KB1                inhibition
RARA                   RXRA                   stimulation
RXRA                   ILK                    stimulation
VDR                    RXRA                   stimulation
CDK1                   RXRA                   stimulation
FGR                    RXRA                   stimulation
TGFB1                  IFNG                   inhibition
IFNG                   TGFB1                  stimulation
TGFB1                  CXCL8                  stimulation
TGFB1                  RB1                    stimulation
RB1                    TGFB1                  stimulation
TGFB1                  SUCLA2                 stimulation
TGFB1                  MAPK1                  stimulation
IL2                    TGFB1                  inhibition
NFKB1                  TGFB1                  stimulation
TGFB1                  EPHB2                  stimulation
EPHB2                  TGFB1                  stimulation
TGFB1                  MAPK14                 stimulation
MAPK14                 TGFB1                  inhibition
TGFB1                  TRAF6                  stimulation
TGFB1                  EGFR                   stimulation
TGFB1                  AR                     stimulation
TGFB1                  EDN1                   stimulation
EDN1                   TGFB1                  stimulation
TGFB1                  PAK2                   stimulation
DAXX                   TGFB1                  inhibition
IRS1                   TGFB1                  inhibition
TGFB1                  TERT                   inhibition
TGFB1                  RPS6KB1                inhibition
RPS6KB1                TGFB1                  stimulation
HIF1A                  TGFB1                  stimulation
EGR1                   TGFB1                  stimulation
TGFB1                  BMP2                   inhibition
TGFB1                  SHC1                   stimulation
TGFB1                  SMAD4                  stimulation
SMAD4                  TGFB1                  inhibition
TGFB1                  VDR                    stimulation
TGFB1                  CDC42                  stimulation
TGFB1                  VEGFA                  stimulation
HSPB1                  TGFB1                  inhibition
EIF4E                  TGFB1                  stimulation
IFNG                   CXCL8                  inhibition
MAPK1                  IFNG                   stimulation
IFNG                   FASLG                  stimulation
IFNG                   MAP3K5                 stimulation
IL2                    IFNG                   stimulation
NFKB1                  IFNG                   stimulation
IFNG                   STAT1                  stimulation
MAPK9                  IFNG                   inhibition
IFNG                   S100B                  stimulation
IFNG                   HSP90AA1               inhibition
IFNG                   MAP3K1                 stimulation
IFNG                   CBL                    stimulation
IFNG                   TERT                   inhibition
IFNG                   IL6                    stimulation
IFNG                   CD40LG                 stimulation
IL12B                  IFNG                   stimulation
IFNG                   IL1B                   stimulation
IFNG                   SMAD7                  stimulation
NOTCH1                 IFNG                   stimulation
PPP3CA                 IFNG                   inhibition
FASLG                  CXCL8                  stimulation
RAC1                   CXCL8                  stimulation
NFKB1                  CXCL8                  stimulation
MAP2K1                 CXCL8                  stimulation
PPP2CA                 CXCL8                  stimulation
MAPK14                 CXCL8                  inhibition
CXCL8                  EGFR                   stimulation
EGFR                   CXCL8                  stimulation
EDN1                   CXCL8                  stimulation
CTNNB1                 CXCL8                  stimulation
CSF2                   CXCL8                  stimulation
HIF1A                  CXCL8                  inhibition
CD40LG                 CXCL8                  stimulation
COMPLEX:P19838_Q04206  CXCL8                  stimulation
IL1B                   CXCL8                  stimulation
EGR1                   CXCL8                  inhibition
BCL2L1                 CXCL8                  stimulation
VEGFA                  CXCL8                  stimulation
RB1                    CASP7                  inhibition
RB1                    MAP3K5                 inhibition
PPP2CA                 RB1                    stimulation
RB1                    E2F2                   inhibition
RB1                    SP1                    stimulation
RB1                    HIF1A                  stimulation
RB1                    TFDP1                  stimulation
SIRT1                  RB1                    stimulation
SMAD7                  RB1                    inhibition
VEGFA                  RB1                    inhibition
RB1                    E2F3                   inhibition
CDK6                   OTUD7B                 stimulation
TP73                   CDK6                   stimulation
CREB1                  CDK6                   stimulation
CDK6                   E2F2                   inhibition
CDK6                   TFDP1                  inhibition
CDK6                   BMP2                   inhibition
CCND3                  CDK6                   stimulation
CDK6                   E2F3                   inhibition
SUCLA2                 MAPK1                  stimulation
SUCLA2                 NFKB1                  stimulation
SUCLA2                 PARP1                  stimulation
SUCLA2                 CTNNB1                 inhibition
SUCLA2                 IL6                    stimulation
CD40LG                 SUCLA2                 stimulation
ACHE                   SUCLA2                 stimulation
MAPK1                  MAP3K5                 stimulation
IL2                    MAPK1                  stimulation
RAC1                   MAPK1                  stimulation
MAPK1                  NFKB1                  stimulation
MAP2K7                 MAPK1                  stimulation
MAP2K1                 MAPK1                  stimulation
MAPK1                  STAT1                  stimulation
PPP2CA                 MAPK1                  inhibition
MAPK1                  OTUD7B                 stimulation
MAPK1                  PARP1                  stimulation
MAP2K4                 MAPK1                  stimulation
PRKCZ                  MAPK1                  stimulation
MAP3K1                 MAPK1                  stimulation
EDN1                   MAPK1                  stimulation
MAPK1                  BAD                    inhibition
MAPK1                  IRS1                   inhibition
MAPK1                  CREB1                  stimulation
MAPK1                  TERT                   stimulation
MAPK1                  SP1                    stimulation
MAPK1                  RPS6KB1                stimulation
CSF2                   MAPK1                  stimulation
MAPK1                  HIF1A                  stimulation
MAPK1                  BCL2L11                inhibition
MAPK1                  RIPK2                  inhibition
MAPK1                  ELK1                   stimulation
MAPK1                  FOXO3                  inhibition
MAPK1                  COMPLEX:P19838_Q04206  stimulation
MAPK1                  RPS6KA2                stimulation
IL1B                   MAPK1                  stimulation
MAPK1                  TSC22D3                stimulation
MAPK1                  EGR1                   stimulation
GNAI1                  MAPK1                  stimulation
BMP2                   MAPK1                  stimulation
SHC1                   MAPK1                  stimulation
MAPK1                  ROCK1                  inhibition
MAPK1                  RARA                   stimulation
MAPK1                  BCL2L1                 stimulation
MAPK1                  CDK1                   inhibition
MAPK1                  MRTFA                  inhibition
MAPK1                  FGR                    stimulation
FGR                    MAPK1                  stimulation
CDC42                  MAPK1                  stimulation
VEGFA                  MAPK1                  stimulation
MAPK1                  FGFR2                  inhibition
MAPK1                  HSPB1                  stimulation
MAPK1                  TSC2                   inhibition
MAPK1                  PPP2R5C                inhibition
FASLG                  CASP7                  stimulation
FASLG                  BID                    stimulation
FASLG                  CHUK                   stimulation
FASLG                  TNFRSF10B              stimulation
NFKB1                  FASLG                  stimulation
FASLG                  MAP2K7                 stimulation
STAT1                  FASLG                  stimulation
FASLG                  EGFR                   stimulation
FASLG                  MAP2K4                 stimulation
FASLG                  IKBKG                  stimulation
RIPK2                  FASLG                  inhibition
IL12B                  FASLG                  stimulation
SIRT1                  FASLG                  inhibition
EGR1                   FASLG                  stimulation
HSPB1                  FASLG                  inhibition
CASP2                  CASP7                  stimulation
CASP7                  PARP1                  inhibition
CASP7                  MAP3K1                 stimulation
CASP7                  AR                     inhibition
CASP7                  EIF4G2                 stimulation
PAK2                   CASP7                  inhibition
CASP7                  PSEN1                  stimulation
CASP10                 CASP7                  stimulation
E2F2                   CASP7                  inhibition
CYCS                   CASP7                  stimulation
TFDP1                  CASP7                  inhibition
BIRC5                  CASP7                  inhibition
NAIP                   CASP7                  inhibition
CASP7                  LYN                    inhibition
CASP7                  PTK2                   stimulation
CASP7                  LAMB2                  stimulation
CASP7                  EIF4E                  stimulation
E2F3                   CASP7                  inhibition
MAP3K5                 BID                    stimulation
CASP2                  BID                    stimulation
DAXX                   BID                    stimulation
CASP10                 BID                    stimulation
ATM                    BID                    stimulation
BID                    DIABLO                 stimulation
BID                    CYCS                   stimulation
HIF1A                  BID                    inhibition
BID                    COX5B                  stimulation
BID                    BCL2L1                 inhibition
TNFRSF1B               MAP3K1                 stimulation
MAP3K5                 CHUK                   stimulation
MAP3K5                 MAP2K7                 stimulation
MAP3K5                 MAPK9                  stimulation
S100B                  MAP3K5                 inhibition
MAP3K5                 MAPK14                 stimulation
TRAF6                  MAP3K5                 stimulation
MAP3K5                 MAP2K4                 stimulation
DAXX                   MAP3K5                 stimulation
AKT3                   MAP3K5                 inhibition
AKT2                   MAP3K5                 inhibition
MAP3K5                 IKBKG                  stimulation
NFKB1                  IL2                    stimulation
IL2                    MAP2K1                 stimulation
IL2                    STAT1                  stimulation
IL2                    MAPK14                 stimulation
IL2                    HSP90AA1               stimulation
IL2                    PRKCZ                  stimulation
IL2                    CBL                    stimulation
IL2                    IRS1                   stimulation
IL2                    IL5                    stimulation
IL5                    IL2                    stimulation
CREB1                  IL2                    stimulation
IL2                    TERT                   stimulation
IL2                    RPS6KB1                stimulation
IL2                    CSF2                   stimulation
CSF2                   IL2                    inhibition
IL2                    IL6                    stimulation
IL6                    IL2                    stimulation
IKBKG                  IL2                    stimulation
CD40LG                 IL2                    inhibition
IL2                    IL1B                   stimulation
IL1B                   IL2                    stimulation
IL2                    SHC1                   stimulation
IL2                    CCND3                  stimulation
IL2                    BCL2L1                 stimulation
IL2                    SOS1                   stimulation
NFKB1                  TNFAIP3                stimulation
TNFAIP3                TRAF6                  inhibition
TNFAIP3                TICAM1                 inhibition
TNFAIP3                IKBKG                  inhibition
RAC1                   NFKB1                  stimulation
RAC1                   MAP2K7                 stimulation
RAC1                   MAP2K1                 stimulation
RAC1                   MAPK9                  stimulation
EPHB2                  RAC1                   stimulation
RAC1                   MAPK14                 stimulation
EGFR                   RAC1                   stimulation
RAC1                   MAP2K4                 stimulation
RAC1                   MAP3K1                 stimulation
EDN1                   RAC1                   stimulation
RAC1                   PAK2                   stimulation
RAC1                   HIF1A                  stimulation
NGFR                   RAC1                   stimulation
GNAI1                  RAC1                   stimulation
RAC1                   PRKCD                  stimulation
SHC1                   RAC1                   stimulation
PTK2B                  RAC1                   stimulation
RAC1                   ROCK1                  stimulation
LYN                    RAC1                   stimulation
RAC1                   VEGFA                  stimulation
VEGFA                  RAC1                   stimulation
GNG2                   RAC1                   stimulation
PTK2                   RAC1                   stimulation
LAMB2                  RAC1                   stimulation
SOS1                   RAC1                   stimulation
TNFRSF10B              CHUK                   stimulation
FLNA                   CHUK                   stimulation
SQSTM1                 CHUK                   stimulation
TRAF6                  CHUK                   stimulation
PRKCZ                  CHUK                   stimulation
MAP3K1                 CHUK                   stimulation
CHUK                   IRS1                   inhibition
TP63                   CHUK                   stimulation
AKT3                   CHUK                   stimulation
AKT2                   CHUK                   stimulation
IKBKG                  CHUK                   stimulation
RIPK2                  CHUK                   stimulation
IRAK1                  CHUK                   stimulation
NGFR                   CHUK                   stimulation
CHUK                   FOXO3                  inhibition
CHUK                   COMPLEX:P19838_Q04206  inhibition
NOTCH1                 CHUK                   stimulation
CHUK                   IRS4                   inhibition
CHUK                   TSC2                   inhibition
NFKB1                  TRAF5                  stimulation
NFKB2                  TRAF5                  stimulation
NFKB1                  TNFRSF10B              stimulation
TNFRSF10B              MAP3K1                 stimulation
TNFRSF10B              CASP10                 stimulation
TNFRSF10B              IKBKG                  stimulation
NOTCH1                 TNFRSF10B              stimulation
MAPK14                 NFKB1                  stimulation
SQSTM1                 NFKB1                  stimulation
NFKB1                  TRAF6                  stimulation
TRAF6                  NFKB1                  stimulation
TICAM1                 NFKB1                  stimulation
EGFR                   NFKB1                  stimulation
PARP1                  NFKB1                  stimulation
PRKCZ                  NFKB1                  stimulation
MAP3K1                 NFKB1                  stimulation
EDN1                   NFKB1                  stimulation
NFKB1                  ALPI                   inhibition
CASP10                 NFKB1                  stimulation
ATM                    NFKB1                  stimulation
BAG1                   NFKB1                  inhibition
PRNP                   NFKB1                  stimulation
NFKB1                  CSF2                   inhibition
CSF2                   NFKB1                  stimulation
NFKB1                  IL6                    stimulation
NFKB1                  BIRC5                  stimulation
NFKB1                  IKBKG                  stimulation
IKBKG                  NFKB1                  stimulation
RIPK2                  NFKB1                  stimulation
IRAK1                  NFKB1                  stimulation
NGFR                   NFKB1                  stimulation
CDKN2A                 NFKB1                  inhibition
NFKB1                  IL12B                  stimulation
IL12B                  NFKB1                  stimulation
CUL1                   NFKB1                  inhibition
NFKB1                  IL1B                   stimulation
TSC22D3                NFKB1                  inhibition
PRKCD                  NFKB1                  stimulation
LYN                    NFKB1                  stimulation
NFKB1                  BCL2L1                 stimulation
NFKB1                  VEGFA                  stimulation
HSPB1                  NFKB1                  inhibition
CDKN2A                 NFKB1                  inhibition
AR                     KRT18                  stimulation
CDK1                   KRT18                  stimulation
CASP2                  MAP2K7                 stimulation
MAP2K7                 MAPK9                  stimulation
FLNA                   MAP2K7                 stimulation
MAP2K7                 MAPK14                 stimulation
MAP2K7                 MAP2K4                 stimulation
MAP3K1                 MAP2K7                 stimulation
DAXX                   MAP2K7                 stimulation
MAP2K7                 IRS1                   inhibition
MAP2K7                 UBB                    stimulation
RIPK2                  MAP2K7                 stimulation
SH3RF1                 MAP2K7                 stimulation
CDC42                  MAP2K7                 stimulation
MAP2K1                 MAPK9                  stimulation
PPP2CA                 MAP2K1                 inhibition
MAPK14                 MAP2K1                 stimulation
EGFR                   MAP2K1                 stimulation
MAP2K1                 MAP2K4                 stimulation
MAP3K1                 MAP2K1                 stimulation
PAK2                   MAP2K1                 stimulation
MAP2K1                 BAD                    inhibition
MAP2K1                 IRS1                   inhibition
MAP2K1                 CREB1                  stimulation
MAP2K1                 RPS6KB1                stimulation
CSF2                   MAP2K1                 stimulation
MAP2K1                 BCL2L11                inhibition
MAP2K1                 ELK1                   stimulation
MAP2K1                 RPS6KA2                stimulation
PRKCD                  MAP2K1                 stimulation
SHC1                   MAP2K1                 stimulation
CDK1                   MAP2K1                 inhibition
MAP2K1                 SOS1                   inhibition
S100B                  CASP2                  inhibition
AR                     CASP2                  inhibition
TP73                   CASP2                  stimulation
CASP2                  EIF4G2                 stimulation
CASP2                  DIABLO                 stimulation
CASP2                  CYCS                   stimulation
CCND3                  CASP2                  stimulation
CASP2                  EIF4E                  stimulation
MAPK9                  STAT1                  stimulation
EPHB2                  STAT1                  stimulation
MAPK14                 STAT1                  stimulation
EGFR                   STAT1                  stimulation
AR                     STAT1                  stimulation
STAT1                  HIF1A                  inhibition
IL6                    STAT1                  stimulation
STAT1                  COMPLEX:P19838_Q04206  inhibition
IL12B                  STAT1                  stimulation
STAT1                  SMAD7                  stimulation
PRKCD                  STAT1                  stimulation
LYN                    STAT1                  stimulation
STAT1                  CCND3                  stimulation
STAT1                  BCL2L1                 stimulation
STAT1                  VEGFA                  stimulation
FGFR2                  STAT1                  stimulation
PTK2                   STAT1                  stimulation
MAPK14                 MAPK9                  stimulation
TRAF6                  MAPK9                  stimulation
MAP2K4                 MAPK9                  stimulation
PRKCZ                  MAPK9                  stimulation
MAPK9                  PSEN1                  stimulation
MAPK9                  BAD                    stimulation
MAPK9                  IRS1                   inhibition
MAPK9                  CTNNB1                 stimulation
MAPK9                  SP1                    stimulation
MAPK9                  ELK1                   stimulation
CD40LG                 MAPK9                  stimulation
NGFR                   MAPK9                  stimulation
MAPK9                  COMPLEX:P19838_Q04206  stimulation
MAPK9                  RPS6KA2                stimulation
MAPK9                  SHC1                   stimulation
MAPK9                  SMAD4                  stimulation
MAPK9                  PTK2B                  stimulation
DUSP4                  MAPK9                  inhibition
CDC42                  MAPK9                  stimulation
MAPK9                  IRS4                   inhibition
MAPK9                  XPO1                   stimulation
PPP2CA                 EPHB2                  inhibition
MAPK14                 EPHB2                  stimulation
EPHB2                  ELK1                   stimulation
EPHB2                  LYN                    stimulation
LYN                    EPHB2                  stimulation
EPHB2                  FGR                    stimulation
FGR                    EPHB2                  stimulation
EPHB2                  CDC42                  stimulation
EPHB2                  PTK2                   inhibition
FLNA                   MAP2K4                 stimulation
FLNA                   IKBKG                  stimulation
PRKCD                  FLNA                   stimulation
PPP3CA                 FLNA                   inhibition
FLNA                   CDC42                  inhibition
PPP2CA                 EGFR                   stimulation
PPP2CA                 PRKCZ                  inhibition
PPP2CA                 ATM                    inhibition
PPP2CA                 CTNNB1                 stimulation
PPP2CA                 SP1                    stimulation
PPP2CA                 AKT3                   inhibition
PPP2CA                 AKT2                   inhibition
PPP2CA                 FOXO3                  stimulation
PPP2CA                 COMPLEX:P19838_Q04206  inhibition
PPP2CA                 PRKCD                  inhibition
CDK3                   PPP2CA                 stimulation
PPP2CA                 EIF4E                  inhibition
PPP2R5C                PPP2CA                 stimulation
NFKB2                  TRAF6                  stimulation
CUL1                   NFKB2                  stimulation
TSC22D3                NFKB2                  inhibition
NFKB2                  BCL2L1                 stimulation
S100B                  DAXX                   inhibition
TRAF6                  MAPK14                 stimulation
MAPK14                 EGFR                   inhibition
MAP2K4                 MAPK14                 stimulation
MAP3K1                 MAPK14                 stimulation
MAPK14                 AR                     stimulation
MAPK14                 TP73                   stimulation
EDN1                   MAPK14                 stimulation
PAK2                   MAPK14                 stimulation
MAPK14                 DDB2                   inhibition
MAPK14                 SP1                    stimulation
MAPK14                 BCL2L11                inhibition
RIPK2                  MAPK14                 stimulation
MAPK14                 ELK1                   stimulation
CD40LG                 MAPK14                 stimulation
MAPK14                 FOXO3                  stimulation
MAPK14                 NFE2L2                 inhibition
MAPK14                 IL1B                   inhibition
ZAP70                  MAPK14                 stimulation
GNAI1                  MAPK14                 stimulation
BMP2                   MAPK14                 stimulation
PTK2B                  MAPK14                 stimulation
DUSP4                  MAPK14                 inhibition
LYN                    MAPK14                 stimulation
MAPK14                 RARA                   stimulation
MAPK14                 MEF2D                  stimulation
CDC42                  MAPK14                 stimulation
GNG2                   MAPK14                 stimulation
MAPK14                 TP53BP1                inhibition
MAPK14                 HSPB1                  stimulation
MAPK14                 EIF4E                  stimulation
MAPK14                 TSC2                   stimulation
MAPK14                 TRIM24                 stimulation
SQSTM1                 TRAF6                  stimulation
SQSTM1                 IKBKG                  stimulation
SQSTM1                 IRAK1                  stimulation
CDK1                   SQSTM1                 stimulation
IRAK1                  OTUD7B                 stimulation
TICAM1                 TRAF6                  stimulation
TRAF6                  EGFR                   inhibition
TRAF6                  MAP3K1                 stimulation
PSEN1                  TRAF6                  inhibition
ATM                    TRAF6                  stimulation
TRAF6                  AKT3                   stimulation
TRAF6                  IKBKG                  inhibition
IRAK1                  TRAF6                  stimulation
IL1B                   TRAF6                  stimulation
TRAF6                  FGFR2                  inhibition
HSPB1                  TRAF6                  stimulation
EGFR                   MAP3K1                 stimulation
AR                     EGFR                   stimulation
EDN1                   EGFR                   stimulation
EGFR                   CASP10                 stimulation
EGFR                   TERT                   stimulation
EGFR                   CSF2                   stimulation
EGR1                   EGFR                   stimulation
PRKCD                  EGFR                   inhibition
EGFR                   SHC1                   stimulation
PTK2B                  EGFR                   stimulation
LYN                    EGFR                   stimulation
RARA                   EGFR                   stimulation
NOTCH1                 EGFR                   stimulation
CDK1                   EGFR                   inhibition
FGR                    EGFR                   stimulation
CDC42                  EGFR                   inhibition
VEGFA                  EGFR                   stimulation
EGFR                   PTK2                   stimulation
EGFR                   LAMB2                  stimulation
EGFR                   SOS1                   stimulation
PARP1                  HIF1A                  stimulation
ILK                    PARP1                  stimulation
HSP90AA1               AR                     stimulation
HSP90AA1               UBB                    inhibition
ZAP70                  HSP90AA1               stimulation
HSP90AA1               PTK2                   stimulation
DAXX                   MAP2K4                 stimulation
CASP10                 MAP2K4                 stimulation
AKT3                   MAP2K4                 inhibition
AKT2                   MAP2K4                 inhibition
CD40LG                 MAP2K4                 stimulation
MAP2K4                 PRKCD                  stimulation
SH3RF1                 MAP2K4                 stimulation
ROCK1                  MAP2K4                 stimulation
PRKCZ                  PSEN1                  stimulation
PRKCZ                  CBL                    stimulation
PRKCZ                  DAXX                   stimulation
PRKCZ                  SP1                    stimulation
PRKCZ                  RPS6KB1                stimulation
PRKCZ                  UBB                    stimulation
PRKCZ                  AKT2                   stimulation
PRKCZ                  IKBKG                  stimulation
PRKCZ                  ELK1                   stimulation
PRKCZ                  COMPLEX:P19838_Q04206  stimulation
PRKCZ                  RPS6KA2                stimulation
SHC1                   PRKCZ                  stimulation
ROCK1                  PRKCZ                  stimulation
PRKCZ                  FGR                    stimulation
CDC42                  PRKCZ                  stimulation
PRKCZ                  GSN                    stimulation
MAP3K1                 AR                     stimulation
PAK2                   MAP3K1                 stimulation
MAP3K1                 CREB1                  stimulation
MAP3K1                 SP1                    stimulation
MAP3K1                 IKBKG                  stimulation
CD40LG                 MAP3K1                 stimulation
IRAK1                  MAP3K1                 stimulation
LAT                    MAP3K1                 stimulation
CDC42                  MAP3K1                 stimulation
EDN1                   AR                     stimulation
DAXX                   AR                     inhibition
AR                     TERT                   inhibition
AR                     FOXO3                  inhibition
SIRT1                  AR                     stimulation
EGR1                   AR                     inhibition
AR                     GNAI1                  stimulation
SMAD4                  AR                     stimulation
CDK1                   AR                     stimulation
AR                     CDC42                  stimulation
AR                     GNG2                   stimulation
TRIM24                 AR                     stimulation
GSN                    AR                     stimulation
TP73                   TP63                   stimulation
TFDP1                  TP73                   stimulation
TP73                   BCL2L11                stimulation
TP73                   FOXO3                  stimulation
SIRT1                  TP73                   inhibition
PRKCD                  TP73                   stimulation
CDK1                   TP73                   inhibition
CASP10                 EIF4G2                 stimulation
CDK1                   EIF4G2                 stimulation
EIF4G2                 EIF4E                  inhibition
CREB1                  EDN1                   stimulation
EDN1                   CSF2                   stimulation
HIF1A                  EDN1                   stimulation
EDN1                   IL6                    stimulation
EDN1                   PTK2B                  stimulation
EDN1                   ILK                    stimulation
EDN1                   CDC42                  stimulation
VEGFA                  EDN1                   inhibition
CDC42                  PAK2                   stimulation
PSEN1                  UBB                    stimulation
ELK1                   PSEN1                  inhibition
PSEN1                  NGFR                   stimulation
PSEN1                  NOTCH1                 stimulation
CASP10                 ALPI                   stimulation
DIABLO                 ALPI                   inhibition
IRS1                   CBL                    stimulation
CBL                    UBB                    stimulation
CBL                    ZAP70                  inhibition
PRKCD                  CBL                    stimulation
PTK2B                  CBL                    stimulation
FGR                    CBL                    stimulation
CBL                    FGFR2                  inhibition
ATM                    DAXX                   inhibition
RIPK2                  DAXX                   inhibition
DAXX                   SMAD4                  inhibition
HSPB1                  DAXX                   inhibition
CASP10                 CYCS                   stimulation
RIPK2                  CASP10                 inhibition
CASP10                 EIF4E                  stimulation
RPS6KB1                BAD                    inhibition
BAD                    CYCS                   stimulation
PPP3CA                 BAD                    stimulation
CDK1                   BAD                    stimulation
PPP2R5C                BAD                    stimulation
IRS1                   ATM                    stimulation
IKBKG                  IRS1                   inhibition
IRS1                   SHC1                   stimulation
IRS1                   IRS4                   stimulation
ATM                    CREB1                  inhibition
ATM                    TP63                   inhibition
ATM                    SP1                    stimulation
ATM                    HIF1A                  stimulation
ATM                    TFDP1                  stimulation
FOXO3                  ATM                    stimulation
CDKN2A                 ATM                    stimulation
RPS6KA2                ATM                    stimulation
ATM                    TP53BP1                stimulation
E2F3                   ATM                    stimulation
CDKN2A                 ATM                    stimulation
ATM                    PPP2R5C                stimulation
IL5                    IL1B                   stimulation
SMAD4                  IL5                    stimulation
SIRT1                  APEX1                  stimulation
APEX1                  EGR1                   stimulation
CREB1                  CTNNB1                 stimulation
CTNNB1                 UBB                    stimulation
AKT3                   CTNNB1                 stimulation
AKT2                   CTNNB1                 stimulation
CTNNB1                 FOXO3                  stimulation
CTNNB1                 CDKN2A                 inhibition
SIRT1                  CTNNB1                 stimulation
CUL1                   CTNNB1                 inhibition
CTNNB1                 SMAD7                  stimulation
PRKCD                  CTNNB1                 inhibition
ROCK1                  CTNNB1                 stimulation
ILK                    CTNNB1                 stimulation
CTNNB1                 NOTCH1                 stimulation
VDR                    CTNNB1                 stimulation
CDK1                   CTNNB1                 stimulation
CTNNB1                 CDC42                  inhibition
CDC42                  CTNNB1                 inhibition
CTNNB1                 CDKN2A                 inhibition
AKT3                   CREB1                  stimulation
AKT2                   CREB1                  stimulation
CREB1                  IL6                    stimulation
RPS6KA2                CREB1                  stimulation
SHC1                   CREB1                  stimulation
SMAD4                  CREB1                  stimulation
ILK                    CREB1                  stimulation
PPP3CA                 CREB1                  inhibition
CREB1                  VEGFA                  stimulation
SOS1                   CREB1                  stimulation
PPP2R5C                CREB1                  inhibition
SP1                    TERT                   inhibition
HIF1A                  TERT                   stimulation
E2F2                   TFDP1                  stimulation
E2F2                   BIRC5                  stimulation
E2F2                   CDKN2A                 stimulation
E2F2                   CCND3                  stimulation
E2F2                   CDK1                   stimulation
E2F2                   CDKN2A                 stimulation
BAG1                   BCL2L11                stimulation
SP1                    PRNP                   stimulation
PTK2                   PRNP                   stimulation
LAMB2                  PRNP                   stimulation
CYCS                   DIABLO                 stimulation
RPS6KB1                TP63                   inhibition
TP63                   CDKN2A                 inhibition
TP63                   PRKCD                  stimulation
TP63                   NOTCH1                 inhibition
TP63                   VDR                    inhibition
TP63                   CDKN2A                 inhibition
SP1                    BIRC5                  stimulation
COMPLEX:P19838_Q04206  SP1                    stimulation
SP1                    LAT                    stimulation
SP1                    SMAD7                  stimulation
CDK1                   SP1                    stimulation
SP1                    VEGFA                  stimulation
COMPLEX:P20248_P24941  SP1                    stimulation
HSPB1                  SP1                    stimulation
RPS6KB1                UBB                    stimulation
AKT3                   RPS6KB1                stimulation
RPS6KB1                SHC1                   stimulation
CDK1                   RPS6KB1                stimulation
RPS6KB1                FGR                    stimulation
CDC42                  RPS6KB1                stimulation
RPS6KB1                PTK2                   stimulation
RHEB                   RPS6KB1                stimulation
RPS6KB1                HSPB1                  inhibition
PPP2R5C                RPS6KB1                inhibition
CUL1                   UBB                    stimulation
PTK2B                  UBB                    stimulation
HTRA2                  CYCS                   inhibition
BCL2L1                 CYCS                   inhibition
HSPB1                  CYCS                   inhibition
GSN                    CYCS                   inhibition
CD40LG                 CSF2                   stimulation
CSF2                   IL1B                   stimulation
IL1B                   CSF2                   stimulation
CSF2                   SMAD7                  inhibition
NOTCH1                 HIF1A                  stimulation
HIF1A                  VEGFA                  stimulation
TFDP1                  CDKN2A                 inhibition
CDKN2A                 TFDP1                  inhibition
TFDP1                  SIRT1                  stimulation
SMAD4                  TFDP1                  stimulation
CCND3                  TFDP1                  inhibition
TFDP1                  CDK1                   stimulation
TFDP1                  DDAH2                  stimulation
E2F3                   TFDP1                  stimulation
TFDP1                  CDKN2A                 inhibition
CDKN2A                 TFDP1                  inhibition
CCNE1                  TFDP1                  stimulation
SIRT1                  BCL2L11                inhibition
BCL2L11                BCL2L1                 inhibition
CDK1                   BCL2L11                stimulation
BCL2L1                 COX5B                  inhibition
ACHE                   COX5B                  stimulation
HSPB1                  COX5B                  inhibition
AKT3                   BIRC5                  stimulation
AKT3                   IKBKG                  stimulation
AKT3                   FOXO3                  inhibition
AKT3                   COMPLEX:P19838_Q04206  stimulation
GNAI1                  AKT3                   stimulation
PTK2B                  AKT3                   stimulation
ILK                    AKT3                   stimulation
AKT3                   BCL2L1                 stimulation
VEGFA                  AKT3                   stimulation
AKT3                   HSPB1                  inhibition
AKT3                   TSC2                   inhibition
AKT2                   BIRC5                  stimulation
AKT2                   IKBKG                  stimulation
AKT2                   HTRA2                  inhibition
AKT2                   FOXO3                  inhibition
AKT2                   COMPLEX:P19838_Q04206  stimulation
AKT2                   SH3RF1                 inhibition
ILK                    AKT2                   stimulation
AKT2                   BCL2L1                 stimulation
AKT2                   HSPB1                  inhibition
AKT2                   TSC2                   inhibition
COMPLEX:P19838_Q04206  IL6                    stimulation
IL12B                  IL6                    stimulation
IL6                    IL1B                   stimulation
IL1B                   IL6                    stimulation
IL6                    SHC1                   stimulation
IL6                    VEGFA                  stimulation
VEGFA                  IL6                    stimulation
PTK2                   IL6                    stimulation
IL6                    SOS1                   stimulation
CDKN2A                 BIRC5                  inhibition
CDK1                   BIRC5                  stimulation
E2F3                   BIRC5                  stimulation
CDKN2A                 BIRC5                  inhibition
RIPK2                  IKBKG                  stimulation
IRAK1                  IKBKG                  stimulation
NGFR                   IKBKG                  stimulation
IKBKG                  COMPLEX:P19838_Q04206  stimulation
IKBKG                  IRS4                   inhibition
RIPK2                  PRKCD                  stimulation
ELK1                   EGR1                   stimulation
SHC1                   ELK1                   stimulation
ELK1                   CCND3                  stimulation
SOS1                   ELK1                   stimulation
CD40LG                 VEGFA                  stimulation
NGFR                   IRAK1                  stimulation
NGFR                   SHC1                   stimulation
NGFR                   SOS1                   stimulation
TSC22D3                FOXO3                  inhibition
SHC1                   FOXO3                  inhibition
PTK2B                  FOXO3                  stimulation
CDKN2A                 CCND3                  inhibition
CDKN2A                 VDR                    inhibition
CDKN2A                 BCL2L1                 inhibition
SIRT1                  NFE2L2                 inhibition
PRKCD                  NFE2L2                 stimulation
COMPLEX:P19838_Q04206  IL12B                  stimulation
COMPLEX:P19838_Q04206  IL1B                   stimulation
TSC22D3                COMPLEX:P19838_Q04206  inhibition
COMPLEX:P19838_Q04206  EGR1                   stimulation
COMPLEX:P19838_Q04206  VEGFA                  stimulation
IL12B                  IL1B                   stimulation
IL1B                   IL12B                  stimulation
RPS6KA2                SMAD4                  stimulation
RPS6KA2                TSC2                   inhibition
RPS6KA2                XPO1                   stimulation
SIRT1                  NOTCH1                 inhibition
CDK1                   SIRT1                  stimulation
HSPB1                  CUL1                   stimulation
CUL1                   CCNE1                  stimulation
IL1B                   EGR1                   stimulation
IL1B                   VEGFA                  stimulation
EGR1                   DUSP4                  stimulation
ZAP70                  LAT                    stimulation
LAT                    SHC1                   stimulation
LYN                    LAT                    stimulation
LAT                    CDC42                  stimulation
LAT                    SOS1                   stimulation
SMAD7                  BMP2                   inhibition
SMAD4                  SMAD7                  stimulation
ZAP70                  SHC1                   stimulation
ZAP70                  FGR                    stimulation
FGR                    ZAP70                  stimulation
GNAI1                  SHC1                   stimulation
GNAI1                  PTK2B                  stimulation
GNAI1                  FGR                    stimulation
GNAI1                  CDC42                  stimulation
GNAI1                  PTK2                   inhibition
GNAI1                  SOS1                   stimulation
PRKCD                  SHC1                   stimulation
PRKCD                  PTK2B                  stimulation
PTK2B                  SHC1                   stimulation
LYN                    SHC1                   stimulation
SHC1                   ILK                    stimulation
SHC1                   CCND3                  stimulation
FGR                    SHC1                   stimulation
VEGFA                  SHC1                   stimulation
FGFR2                  SHC1                   stimulation
PTK2                   SHC1                   stimulation
SHC1                   SOS1                   stimulation
FGFR2                  SMAD4                  stimulation
PTK2                   SMAD4                  stimulation
EIF4E                  SMAD4                  stimulation
LYN                    PTK2B                  stimulation
PTK2B                  ARHGDIB                stimulation
FGR                    PTK2B                  stimulation
VEGFA                  PTK2B                  stimulation
PTK2B                  PTK2                   stimulation
PTK2B                  SOS1                   stimulation
PTK2B                  GSN                    stimulation
ROCK1                  PTK2                   stimulation
GNG2                   LYN                    stimulation
LYN                    PTK2                   stimulation
LYN                    SOS1                   stimulation
SOS1                   ILK                    stimulation
PPP3CA                 MEF2D                  stimulation
SOS1                   CCND3                  stimulation
E2F3                   CCND3                  stimulation
CDKN2A                 CCND3                  inhibition
CCND3                  CCNE1                  stimulation
CDKN2A                 VDR                    inhibition
CDK1                   BCL2L1                 inhibition
CDKN2A                 BCL2L1                 inhibition
CDK1                   TP53BP1                inhibition
E2F3                   CDK1                   stimulation
GNG2                   FGR                    stimulation
FGR                    PTK2                   stimulation
FGR                    TRIM24                 stimulation
VEGFA                  CDC42                  stimulation
GNG2                   CDC42                  stimulation
PTK2                   CDC42                  stimulation
LAMB2                  CDC42                  stimulation
VEGFA                  PTK2                   stimulation
VEGFA                  SOS1                   stimulation
GNG2                   PTK2                   stimulation
SOS1                   PTK2                   stimulation
RHEB                   EIF4E                  stimulation
CCNE1                  DDAH2                  stimulation

**Tool Output:**

{
  "result": "source                 target                 Effect\nTNFRSF1A               MAP4K4                 stimulation\nMAP4K4                 TNF                    inhibition\nTNF                    TNFRSF1A               stimulation\nTRADD                  TRAF1                  stimulation\nTRAF1                  TNF                    inhibition\nTNF                    TRADD                  inhibition\nTRAF2                  TRAF1                  stimulation\nRIPK1                  MAP4K4                 stimulation\nTRADD                  RIPK1                  stimulation\nFADD                   MYD88                  inhibition\nMYD88                  TNF                    stimulation\nTRADD                  FADD                   stimulation\nTNF                    CASP8                  stimulation\nCFLAR                  TNF                    inhibition\nTNF                    MAPK8                  stimulation\nMAPK8                  CFLAR                  inhibition\nBCL2                   MYC                    stimulation\nMYC                    TNF                    stimulation\nTNF                    MAPK3                  stimulation\nMAPK8                  BAX                    stimulation\nMAPK3                  MCL1                   stimulation\nXIAP                   PTEN                   stimulation\nPTEN                   TNF                    inhibition\nTNF                    RELA                   stimulation\nRELA                   XIAP                   stimulation\nBIRC2                  CFLAR                  inhibition\nTRADD                  BIRC2                  stimulation\nBIRC3                  MAP4K4                 stimulation\nTNF                    CSF3                   stimulation\nCSF3                   BIRC3                  stimulation\nCYLD                   TNF                    inhibition\nTNF                    IKBKB                  stimulation\nNFKBIA                 IL23A                  stimulation\nIL23A                  TNF                    stimulation\nTNF                    NFKBIA                 inhibition\nRELA                   PPARA                  inhibition\nPPARA                  TNF                    inhibition\nMAP3K7                 MAP2K3                 stimulation\nMAP2K3                 TNF                    inhibition\nTNF                    IL1A                   stimulation\nIL1A                   MAP3K7                 stimulation\nMAPK8                  INS                    inhibition\nINS                    TNF                    inhibition\nJUN                    LPL                    inhibition\nLPL                    TNF                    stimulation\nTNF                    JUN                    stimulation\nFOS                    TNF                    stimulation\nMAPK3                  FOS                    stimulation\nPIK3CA                 MAPK11                 inhibition\nMAPK11                 TNF                    inhibition\nTNF                    BDNF                   stimulation\nBDNF                   PIK3CA                 stimulation\nAKT1                   RXRA                   stimulation\nRXRA                   TNF                    stimulation\nTNF                    AKT1                   stimulation\nTNF                    TGFB1                  inhibition\nTGFB1                  PTEN                   stimulation\nMTOR                   IFNG                   stimulation\nIFNG                   TNF                    stimulation\nTNF                    CXCL8                  stimulation\nCXCL8                  MTOR                   stimulation\nCCND1                  TNF                    inhibition\nMAPK3                  CCND1                  stimulation\nRB1                    TNF                    stimulation\nMAPK3                  CDK4                   stimulation\nE2F1                   MYC                    stimulation\nMAPK3                  E2F1                   stimulation\nMAPK3                  MYC                    stimulation\nTP53                   PTEN                   stimulation\nMAPK3                  TP53                   stimulation\nCDKN1A                 CCND1                  inhibition\nTNF                    CDK6                   inhibition\nCDK6                   CDKN1A                 inhibition\nCASP3                  PTEN                   stimulation\nTNF                    CASP3                  stimulation\nMAPK3                  CASP9                  inhibition\nTNF                    SUCLA2                 stimulation\nSUCLA2                 APAF1                  stimulation\nTRADD                  MAPK1                  inhibition\nMAPK1                  TNFRSF1A               inhibition\nTNFRSF1A               TRADD                  stimulation\nTNFRSF1A               TRAF2                  stimulation\nRIPK1                  FASLG                  stimulation\nFASLG                  TNFRSF1A               stimulation\nTNFRSF1A               RIPK1                  stimulation\nFADD                   MAPK1                  stimulation\nTNFRSF1A               FADD                   stimulation\nCASP8                  CASP7                  stimulation\nTNFRSF1A               CASP8                  stimulation\nTNFRSF1A               MAPK3                  stimulation\nTNFRSF1A               BID                    stimulation\nBID                    BAX                    stimulation\nXIAP                   CASP7                  inhibition\nTNFRSF1A               RELA                   stimulation\nBIRC2                  FASLG                  inhibition\nTNFRSF1A               TNFRSF1B               stimulation\nTNFRSF1B               BIRC2                  stimulation\nBIRC3                  FASLG                  inhibition\nRELA                   BIRC3                  stimulation\nCYLD                   TNFRSF1A               inhibition\nTNFRSF1A               MAP3K5                 stimulation\nMAP3K5                 IKBKB                  stimulation\nIL2                    TNFRSF1A               stimulation\nTNFRSF1A               NFKBIA                 inhibition\nRELA                   TNFAIP3                stimulation\nTNFAIP3                TNFRSF1A               stimulation\nMAP3K7                 IL2                    inhibition\nTRAF2                  MAP3K7                 stimulation\nMAPK8                  FASLG                  stimulation\nMAPK3                  MAPK8                  stimulation\nJUN                    FASLG                  stimulation\nRELA                   JUN                    stimulation\nFOS                    FASLG                  stimulation\nPIK3CA                 MAPK1                  inhibition\nTNFRSF1A               RAC1                   stimulation\nRAC1                   PIK3CA                 stimulation\nTNFRSF1A               CASP3                  stimulation\nCASP3                  AKT1                   inhibition\nRELA                   PTEN                   inhibition\nTNFRSF1A               CHUK                   stimulation\nCHUK                   MTOR                   stimulation\nTP53                   FASLG                  stimulation\nMAP3K5                 CDKN1A                 stimulation\nCASP3                  CASP7                  stimulation\nCASP9                  CASP7                  stimulation\nAPAF1                  CASP7                  stimulation\nTRADD                  CASP8                  stimulation\nCFLAR                  TRADD                  inhibition\nTRADD                  RELA                   stimulation\nRELA                   BCL2                   stimulation\nTRADD                  BID                    stimulation\nMAPK1                  MCL1                   stimulation\nBIRC3                  CFLAR                  inhibition\nCYLD                   TRADD                  inhibition\nTRADD                  IKBKB                  stimulation\nTRADD                  MAP3K5                 stimulation\nMAP3K5                 MAPK8                  stimulation\nRELA                   FOS                    stimulation\nTRADD                  TRAF5                  stimulation\nTRAF5                  PIK3CA                 stimulation\nAKT1                   CFLAR                  inhibition\nIKBKB                  MTOR                   stimulation\nRELA                   CCND1                  stimulation\nMAPK1                  CDK4                   stimulation\nMAPK1                  E2F1                   stimulation\nMAP3K5                 MYC                    stimulation\nTP53                   TNFRSF10B              stimulation\nTNFRSF10B              TRADD                  stimulation\nTRADD                  NFKB1                  stimulation\nNFKB1                  TP53                   stimulation\nCASP3                  KRT18                  stimulation\nKRT18                  TRADD                  inhibition\nFADD                   CASP3                  stimulation\nBIRC2                  CASP9                  inhibition\nBIRC2                  APAF1                  inhibition\nRIPK1                  RELA                   stimulation\nRELA                   TRAF2                  stimulation\nTRAF2                  RIPK1                  stimulation\nTRAF2                  MAP2K7                 stimulation\nMAP2K7                 FADD                   inhibition\nTRAF1                  TRAF2                  stimulation\nTRAF2                  CASP8                  stimulation\nTRAF2                  BIRC3                  stimulation\nTRAF2                  MAP2K1                 stimulation\nMAP2K1                 BCL2                   stimulation\nTRAF2                  BID                    stimulation\nMAP2K1                 MCL1                   stimulation\nTRAF2                  TP53                   stimulation\nTP53                   XIAP                   stimulation\nBIRC2                  CASP2                  inhibition\nCASP2                  TRAF2                  stimulation\nTRAF2                  BIRC2                  stimulation\nCYLD                   TRAF2                  inhibition\nTRAF2                  IKBKB                  stimulation\nTRAF2                  NFKBIA                 stimulation\nTRAF2                  RELA                   stimulation\nMAPK8                  STAT1                  stimulation\nSTAT1                  TRAF2                  inhibition\nTRAF2                  MAPK8                  stimulation\nTRAF2                  MAPK9                  stimulation\nMAPK9                  JUN                    stimulation\nPIK3CA                 RELA                   stimulation\nTRAF2                  EPHB2                  stimulation\nEPHB2                  PIK3CA                 stimulation\nAKT1                   FLNA                   stimulation\nFLNA                   TRAF2                  inhibition\nMAPK8                  AKT1                   stimulation\nMTOR                   PPP2CA                 inhibition\nPPP2CA                 TRAF2                  inhibition\nCCND1                  STAT1                  inhibition\nE2F1                   RELA                   stimulation\nMYC                    NFKB2                  inhibition\nNFKB2                  TRAF2                  stimulation\nTP53                   S100B                  inhibition\nS100B                  TRAF2                  inhibition\nCASP3                  CASP2                  stimulation\nBIRC3                  CASP3                  inhibition\nBIRC3                  CASP9                  inhibition\nBIRC3                  APAF1                  inhibition\nFADD                   RIPK1                  stimulation\nRIPK1                  MAP2K7                 stimulation\nCASP8                  RIPK1                  inhibition\nRELA                   CASP8                  inhibition\nCFLAR                  RIPK1                  inhibition\nRIPK1                  MAPK14                 stimulation\nMAPK14                 CFLAR                  stimulation\nBCL2                   CASP8                  inhibition\nRIPK1                  BID                    stimulation\nBIRC2                  RIPK1                  stimulation\nRELA                   BIRC2                  stimulation\nBIRC3                  RIPK1                  stimulation\nIKBKB                  SQSTM1                 stimulation\nSQSTM1                 RIPK1                  stimulation\nRIPK1                  IKBKB                  stimulation\nNFKBIA                 BIRC3                  stimulation\nMAP3K7                 OTUD7B                 stimulation\nOTUD7B                 RIPK1                  inhibition\nTRAF6                  MAP3K7                 stimulation\nMAP2K7                 MAPK8                  stimulation\nPIK3CA                 TICAM1                 stimulation\nTICAM1                 RIPK1                  stimulation\nRIPK1                  EGFR                   inhibition\nEGFR                   PIK3CA                 stimulation\nAKT1                   RNF11                  inhibition\nRNF11                  RIPK1                  inhibition\nTRAF6                  AKT1                   stimulation\nCDK4                   OTUD7B                 stimulation\nE2F1                   CASP8                  stimulation\nRIPK1                  PARP1                  inhibition\nPARP1                  E2F1                   stimulation\nMYC                    HSP90AA1               stimulation\nHSP90AA1               RIPK1                  stimulation\nRELA                   MYC                    inhibition\nTP53                   BIRC3                  inhibition\nTRAF6                  TP53                   stimulation\nMAPK14                 CDKN1A                 stimulation\nCASP2                  RIPK1                  stimulation\nMAPK14                 CASP3                  inhibition\nCASP8                  MAP2K7                 stimulation\nFADD                   CASP8                  stimulation\nFADD                   NFKB1                  stimulation\nNFKB1                  BCL2                   stimulation\nFADD                   BID                    stimulation\nCASP3                  MCL1                   inhibition\nXIAP                   TP53                   stimulation\nTP53                   FADD                   stimulation\nNFKB1                  XIAP                   stimulation\nBIRC2                  FADD                   inhibition\nNFKB1                  BIRC2                  stimulation\nBIRC3                  MAP2K7                 stimulation\nNFKB1                  BIRC3                  stimulation\nFADD                   IKBKB                  stimulation\nIKBKB                  RELA                   stimulation\nMAP3K7                 MAP2K7                 stimulation\nMYD88                  MAP3K7                 stimulation\nMAPK8                  TP53                   stimulation\nFADD                   MAP2K4                 stimulation\nMAP2K4                 MAPK8                  stimulation\nJUN                    TP53                   inhibition\nNFKB1                  JUN                    stimulation\nFOS                    TP53                   inhibition\nNFKB1                  FOS                    stimulation\nPIK3CA                 PRKCZ                  stimulation\nAKT1                   MAP3K1                 stimulation\nMAP3K1                 FADD                   inhibition\nSTAT1                  FADD                   stimulation\nNFKB1                  CCND1                  stimulation\nE2F1                   TP53                   stimulation\nMYC                    CFLAR                  inhibition\nNFKB1                  MYC                    stimulation\nCASP3                  CDKN1A                 stimulation\nCASP3                  MAP3K1                 stimulation\nMAPK1                  CASP9                  inhibition\nCFLAR                  CASP8                  inhibition\nCASP8                  AR                     inhibition\nAR                     CFLAR                  stimulation\nCASP8                  CASP3                  stimulation\nCASP3                  BCL2                   inhibition\nCASP8                  TP73                   stimulation\nTP73                   BAX                    stimulation\nTP53                   CASP8                  stimulation\nCASP8                  EIF4G2                 stimulation\nEIF4G2                 XIAP                   stimulation\nBIRC2                  CASP8                  inhibition\nEIF4G2                 BIRC2                  stimulation\nBIRC3                  CASP8                  inhibition\nCASP8                  IKBKB                  stimulation\nMAP3K7                 MAPK3                  stimulation\nMAPK3                  CASP8                  inhibition\nJUN                    EDN1                   stimulation\nEDN1                   CASP8                  stimulation\nCASP8                  PAK2                   stimulation\nPAK2                   JUN                    stimulation\nFOS                    EDN1                   stimulation\nPIK3CA                 MAPK3                  inhibition\nCASP8                  RALBP1                 stimulation\nRALBP1                 AKT1                   inhibition\nMTOR                   BCL2                   stimulation\nCASP8                  CHUK                   stimulation\nCASP8                  PSEN1                  stimulation\nPSEN1                  TP53                   stimulation\nCDKN1A                 E2F1                   inhibition\nCASP2                  CASP8                  stimulation\nCASP8                  ALPI                   stimulation\nALPI                   CASP9                  inhibition\nTP53                   CFLAR                  stimulation\nMAP3K7                 MAPK8                  stimulation\nPIK3CA                 MAPK8                  stimulation\nPTEN                   AR                     inhibition\nMTOR                   AKT1                   stimulation\nCDK4                   CBL                    stimulation\nCBL                    CFLAR                  inhibition\nE2F1                   DDB2                   stimulation\nDDB2                   CFLAR                  stimulation\nCFLAR                  DAXX                   inhibition\nDAXX                   TP53                   stimulation\nCFLAR                  CASP10                 inhibition\nCASP10                 CASP3                  stimulation\nCASP10                 APAF1                  stimulation\nBAX                    BAD                    inhibition\nBCL2                   BAX                    inhibition\nTP53                   BCL2                   inhibition\nBIRC2                  CASP3                  inhibition\nIKBKB                  IRS1                   inhibition\nIRS1                   BCL2                   inhibition\nBCL2                   ATM                    stimulation\nATM                    NFKBIA                 stimulation\nJUN                    IL5                    stimulation\nIL5                    BCL2                   inhibition\nFOS                    IL5                    stimulation\nBCL2                   APEX1                  stimulation\nAPEX1                  FOS                    stimulation\nBCL2                   CTNNB1                 stimulation\nCTNNB1                 PIK3CA                 stimulation\nATM                    AKT1                   stimulation\nPTEN                   CREB1                  inhibition\nCREB1                  BCL2                   stimulation\nBCL2                   TERT                   stimulation\nCCND1                  CDK6                   stimulation\nCDK6                   BCL2                   inhibition\nBCL2                   CCND1                  inhibition\nCDK4                   E2F2                   inhibition\nE2F2                   BCL2                   stimulation\nMYC                    CDK4                   stimulation\nBCL2                   PARP1                  inhibition\nMYC                    BAG1                   stimulation\nBAG1                   BCL2                   stimulation\nPARP1                  TP53                   stimulation\nMYC                    CDKN1A                 inhibition\nBCL2                   PRNP                   stimulation\nPRNP                   CASP3                  stimulation\nBCL2                   APAF1                  inhibition\nAPAF1                  CASP9                  stimulation\nMCL1                   BAX                    inhibition\nTP53                   BAX                    stimulation\nBAX                    DIABLO                 stimulation\nCASP3                  BAX                    stimulation\nBIRC3                  BID                    stimulation\nIKBKB                  TP63                   stimulation\nTP63                   BAX                    stimulation\nRELA                   BAX                    inhibition\nAKT1                   BAX                    inhibition\nPTEN                   SP1                    inhibition\nSP1                    BAX                    stimulation\nMTOR                   RPS6KB1                stimulation\nRPS6KB1                BAX                    stimulation\nCDK4                   UBB                    stimulation\nUBB                    BAX                    inhibition\nE2F1                   TP73                   stimulation\nMYC                    BAX                    stimulation\nBAD                    TP53                   stimulation\nBAX                    CYCS                   stimulation\nCYCS                   CASP3                  stimulation\nBAX                    APAF1                  stimulation\nRELA                   CSF2                   inhibition\nCSF2                   MCL1                   stimulation\nJUN                    CSF2                   stimulation\nFOS                    CSF2                   stimulation\nAKT1                   MCL1                   stimulation\nPTEN                   E2F1                   stimulation\nE2F1                   MCL1                   inhibition\nMTOR                   HIF1A                  stimulation\nHIF1A                  MCL1                   stimulation\nCCND1                  TFDP1                  inhibition\nTFDP1                  MCL1                   inhibition\nCDK4                   TFDP1                  inhibition\nMYC                    BCL2L11                stimulation\nBCL2L11                MCL1                   inhibition\nCDKN1A                 TFDP1                  inhibition\nBAD                    CASP9                  inhibition\nMCL1                   COX5B                  inhibition\nCOX5B                  APAF1                  stimulation\nXIAP                   MAP3K7                 stimulation\nMAP3K7                 IKBKB                  stimulation\nXIAP                   CASP3                  inhibition\nCASP3                  NFKBIA                 stimulation\nCASP3                  RELA                   inhibition\nMAP3K7                 AKT3                   stimulation\nAKT3                   XIAP                   stimulation\nAKT1                   XIAP                   stimulation\nXIAP                   MAPK8                  stimulation\nMAPK8                  JUN                    stimulation\nMAPK8                  FOS                    stimulation\nPIK3CA                 AKT2                   stimulation\nAKT2                   XIAP                   stimulation\nPTEN                   PIK3CA                 inhibition\nMTOR                   AKT2                   stimulation\nXIAP                   IL6                    stimulation\nIL6                    CDK4                   stimulation\nMYC                    BIRC5                  stimulation\nBIRC5                  XIAP                   stimulation\nMAPK8                  MYC                    stimulation\nCASP9                  EIF4G2                 stimulation\nXIAP                   APAF1                  inhibition\nBIRC3                  BIRC2                  stimulation\nBIRC2                  IKBKG                  stimulation\nIKBKG                  NFKBIA                 stimulation\nIKBKG                  RELA                   stimulation\nMAP3K7                 NFKB1                  stimulation\nBIRC2                  RIPK2                  stimulation\nRIPK2                  MAP3K7                 stimulation\nMAPK8                  ELK1                   stimulation\nELK1                   BIRC2                  stimulation\nRIPK2                  MAPK8                  stimulation\nJUN                    CD40LG                 stimulation\nCD40LG                 BIRC2                  stimulation\nFOS                    CD40LG                 stimulation\nAKT1                   HTRA2                  inhibition\nHTRA2                  BIRC2                  inhibition\nFASLG                  AKT1                   stimulation\nNFKB2                  BIRC2                  stimulation\nBIRC3                  RIPK2                  stimulation\nRIPK2                  IKBKB                  stimulation\nHTRA2                  BIRC3                  inhibition\nNFKB2                  BIRC3                  stimulation\nIKBKB                  IRAK1                  stimulation\nIRAK1                  MAP3K7                 stimulation\nAKT1                   IKBKB                  stimulation\nIKBKB                  NGFR                   stimulation\nNGFR                   MAPK8                  stimulation\nFASLG                  IKBKB                  stimulation\nAKT2                   IKBKB                  stimulation\nIKBKB                  FOXO3                  inhibition\nFOXO3                  PIK3CA                 stimulation\nIKBKB                  CDKN2A                 inhibition\nCDKN2A                 CCND1                  inhibition\nCDKN2A                 CDK4                   inhibition\nE2F1                   MAP3K5                 stimulation\nNGFR                   TP53                   stimulation\nCASP3                  IKBKB                  inhibition\nIKBKB                  NFE2L2                 inhibition\nNFE2L2                 CASP3                  stimulation\nIKBKB                  BAD                    inhibition\nRELA                   NFKBIA                 inhibition\nIL23A                  RELA                   stimulation\nMAPK3                  NFKBIA                 inhibition\nRXRA                   NFKBIA                 stimulation\nIL2                    MAPK8                  stimulation\nJUN                    NFKBIA                 inhibition\nCOMPLEX:P19838_Q04206  JUN                    stimulation\nFOS                    IL12B                  stimulation\nIL12B                  NFKBIA                 stimulation\nIL23A                  PIK3CA                 stimulation\nIL2                    AKT1                   stimulation\nMTOR                   RPS6KA2                stimulation\nRPS6KA2                NFKBIA                 inhibition\nIL2                    MTOR                   stimulation\nCOMPLEX:P19838_Q04206  CCND1                  stimulation\nE2F1                   SIRT1                  stimulation\nMYC                    CUL1                   stimulation\nCUL1                   NFKBIA                 inhibition\nIL2                    MYC                    stimulation\nMAPK3                  RELA                   stimulation\nSTAT1                  RELA                   inhibition\nJUN                    IL1B                   stimulation\nIL1B                   RELA                   stimulation\nFOS                    IL1B                   stimulation\nAKT1                   TSC22D3                stimulation\nTSC22D3                RELA                   inhibition\nRELA                   TGFB1                  stimulation\nTGFB1                  AKT1                   stimulation\nPPP2CA                 RELA                   inhibition\nRELA                   CXCL8                  stimulation\nFOS                    CDK4                   stimulation\nCUL1                   RELA                   stimulation\nTP53                   RAC1                   inhibition\nRAC1                   RELA                   stimulation\nRELA                   EGR1                   stimulation\nEGR1                   TP53                   stimulation\nEGR1                   CDKN1A                 stimulation\nMAPK8                  LAT                    inhibition\nLAT                    MAP3K7                 stimulation\nJUN                    SMAD7                  stimulation\nSMAD7                  MAP3K7                 stimulation\nIL2                    JUN                    stimulation\nFOS                    SMAD7                  stimulation\nMAPK11                 MAP3K7                 inhibition\nMAP3K7                 ZAP70                  stimulation\nZAP70                  PIK3CA                 stimulation\nAKT1                   GNAI1                  stimulation\nGNAI1                  MAP3K7                 stimulation\nMAP3K7                 BMP2                   inhibition\nBMP2                   PTEN                   inhibition\nPPP2CA                 MAP3K7                 inhibition\nMYC                    TRIM8                  inhibition\nTRIM8                  MAP3K7                 stimulation\nMAPK8                  CDKN1A                 stimulation\nMAP3K1                 MAP3K7                 stimulation\nMAP3K7                 PRKCD                  stimulation\nPRKCD                  CASP3                  stimulation\nJUN                    IL2                    stimulation\nFOS                    IL2                    stimulation\nINS                    PIK3CA                 stimulation\nAKT1                   SH3RF1                 inhibition\nSH3RF1                 MAPK8                  stimulation\nAKT1                   PTEN                   inhibition\nAKT2                   MAPK8                  inhibition\nMAPK8                  SHC1                   stimulation\nSHC1                   MTOR                   stimulation\nMAPK8                  SMAD4                  stimulation\nSMAD4                  CCND1                  stimulation\nCDKN1A                 CDK4                   inhibition\nMYC                    PTK2B                  inhibition\nPTK2B                  MAPK8                  stimulation\nTP53                   DUSP4                  stimulation\nCDKN1A                 RAC1                   stimulation\nRAC1                   MAPK8                  stimulation\nCASP3                  ROCK1                  stimulation\nROCK1                  MAPK8                  stimulation\nMAPK8                  NAIP                   inhibition\nNAIP                   CASP3                  inhibition\nCASP9                  LYN                    inhibition\nLYN                    MAPK8                  stimulation\nMAPK8                  RARA                   stimulation\nRARA                   CASP9                  stimulation\nFOS                    JUN                    stimulation\nJUN                    SMAD4                  stimulation\nSMAD4                  FOS                    stimulation\nPIK3CA                 ILK                    stimulation\nILK                    JUN                    stimulation\nJUN                    PTEN                   inhibition\nAKT1                   JUN                    stimulation\nPTEN                   NOTCH1                 stimulation\nNOTCH1                 JUN                    inhibition\nAKT2                   JUN                    stimulation\nJUN                    CCND1                  stimulation\nCDK4                   MEF2D                  inhibition\nMEF2D                  JUN                    stimulation\nJUN                    CDK4                   stimulation\nE2F1                   AR                     inhibition\nAR                     JUN                    stimulation\nJUN                    CCND3                  stimulation\nCCND3                  E2F1                   inhibition\nJUN                    MYC                    inhibition\nTP53                   VDR                    stimulation\nVDR                    JUN                    inhibition\nCDKN1A                 CDK3                   inhibition\nCDK3                   JUN                    stimulation\nJUN                    CDKN1A                 stimulation\nCASP3                  ARHGDIB                stimulation\nARHGDIB                JUN                    stimulation\nJUN                    IFNG                   stimulation\nIFNG                   CASP3                  stimulation\nLYN                    JUN                    inhibition\nJUN                    BCL2L1                 stimulation\nBCL2L1                 CASP9                  inhibition\nJUN                    ACHE                   stimulation\nACHE                   APAF1                  stimulation\nFOS                    PTEN                   inhibition\nAKT1                   FOS                    stimulation\nNOTCH1                 FOS                    inhibition\nAKT2                   FOS                    stimulation\nFOS                    CCND1                  stimulation\nCDK4                   SMAD4                  stimulation\nMYC                    HNRNPR                 stimulation\nHNRNPR                 FOS                    stimulation\nVDR                    FOS                    inhibition\nIL1B                   CDKN1A                 stimulation\nCASP3                  PPP3CA                 stimulation\nPPP3CA                 FOS                    inhibition\nLYN                    FOS                    inhibition\nFOS                    CDK1                   stimulation\nCDK1                   CASP9                  inhibition\nAPAF1                  MRTFA                  stimulation\nMRTFA                  FOS                    stimulation\nTP53                   APAF1                  stimulation\nAKT1                   FGR                    stimulation\nFGR                    PIK3CA                 stimulation\nPIK3CA                 CDC42                  stimulation\nCDC42                  PTEN                   stimulation\nMTOR                   IRS4                   inhibition\nIRS4                   PIK3CA                 stimulation\nPIK3CA                 MTOR                   stimulation\nCCND1                  VEGFA                  inhibition\nVEGFA                  PIK3CA                 stimulation\nPIK3CA                 CCND1                  stimulation\nE2F1                   FGFR2                  stimulation\nFGFR2                  PIK3CA                 stimulation\nMYC                    GNG2                   inhibition\nGNG2                   PIK3CA                 stimulation\nPIK3CA                 MYC                    stimulation\nTP53                   PTK2                   inhibition\nPTK2                   PIK3CA                 stimulation\nCASP3                  LAMB2                  stimulation\nLAMB2                  PIK3CA                 stimulation\nPIK3CA                 PRKCD                  stimulation\nLYN                    PIK3CA                 stimulation\nPIK3CA                 RAC1                   stimulation\nRAC1                   APAF1                  stimulation\nAKT1                   RHEB                   stimulation\nRHEB                   MTOR                   stimulation\nCDK4                   PELP1                  stimulation\nPELP1                  AKT1                   stimulation\nSIRT1                  AKT1                   stimulation\nAKT1                   TP53BP1                inhibition\nTP53BP1                TP53                   stimulation\nCDKN1A                 COMPLEX:P20248_P24941  inhibition\nCOMPLEX:P20248_P24941  AKT1                   stimulation\nAKT1                   HSPB1                  inhibition\nHSPB1                  CASP3                  inhibition\nCASP9                  EIF4E                  stimulation\nEIF4E                  AKT1                   stimulation\nAKT1                   APAF1                  inhibition\nPTEN                   SOS1                   inhibition\nSOS1                   MTOR                   stimulation\nNOTCH1                 CCND1                  stimulation\nE2F1                   EGR1                   stimulation\nEGR1                   PTEN                   stimulation\nHSP90AA1               PTEN                   stimulation\nNOTCH1                 TP53                   inhibition\nNOTCH1                 CDKN1A                 stimulation\nE2F1                   CASP9                  stimulation\nE2F1                   APAF1                  stimulation\nMYC                    TSC2                   inhibition\nTSC2                   MTOR                   stimulation\nRPS6KB1                MYC                    stimulation\nTP53                   EGFR                   stimulation\nEGFR                   MTOR                   stimulation\nMTOR                   TRIM24                 stimulation\nTRIM24                 TP53                   inhibition\nCCND1                  CDK4                   stimulation\nE2F1                   DDAH2                  stimulation\nDDAH2                  CCND1                  stimulation\nMYC                    CCND1                  stimulation\nCCND1                  E2F3                   inhibition\nE2F3                   MYC                    stimulation\nEGFR                   CCND1                  stimulation\nE2F3                   CDKN1A                 stimulation\nTFDP1                  APAF1                  stimulation\nCDKN2A                 CDK4                   inhibition\nSMAD4                  MYC                    stimulation\nCDK4                   XPO1                   stimulation\nXPO1                   TP53                   inhibition\nSMAD4                  CDKN1A                 stimulation\nE2F1                   CASP3                  stimulation\nCUL1                   E2F1                   stimulation\nEGFR                   E2F1                   stimulation\nTP73                   CDKN1A                 inhibition\nRAC1                   MYC                    stimulation\nPTK2B                  TP53                   stimulation\nCASP3                  RB1                    inhibition\nRB1                    MYC                    inhibition\nBIRC5                  CASP9                  inhibition\nMYC                    HSPA4                  stimulation\nHSPA4                  APAF1                  inhibition\nCDKN1A                 CCNE1                  inhibition\nCCNE1                  TP53                   stimulation\nCASP3                  PPP2R5C                inhibition\nPPP2R5C                TP53                   stimulation\nGSN                    CASP9                  inhibition\nTNF                    MAP4K4                 stimulation\nCSF3                   TNF                    inhibition\nTNF                    IL23A                  stimulation\nTNF                    MAP2K3                 stimulation\nTNF                    LPL                    stimulation\nTNF                    IFNG                   inhibition\nTNF                    MAPK1                  stimulation\nTNF                    BID                    stimulation\nTNF                    TNFRSF1B               stimulation\nTNF                    MAP3K5                 stimulation\nTNF                    TNFAIP3                stimulation\nTNFAIP3                TNF                    stimulation\nTNF                    CHUK                   stimulation\nTNF                    NFKB1                  stimulation\nTNF                    MAP2K7                 stimulation\nS100B                  TNF                    inhibition\nTNF                    MAPK14                 stimulation\nMAPK14                 TNF                    inhibition\nTNF                    MAP2K4                 stimulation\nTNF                    MAP3K1                 stimulation\nTNF                    EDN1                   stimulation\nTNF                    PSEN1                  stimulation\nTNF                    IRS1                   stimulation\nTNF                    ATM                    stimulation\nAPEX1                  TNF                    inhibition\nCREB1                  TNF                    stimulation\nSP1                    TNF                    inhibition\nTNF                    RPS6KB1                stimulation\nTNF                    CSF2                   stimulation\nCSF2                   TNF                    inhibition\nTNF                    IL6                    stimulation\nTNF                    IKBKG                  stimulation\nTNF                    NFE2L2                 stimulation\nCOMPLEX:P19838_Q04206  TNF                    stimulation\nIL12B                  TNF                    stimulation\nTNF                    IL1B                   stimulation\nTNF                    FGR                    stimulation\nTNF                    IRS4                   stimulation\nTNF                    PTK2                   stimulation\nTNFRSF1A               MAP2K3                 stimulation\nTNFRSF1B               TNFRSF1A               stimulation\nTNFRSF1A               TNFAIP3                stimulation\nTNFRSF1A               NFKB1                  stimulation\nTNFRSF1A               MAP2K7                 stimulation\nS100B                  TNFRSF1A               inhibition\nTNFRSF1A               MAP2K4                 stimulation\nTNFRSF1A               MAP3K1                 stimulation\nTNFRSF1A               DAXX                   stimulation\nTNFRSF1A               IKBKG                  stimulation\nTRADD                  MAP4K4                 stimulation\nTRADD                  MAP2K3                 stimulation\nTRADD                  CHUK                   stimulation\nTRADD                  MAP2K7                 stimulation\nTRADD                  CASP2                  stimulation\nS100B                  TRADD                  inhibition\nTRADD                  MAP2K4                 stimulation\nTRADD                  MAP3K1                 stimulation\nTRADD                  IKBKG                  stimulation\nTRAF2                  MAP2K3                 stimulation\nTRAF2                  LPL                    stimulation\nTRAF2                  MAPK11                 stimulation\nTNFRSF1B               TRAF2                  stimulation\nTNFAIP3                TRAF2                  inhibition\nTRAF2                  CHUK                   stimulation\nTRAF2                  NFKB1                  stimulation\nTRAF2                  MAPK14                 stimulation\nTRAF2                  TICAM1                 stimulation\nTRAF2                  MAP2K4                 stimulation\nTRAF2                  MAP3K1                 stimulation\nTRAF2                  IKBKG                  stimulation\nRIPK1                  MAP2K3                 stimulation\nTNFAIP3                RIPK1                  inhibition\nRIPK1                  CHUK                   stimulation\nTNFRSF10B              RIPK1                  stimulation\nRIPK1                  NFKB1                  stimulation\nS100B                  RIPK1                  inhibition\nRIPK1                  MAP2K4                 stimulation\nRIPK1                  MAP3K1                 stimulation\nCASP10                 RIPK1                  inhibition\nRIPK1                  IKBKG                  stimulation\nFADD                   MAP4K4                 stimulation\nMYD88                  FADD                   stimulation\nFADD                   CASP7                  stimulation\nFADD                   CHUK                   stimulation\nTNFRSF10B              FADD                   stimulation\nS100B                  FADD                   inhibition\nFADD                   CASP10                 stimulation\nFADD                   IKBKG                  stimulation\nRIPK2                  FADD                   inhibition\nIFNG                   CASP8                  stimulation\nMAPK1                  CASP8                  inhibition\nCASP8                  BID                    stimulation\nTNFRSF10B              CASP8                  stimulation\nNFKB1                  CASP8                  inhibition\nS100B                  CASP8                  inhibition\nMAPK14                 CASP8                  inhibition\nCASP8                  CASP10                 inhibition\nCASP8                  TP63                   stimulation\nCASP8                  IKBKG                  stimulation\nCDK1                   CASP8                  inhibition\nCASP8                  EIF4E                  stimulation\nATM                    CFLAR                  inhibition\nBCL2                   BID                    inhibition\nSTAT1                  BCL2                   stimulation\nPPP2CA                 BCL2                   stimulation\nNFKB2                  BCL2                   stimulation\nMAPK14                 BCL2                   inhibition\nHSP90AA1               BCL2                   stimulation\nEIF4G2                 BCL2                   stimulation\nATM                    BCL2                   inhibition\nCTNNB1                 BCL2                   stimulation\nBCL2                   CYCS                   inhibition\nBCL2L11                BCL2                   inhibition\nBCL2                   COX5B                  inhibition\nIL6                    BCL2                   stimulation\nBCL2L1                 BCL2                   stimulation\nVEGFA                  BCL2                   stimulation\nPPP2R5C                BCL2                   inhibition\nPRKCZ                  BAX                    inhibition\nPRNP                   BAX                    inhibition\nBCL2L11                BAX                    stimulation\nBAX                    COX5B                  stimulation\nAKT3                   BAX                    inhibition\nBAX                    HTRA2                  stimulation\nBCL2L1                 BAX                    inhibition\nIL6                    MCL1                   stimulation\nCDK1                   MCL1                   inhibition\nVEGFA                  MCL1                   stimulation\nNFKB2                  XIAP                   stimulation\nXIAP                   RIPK2                  stimulation\nELK1                   XIAP                   stimulation\nHTRA2                  XIAP                   inhibition\nBIRC2                  CASP7                  inhibition\nBIRC3                  CASP7                  inhibition\nS100B                  BIRC3                  inhibition\nBIRC3                  MAP2K4                 stimulation\nELK1                   BIRC3                  stimulation\nMAP4K4                 IKBKB                  stimulation\nMYD88                  IKBKB                  stimulation\nCHUK                   IKBKB                  stimulation\nTNFRSF10B              IKBKB                  stimulation\nFLNA                   IKBKB                  stimulation\nSQSTM1                 IKBKB                  stimulation\nTRAF6                  IKBKB                  stimulation\nPRKCZ                  IKBKB                  stimulation\nMAP3K1                 IKBKB                  stimulation\nAKT3                   IKBKB                  stimulation\nIKBKG                  IKBKB                  stimulation\nIRAK1                  IKBKB                  stimulation\nNGFR                   IKBKB                  stimulation\nIKBKB                  COMPLEX:P19838_Q04206  inhibition\nIKBKB                  TSC22D3                stimulation\nIKBKB                  IRS4                   inhibition\nTRAF1                  NFKBIA                 stimulation\nIL23A                  NFKBIA                 stimulation\nPPARA                  NFKBIA                 inhibition\nMAPK1                  NFKBIA                 inhibition\nTNFAIP3                NFKBIA                 inhibition\nNFKB1                  NFKBIA                 stimulation\nMAPK14                 NFKBIA                 inhibition\nTRAF6                  NFKBIA                 stimulation\nPRKCZ                  NFKBIA                 inhibition\nMAP3K1                 NFKBIA                 stimulation\nSP1                    NFKBIA                 inhibition\nPRKCD                  NFKBIA                 inhibition\nHSPB1                  NFKBIA                 inhibition\nRELA                   TRAF1                  stimulation\nTRAF1                  RELA                   stimulation\nRELA                   IL23A                  stimulation\nRELA                   LPL                    inhibition\nMAPK1                  RELA                   stimulation\nCHUK                   RELA                   stimulation\nRELA                   TRAF5                  stimulation\nNFKB1                  RELA                   stimulation\nMAPK14                 RELA                   stimulation\nSQSTM1                 RELA                   stimulation\nRELA                   TRAF6                  stimulation\nTRAF6                  RELA                   stimulation\nPRKCZ                  RELA                   stimulation\nMAP3K1                 RELA                   stimulation\nRELA                   AR                     inhibition\nRELA                   SP1                    stimulation\nRELA                   IL6                    stimulation\nRELA                   BIRC5                  stimulation\nIRAK1                  RELA                   stimulation\nNGFR                   RELA                   stimulation\nRELA                   IL12B                  stimulation\nIL12B                  RELA                   stimulation\nRPS6KA2                RELA                   stimulation\nSIRT1                  RELA                   inhibition\nPRKCD                  RELA                   stimulation\nRELA                   BCL2L1                 stimulation\nRELA                   VEGFA                  stimulation\nMAP4K4                 MAP3K7                 stimulation\nCYLD                   MAP3K7                 stimulation\nMAP3K7                 RXRA                   stimulation\nMAP3K7                 TGFB1                  stimulation\nTGFB1                  MAP3K7                 stimulation\nMAP3K7                 CHUK                   stimulation\nMAP3K7                 MAP2K1                 stimulation\nEPHB2                  MAP3K7                 stimulation\nMAP3K7                 MAPK14                 stimulation\nTICAM1                 MAP3K7                 stimulation\nMAP3K7                 MAP2K4                 stimulation\nMAP3K7                 DAXX                   stimulation\nMAP3K7                 TERT                   inhibition\nBMP2                   MAP3K7                 stimulation\nMAPK8                  PPARA                  stimulation\nMAP2K3                 MAPK8                  stimulation\nBDNF                   MAPK8                  stimulation\nTGFB1                  MAPK8                  stimulation\nMAPK1                  MAPK8                  inhibition\nMAPK8                  BID                    stimulation\nMAP2K1                 MAPK8                  stimulation\nMAPK8                  MAPK9                  stimulation\nMAPK8                  MAPK14                 stimulation\nTRAF6                  MAPK8                  stimulation\nPRKCZ                  MAPK8                  stimulation\nMAP3K1                 MAPK8                  stimulation\nMAPK8                  AR                     stimulation\nEDN1                   MAPK8                  stimulation\nMAPK8                  CREB1                  stimulation\nMAPK8                  SP1                    stimulation\nMAPK8                  RPS6KB1                stimulation\nMAPK8                  IL6                    stimulation\nCD40LG                 MAPK8                  stimulation\nMAPK8                  COMPLEX:P19838_Q04206  stimulation\nMAPK8                  SIRT1                  stimulation\nIL1B                   MAPK8                  stimulation\nGNAI1                  MAPK8                  stimulation\nPRKCD                  MAPK8                  stimulation\nILK                    MAPK8                  stimulation\nMAPK8                  BCL2L1                 inhibition\nCDC42                  MAPK8                  stimulation\nMAPK8                  IRS4                   inhibition\nMAPK8                  TRIM24                 stimulation\nMAPK8                  XPO1                   stimulation\nJUN                    IL23A                  stimulation\nMAPK11                 JUN                    stimulation\nBDNF                   JUN                    stimulation\nJUN                    TGFB1                  stimulation\nJUN                    CXCL8                  stimulation\nRB1                    JUN                    stimulation\nMAPK1                  JUN                    stimulation\nMAPK14                 JUN                    stimulation\nMAP3K1                 JUN                    stimulation\nJUN                    CTNNB1                 stimulation\nJUN                    CREB1                  stimulation\nJUN                    TERT                   inhibition\nJUN                    BCL2L11                stimulation\nAKT3                   JUN                    stimulation\nJUN                    IL6                    stimulation\nELK1                   JUN                    stimulation\nJUN                    CDKN2A                 stimulation\nJUN                    IL12B                  stimulation\nJUN                    EGR1                   stimulation\nJUN                    VEGFA                  stimulation\nJUN                    CDKN2A                 stimulation\nMAPK11                 FOS                    stimulation\nFOS                    TGFB1                  stimulation\nFOS                    IFNG                   stimulation\nFOS                    CXCL8                  stimulation\nMAPK1                  FOS                    stimulation\nMAPK14                 FOS                    stimulation\nCREB1                  FOS                    stimulation\nFOS                    TERT                   inhibition\nFOS                    BCL2L11                stimulation\nAKT3                   FOS                    stimulation\nFOS                    IL6                    stimulation\nELK1                   FOS                    stimulation\nIL12B                  FOS                    stimulation\nILK                    FOS                    stimulation\nFOS                    VEGFA                  stimulation\nTGFB1                  PIK3CA                 stimulation\nIFNG                   PIK3CA                 stimulation\nPIK3CA                 NFKB1                  stimulation\nPIK3CA                 MAP2K1                 stimulation\nPIK3CA                 MAPK14                 stimulation\nIRS1                   PIK3CA                 stimulation\nIL5                    PIK3CA                 stimulation\nPIK3CA                 CREB1                  stimulation\nPIK3CA                 SP1                    stimulation\nPIK3CA                 RPS6KB1                stimulation\nPIK3CA                 AKT3                   stimulation\nCD40LG                 PIK3CA                 stimulation\nCDKN2A                 PIK3CA                 inhibition\nIL12B                  PIK3CA                 stimulation\nLAT                    PIK3CA                 stimulation\nGNAI1                  PIK3CA                 stimulation\nSHC1                   PIK3CA                 stimulation\nPIK3CA                 PTK2B                  stimulation\nPIK3CA                 CCND3                  stimulation\nPIK3CA                 BCL2L1                 stimulation\nPIK3CA                 SOS1                   stimulation\nSOS1                   PIK3CA                 stimulation\nPIK3CA                 DDAH2                  stimulation\nCDKN2A                 PIK3CA                 inhibition\nAKT1                   MAPK3                  stimulation\nINS                    AKT1                   stimulation\nAKT1                   TGFB1                  inhibition\nAKT1                   RB1                    stimulation\nAKT1                   MAP3K5                 inhibition\nRAC1                   AKT1                   stimulation\nAKT1                   CHUK                   stimulation\nAKT1                   NFKB1                  stimulation\nPPP2CA                 AKT1                   inhibition\nAKT1                   OTUD7B                 stimulation\nAKT1                   MAP2K4                 inhibition\nPRKCZ                  AKT1                   inhibition\nEDN1                   AKT1                   stimulation\nAKT1                   CBL                    stimulation\nAKT1                   IRS1                   stimulation\nAKT1                   CTNNB1                 stimulation\nAKT1                   CREB1                  stimulation\nAKT1                   TERT                   stimulation\nAKT1                   RPS6KB1                stimulation\nAKT1                   HIF1A                  stimulation\nAKT1                   BCL2L11                inhibition\nAKT1                   AKT2                   inhibition\nAKT1                   BIRC5                  stimulation\nCD40LG                 AKT1                   stimulation\nAKT1                   IRAK1                  inhibition\nAKT1                   COMPLEX:P19838_Q04206  stimulation\nGNAI1                  AKT1                   stimulation\nAKT1                   PRKCD                  stimulation\nSHC1                   AKT1                   stimulation\nILK                    AKT1                   stimulation\nAKT1                   MEF2D                  stimulation\nAKT1                   BCL2L1                 stimulation\nLAMB2                  AKT1                   stimulation\nSOS1                   AKT1                   stimulation\nAKT1                   TSC2                   inhibition\nPPP2R5C                AKT1                   inhibition\nPTEN                   RAC1                   stimulation\nPTEN                   EGFR                   inhibition\nPTEN                   AKT2                   inhibition\nPTEN                   SHC1                   inhibition\nROCK1                  PTEN                   stimulation\nPTEN                   PTK2                   inhibition\nTGFB1                  MTOR                   stimulation\nMTOR                   IRS1                   inhibition\nMTOR                   CYCS                   stimulation\nMTOR                   AKT3                   stimulation\nMTOR                   PPP3CA                 stimulation\nCDC42                  MTOR                   stimulation\nMTOR                   EIF4E                  inhibition\nMAPK1                  CCND1                  stimulation\nRAC1                   CCND1                  stimulation\nSTAT1                  CCND1                  stimulation\nNFKB2                  CCND1                  stimulation\nMAPK14                 CCND1                  stimulation\nCREB1                  CCND1                  stimulation\nTERT                   CCND1                  stimulation\nCCND1                  E2F2                   inhibition\nSP1                    CCND1                  stimulation\nELK1                   CCND1                  stimulation\nCCND1                  DDAH2                  inhibition\nCDKN2A                 CCND1                  inhibition\nTGFB1                  CDK4                   inhibition\nCCND3                  CDK4                   stimulation\nCDK4                   E2F3                   inhibition\nRB1                    E2F1                   inhibition\nE2F1                   BID                    stimulation\nE2F1                   NFKB1                  inhibition\nATM                    E2F1                   stimulation\nE2F1                   CTNNB1                 inhibition\nE2F1                   E2F2                   stimulation\nSP1                    E2F1                   stimulation\nE2F1                   CYCS                   stimulation\nE2F1                   TFDP1                  stimulation\nE2F1                   BCL2L11                stimulation\nE2F1                   BIRC5                  stimulation\nSIRT1                  E2F1                   inhibition\nCDK3                   E2F1                   inhibition\nCDK1                   E2F1                   stimulation\nVEGFA                  E2F1                   stimulation\nCOMPLEX:P20248_P24941  E2F1                   stimulation\nE2F3                   E2F1                   stimulation\nCCNE1                  E2F1                   stimulation\nMYC                    TRAF1                  inhibition\nPPARA                  MYC                    inhibition\nINS                    MYC                    stimulation\nMAPK11                 MYC                    stimulation\nRXRA                   MYC                    stimulation\nMYC                    CXCL8                  stimulation\nMYC                    CDK6                   stimulation\nMAPK1                  MYC                    stimulation\nCHUK                   MYC                    stimulation\nMAPK9                  MYC                    stimulation\nPPP2CA                 MYC                    stimulation\nMAPK14                 MYC                    stimulation\nPAK2                   MYC                    inhibition\nIL5                    MYC                    stimulation\nCTNNB1                 MYC                    stimulation\nCREB1                  MYC                    stimulation\nE2F2                   MYC                    stimulation\nMYC                    SP1                    stimulation\nMYC                    CYCS                   stimulation\nMYC                    TFDP1                  stimulation\nMYC                    VEGFA                  stimulation\nMYC                    EIF4E                  stimulation\nMYC                    CCNE1                  stimulation\nTP53                   MAP4K4                 stimulation\nMAPK11                 TP53                   stimulation\nBDNF                   TP53                   stimulation\nTGFB1                  TP53                   stimulation\nTP53                   RB1                    stimulation\nMAPK1                  TP53                   stimulation\nTP53                   BID                    stimulation\nRAC1                   TP53                   stimulation\nMAPK9                  TP53                   stimulation\nTP53                   NFKB2                  stimulation\nMAPK14                 TP53                   stimulation\nHSP90AA1               TP53                   inhibition\nTP53                   AR                     inhibition\nTP53                   TP73                   stimulation\nTP53                   DDB2                   stimulation\nTP53                   CASP10                 stimulation\nAPEX1                  TP53                   stimulation\nCREB1                  TP53                   stimulation\nTP53                   TERT                   inhibition\nBAG1                   TP53                   inhibition\nTP53                   TP63                   stimulation\nTP53                   UBB                    stimulation\nTP53                   BIRC5                  inhibition\nCD40LG                 TP53                   stimulation\nTP53                   NFE2L2                 inhibition\nSIRT1                  TP53                   inhibition\nPRKCD                  TP53                   stimulation\nTP53                   BCL2L1                 inhibition\nBCL2L1                 TP53                   inhibition\nCDK1                   TP53                   stimulation\nCOMPLEX:P20248_P24941  TP53                   stimulation\nHSPB1                  TP53                   inhibition\nTP53                   EIF4E                  inhibition\nTP53                   TSC2                   stimulation\nIL1A                   CDKN1A                 stimulation\nTGFB1                  CDKN1A                 stimulation\nIFNG                   CDKN1A                 stimulation\nCDKN1A                 RB1                    inhibition\nRAC1                   CDKN1A                 stimulation\nSTAT1                  CDKN1A                 stimulation\nAR                     CDKN1A                 stimulation\nDDB2                   CDKN1A                 inhibition\nCREB1                  CDKN1A                 stimulation\nCDKN1A                 E2F2                   inhibition\nTP63                   CDKN1A                 inhibition\nSP1                    CDKN1A                 stimulation\nHIF1A                  CDKN1A                 stimulation\nCDKN2A                 CDKN1A                 inhibition\nCUL1                   CDKN1A                 inhibition\nCDKN1A                 CCND3                  inhibition\nCDKN1A                 CDK1                   inhibition\nCDKN1A                 DDAH2                  stimulation\nCDKN2A                 CDKN1A                 inhibition\nCASP3                  BID                    stimulation\nCASP3                  TP73                   stimulation\nCASP3                  PAK2                   stimulation\nCASP3                  PSEN1                  stimulation\nCASP3                  BAD                    stimulation\nCASP3                  TERT                   stimulation\nCASP3                  TP63                   stimulation\nCASP3                  BCL2L11                stimulation\nVDR                    CASP3                  stimulation\nCASP3                  BCL2L1                 inhibition\nCASP3                  PTK2                   inhibition\nCASP3                  EIF4E                  stimulation\nMAP2K1                 CASP9                  inhibition\nPRKCZ                  CASP9                  inhibition\nDIABLO                 CASP9                  stimulation\nCYCS                   CASP9                  stimulation\nAKT3                   CASP9                  inhibition\nNAIP                   CASP9                  inhibition\nHSP90AA1               APAF1                  inhibition\nEIF4G2                 APAF1                  stimulation\nDIABLO                 APAF1                  stimulation\nCYCS                   APAF1                  stimulation\nBIRC5                  APAF1                  inhibition\nMYD88                  MAP4K4                 stimulation\nIL1A                   MAP4K4                 stimulation\nMAP3K5                 MAP4K4                 stimulation\nMAP4K4                 CHUK                   stimulation\nCASP2                  MAP4K4                 stimulation\nEPHB2                  MAP4K4                 stimulation\nTRAF6                  MAP4K4                 stimulation\nMAP4K4                 MAP3K1                 stimulation\nMAP4K4                 IKBKG                  stimulation\nCD40LG                 MAP4K4                 stimulation\nIRAK1                  MAP4K4                 stimulation\nCYLD                   TRAF1                  inhibition\nTNFRSF1B               TRAF1                  stimulation\nTRAF1                  NFKB1                  stimulation\nNFKB1                  TRAF1                  stimulation\nTRAF1                  MAP2K7                 stimulation\nNFKB2                  TRAF1                  stimulation\nS100B                  TRAF1                  inhibition\nTRAF1                  TICAM1                 inhibition\nTICAM1                 TRAF1                  stimulation\nTRAF1                  MAP3K1                 stimulation\nMYD88                  CHUK                   stimulation\nMYD88                  TRAF6                  stimulation\nMYD88                  MAP3K1                 stimulation\nMYD88                  IKBKG                  stimulation\nMYD88                  RIPK2                  stimulation\nMYD88                  IRAK1                  stimulation\nMYD88                  NGFR                   stimulation\nMYD88                  IL1B                   inhibition\nIL1B                   MYD88                  inhibition\nCSF3                   MAPK3                  stimulation\nMAPK3                  PPARA                  stimulation\nMAP2K3                 MAPK3                  stimulation\nMAPK11                 MAPK3                  stimulation\nMAPK3                  BDNF                   stimulation\nBDNF                   MAPK3                  stimulation\nTGFB1                  MAPK3                  stimulation\nMAPK3                  IFNG                   stimulation\nMAPK3                  CXCL8                  inhibition\nSUCLA2                 MAPK3                  stimulation\nMAPK1                  MAPK3                  stimulation\nIL2                    MAPK3                  stimulation\nMAPK3                  CHUK                   stimulation\nNFKB1                  MAPK3                  stimulation\nMAP2K7                 MAPK3                  stimulation\nMAP2K1                 MAPK3                  stimulation\nMAPK9                  MAPK3                  stimulation\nEPHB2                  MAPK3                  stimulation\nPPP2CA                 MAPK3                  inhibition\nMAPK14                 MAPK3                  inhibition\nTRAF6                  MAPK3                  stimulation\nMAP2K4                 MAPK3                  stimulation\nPRKCZ                  MAPK3                  stimulation\nMAP3K1                 MAPK3                  stimulation\nEDN1                   MAPK3                  stimulation\nMAPK3                  BAD                    inhibition\nMAPK3                  IRS1                   inhibition\nIL5                    MAPK3                  stimulation\nMAPK3                  CREB1                  stimulation\nMAPK3                  TERT                   stimulation\nMAPK3                  SP1                    stimulation\nMAPK3                  RPS6KB1                stimulation\nCSF2                   MAPK3                  stimulation\nMAPK3                  HIF1A                  stimulation\nMAPK3                  BCL2L11                inhibition\nIL6                    MAPK3                  stimulation\nRIPK2                  MAPK3                  stimulation\nMAPK3                  ELK1                   stimulation\nMAPK3                  FOXO3                  inhibition\nMAPK3                  COMPLEX:P19838_Q04206  stimulation\nMAPK3                  RPS6KA2                stimulation\nIL1B                   MAPK3                  stimulation\nTSC22D3                MAPK3                  inhibition\nMAPK3                  EGR1                   stimulation\nMAPK3                  LAT                    inhibition\nGNAI1                  MAPK3                  stimulation\nPRKCD                  MAPK3                  inhibition\nMAPK3                  SHC1                   stimulation\nPTK2B                  MAPK3                  stimulation\nMAPK3                  ROCK1                  inhibition\nLYN                    MAPK3                  stimulation\nMAPK3                  RARA                   stimulation\nMAPK3                  BCL2L1                 stimulation\nMAPK3                  MRTFA                  inhibition\nVEGFA                  MAPK3                  stimulation\nMAPK3                  FGFR2                  inhibition\nPELP1                  MAPK3                  stimulation\nMAPK3                  TSC2                   inhibition\nMAPK3                  PPP2R5C                inhibition\nIFNG                   CSF3                   stimulation\nCXCL8                  CSF3                   inhibition\nCSF3                   IL2                    inhibition\nCSF3                   STAT1                  stimulation\nCSF3                   CSF2                   stimulation\nCYLD                   STAT1                  inhibition\nCYLD                   IKBKG                  inhibition\nIL23A                  IFNG                   stimulation\nMAPK1                  IL23A                  inhibition\nIL23A                  NFKB1                  stimulation\nNFKB1                  IL23A                  stimulation\nIL23A                  STAT1                  stimulation\nIL23A                  IL6                    stimulation\nIL23A                  IL1B                   stimulation\nIL1B                   IL23A                  stimulation\nRXRA                   PPARA                  stimulation\nMAPK1                  PPARA                  stimulation\nPPARA                  HSP90AA1               stimulation\nPPARA                  EDN1                   stimulation\nPPARA                  RPS6KB1                inhibition\nMAP2K3                 MAPK11                 stimulation\nMAP2K3                 TGFB1                  inhibition\nTGFB1                  MAP2K3                 stimulation\nMAPK1                  MAP2K3                 stimulation\nFASLG                  MAP2K3                 stimulation\nMAP3K5                 MAP2K3                 stimulation\nRAC1                   MAP2K3                 stimulation\nMAP2K3                 MAPK9                  stimulation\nMAP2K3                 MAPK14                 stimulation\nTRAF6                  MAP2K3                 stimulation\nMAP3K1                 MAP2K3                 stimulation\nDAXX                   MAP2K3                 stimulation\nIL1B                   MAP2K3                 stimulation\nPTK2B                  MAP2K3                 stimulation\nCDC42                  MAP2K3                 stimulation\nIFNG                   IL1A                   inhibition\nIL1A                   CXCL8                  stimulation\nIL1A                   MAPK1                  stimulation\nIL1A                   IL2                    stimulation\nIL1A                   CHUK                   stimulation\nIL1A                   TRAF6                  stimulation\nIL1A                   MAP3K1                 stimulation\nTP63                   IL1A                   stimulation\nIL1A                   CSF2                   stimulation\nIL1A                   IL6                    stimulation\nIL6                    IL1A                   stimulation\nIL1B                   IL1A                   stimulation\nINS                    MAPK1                  stimulation\nINS                    EGFR                   stimulation\nINS                    PARP1                  stimulation\nINS                    PRKCZ                  stimulation\nINS                    CBL                    stimulation\nINS                    IRS1                   stimulation\nINS                    AKT2                   stimulation\nINS                    SHC1                   stimulation\nINS                    IRS4                   stimulation\nINS                    FGFR2                  stimulation\nINS                    SOS1                   stimulation\nRXRA                   LPL                    stimulation\nTGFB1                  LPL                    inhibition\nLPL                    IFNG                   stimulation\nIFNG                   LPL                    inhibition\nSP1                    LPL                    inhibition\nMAPK11                 CXCL8                  inhibition\nIL2                    MAPK11                 stimulation\nRAC1                   MAPK11                 stimulation\nMAP2K7                 MAPK11                 stimulation\nMAPK11                 STAT1                  stimulation\nMAPK11                 MAPK14                 stimulation\nTRAF6                  MAPK11                 stimulation\nMAPK11                 EGFR                   inhibition\nMAP2K4                 MAPK11                 stimulation\nMAP3K1                 MAPK11                 stimulation\nMAPK11                 TP73                   stimulation\nPAK2                   MAPK11                 stimulation\nMAPK11                 CREB1                  stimulation\nMAPK11                 SP1                    stimulation\nMAPK11                 HIF1A                  stimulation\nMAPK11                 ELK1                   stimulation\nCD40LG                 MAPK11                 stimulation\nMAPK11                 NFE2L2                 inhibition\nMAPK11                 IL1B                   inhibition\nZAP70                  MAPK11                 stimulation\nSHC1                   MAPK11                 stimulation\nDUSP4                  MAPK11                 inhibition\nLYN                    MAPK11                 stimulation\nMAPK11                 MEF2D                  stimulation\nFGR                    MAPK11                 stimulation\nCDC42                  MAPK11                 stimulation\nVEGFA                  MAPK11                 stimulation\nGNG2                   MAPK11                 stimulation\nMAPK11                 TP53BP1                inhibition\nMAPK11                 HSPB1                  stimulation\nMAPK11                 EIF4E                  stimulation\nMAPK11                 TSC2                   stimulation\nBDNF                   MAPK1                  stimulation\nBDNF                   NFKB1                  stimulation\nBDNF                   MAPK9                  stimulation\nBDNF                   CTNNB1                 stimulation\nBDNF                   NGFR                   stimulation\nBDNF                   SHC1                   stimulation\nBDNF                   CDC42                  stimulation\nBDNF                   SOS1                   stimulation\nMAPK9                  RXRA                   inhibition\nMAP2K4                 RXRA                   inhibition\nRXRA                   AR                     stimulation\nAR                     RXRA                   stimulation\nRXRA                   CTNNB1                 inhibition\nRXRA                   RPS6KB1                inhibition\nRARA                   RXRA                   stimulation\nRXRA                   ILK                    stimulation\nVDR                    RXRA                   stimulation\nCDK1                   RXRA                   stimulation\nFGR                    RXRA                   stimulation\nTGFB1                  IFNG                   inhibition\nIFNG                   TGFB1                  stimulation\nTGFB1                  CXCL8                  stimulation\nTGFB1                  RB1                    stimulation\nRB1                    TGFB1                  stimulation\nTGFB1                  SUCLA2                 stimulation\nTGFB1                  MAPK1                  stimulation\nIL2                    TGFB1                  inhibition\nNFKB1                  TGFB1                  stimulation\nTGFB1                  EPHB2                  stimulation\nEPHB2                  TGFB1                  stimulation\nTGFB1                  MAPK14                 stimulation\nMAPK14                 TGFB1                  inhibition\nTGFB1                  TRAF6                  stimulation\nTGFB1                  EGFR                   stimulation\nTGFB1                  AR                     stimulation\nTGFB1                  EDN1                   stimulation\nEDN1                   TGFB1                  stimulation\nTGFB1                  PAK2                   stimulation\nDAXX                   TGFB1                  inhibition\nIRS1                   TGFB1                  inhibition\nTGFB1                  TERT                   inhibition\nTGFB1                  RPS6KB1                inhibition\nRPS6KB1                TGFB1                  stimulation\nHIF1A                  TGFB1                  stimulation\nEGR1                   TGFB1                  stimulation\nTGFB1                  BMP2                   inhibition\nTGFB1                  SHC1                   stimulation\nTGFB1                  SMAD4                  stimulation\nSMAD4                  TGFB1                  inhibition\nTGFB1                  VDR                    stimulation\nTGFB1                  CDC42                  stimulation\nTGFB1                  VEGFA                  stimulation\nHSPB1                  TGFB1                  inhibition\nEIF4E                  TGFB1                  stimulation\nIFNG                   CXCL8                  inhibition\nMAPK1                  IFNG                   stimulation\nIFNG                   FASLG                  stimulation\nIFNG                   MAP3K5                 stimulation\nIL2                    IFNG                   stimulation\nNFKB1                  IFNG                   stimulation\nIFNG                   STAT1                  stimulation\nMAPK9                  IFNG                   inhibition\nIFNG                   S100B                  stimulation\nIFNG                   HSP90AA1               inhibition\nIFNG                   MAP3K1                 stimulation\nIFNG                   CBL                    stimulation\nIFNG                   TERT                   inhibition\nIFNG                   IL6                    stimulation\nIFNG                   CD40LG                 stimulation\nIL12B                  IFNG                   stimulation\nIFNG                   IL1B                   stimulation\nIFNG                   SMAD7                  stimulation\nNOTCH1                 IFNG                   stimulation\nPPP3CA                 IFNG                   inhibition\nFASLG                  CXCL8                  stimulation\nRAC1                   CXCL8                  stimulation\nNFKB1                  CXCL8                  stimulation\nMAP2K1                 CXCL8                  stimulation\nPPP2CA                 CXCL8                  stimulation\nMAPK14                 CXCL8                  inhibition\nCXCL8                  EGFR                   stimulation\nEGFR                   CXCL8                  stimulation\nEDN1                   CXCL8                  stimulation\nCTNNB1                 CXCL8                  stimulation\nCSF2                   CXCL8                  stimulation\nHIF1A                  CXCL8                  inhibition\nCD40LG                 CXCL8                  stimulation\nCOMPLEX:P19838_Q04206  CXCL8                  stimulation\nIL1B                   CXCL8                  stimulation\nEGR1                   CXCL8                  inhibition\nBCL2L1                 CXCL8                  stimulation\nVEGFA                  CXCL8                  stimulation\nRB1                    CASP7                  inhibition\nRB1                    MAP3K5                 inhibition\nPPP2CA                 RB1                    stimulation\nRB1                    E2F2                   inhibition\nRB1                    SP1                    stimulation\nRB1                    HIF1A                  stimulation\nRB1                    TFDP1                  stimulation\nSIRT1                  RB1                    stimulation\nSMAD7                  RB1                    inhibition\nVEGFA                  RB1                    inhibition\nRB1                    E2F3                   inhibition\nCDK6                   OTUD7B                 stimulation\nTP73                   CDK6                   stimulation\nCREB1                  CDK6                   stimulation\nCDK6                   E2F2                   inhibition\nCDK6                   TFDP1                  inhibition\nCDK6                   BMP2                   inhibition\nCCND3                  CDK6                   stimulation\nCDK6                   E2F3                   inhibition\nSUCLA2                 MAPK1                  stimulation\nSUCLA2                 NFKB1                  stimulation\nSUCLA2                 PARP1                  stimulation\nSUCLA2                 CTNNB1                 inhibition\nSUCLA2                 IL6                    stimulation\nCD40LG                 SUCLA2                 stimulation\nACHE                   SUCLA2                 stimulation\nMAPK1                  MAP3K5                 stimulation\nIL2                    MAPK1                  stimulation\nRAC1                   MAPK1                  stimulation\nMAPK1                  NFKB1                  stimulation\nMAP2K7                 MAPK1                  stimulation\nMAP2K1                 MAPK1                  stimulation\nMAPK1                  STAT1                  stimulation\nPPP2CA                 MAPK1                  inhibition\nMAPK1                  OTUD7B                 stimulation\nMAPK1                  PARP1                  stimulation\nMAP2K4                 MAPK1                  stimulation\nPRKCZ                  MAPK1                  stimulation\nMAP3K1                 MAPK1                  stimulation\nEDN1                   MAPK1                  stimulation\nMAPK1                  BAD                    inhibition\nMAPK1                  IRS1                   inhibition\nMAPK1                  CREB1                  stimulation\nMAPK1                  TERT                   stimulation\nMAPK1                  SP1                    stimulation\nMAPK1                  RPS6KB1                stimulation\nCSF2                   MAPK1                  stimulation\nMAPK1                  HIF1A                  stimulation\nMAPK1                  BCL2L11                inhibition\nMAPK1                  RIPK2                  inhibition\nMAPK1                  ELK1                   stimulation\nMAPK1                  FOXO3                  inhibition\nMAPK1                  COMPLEX:P19838_Q04206  stimulation\nMAPK1                  RPS6KA2                stimulation\nIL1B                   MAPK1                  stimulation\nMAPK1                  TSC22D3                stimulation\nMAPK1                  EGR1                   stimulation\nGNAI1                  MAPK1                  stimulation\nBMP2                   MAPK1                  stimulation\nSHC1                   MAPK1                  stimulation\nMAPK1                  ROCK1                  inhibition\nMAPK1                  RARA                   stimulation\nMAPK1                  BCL2L1                 stimulation\nMAPK1                  CDK1                   inhibition\nMAPK1                  MRTFA                  inhibition\nMAPK1                  FGR                    stimulation\nFGR                    MAPK1                  stimulation\nCDC42                  MAPK1                  stimulation\nVEGFA                  MAPK1                  stimulation\nMAPK1                  FGFR2                  inhibition\nMAPK1                  HSPB1                  stimulation\nMAPK1                  TSC2                   inhibition\nMAPK1                  PPP2R5C                inhibition\nFASLG                  CASP7                  stimulation\nFASLG                  BID                    stimulation\nFASLG                  CHUK                   stimulation\nFASLG                  TNFRSF10B              stimulation\nNFKB1                  FASLG                  stimulation\nFASLG                  MAP2K7                 stimulation\nSTAT1                  FASLG                  stimulation\nFASLG                  EGFR                   stimulation\nFASLG                  MAP2K4                 stimulation\nFASLG                  IKBKG                  stimulation\nRIPK2                  FASLG                  inhibition\nIL12B                  FASLG                  stimulation\nSIRT1                  FASLG                  inhibition\nEGR1                   FASLG                  stimulation\nHSPB1                  FASLG                  inhibition\nCASP2                  CASP7                  stimulation\nCASP7                  PARP1                  inhibition\nCASP7                  MAP3K1                 stimulation\nCASP7                  AR                     inhibition\nCASP7                  EIF4G2                 stimulation\nPAK2                   CASP7                  inhibition\nCASP7                  PSEN1                  stimulation\nCASP10                 CASP7                  stimulation\nE2F2                   CASP7                  inhibition\nCYCS                   CASP7                  stimulation\nTFDP1                  CASP7                  inhibition\nBIRC5                  CASP7                  inhibition\nNAIP                   CASP7                  inhibition\nCASP7                  LYN                    inhibition\nCASP7                  PTK2                   stimulation\nCASP7                  LAMB2                  stimulation\nCASP7                  EIF4E                  stimulation\nE2F3                   CASP7                  inhibition\nMAP3K5                 BID                    stimulation\nCASP2                  BID                    stimulation\nDAXX                   BID                    stimulation\nCASP10                 BID                    stimulation\nATM                    BID                    stimulation\nBID                    DIABLO                 stimulation\nBID                    CYCS                   stimulation\nHIF1A                  BID                    inhibition\nBID                    COX5B                  stimulation\nBID                    BCL2L1                 inhibition\nTNFRSF1B               MAP3K1                 stimulation\nMAP3K5                 CHUK                   stimulation\nMAP3K5                 MAP2K7                 stimulation\nMAP3K5                 MAPK9                  stimulation\nS100B                  MAP3K5                 inhibition\nMAP3K5                 MAPK14                 stimulation\nTRAF6                  MAP3K5                 stimulation\nMAP3K5                 MAP2K4                 stimulation\nDAXX                   MAP3K5                 stimulation\nAKT3                   MAP3K5                 inhibition\nAKT2                   MAP3K5                 inhibition\nMAP3K5                 IKBKG                  stimulation\nNFKB1                  IL2                    stimulation\nIL2                    MAP2K1                 stimulation\nIL2                    STAT1                  stimulation\nIL2                    MAPK14                 stimulation\nIL2                    HSP90AA1               stimulation\nIL2                    PRKCZ                  stimulation\nIL2                    CBL                    stimulation\nIL2                    IRS1                   stimulation\nIL2                    IL5                    stimulation\nIL5                    IL2                    stimulation\nCREB1                  IL2                    stimulation\nIL2                    TERT                   stimulation\nIL2                    RPS6KB1                stimulation\nIL2                    CSF2                   stimulation\nCSF2                   IL2                    inhibition\nIL2                    IL6                    stimulation\nIL6                    IL2                    stimulation\nIKBKG                  IL2                    stimulation\nCD40LG                 IL2                    inhibition\nIL2                    IL1B                   stimulation\nIL1B                   IL2                    stimulation\nIL2                    SHC1                   stimulation\nIL2                    CCND3                  stimulation\nIL2                    BCL2L1                 stimulation\nIL2                    SOS1                   stimulation\nNFKB1                  TNFAIP3                stimulation\nTNFAIP3                TRAF6                  inhibition\nTNFAIP3                TICAM1                 inhibition\nTNFAIP3                IKBKG                  inhibition\nRAC1                   NFKB1                  stimulation\nRAC1                   MAP2K7                 stimulation\nRAC1                   MAP2K1                 stimulation\nRAC1                   MAPK9                  stimulation\nEPHB2                  RAC1                   stimulation\nRAC1                   MAPK14                 stimulation\nEGFR                   RAC1                   stimulation\nRAC1                   MAP2K4                 stimulation\nRAC1                   MAP3K1                 stimulation\nEDN1                   RAC1                   stimulation\nRAC1                   PAK2                   stimulation\nRAC1                   HIF1A                  stimulation\nNGFR                   RAC1                   stimulation\nGNAI1                  RAC1                   stimulation\nRAC1                   PRKCD                  stimulation\nSHC1                   RAC1                   stimulation\nPTK2B                  RAC1                   stimulation\nRAC1                   ROCK1                  stimulation\nLYN                    RAC1                   stimulation\nRAC1                   VEGFA                  stimulation\nVEGFA                  RAC1                   stimulation\nGNG2                   RAC1                   stimulation\nPTK2                   RAC1                   stimulation\nLAMB2                  RAC1                   stimulation\nSOS1                   RAC1                   stimulation\nTNFRSF10B              CHUK                   stimulation\nFLNA                   CHUK                   stimulation\nSQSTM1                 CHUK                   stimulation\nTRAF6                  CHUK                   stimulation\nPRKCZ                  CHUK                   stimulation\nMAP3K1                 CHUK                   stimulation\nCHUK                   IRS1                   inhibition\nTP63                   CHUK                   stimulation\nAKT3                   CHUK                   stimulation\nAKT2                   CHUK                   stimulation\nIKBKG                  CHUK                   stimulation\nRIPK2                  CHUK                   stimulation\nIRAK1                  CHUK                   stimulation\nNGFR                   CHUK                   stimulation\nCHUK                   FOXO3                  inhibition\nCHUK                   COMPLEX:P19838_Q04206  inhibition\nNOTCH1                 CHUK                   stimulation\nCHUK                   IRS4                   inhibition\nCHUK                   TSC2                   inhibition\nNFKB1                  TRAF5                  stimulation\nNFKB2                  TRAF5                  stimulation\nNFKB1                  TNFRSF10B              stimulation\nTNFRSF10B              MAP3K1                 stimulation\nTNFRSF10B              CASP10                 stimulation\nTNFRSF10B              IKBKG                  stimulation\nNOTCH1                 TNFRSF10B              stimulation\nMAPK14                 NFKB1                  stimulation\nSQSTM1                 NFKB1                  stimulation\nNFKB1                  TRAF6                  stimulation\nTRAF6                  NFKB1                  stimulation\nTICAM1                 NFKB1                  stimulation\nEGFR                   NFKB1                  stimulation\nPARP1                  NFKB1                  stimulation\nPRKCZ                  NFKB1                  stimulation\nMAP3K1                 NFKB1                  stimulation\nEDN1                   NFKB1                  stimulation\nNFKB1                  ALPI                   inhibition\nCASP10                 NFKB1                  stimulation\nATM                    NFKB1                  stimulation\nBAG1                   NFKB1                  inhibition\nPRNP                   NFKB1                  stimulation\nNFKB1                  CSF2                   inhibition\nCSF2                   NFKB1                  stimulation\nNFKB1                  IL6                    stimulation\nNFKB1                  BIRC5                  stimulation\nNFKB1                  IKBKG                  stimulation\nIKBKG                  NFKB1                  stimulation\nRIPK2                  NFKB1                  stimulation\nIRAK1                  NFKB1                  stimulation\nNGFR                   NFKB1                  stimulation\nCDKN2A                 NFKB1                  inhibition\nNFKB1                  IL12B                  stimulation\nIL12B                  NFKB1                  stimulation\nCUL1                   NFKB1                  inhibition\nNFKB1                  IL1B                   stimulation\nTSC22D3                NFKB1                  inhibition\nPRKCD                  NFKB1                  stimulation\nLYN                    NFKB1                  stimulation\nNFKB1                  BCL2L1                 stimulation\nNFKB1                  VEGFA                  stimulation\nHSPB1                  NFKB1                  inhibition\nCDKN2A                 NFKB1                  inhibition\nAR                     KRT18                  stimulation\nCDK1                   KRT18                  stimulation\nCASP2                  MAP2K7                 stimulation\nMAP2K7                 MAPK9                  stimulation\nFLNA                   MAP2K7                 stimulation\nMAP2K7                 MAPK14                 stimulation\nMAP2K7                 MAP2K4                 stimulation\nMAP3K1                 MAP2K7                 stimulation\nDAXX                   MAP2K7                 stimulation\nMAP2K7                 IRS1                   inhibition\nMAP2K7                 UBB                    stimulation\nRIPK2                  MAP2K7                 stimulation\nSH3RF1                 MAP2K7                 stimulation\nCDC42                  MAP2K7                 stimulation\nMAP2K1                 MAPK9                  stimulation\nPPP2CA                 MAP2K1                 inhibition\nMAPK14                 MAP2K1                 stimulation\nEGFR                   MAP2K1                 stimulation\nMAP2K1                 MAP2K4                 stimulation\nMAP3K1                 MAP2K1                 stimulation\nPAK2                   MAP2K1                 stimulation\nMAP2K1                 BAD                    inhibition\nMAP2K1                 IRS1                   inhibition\nMAP2K1                 CREB1                  stimulation\nMAP2K1                 RPS6KB1                stimulation\nCSF2                   MAP2K1                 stimulation\nMAP2K1                 BCL2L11                inhibition\nMAP2K1                 ELK1                   stimulation\nMAP2K1                 RPS6KA2                stimulation\nPRKCD                  MAP2K1                 stimulation\nSHC1                   MAP2K1                 stimulation\nCDK1                   MAP2K1                 inhibition\nMAP2K1                 SOS1                   inhibition\nS100B                  CASP2                  inhibition\nAR                     CASP2                  inhibition\nTP73                   CASP2                  stimulation\nCASP2                  EIF4G2                 stimulation\nCASP2                  DIABLO                 stimulation\nCASP2                  CYCS                   stimulation\nCCND3                  CASP2                  stimulation\nCASP2                  EIF4E                  stimulation\nMAPK9                  STAT1                  stimulation\nEPHB2                  STAT1                  stimulation\nMAPK14                 STAT1                  stimulation\nEGFR                   STAT1                  stimulation\nAR                     STAT1                  stimulation\nSTAT1                  HIF1A                  inhibition\nIL6                    STAT1                  stimulation\nSTAT1                  COMPLEX:P19838_Q04206  inhibition\nIL12B                  STAT1                  stimulation\nSTAT1                  SMAD7                  stimulation\nPRKCD                  STAT1                  stimulation\nLYN                    STAT1                  stimulation\nSTAT1                  CCND3                  stimulation\nSTAT1                  BCL2L1                 stimulation\nSTAT1                  VEGFA                  stimulation\nFGFR2                  STAT1                  stimulation\nPTK2                   STAT1                  stimulation\nMAPK14                 MAPK9                  stimulation\nTRAF6                  MAPK9                  stimulation\nMAP2K4                 MAPK9                  stimulation\nPRKCZ                  MAPK9                  stimulation\nMAPK9                  PSEN1                  stimulation\nMAPK9                  BAD                    stimulation\nMAPK9                  IRS1                   inhibition\nMAPK9                  CTNNB1                 stimulation\nMAPK9                  SP1                    stimulation\nMAPK9                  ELK1                   stimulation\nCD40LG                 MAPK9                  stimulation\nNGFR                   MAPK9                  stimulation\nMAPK9                  COMPLEX:P19838_Q04206  stimulation\nMAPK9                  RPS6KA2                stimulation\nMAPK9                  SHC1                   stimulation\nMAPK9                  SMAD4                  stimulation\nMAPK9                  PTK2B                  stimulation\nDUSP4                  MAPK9                  inhibition\nCDC42                  MAPK9                  stimulation\nMAPK9                  IRS4                   inhibition\nMAPK9                  XPO1                   stimulation\nPPP2CA                 EPHB2                  inhibition\nMAPK14                 EPHB2                  stimulation\nEPHB2                  ELK1                   stimulation\nEPHB2                  LYN                    stimulation\nLYN                    EPHB2                  stimulation\nEPHB2                  FGR                    stimulation\nFGR                    EPHB2                  stimulation\nEPHB2                  CDC42                  stimulation\nEPHB2                  PTK2                   inhibition\nFLNA                   MAP2K4                 stimulation\nFLNA                   IKBKG                  stimulation\nPRKCD                  FLNA                   stimulation\nPPP3CA                 FLNA                   inhibition\nFLNA                   CDC42                  inhibition\nPPP2CA                 EGFR                   stimulation\nPPP2CA                 PRKCZ                  inhibition\nPPP2CA                 ATM                    inhibition\nPPP2CA                 CTNNB1                 stimulation\nPPP2CA                 SP1                    stimulation\nPPP2CA                 AKT3                   inhibition\nPPP2CA                 AKT2                   inhibition\nPPP2CA                 FOXO3                  stimulation\nPPP2CA                 COMPLEX:P19838_Q04206  inhibition\nPPP2CA                 PRKCD                  inhibition\nCDK3                   PPP2CA                 stimulation\nPPP2CA                 EIF4E                  inhibition\nPPP2R5C                PPP2CA                 stimulation\nNFKB2                  TRAF6                  stimulation\nCUL1                   NFKB2                  stimulation\nTSC22D3                NFKB2                  inhibition\nNFKB2                  BCL2L1                 stimulation\nS100B                  DAXX                   inhibition\nTRAF6                  MAPK14                 stimulation\nMAPK14                 EGFR                   inhibition\nMAP2K4                 MAPK14                 stimulation\nMAP3K1                 MAPK14                 stimulation\nMAPK14                 AR                     stimulation\nMAPK14                 TP73                   stimulation\nEDN1                   MAPK14                 stimulation\nPAK2                   MAPK14                 stimulation\nMAPK14                 DDB2                   inhibition\nMAPK14                 SP1                    stimulation\nMAPK14                 BCL2L11                inhibition\nRIPK2                  MAPK14                 stimulation\nMAPK14                 ELK1                   stimulation\nCD40LG                 MAPK14                 stimulation\nMAPK14                 FOXO3                  stimulation\nMAPK14                 NFE2L2                 inhibition\nMAPK14                 IL1B                   inhibition\nZAP70                  MAPK14                 stimulation\nGNAI1                  MAPK14                 stimulation\nBMP2                   MAPK14                 stimulation\nPTK2B                  MAPK14                 stimulation\nDUSP4                  MAPK14                 inhibition\nLYN                    MAPK14                 stimulation\nMAPK14                 RARA                   stimulation\nMAPK14                 MEF2D                  stimulation\nCDC42                  MAPK14                 stimulation\nGNG2                   MAPK14                 stimulation\nMAPK14                 TP53BP1                inhibition\nMAPK14                 HSPB1                  stimulation\nMAPK14                 EIF4E                  stimulation\nMAPK14                 TSC2                   stimulation\nMAPK14                 TRIM24                 stimulation\nSQSTM1                 TRAF6                  stimulation\nSQSTM1                 IKBKG                  stimulation\nSQSTM1                 IRAK1                  stimulation\nCDK1                   SQSTM1                 stimulation\nIRAK1                  OTUD7B                 stimulation\nTICAM1                 TRAF6                  stimulation\nTRAF6                  EGFR                   inhibition\nTRAF6                  MAP3K1                 stimulation\nPSEN1                  TRAF6                  inhibition\nATM                    TRAF6                  stimulation\nTRAF6                  AKT3                   stimulation\nTRAF6                  IKBKG                  inhibition\nIRAK1                  TRAF6                  stimulation\nIL1B                   TRAF6                  stimulation\nTRAF6                  FGFR2                  inhibition\nHSPB1                  TRAF6                  stimulation\nEGFR                   MAP3K1                 stimulation\nAR                     EGFR                   stimulation\nEDN1                   EGFR                   stimulation\nEGFR                   CASP10                 stimulation\nEGFR                   TERT                   stimulation\nEGFR                   CSF2                   stimulation\nEGR1                   EGFR                   stimulation\nPRKCD                  EGFR                   inhibition\nEGFR                   SHC1                   stimulation\nPTK2B                  EGFR                   stimulation\nLYN                    EGFR                   stimulation\nRARA                   EGFR                   stimulation\nNOTCH1                 EGFR                   stimulation\nCDK1                   EGFR                   inhibition\nFGR                    EGFR                   stimulation\nCDC42                  EGFR                   inhibition\nVEGFA                  EGFR                   stimulation\nEGFR                   PTK2                   stimulation\nEGFR                   LAMB2                  stimulation\nEGFR                   SOS1                   stimulation\nPARP1                  HIF1A                  stimulation\nILK                    PARP1                  stimulation\nHSP90AA1               AR                     stimulation\nHSP90AA1               UBB                    inhibition\nZAP70                  HSP90AA1               stimulation\nHSP90AA1               PTK2                   stimulation\nDAXX                   MAP2K4                 stimulation\nCASP10                 MAP2K4                 stimulation\nAKT3                   MAP2K4                 inhibition\nAKT2                   MAP2K4                 inhibition\nCD40LG                 MAP2K4                 stimulation\nMAP2K4                 PRKCD                  stimulation\nSH3RF1                 MAP2K4                 stimulation\nROCK1                  MAP2K4                 stimulation\nPRKCZ                  PSEN1                  stimulation\nPRKCZ                  CBL                    stimulation\nPRKCZ                  DAXX                   stimulation\nPRKCZ                  SP1                    stimulation\nPRKCZ                  RPS6KB1                stimulation\nPRKCZ                  UBB                    stimulation\nPRKCZ                  AKT2                   stimulation\nPRKCZ                  IKBKG                  stimulation\nPRKCZ                  ELK1                   stimulation\nPRKCZ                  COMPLEX:P19838_Q04206  stimulation\nPRKCZ                  RPS6KA2                stimulation\nSHC1                   PRKCZ                  stimulation\nROCK1                  PRKCZ                  stimulation\nPRKCZ                  FGR                    stimulation\nCDC42                  PRKCZ                  stimulation\nPRKCZ                  GSN                    stimulation\nMAP3K1                 AR                     stimulation\nPAK2                   MAP3K1                 stimulation\nMAP3K1                 CREB1                  stimulation\nMAP3K1                 SP1                    stimulation\nMAP3K1                 IKBKG                  stimulation\nCD40LG                 MAP3K1                 stimulation\nIRAK1                  MAP3K1                 stimulation\nLAT                    MAP3K1                 stimulation\nCDC42                  MAP3K1                 stimulation\nEDN1                   AR                     stimulation\nDAXX                   AR                     inhibition\nAR                     TERT                   inhibition\nAR                     FOXO3                  inhibition\nSIRT1                  AR                     stimulation\nEGR1                   AR                     inhibition\nAR                     GNAI1                  stimulation\nSMAD4                  AR                     stimulation\nCDK1                   AR                     stimulation\nAR                     CDC42                  stimulation\nAR                     GNG2                   stimulation\nTRIM24                 AR                     stimulation\nGSN                    AR                     stimulation\nTP73                   TP63                   stimulation\nTFDP1                  TP73                   stimulation\nTP73                   BCL2L11                stimulation\nTP73                   FOXO3                  stimulation\nSIRT1                  TP73                   inhibition\nPRKCD                  TP73                   stimulation\nCDK1                   TP73                   inhibition\nCASP10                 EIF4G2                 stimulation\nCDK1                   EIF4G2                 stimulation\nEIF4G2                 EIF4E                  inhibition\nCREB1                  EDN1                   stimulation\nEDN1                   CSF2                   stimulation\nHIF1A                  EDN1                   stimulation\nEDN1                   IL6                    stimulation\nEDN1                   PTK2B                  stimulation\nEDN1                   ILK                    stimulation\nEDN1                   CDC42                  stimulation\nVEGFA                  EDN1                   inhibition\nCDC42                  PAK2                   stimulation\nPSEN1                  UBB                    stimulation\nELK1                   PSEN1                  inhibition\nPSEN1                  NGFR                   stimulation\nPSEN1                  NOTCH1                 stimulation\nCASP10                 ALPI                   stimulation\nDIABLO                 ALPI                   inhibition\nIRS1                   CBL                    stimulation\nCBL                    UBB                    stimulation\nCBL                    ZAP70                  inhibition\nPRKCD                  CBL                    stimulation\nPTK2B                  CBL                    stimulation\nFGR                    CBL                    stimulation\nCBL                    FGFR2                  inhibition\nATM                    DAXX                   inhibition\nRIPK2                  DAXX                   inhibition\nDAXX                   SMAD4                  inhibition\nHSPB1                  DAXX                   inhibition\nCASP10                 CYCS                   stimulation\nRIPK2                  CASP10                 inhibition\nCASP10                 EIF4E                  stimulation\nRPS6KB1                BAD                    inhibition\nBAD                    CYCS                   stimulation\nPPP3CA                 BAD                    stimulation\nCDK1                   BAD                    stimulation\nPPP2R5C                BAD                    stimulation\nIRS1                   ATM                    stimulation\nIKBKG                  IRS1                   inhibition\nIRS1                   SHC1                   stimulation\nIRS1                   IRS4                   stimulation\nATM                    CREB1                  inhibition\nATM                    TP63                   inhibition\nATM                    SP1                    stimulation\nATM                    HIF1A                  stimulation\nATM                    TFDP1                  stimulation\nFOXO3                  ATM                    stimulation\nCDKN2A                 ATM                    stimulation\nRPS6KA2                ATM                    stimulation\nATM                    TP53BP1                stimulation\nE2F3                   ATM                    stimulation\nCDKN2A                 ATM                    stimulation\nATM                    PPP2R5C                stimulation\nIL5                    IL1B                   stimulation\nSMAD4                  IL5                    stimulation\nSIRT1                  APEX1                  stimulation\nAPEX1                  EGR1                   stimulation\nCREB1                  CTNNB1                 stimulation\nCTNNB1                 UBB                    stimulation\nAKT3                   CTNNB1                 stimulation\nAKT2                   CTNNB1                 stimulation\nCTNNB1                 FOXO3                  stimulation\nCTNNB1                 CDKN2A                 inhibition\nSIRT1                  CTNNB1                 stimulation\nCUL1                   CTNNB1                 inhibition\nCTNNB1                 SMAD7                  stimulation\nPRKCD                  CTNNB1                 inhibition\nROCK1                  CTNNB1                 stimulation\nILK                    CTNNB1                 stimulation\nCTNNB1                 NOTCH1                 stimulation\nVDR                    CTNNB1                 stimulation\nCDK1                   CTNNB1                 stimulation\nCTNNB1                 CDC42                  inhibition\nCDC42                  CTNNB1                 inhibition\nCTNNB1                 CDKN2A                 inhibition\nAKT3                   CREB1                  stimulation\nAKT2                   CREB1                  stimulation\nCREB1                  IL6                    stimulation\nRPS6KA2                CREB1                  stimulation\nSHC1                   CREB1                  stimulation\nSMAD4                  CREB1                  stimulation\nILK                    CREB1                  stimulation\nPPP3CA                 CREB1                  inhibition\nCREB1                  VEGFA                  stimulation\nSOS1                   CREB1                  stimulation\nPPP2R5C                CREB1                  inhibition\nSP1                    TERT                   inhibition\nHIF1A                  TERT                   stimulation\nE2F2                   TFDP1                  stimulation\nE2F2                   BIRC5                  stimulation\nE2F2                   CDKN2A                 stimulation\nE2F2                   CCND3                  stimulation\nE2F2                   CDK1                   stimulation\nE2F2                   CDKN2A                 stimulation\nBAG1                   BCL2L11                stimulation\nSP1                    PRNP                   stimulation\nPTK2                   PRNP                   stimulation\nLAMB2                  PRNP                   stimulation\nCYCS                   DIABLO                 stimulation\nRPS6KB1                TP63                   inhibition\nTP63                   CDKN2A                 inhibition\nTP63                   PRKCD                  stimulation\nTP63                   NOTCH1                 inhibition\nTP63                   VDR                    inhibition\nTP63                   CDKN2A                 inhibition\nSP1                    BIRC5                  stimulation\nCOMPLEX:P19838_Q04206  SP1                    stimulation\nSP1                    LAT                    stimulation\nSP1                    SMAD7                  stimulation\nCDK1                   SP1                    stimulation\nSP1                    VEGFA                  stimulation\nCOMPLEX:P20248_P24941  SP1                    stimulation\nHSPB1                  SP1                    stimulation\nRPS6KB1                UBB                    stimulation\nAKT3                   RPS6KB1                stimulation\nRPS6KB1                SHC1                   stimulation\nCDK1                   RPS6KB1                stimulation\nRPS6KB1                FGR                    stimulation\nCDC42                  RPS6KB1                stimulation\nRPS6KB1                PTK2                   stimulation\nRHEB                   RPS6KB1                stimulation\nRPS6KB1                HSPB1                  inhibition\nPPP2R5C                RPS6KB1                inhibition\nCUL1                   UBB                    stimulation\nPTK2B                  UBB                    stimulation\nHTRA2                  CYCS                   inhibition\nBCL2L1                 CYCS                   inhibition\nHSPB1                  CYCS                   inhibition\nGSN                    CYCS                   inhibition\nCD40LG                 CSF2                   stimulation\nCSF2                   IL1B                   stimulation\nIL1B                   CSF2                   stimulation\nCSF2                   SMAD7                  inhibition\nNOTCH1                 HIF1A                  stimulation\nHIF1A                  VEGFA                  stimulation\nTFDP1                  CDKN2A                 inhibition\nCDKN2A                 TFDP1                  inhibition\nTFDP1                  SIRT1                  stimulation\nSMAD4                  TFDP1                  stimulation\nCCND3                  TFDP1                  inhibition\nTFDP1                  CDK1                   stimulation\nTFDP1                  DDAH2                  stimulation\nE2F3                   TFDP1                  stimulation\nTFDP1                  CDKN2A                 inhibition\nCDKN2A                 TFDP1                  inhibition\nCCNE1                  TFDP1                  stimulation\nSIRT1                  BCL2L11                inhibition\nBCL2L11                BCL2L1                 inhibition\nCDK1                   BCL2L11                stimulation\nBCL2L1                 COX5B                  inhibition\nACHE                   COX5B                  stimulation\nHSPB1                  COX5B                  inhibition\nAKT3                   BIRC5                  stimulation\nAKT3                   IKBKG                  stimulation\nAKT3                   FOXO3                  inhibition\nAKT3                   COMPLEX:P19838_Q04206  stimulation\nGNAI1                  AKT3                   stimulation\nPTK2B                  AKT3                   stimulation\nILK                    AKT3                   stimulation\nAKT3                   BCL2L1                 stimulation\nVEGFA                  AKT3                   stimulation\nAKT3                   HSPB1                  inhibition\nAKT3                   TSC2                   inhibition\nAKT2                   BIRC5                  stimulation\nAKT2                   IKBKG                  stimulation\nAKT2                   HTRA2                  inhibition\nAKT2                   FOXO3                  inhibition\nAKT2                   COMPLEX:P19838_Q04206  stimulation\nAKT2                   SH3RF1                 inhibition\nILK                    AKT2                   stimulation\nAKT2                   BCL2L1                 stimulation\nAKT2                   HSPB1                  inhibition\nAKT2                   TSC2                   inhibition\nCOMPLEX:P19838_Q04206  IL6                    stimulation\nIL12B                  IL6                    stimulation\nIL6                    IL1B                   stimulation\nIL1B                   IL6                    stimulation\nIL6                    SHC1                   stimulation\nIL6                    VEGFA                  stimulation\nVEGFA                  IL6                    stimulation\nPTK2                   IL6                    stimulation\nIL6                    SOS1                   stimulation\nCDKN2A                 BIRC5                  inhibition\nCDK1                   BIRC5                  stimulation\nE2F3                   BIRC5                  stimulation\nCDKN2A                 BIRC5                  inhibition\nRIPK2                  IKBKG                  stimulation\nIRAK1                  IKBKG                  stimulation\nNGFR                   IKBKG                  stimulation\nIKBKG                  COMPLEX:P19838_Q04206  stimulation\nIKBKG                  IRS4                   inhibition\nRIPK2                  PRKCD                  stimulation\nELK1                   EGR1                   stimulation\nSHC1                   ELK1                   stimulation\nELK1                   CCND3                  stimulation\nSOS1                   ELK1                   stimulation\nCD40LG                 VEGFA                  stimulation\nNGFR                   IRAK1                  stimulation\nNGFR                   SHC1                   stimulation\nNGFR                   SOS1                   stimulation\nTSC22D3                FOXO3                  inhibition\nSHC1                   FOXO3                  inhibition\nPTK2B                  FOXO3                  stimulation\nCDKN2A                 CCND3                  inhibition\nCDKN2A                 VDR                    inhibition\nCDKN2A                 BCL2L1                 inhibition\nSIRT1                  NFE2L2                 inhibition\nPRKCD                  NFE2L2                 stimulation\nCOMPLEX:P19838_Q04206  IL12B                  stimulation\nCOMPLEX:P19838_Q04206  IL1B                   stimulation\nTSC22D3                COMPLEX:P19838_Q04206  inhibition\nCOMPLEX:P19838_Q04206  EGR1                   stimulation\nCOMPLEX:P19838_Q04206  VEGFA                  stimulation\nIL12B                  IL1B                   stimulation\nIL1B                   IL12B                  stimulation\nRPS6KA2                SMAD4                  stimulation\nRPS6KA2                TSC2                   inhibition\nRPS6KA2                XPO1                   stimulation\nSIRT1                  NOTCH1                 inhibition\nCDK1                   SIRT1                  stimulation\nHSPB1                  CUL1                   stimulation\nCUL1                   CCNE1                  stimulation\nIL1B                   EGR1                   stimulation\nIL1B                   VEGFA                  stimulation\nEGR1                   DUSP4                  stimulation\nZAP70                  LAT                    stimulation\nLAT                    SHC1                   stimulation\nLYN                    LAT                    stimulation\nLAT                    CDC42                  stimulation\nLAT                    SOS1                   stimulation\nSMAD7                  BMP2                   inhibition\nSMAD4                  SMAD7                  stimulation\nZAP70                  SHC1                   stimulation\nZAP70                  FGR                    stimulation\nFGR                    ZAP70                  stimulation\nGNAI1                  SHC1                   stimulation\nGNAI1                  PTK2B                  stimulation\nGNAI1                  FGR                    stimulation\nGNAI1                  CDC42                  stimulation\nGNAI1                  PTK2                   inhibition\nGNAI1                  SOS1                   stimulation\nPRKCD                  SHC1                   stimulation\nPRKCD                  PTK2B                  stimulation\nPTK2B                  SHC1                   stimulation\nLYN                    SHC1                   stimulation\nSHC1                   ILK                    stimulation\nSHC1                   CCND3                  stimulation\nFGR                    SHC1                   stimulation\nVEGFA                  SHC1                   stimulation\nFGFR2                  SHC1                   stimulation\nPTK2                   SHC1                   stimulation\nSHC1                   SOS1                   stimulation\nFGFR2                  SMAD4                  stimulation\nPTK2                   SMAD4                  stimulation\nEIF4E                  SMAD4                  stimulation\nLYN                    PTK2B                  stimulation\nPTK2B                  ARHGDIB                stimulation\nFGR                    PTK2B                  stimulation\nVEGFA                  PTK2B                  stimulation\nPTK2B                  PTK2                   stimulation\nPTK2B                  SOS1                   stimulation\nPTK2B                  GSN                    stimulation\nROCK1                  PTK2                   stimulation\nGNG2                   LYN                    stimulation\nLYN                    PTK2                   stimulation\nLYN                    SOS1                   stimulation\nSOS1                   ILK                    stimulation\nPPP3CA                 MEF2D                  stimulation\nSOS1                   CCND3                  stimulation\nE2F3                   CCND3                  stimulation\nCDKN2A                 CCND3                  inhibition\nCCND3                  CCNE1                  stimulation\nCDKN2A                 VDR                    inhibition\nCDK1                   BCL2L1                 inhibition\nCDKN2A                 BCL2L1                 inhibition\nCDK1                   TP53BP1                inhibition\nE2F3                   CDK1                   stimulation\nGNG2                   FGR                    stimulation\nFGR                    PTK2                   stimulation\nFGR                    TRIM24                 stimulation\nVEGFA                  CDC42                  stimulation\nGNG2                   CDC42                  stimulation\nPTK2                   CDC42                  stimulation\nLAMB2                  CDC42                  stimulation\nVEGFA                  PTK2                   stimulation\nVEGFA                  SOS1                   stimulation\nGNG2                   PTK2                   stimulation\nSOS1                   PTK2                   stimulation\nRHEB                   EIF4E                  stimulation\nCCNE1                  DDAH2                  stimulation"
}

**Tool Output:**

Network_1.bnet

**Tool Output:**

Error executing tool bnet_to_bnd_and_cfg: node CDKN2A already defined

**Tool Output:**

Removed 0 undefined interactions from the network.

**Tool Output:**

{
  "result": "Removed 0 undefined interactions from the network."
}

**Tool Output:**

**Exported to** `Network_1.bnet`

_Preview (first 100 lines) of the BNET file:_

gene       expression
TNF        (MYD88 | MYC | IL23A | LPL | FOS | RXRA | IFNG | RB1 | TNFAIP3 | CREB1 | COMPLEX_P19838_Q04206 | IL12B) & !(MAP4K4 | TRAF1 | CFLAR | PTEN | CYLD | PPARA | MAP2K3 | INS | MAPK11 | CCND1 | CSF3 | S100B | MAPK14 | APEX1 | SP1 | CSF2)
TNFRSF1A   (TNF | FASLG | IL2 | TNFAIP3 | TNFRSF1B) & !(MAPK1 | CYLD | S100B)
TRADD      (TNFRSF1A | TNFRSF10B) & !(TNF | CFLAR | CYLD | KRT18 | S100B)
TRAF2      (TNFRSF1A | RELA | TRAF1 | CASP2 | NFKB2 | TNFRSF1B) & !(CYLD | STAT1 | FLNA | PPP2CA | S100B | TNFAIP3)
RIPK1      (TRADD | TNFRSF1A | TRAF2 | FADD | BIRC2 | BIRC3 | SQSTM1 | TICAM1 | HSP90AA1 | CASP2 | TNFRSF10B) & !(CASP8 | CFLAR | OTUD7B | RNF11 | TNFAIP3 | S100B | CASP10)
FADD       (TRADD | TNFRSF1A | TP53 | STAT1 | MYD88 | TNFRSF10B) & !(MAP2K7 | BIRC2 | MAP3K1 | S100B | RIPK2)
CASP8      (TNF | TNFRSF1A | TRADD | TRAF2 | E2F1 | FADD | TP53 | EDN1 | CASP2 | IFNG | TNFRSF10B) & !(RELA | BCL2 | CFLAR | BIRC2 | BIRC3 | MAPK3 | MAPK1 | NFKB1 | S100B | MAPK14 | CDK1)
CFLAR      (MAPK14 | AR | TP53 | DDB2) & !(MAPK8 | BIRC2 | BIRC3 | AKT1 | MYC | CBL | ATM)
BCL2       (RELA | MAP2K1 | NFKB1 | MTOR | CREB1 | E2F2 | BAG1 | STAT1 | PPP2CA | NFKB2 | HSP90AA1 | EIF4G2 | CTNNB1 | IL6 | BCL2L1 | VEGFA) & !(CASP3 | TP53 | IRS1 | IL5 | CDK6 | MAPK14 | ATM | BCL2L11 | PPP2R5C)
BAX        (MAPK8 | BID | TP73 | TP53 | CASP3 | TP63 | SP1 | RPS6KB1 | MYC | BCL2L11) & !(BCL2 | MCL1 | RELA | AKT1 | UBB | PRKCZ | PRNP | AKT3 | BCL2L1)
MCL1       (MAPK3 | MAPK1 | MAP2K1 | CSF2 | AKT1 | HIF1A | IL6 | VEGFA) & !(CASP3 | E2F1 | TFDP1 | BCL2L11 | CDK1)
XIAP       (RELA | TP53 | NFKB1 | EIF4G2 | AKT3 | AKT1 | AKT2 | BIRC5 | NFKB2 | ELK1) & !(HTRA2)
BIRC2      (TRADD | TNFRSF1B | TRAF2 | RELA | NFKB1 | EIF4G2 | BIRC3 | ELK1 | CD40LG | NFKB2) & !(HTRA2)
BIRC3      (CSF3 | RELA | TRAF2 | NFKBIA | NFKB1 | NFKB2 | ELK1) & !(TP53 | HTRA2 | S100B)
IKBKB      (TNF | MAP3K5 | TRADD | TRAF2 | RIPK1 | FADD | CASP8 | MAP3K7 | RIPK2 | AKT1 | FASLG | AKT2 | MAP4K4 | MYD88 | CHUK | TNFRSF10B | FLNA | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | AKT3 | IKBKG | IRAK1 | NGFR) & !(CASP3)
NFKBIA     (TRAF2 | ATM | CASP3 | IKBKG | RXRA | IL12B | TRAF1 | IL23A | NFKB1 | TRAF6 | MAP3K1) & !(TNF | TNFRSF1A | RELA | MAPK3 | JUN | RPS6KA2 | CUL1 | PPARA | MAPK1 | TNFAIP3 | MAPK14 | PRKCZ | SP1 | PRKCD | HSPB1)
RELA       (TNF | TNFRSF1A | TRADD | RIPK1 | TRAF2 | PIK3CA | E2F1 | IKBKB | IKBKG | IL23A | MAPK3 | IL1B | CUL1 | RAC1 | TRAF1 | MAPK1 | CHUK | NFKB1 | MAPK14 | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | IRAK1 | NGFR | IL12B | RPS6KA2 | PRKCD) & !(CASP3 | STAT1 | TSC22D3 | PPP2CA | SIRT1)
MAP3K7     (IL1A | TRAF2 | TRAF6 | MYD88 | XIAP | RIPK2 | IRAK1 | LAT | SMAD7 | GNAI1 | TRIM8 | MAP3K1 | MAP4K4 | CYLD | TGFB1 | EPHB2 | TICAM1 | BMP2) & !(MAPK11 | PPP2CA)
MAPK8      (TNF | MAPK3 | MAP3K5 | TRAF2 | MAP2K7 | MAP2K4 | MAP3K7 | PIK3CA | XIAP | RIPK2 | NGFR | IL2 | SH3RF1 | PTK2B | RAC1 | ROCK1 | LYN | MAP2K3 | BDNF | TGFB1 | MAP2K1 | TRAF6 | PRKCZ | MAP3K1 | EDN1 | CD40LG | IL1B | GNAI1 | PRKCD | ILK | CDC42) & !(AKT2 | MAPK1)
JUN        (TNF | RELA | MAPK9 | NFKB1 | PAK2 | MAPK8 | COMPLEX_P19838_Q04206 | IL2 | FOS | ILK | AKT1 | AKT2 | MEF2D | AR | CDK3 | ARHGDIB | MAPK11 | BDNF | RB1 | MAPK1 | MAPK14 | MAP3K1 | AKT3 | ELK1) & !(NOTCH1 | VDR | LYN)
FOS        (MAPK3 | RELA | NFKB1 | APEX1 | MAPK8 | SMAD4 | AKT1 | AKT2 | HNRNPR | MRTFA | MAPK11 | MAPK1 | MAPK14 | CREB1 | AKT3 | ELK1 | IL12B | ILK) & !(NOTCH1 | VDR | PPP3CA | LYN)
PIK3CA     (BDNF | RAC1 | TRAF5 | EPHB2 | EGFR | CTNNB1 | FOXO3 | IL23A | ZAP70 | INS | FGR | IRS4 | VEGFA | FGFR2 | GNG2 | PTK2 | LAMB2 | LYN | TGFB1 | IFNG | IRS1 | IL5 | CD40LG | IL12B | LAT | GNAI1 | SHC1 | SOS1) & !(PTEN | CDKN2A | CDKN2A)
AKT1       (TNF | MAPK8 | TRAF6 | MTOR | ATM | FASLG | IL2 | TGFB1 | PELP1 | SIRT1 | COMPLEX_P20248_P24941 | EIF4E | INS | RAC1 | EDN1 | CD40LG | GNAI1 | SHC1 | ILK | LAMB2 | SOS1) & !(CASP3 | RALBP1 | PPP2CA | PRKCZ | PPP2R5C)
PTEN       (XIAP | TGFB1 | TP53 | CASP3 | CDC42 | EGR1 | HSP90AA1 | ROCK1) & !(RELA | BMP2 | AKT1 | JUN | FOS)
MTOR       (CXCL8 | CHUK | IKBKB | IL2 | SHC1 | PIK3CA | RHEB | SOS1 | TSC2 | EGFR | TGFB1 | CDC42)
CCND1      (MAPK3 | RELA | NFKB1 | COMPLEX_P19838_Q04206 | SMAD4 | JUN | FOS | PIK3CA | NOTCH1 | DDAH2 | MYC | EGFR | MAPK1 | RAC1 | STAT1 | NFKB2 | MAPK14 | CREB1 | TERT | SP1 | ELK1) & !(CDKN1A | BCL2 | CDKN2A | CDKN2A)
CDK4       (MAPK3 | MAPK1 | MYC | IL6 | FOS | JUN | CCND1 | CCND3) & !(CDKN2A | CDKN1A | CDKN2A | TGFB1)
E2F1       (MAPK3 | MAPK1 | PARP1 | PTEN | CUL1 | EGFR | ATM | SP1 | CDK1 | VEGFA | COMPLEX_P20248_P24941 | E2F3 | CCNE1) & !(CDKN1A | CCND3 | RB1 | SIRT1 | CDK3)
MYC        (BCL2 | E2F1 | MAPK3 | MAP3K5 | NFKB1 | MAPK8 | IL2 | PIK3CA | RPS6KB1 | E2F3 | SMAD4 | RAC1 | INS | MAPK11 | RXRA | MAPK1 | CHUK | MAPK9 | PPP2CA | MAPK14 | IL5 | CTNNB1 | CREB1 | E2F2) & !(RELA | JUN | RB1 | PPARA | PAK2)
TP53       (MAPK3 | NFKB1 | TRAF2 | TRAF6 | XIAP | MAPK8 | E2F1 | PSEN1 | DAXX | PARP1 | BAD | NGFR | EGR1 | TP53BP1 | PTK2B | CCNE1 | PPP2R5C | MAPK11 | BDNF | TGFB1 | MAPK1 | RAC1 | MAPK9 | MAPK14 | APEX1 | CREB1 | CD40LG | PRKCD | CDK1 | COMPLEX_P20248_P24941) & !(JUN | FOS | NOTCH1 | TRIM24 | XPO1 | HSP90AA1 | BAG1 | SIRT1 | BCL2L1 | HSPB1)
CDKN1A     (MAP3K5 | MAPK14 | CASP3 | EGR1 | MAPK8 | JUN | IL1B | NOTCH1 | E2F3 | SMAD4 | IL1A | TGFB1 | IFNG | RAC1 | STAT1 | AR | CREB1 | SP1 | HIF1A) & !(CDK6 | MYC | TP73 | DDB2 | TP63 | CDKN2A | CUL1 | CDKN2A)
CASP3      (TNF | TNFRSF1A | FADD | CASP8 | CASP10 | PRNP | CYCS | NFE2L2 | PRKCD | IFNG | E2F1 | VDR) & !(BIRC3 | MAPK14 | BIRC2 | XIAP | NAIP | HSPB1)
CASP9      (APAF1 | RARA | E2F1 | DIABLO | CYCS) & !(MAPK3 | BIRC2 | BIRC3 | MAPK1 | ALPI | BAD | BCL2L1 | CDK1 | BIRC5 | GSN | MAP2K1 | PRKCZ | AKT3 | NAIP)
APAF1      (SUCLA2 | CASP10 | BAX | COX5B | ACHE | TP53 | RAC1 | E2F1 | TFDP1 | EIF4G2 | DIABLO | CYCS) & !(BIRC2 | BIRC3 | BCL2 | XIAP | AKT1 | HSPA4 | HSP90AA1 | BIRC5)
MAP4K4     (TNFRSF1A | RIPK1 | BIRC3 | TNF | TRADD | FADD | TP53 | MYD88 | IL1A | MAP3K5 | CASP2 | EPHB2 | TRAF6 | CD40LG | IRAK1)
TRAF1      (TRADD | TRAF2 | RELA | TNFRSF1B | NFKB1 | NFKB2 | TICAM1) & !(MYC | CYLD | S100B)
MYD88      !(FADD | IL1B)
MAPK3      (TNF | TNFRSF1A | MAP3K7 | AKT1 | CSF3 | MAP2K3 | MAPK11 | BDNF | TGFB1 | SUCLA2 | MAPK1 | IL2 | NFKB1 | MAP2K7 | MAP2K1 | MAPK9 | EPHB2 | TRAF6 | MAP2K4 | PRKCZ | MAP3K1 | EDN1 | IL5 | CSF2 | IL6 | RIPK2 | IL1B | GNAI1 | PTK2B | LYN | VEGFA | PELP1) & !(PIK3CA | PPP2CA | MAPK14 | TSC22D3 | PRKCD)
CSF3       (TNF | IFNG) & !(CXCL8)
CYLD       CYLD
IL23A      (NFKBIA | TNF | RELA | JUN | NFKB1 | IL1B) & !(MAPK1)
PPARA      (MAPK8 | MAPK3 | RXRA | MAPK1) & !(RELA)
MAP2K3     (MAP3K7 | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | TGFB1 | MAPK1 | FASLG | MAP3K5 | RAC1 | TRAF6 | MAP3K1 | DAXX | IL1B | PTK2B | CDC42)
IL1A       (TNF | TP63 | IL6 | IL1B) & !(IFNG)
INS        !(MAPK8)
LPL        (TNF | TRAF2 | RXRA) & !(JUN | RELA | TGFB1 | IFNG | SP1)
MAPK11     (TRAF2 | MAP2K3 | IL2 | RAC1 | MAP2K7 | TRAF6 | MAP2K4 | MAP3K1 | PAK2 | CD40LG | ZAP70 | SHC1 | LYN | FGR | CDC42 | VEGFA | GNG2) & !(PIK3CA | DUSP4)
BDNF       (TNF | MAPK3)
RXRA       (AKT1 | MAP3K7 | AR | RARA | VDR | CDK1 | FGR) & !(MAPK9 | MAP2K4)
TGFB1      (RELA | MAP3K7 | JUN | FOS | IFNG | RB1 | NFKB1 | EPHB2 | EDN1 | RPS6KB1 | HIF1A | EGR1 | EIF4E) & !(TNF | AKT1 | MAP2K3 | IL2 | MAPK14 | DAXX | IRS1 | SMAD4 | HSPB1)
IFNG       (MTOR | JUN | FOS | MAPK3 | IL23A | LPL | MAPK1 | IL2 | NFKB1 | IL12B | NOTCH1) & !(TNF | TGFB1 | MAPK9 | PPP3CA)
CXCL8      (TNF | RELA | JUN | FOS | MYC | IL1A | TGFB1 | FASLG | RAC1 | NFKB1 | MAP2K1 | PPP2CA | EGFR | EDN1 | CTNNB1 | CSF2 | CD40LG | COMPLEX_P19838_Q04206 | IL1B | BCL2L1 | VEGFA) & !(MAPK3 | MAPK11 | IFNG | MAPK14 | HIF1A | EGR1)
RB1        (AKT1 | TP53 | TGFB1 | PPP2CA | SIRT1) & !(CASP3 | CDKN1A | SMAD7 | VEGFA)
CDK6       (CCND1 | MYC | TP73 | CREB1 | CCND3) & !(TNF)
SUCLA2     (TNF | TGFB1 | CD40LG | ACHE)
MAPK1      (FADD | TNF | IL1A | INS | BDNF | TGFB1 | SUCLA2 | IL2 | RAC1 | MAP2K7 | MAP2K1 | MAP2K4 | PRKCZ | MAP3K1 | EDN1 | CSF2 | IL1B | GNAI1 | BMP2 | SHC1 | FGR | CDC42 | VEGFA) & !(TRADD | PIK3CA | PPP2CA)
FASLG      (RIPK1 | MAPK8 | JUN | FOS | TP53 | IFNG | NFKB1 | STAT1 | IL12B | EGR1) & !(BIRC2 | BIRC3 | RIPK2 | SIRT1 | HSPB1)
CASP7      (CASP8 | CASP3 | CASP9 | APAF1 | FADD | FASLG | CASP2 | CASP10 | CYCS) & !(XIAP | BIRC2 | BIRC3 | RB1 | PAK2 | E2F2 | TFDP1 | BIRC5 | NAIP | E2F3)
BID        (TNFRSF1A | TRADD | TRAF2 | RIPK1 | FADD | BIRC3 | TNF | CASP8 | MAPK8 | E2F1 | TP53 | CASP3 | FASLG | MAP3K5 | CASP2 | DAXX | CASP10 | ATM) & !(BCL2 | HIF1A)
TNFRSF1B   (TNFRSF1A | TNF)
MAP3K5     (TNFRSF1A | TRADD | E2F1 | TNF | IFNG | MAPK1 | TRAF6 | DAXX) & !(AKT1 | RB1 | S100B | AKT3 | AKT2)
IL2        (JUN | FOS | IL1A | NFKB1 | IL5 | CREB1 | IL6 | IKBKG | IL1B) & !(MAP3K7 | CSF3 | CSF2 | CD40LG)
TNFAIP3    (RELA | TNF | TNFRSF1A | NFKB1)
RAC1       (TNFRSF1A | CDKN1A | PIK3CA | PTEN | EPHB2 | EGFR | EDN1 | NGFR | GNAI1 | SHC1 | PTK2B | LYN | VEGFA | GNG2 | PTK2 | LAMB2 | SOS1) & !(TP53)
CHUK       (TNFRSF1A | CASP8 | TNF | TRADD | TRAF2 | RIPK1 | FADD | MAP3K7 | AKT1 | MAP4K4 | MYD88 | MAPK3 | IL1A | FASLG | MAP3K5 | TNFRSF10B | FLNA | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | TP63 | AKT3 | AKT2 | IKBKG | RIPK2 | IRAK1 | NGFR | NOTCH1)
TRAF5      (TRADD | RELA | NFKB1 | NFKB2)
TNFRSF10B  (TP53 | FASLG | NFKB1 | NOTCH1)
NFKB1      (TRADD | FADD | MAP3K7 | TNF | TNFRSF1A | TRAF2 | RIPK1 | PIK3CA | AKT1 | TRAF1 | IL23A | BDNF | SUCLA2 | MAPK1 | RAC1 | MAPK14 | SQSTM1 | TRAF6 | TICAM1 | EGFR | PARP1 | PRKCZ | MAP3K1 | EDN1 | CASP10 | ATM | PRNP | CSF2 | IKBKG | RIPK2 | IRAK1 | NGFR | IL12B | PRKCD | LYN) & !(E2F1 | BAG1 | CDKN2A | CUL1 | TSC22D3 | HSPB1 | CDKN2A)
KRT18      (CASP3 | AR | CDK1)
MAP2K7     (TRAF2 | RIPK1 | CASP8 | BIRC3 | MAP3K7 | TNF | TNFRSF1A | TRADD | TRAF1 | FASLG | MAP3K5 | RAC1 | CASP2 | FLNA | MAP3K1 | DAXX | RIPK2 | SH3RF1 | CDC42)
MAP2K1     (TRAF2 | MAP3K7 | PIK3CA | IL2 | RAC1 | MAPK14 | EGFR | MAP3K1 | PAK2 | CSF2 | PRKCD | SHC1) & !(PPP2CA | CDK1)
CASP2      (CASP3 | TRADD | TP73 | CCND3) & !(BIRC2 | S100B | AR)
STAT1      (MAPK8 | CSF3 | IL23A | MAPK11 | IFNG | MAPK1 | IL2 | MAPK9 | EPHB2 | MAPK14 | EGFR | AR | IL6 | IL12B | PRKCD | LYN | FGFR2 | PTK2) & !(CCND1 | CYLD)
MAPK9      (TRAF2 | MAPK8 | MAP2K3 | BDNF | MAP3K5 | RAC1 | MAP2K7 | MAP2K1 | MAPK14 | TRAF6 | MAP2K4 | PRKCZ | CD40LG | NGFR | CDC42) & !(DUSP4)
EPHB2      (TRAF2 | TGFB1 | MAPK14 | LYN | FGR) & !(PPP2CA)
FLNA       (AKT1 | PRKCD) & !(PPP3CA)
PPP2CA     (CDK3 | PPP2R5C) & !(MTOR)
NFKB2      (TP53 | CUL1) & !(MYC | TSC22D3)
S100B      (IFNG) & !(TP53)
MAPK14     (RIPK1 | TNF | TRAF2 | MAP3K7 | MAPK8 | PIK3CA | MAP2K3 | MAPK11 | TGFB1 | MAP3K5 | IL2 | RAC1 | MAP2K7 | TRAF6 | MAP2K4 | MAP3K1 | EDN1 | PAK2 | RIPK2 | CD40LG | ZAP70 | GNAI1 | BMP2 | PTK2B | LYN | CDC42 | GNG2) & !(DUSP4)
SQSTM1     (IKBKB | CDK1)
OTUD7B     (MAP3K7 | CDK4 | AKT1 | CDK6 | MAPK1 | IRAK1)
TRAF6      (RELA | MYD88 | IL1A | TGFB1 | NFKB1 | NFKB2 | SQSTM1 | TICAM1 | ATM | IRAK1 | IL1B | HSPB1) & !(TNFAIP3 | PSEN1)
TICAM1     (PIK3CA | TRAF2) & !(TRAF1 | TNFAIP3)
EGFR       (TP53 | INS | TGFB1 | CXCL8 | FASLG | PPP2CA | AR | EDN1 | EGR1 | PTK2B | LYN | RARA | NOTCH1 | FGR | VEGFA) & !(RIPK1 | PTEN | MAPK11 | MAPK14 | TRAF6 | PRKCD | CDK1 | CDC42)
RNF11      !(AKT1)
PARP1      (INS | SUCLA2 | MAPK1 | ILK) & !(RIPK1 | BCL2 | CASP7)
HSP90AA1   (MYC | PPARA | IL2 | ZAP70) & !(IFNG)
MAP2K4     (FADD | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | BIRC3 | MAP3K7 | FASLG | MAP3K5 | RAC1 | MAP2K7 | MAP2K1 | FLNA | DAXX | CASP10 | CD40LG | SH3RF1 | ROCK1) & !(AKT1 | AKT3 | AKT2)
PRKCZ      (PIK3CA | INS | IL2 | SHC1 | ROCK1 | CDC42) & !(PPP2CA)
MAP3K1     (AKT1 | CASP3 | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | MAP4K4 | TRAF1 | MYD88 | IL1A | IFNG | CASP7 | TNFRSF1B | RAC1 | TNFRSF10B | TRAF6 | EGFR | PAK2 | CD40LG | IRAK1 | LAT | CDC42)
AR         (MAPK8 | RXRA | TGFB1 | MAPK14 | HSP90AA1 | MAP3K1 | EDN1 | SIRT1 | SMAD4 | CDK1 | TRIM24 | GSN) & !(CASP8 | PTEN | E2F1 | RELA | TP53 | CASP7 | DAXX | EGR1)
TP73       (CASP8 | E2F1 | TP53 | CASP3 | MAPK11 | MAPK14 | TFDP1 | PRKCD) & !(SIRT1 | CDK1)
EIF4G2     (CASP8 | CASP9 | CASP7 | CASP2 | CASP10 | CDK1)
EDN1       (JUN | FOS | TNF | PPARA | TGFB1 | CREB1 | HIF1A) & !(VEGFA)
PAK2       (CASP8 | CASP3 | TGFB1 | RAC1 | CDC42)
RALBP1     (CASP8)
PSEN1      (CASP8 | TNF | CASP3 | CASP7 | MAPK9 | PRKCZ) & !(ELK1)
ALPI       (CASP8 | CASP10) & !(NFKB1 | DIABLO)
CBL        (CDK4 | AKT1 | INS | IFNG | IL2 | PRKCZ | IRS1 | PRKCD | PTK2B | FGR)

**Warning:** The following gene/node names were modified to remove special characters: COMPLEX:P19838_Q04206, COMPLEX:P20248_P24941

**Tool Output:**

{
  "result": "**Exported to** `Network_1.bnet`\n\n_Preview (first 100 lines) of the BNET file:_\n\ngene       expression\nTNF        (MYD88 | MYC | IL23A | LPL | FOS | RXRA | IFNG | RB1 | TNFAIP3 | CREB1 | COMPLEX_P19838_Q04206 | IL12B) & !(MAP4K4 | TRAF1 | CFLAR | PTEN | CYLD | PPARA | MAP2K3 | INS | MAPK11 | CCND1 | CSF3 | S100B | MAPK14 | APEX1 | SP1 | CSF2)\nTNFRSF1A   (TNF | FASLG | IL2 | TNFAIP3 | TNFRSF1B) & !(MAPK1 | CYLD | S100B)\nTRADD      (TNFRSF1A | TNFRSF10B) & !(TNF | CFLAR | CYLD | KRT18 | S100B)\nTRAF2      (TNFRSF1A | RELA | TRAF1 | CASP2 | NFKB2 | TNFRSF1B) & !(CYLD | STAT1 | FLNA | PPP2CA | S100B | TNFAIP3)\nRIPK1      (TRADD | TNFRSF1A | TRAF2 | FADD | BIRC2 | BIRC3 | SQSTM1 | TICAM1 | HSP90AA1 | CASP2 | TNFRSF10B) & !(CASP8 | CFLAR | OTUD7B | RNF11 | TNFAIP3 | S100B | CASP10)\nFADD       (TRADD | TNFRSF1A | TP53 | STAT1 | MYD88 | TNFRSF10B) & !(MAP2K7 | BIRC2 | MAP3K1 | S100B | RIPK2)\nCASP8      (TNF | TNFRSF1A | TRADD | TRAF2 | E2F1 | FADD | TP53 | EDN1 | CASP2 | IFNG | TNFRSF10B) & !(RELA | BCL2 | CFLAR | BIRC2 | BIRC3 | MAPK3 | MAPK1 | NFKB1 | S100B | MAPK14 | CDK1)\nCFLAR      (MAPK14 | AR | TP53 | DDB2) & !(MAPK8 | BIRC2 | BIRC3 | AKT1 | MYC | CBL | ATM)\nBCL2       (RELA | MAP2K1 | NFKB1 | MTOR | CREB1 | E2F2 | BAG1 | STAT1 | PPP2CA | NFKB2 | HSP90AA1 | EIF4G2 | CTNNB1 | IL6 | BCL2L1 | VEGFA) & !(CASP3 | TP53 | IRS1 | IL5 | CDK6 | MAPK14 | ATM | BCL2L11 | PPP2R5C)\nBAX        (MAPK8 | BID | TP73 | TP53 | CASP3 | TP63 | SP1 | RPS6KB1 | MYC | BCL2L11) & !(BCL2 | MCL1 | RELA | AKT1 | UBB | PRKCZ | PRNP | AKT3 | BCL2L1)\nMCL1       (MAPK3 | MAPK1 | MAP2K1 | CSF2 | AKT1 | HIF1A | IL6 | VEGFA) & !(CASP3 | E2F1 | TFDP1 | BCL2L11 | CDK1)\nXIAP       (RELA | TP53 | NFKB1 | EIF4G2 | AKT3 | AKT1 | AKT2 | BIRC5 | NFKB2 | ELK1) & !(HTRA2)\nBIRC2      (TRADD | TNFRSF1B | TRAF2 | RELA | NFKB1 | EIF4G2 | BIRC3 | ELK1 | CD40LG | NFKB2) & !(HTRA2)\nBIRC3      (CSF3 | RELA | TRAF2 | NFKBIA | NFKB1 | NFKB2 | ELK1) & !(TP53 | HTRA2 | S100B)\nIKBKB      (TNF | MAP3K5 | TRADD | TRAF2 | RIPK1 | FADD | CASP8 | MAP3K7 | RIPK2 | AKT1 | FASLG | AKT2 | MAP4K4 | MYD88 | CHUK | TNFRSF10B | FLNA | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | AKT3 | IKBKG | IRAK1 | NGFR) & !(CASP3)\nNFKBIA     (TRAF2 | ATM | CASP3 | IKBKG | RXRA | IL12B | TRAF1 | IL23A | NFKB1 | TRAF6 | MAP3K1) & !(TNF | TNFRSF1A | RELA | MAPK3 | JUN | RPS6KA2 | CUL1 | PPARA | MAPK1 | TNFAIP3 | MAPK14 | PRKCZ | SP1 | PRKCD | HSPB1)\nRELA       (TNF | TNFRSF1A | TRADD | RIPK1 | TRAF2 | PIK3CA | E2F1 | IKBKB | IKBKG | IL23A | MAPK3 | IL1B | CUL1 | RAC1 | TRAF1 | MAPK1 | CHUK | NFKB1 | MAPK14 | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | IRAK1 | NGFR | IL12B | RPS6KA2 | PRKCD) & !(CASP3 | STAT1 | TSC22D3 | PPP2CA | SIRT1)\nMAP3K7     (IL1A | TRAF2 | TRAF6 | MYD88 | XIAP | RIPK2 | IRAK1 | LAT | SMAD7 | GNAI1 | TRIM8 | MAP3K1 | MAP4K4 | CYLD | TGFB1 | EPHB2 | TICAM1 | BMP2) & !(MAPK11 | PPP2CA)\nMAPK8      (TNF | MAPK3 | MAP3K5 | TRAF2 | MAP2K7 | MAP2K4 | MAP3K7 | PIK3CA | XIAP | RIPK2 | NGFR | IL2 | SH3RF1 | PTK2B | RAC1 | ROCK1 | LYN | MAP2K3 | BDNF | TGFB1 | MAP2K1 | TRAF6 | PRKCZ | MAP3K1 | EDN1 | CD40LG | IL1B | GNAI1 | PRKCD | ILK | CDC42) & !(AKT2 | MAPK1)\nJUN        (TNF | RELA | MAPK9 | NFKB1 | PAK2 | MAPK8 | COMPLEX_P19838_Q04206 | IL2 | FOS | ILK | AKT1 | AKT2 | MEF2D | AR | CDK3 | ARHGDIB | MAPK11 | BDNF | RB1 | MAPK1 | MAPK14 | MAP3K1 | AKT3 | ELK1) & !(NOTCH1 | VDR | LYN)\nFOS        (MAPK3 | RELA | NFKB1 | APEX1 | MAPK8 | SMAD4 | AKT1 | AKT2 | HNRNPR | MRTFA | MAPK11 | MAPK1 | MAPK14 | CREB1 | AKT3 | ELK1 | IL12B | ILK) & !(NOTCH1 | VDR | PPP3CA | LYN)\nPIK3CA     (BDNF | RAC1 | TRAF5 | EPHB2 | EGFR | CTNNB1 | FOXO3 | IL23A | ZAP70 | INS | FGR | IRS4 | VEGFA | FGFR2 | GNG2 | PTK2 | LAMB2 | LYN | TGFB1 | IFNG | IRS1 | IL5 | CD40LG | IL12B | LAT | GNAI1 | SHC1 | SOS1) & !(PTEN | CDKN2A | CDKN2A)\nAKT1       (TNF | MAPK8 | TRAF6 | MTOR | ATM | FASLG | IL2 | TGFB1 | PELP1 | SIRT1 | COMPLEX_P20248_P24941 | EIF4E | INS | RAC1 | EDN1 | CD40LG | GNAI1 | SHC1 | ILK | LAMB2 | SOS1) & !(CASP3 | RALBP1 | PPP2CA | PRKCZ | PPP2R5C)\nPTEN       (XIAP | TGFB1 | TP53 | CASP3 | CDC42 | EGR1 | HSP90AA1 | ROCK1) & !(RELA | BMP2 | AKT1 | JUN | FOS)\nMTOR       (CXCL8 | CHUK | IKBKB | IL2 | SHC1 | PIK3CA | RHEB | SOS1 | TSC2 | EGFR | TGFB1 | CDC42)\nCCND1      (MAPK3 | RELA | NFKB1 | COMPLEX_P19838_Q04206 | SMAD4 | JUN | FOS | PIK3CA | NOTCH1 | DDAH2 | MYC | EGFR | MAPK1 | RAC1 | STAT1 | NFKB2 | MAPK14 | CREB1 | TERT | SP1 | ELK1) & !(CDKN1A | BCL2 | CDKN2A | CDKN2A)\nCDK4       (MAPK3 | MAPK1 | MYC | IL6 | FOS | JUN | CCND1 | CCND3) & !(CDKN2A | CDKN1A | CDKN2A | TGFB1)\nE2F1       (MAPK3 | MAPK1 | PARP1 | PTEN | CUL1 | EGFR | ATM | SP1 | CDK1 | VEGFA | COMPLEX_P20248_P24941 | E2F3 | CCNE1) & !(CDKN1A | CCND3 | RB1 | SIRT1 | CDK3)\nMYC        (BCL2 | E2F1 | MAPK3 | MAP3K5 | NFKB1 | MAPK8 | IL2 | PIK3CA | RPS6KB1 | E2F3 | SMAD4 | RAC1 | INS | MAPK11 | RXRA | MAPK1 | CHUK | MAPK9 | PPP2CA | MAPK14 | IL5 | CTNNB1 | CREB1 | E2F2) & !(RELA | JUN | RB1 | PPARA | PAK2)\nTP53       (MAPK3 | NFKB1 | TRAF2 | TRAF6 | XIAP | MAPK8 | E2F1 | PSEN1 | DAXX | PARP1 | BAD | NGFR | EGR1 | TP53BP1 | PTK2B | CCNE1 | PPP2R5C | MAPK11 | BDNF | TGFB1 | MAPK1 | RAC1 | MAPK9 | MAPK14 | APEX1 | CREB1 | CD40LG | PRKCD | CDK1 | COMPLEX_P20248_P24941) & !(JUN | FOS | NOTCH1 | TRIM24 | XPO1 | HSP90AA1 | BAG1 | SIRT1 | BCL2L1 | HSPB1)\nCDKN1A     (MAP3K5 | MAPK14 | CASP3 | EGR1 | MAPK8 | JUN | IL1B | NOTCH1 | E2F3 | SMAD4 | IL1A | TGFB1 | IFNG | RAC1 | STAT1 | AR | CREB1 | SP1 | HIF1A) & !(CDK6 | MYC | TP73 | DDB2 | TP63 | CDKN2A | CUL1 | CDKN2A)\nCASP3      (TNF | TNFRSF1A | FADD | CASP8 | CASP10 | PRNP | CYCS | NFE2L2 | PRKCD | IFNG | E2F1 | VDR) & !(BIRC3 | MAPK14 | BIRC2 | XIAP | NAIP | HSPB1)\nCASP9      (APAF1 | RARA | E2F1 | DIABLO | CYCS) & !(MAPK3 | BIRC2 | BIRC3 | MAPK1 | ALPI | BAD | BCL2L1 | CDK1 | BIRC5 | GSN | MAP2K1 | PRKCZ | AKT3 | NAIP)\nAPAF1      (SUCLA2 | CASP10 | BAX | COX5B | ACHE | TP53 | RAC1 | E2F1 | TFDP1 | EIF4G2 | DIABLO | CYCS) & !(BIRC2 | BIRC3 | BCL2 | XIAP | AKT1 | HSPA4 | HSP90AA1 | BIRC5)\nMAP4K4     (TNFRSF1A | RIPK1 | BIRC3 | TNF | TRADD | FADD | TP53 | MYD88 | IL1A | MAP3K5 | CASP2 | EPHB2 | TRAF6 | CD40LG | IRAK1)\nTRAF1      (TRADD | TRAF2 | RELA | TNFRSF1B | NFKB1 | NFKB2 | TICAM1) & !(MYC | CYLD | S100B)\nMYD88      !(FADD | IL1B)\nMAPK3      (TNF | TNFRSF1A | MAP3K7 | AKT1 | CSF3 | MAP2K3 | MAPK11 | BDNF | TGFB1 | SUCLA2 | MAPK1 | IL2 | NFKB1 | MAP2K7 | MAP2K1 | MAPK9 | EPHB2 | TRAF6 | MAP2K4 | PRKCZ | MAP3K1 | EDN1 | IL5 | CSF2 | IL6 | RIPK2 | IL1B | GNAI1 | PTK2B | LYN | VEGFA | PELP1) & !(PIK3CA | PPP2CA | MAPK14 | TSC22D3 | PRKCD)\nCSF3       (TNF | IFNG) & !(CXCL8)\nCYLD       CYLD\nIL23A      (NFKBIA | TNF | RELA | JUN | NFKB1 | IL1B) & !(MAPK1)\nPPARA      (MAPK8 | MAPK3 | RXRA | MAPK1) & !(RELA)\nMAP2K3     (MAP3K7 | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | TGFB1 | MAPK1 | FASLG | MAP3K5 | RAC1 | TRAF6 | MAP3K1 | DAXX | IL1B | PTK2B | CDC42)\nIL1A       (TNF | TP63 | IL6 | IL1B) & !(IFNG)\nINS        !(MAPK8)\nLPL        (TNF | TRAF2 | RXRA) & !(JUN | RELA | TGFB1 | IFNG | SP1)\nMAPK11     (TRAF2 | MAP2K3 | IL2 | RAC1 | MAP2K7 | TRAF6 | MAP2K4 | MAP3K1 | PAK2 | CD40LG | ZAP70 | SHC1 | LYN | FGR | CDC42 | VEGFA | GNG2) & !(PIK3CA | DUSP4)\nBDNF       (TNF | MAPK3)\nRXRA       (AKT1 | MAP3K7 | AR | RARA | VDR | CDK1 | FGR) & !(MAPK9 | MAP2K4)\nTGFB1      (RELA | MAP3K7 | JUN | FOS | IFNG | RB1 | NFKB1 | EPHB2 | EDN1 | RPS6KB1 | HIF1A | EGR1 | EIF4E) & !(TNF | AKT1 | MAP2K3 | IL2 | MAPK14 | DAXX | IRS1 | SMAD4 | HSPB1)\nIFNG       (MTOR | JUN | FOS | MAPK3 | IL23A | LPL | MAPK1 | IL2 | NFKB1 | IL12B | NOTCH1) & !(TNF | TGFB1 | MAPK9 | PPP3CA)\nCXCL8      (TNF | RELA | JUN | FOS | MYC | IL1A | TGFB1 | FASLG | RAC1 | NFKB1 | MAP2K1 | PPP2CA | EGFR | EDN1 | CTNNB1 | CSF2 | CD40LG | COMPLEX_P19838_Q04206 | IL1B | BCL2L1 | VEGFA) & !(MAPK3 | MAPK11 | IFNG | MAPK14 | HIF1A | EGR1)\nRB1        (AKT1 | TP53 | TGFB1 | PPP2CA | SIRT1) & !(CASP3 | CDKN1A | SMAD7 | VEGFA)\nCDK6       (CCND1 | MYC | TP73 | CREB1 | CCND3) & !(TNF)\nSUCLA2     (TNF | TGFB1 | CD40LG | ACHE)\nMAPK1      (FADD | TNF | IL1A | INS | BDNF | TGFB1 | SUCLA2 | IL2 | RAC1 | MAP2K7 | MAP2K1 | MAP2K4 | PRKCZ | MAP3K1 | EDN1 | CSF2 | IL1B | GNAI1 | BMP2 | SHC1 | FGR | CDC42 | VEGFA) & !(TRADD | PIK3CA | PPP2CA)\nFASLG      (RIPK1 | MAPK8 | JUN | FOS | TP53 | IFNG | NFKB1 | STAT1 | IL12B | EGR1) & !(BIRC2 | BIRC3 | RIPK2 | SIRT1 | HSPB1)\nCASP7      (CASP8 | CASP3 | CASP9 | APAF1 | FADD | FASLG | CASP2 | CASP10 | CYCS) & !(XIAP | BIRC2 | BIRC3 | RB1 | PAK2 | E2F2 | TFDP1 | BIRC5 | NAIP | E2F3)\nBID        (TNFRSF1A | TRADD | TRAF2 | RIPK1 | FADD | BIRC3 | TNF | CASP8 | MAPK8 | E2F1 | TP53 | CASP3 | FASLG | MAP3K5 | CASP2 | DAXX | CASP10 | ATM) & !(BCL2 | HIF1A)\nTNFRSF1B   (TNFRSF1A | TNF)\nMAP3K5     (TNFRSF1A | TRADD | E2F1 | TNF | IFNG | MAPK1 | TRAF6 | DAXX) & !(AKT1 | RB1 | S100B | AKT3 | AKT2)\nIL2        (JUN | FOS | IL1A | NFKB1 | IL5 | CREB1 | IL6 | IKBKG | IL1B) & !(MAP3K7 | CSF3 | CSF2 | CD40LG)\nTNFAIP3    (RELA | TNF | TNFRSF1A | NFKB1)\nRAC1       (TNFRSF1A | CDKN1A | PIK3CA | PTEN | EPHB2 | EGFR | EDN1 | NGFR | GNAI1 | SHC1 | PTK2B | LYN | VEGFA | GNG2 | PTK2 | LAMB2 | SOS1) & !(TP53)\nCHUK       (TNFRSF1A | CASP8 | TNF | TRADD | TRAF2 | RIPK1 | FADD | MAP3K7 | AKT1 | MAP4K4 | MYD88 | MAPK3 | IL1A | FASLG | MAP3K5 | TNFRSF10B | FLNA | SQSTM1 | TRAF6 | PRKCZ | MAP3K1 | TP63 | AKT3 | AKT2 | IKBKG | RIPK2 | IRAK1 | NGFR | NOTCH1)\nTRAF5      (TRADD | RELA | NFKB1 | NFKB2)\nTNFRSF10B  (TP53 | FASLG | NFKB1 | NOTCH1)\nNFKB1      (TRADD | FADD | MAP3K7 | TNF | TNFRSF1A | TRAF2 | RIPK1 | PIK3CA | AKT1 | TRAF1 | IL23A | BDNF | SUCLA2 | MAPK1 | RAC1 | MAPK14 | SQSTM1 | TRAF6 | TICAM1 | EGFR | PARP1 | PRKCZ | MAP3K1 | EDN1 | CASP10 | ATM | PRNP | CSF2 | IKBKG | RIPK2 | IRAK1 | NGFR | IL12B | PRKCD | LYN) & !(E2F1 | BAG1 | CDKN2A | CUL1 | TSC22D3 | HSPB1 | CDKN2A)\nKRT18      (CASP3 | AR | CDK1)\nMAP2K7     (TRAF2 | RIPK1 | CASP8 | BIRC3 | MAP3K7 | TNF | TNFRSF1A | TRADD | TRAF1 | FASLG | MAP3K5 | RAC1 | CASP2 | FLNA | MAP3K1 | DAXX | RIPK2 | SH3RF1 | CDC42)\nMAP2K1     (TRAF2 | MAP3K7 | PIK3CA | IL2 | RAC1 | MAPK14 | EGFR | MAP3K1 | PAK2 | CSF2 | PRKCD | SHC1) & !(PPP2CA | CDK1)\nCASP2      (CASP3 | TRADD | TP73 | CCND3) & !(BIRC2 | S100B | AR)\nSTAT1      (MAPK8 | CSF3 | IL23A | MAPK11 | IFNG | MAPK1 | IL2 | MAPK9 | EPHB2 | MAPK14 | EGFR | AR | IL6 | IL12B | PRKCD | LYN | FGFR2 | PTK2) & !(CCND1 | CYLD)\nMAPK9      (TRAF2 | MAPK8 | MAP2K3 | BDNF | MAP3K5 | RAC1 | MAP2K7 | MAP2K1 | MAPK14 | TRAF6 | MAP2K4 | PRKCZ | CD40LG | NGFR | CDC42) & !(DUSP4)\nEPHB2      (TRAF2 | TGFB1 | MAPK14 | LYN | FGR) & !(PPP2CA)\nFLNA       (AKT1 | PRKCD) & !(PPP3CA)\nPPP2CA     (CDK3 | PPP2R5C) & !(MTOR)\nNFKB2      (TP53 | CUL1) & !(MYC | TSC22D3)\nS100B      (IFNG) & !(TP53)\nMAPK14     (RIPK1 | TNF | TRAF2 | MAP3K7 | MAPK8 | PIK3CA | MAP2K3 | MAPK11 | TGFB1 | MAP3K5 | IL2 | RAC1 | MAP2K7 | TRAF6 | MAP2K4 | MAP3K1 | EDN1 | PAK2 | RIPK2 | CD40LG | ZAP70 | GNAI1 | BMP2 | PTK2B | LYN | CDC42 | GNG2) & !(DUSP4)\nSQSTM1     (IKBKB | CDK1)\nOTUD7B     (MAP3K7 | CDK4 | AKT1 | CDK6 | MAPK1 | IRAK1)\nTRAF6      (RELA | MYD88 | IL1A | TGFB1 | NFKB1 | NFKB2 | SQSTM1 | TICAM1 | ATM | IRAK1 | IL1B | HSPB1) & !(TNFAIP3 | PSEN1)\nTICAM1     (PIK3CA | TRAF2) & !(TRAF1 | TNFAIP3)\nEGFR       (TP53 | INS | TGFB1 | CXCL8 | FASLG | PPP2CA | AR | EDN1 | EGR1 | PTK2B | LYN | RARA | NOTCH1 | FGR | VEGFA) & !(RIPK1 | PTEN | MAPK11 | MAPK14 | TRAF6 | PRKCD | CDK1 | CDC42)\nRNF11      !(AKT1)\nPARP1      (INS | SUCLA2 | MAPK1 | ILK) & !(RIPK1 | BCL2 | CASP7)\nHSP90AA1   (MYC | PPARA | IL2 | ZAP70) & !(IFNG)\nMAP2K4     (FADD | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | BIRC3 | MAP3K7 | FASLG | MAP3K5 | RAC1 | MAP2K7 | MAP2K1 | FLNA | DAXX | CASP10 | CD40LG | SH3RF1 | ROCK1) & !(AKT1 | AKT3 | AKT2)\nPRKCZ      (PIK3CA | INS | IL2 | SHC1 | ROCK1 | CDC42) & !(PPP2CA)\nMAP3K1     (AKT1 | CASP3 | TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | MAP4K4 | TRAF1 | MYD88 | IL1A | IFNG | CASP7 | TNFRSF1B | RAC1 | TNFRSF10B | TRAF6 | EGFR | PAK2 | CD40LG | IRAK1 | LAT | CDC42)\nAR         (MAPK8 | RXRA | TGFB1 | MAPK14 | HSP90AA1 | MAP3K1 | EDN1 | SIRT1 | SMAD4 | CDK1 | TRIM24 | GSN) & !(CASP8 | PTEN | E2F1 | RELA | TP53 | CASP7 | DAXX | EGR1)\nTP73       (CASP8 | E2F1 | TP53 | CASP3 | MAPK11 | MAPK14 | TFDP1 | PRKCD) & !(SIRT1 | CDK1)\nEIF4G2     (CASP8 | CASP9 | CASP7 | CASP2 | CASP10 | CDK1)\nEDN1       (JUN | FOS | TNF | PPARA | TGFB1 | CREB1 | HIF1A) & !(VEGFA)\nPAK2       (CASP8 | CASP3 | TGFB1 | RAC1 | CDC42)\nRALBP1     (CASP8)\nPSEN1      (CASP8 | TNF | CASP3 | CASP7 | MAPK9 | PRKCZ) & !(ELK1)\nALPI       (CASP8 | CASP10) & !(NFKB1 | DIABLO)\nCBL        (CDK4 | AKT1 | INS | IFNG | IL2 | PRKCZ | IRS1 | PRKCD | PTK2B | FGR)\n\n**Warning:** The following gene/node names were modified to remove special characters: COMPLEX:P19838_Q04206, COMPLEX:P20248_P24941"
}

**Tool Output:**

**Gene not found:** CDKN2A is not in the current network
**Tip:** Use `get_network()` to see all available genes

**Tool Output:**

{
  "result": "**Gene not found:** CDKN2A is not in the current network\n**Tip:** Use `get_network()` to see all available genes"
}

**Tool Output:**

No BND or CFG files found in the current directory.

**Tool Output:**

{
  "result": "No BND or CFG files found in the current directory."
}

**Tool Output:**

**References for interactions involving `CDKN2A`:**

source    target    Effect       References
IKBKB     CDKN2A    inhibition   ProtMapper:20152798; ProtMapper:21619050; ProtMapper:29292732; SIGNOR:20152798; iPTMnet:20152798 (+5 more)
CDKN2A    CCND1     inhibition
CDKN2A    CDK4      inhibition   BioGRID:10719365; BioGRID:12529334; HPRD:15232106; HPRD:17517622; HPRD:9228064 (+69 more)
CDKN2A    CDK4      inhibition   BioGRID:10719365; BioGRID:12529334; HPRD:15232106; HPRD:17517622; HPRD:9228064 (+47 more)
JUN       CDKN2A    stimulation
JUN       CDKN2A    stimulation
CDKN2A    PIK3CA    inhibition
CDKN2A    PIK3CA    inhibition
CDKN2A    CCND1     inhibition
CDKN2A    CDKN1A    inhibition
CDKN2A    CDKN1A    inhibition
CDKN2A    NFKB1     inhibition
CDKN2A    NFKB1     inhibition
CDKN2A    ATM       stimulation
CDKN2A    ATM       stimulation
CTNNB1    CDKN2A    inhibition
CTNNB1    CDKN2A    inhibition
E2F2      CDKN2A    stimulation  ACSN:11883935; SPIKE:11883935; SPIKE:18319725; SPIKE_LC:11883935; SPIKE_LC:18319725
E2F2      CDKN2A    stimulation  ACSN:11883935; SPIKE:11883935; SPIKE:18319725; SPIKE_LC:11883935; SPIKE_LC:18319725
TP63      CDKN2A    inhibition
TP63      CDKN2A    inhibition
TFDP1     CDKN2A    inhibition
CDKN2A    TFDP1     inhibition
TFDP1     CDKN2A    inhibition
CDKN2A    TFDP1     inhibition
CDKN2A    BIRC5     inhibition
CDKN2A    BIRC5     inhibition
CDKN2A    CCND3     inhibition
CDKN2A    VDR       inhibition
CDKN2A    BCL2L1    inhibition   SPIKE:19049976; SPIKE_LC:19049976
CDKN2A    CCND3     inhibition
CDKN2A    VDR       inhibition
CDKN2A    BCL2L1    inhibition   SPIKE:19049976; SPIKE_LC:19049976

**Tool Output:**

{
  "result": "**References for interactions involving `CDKN2A`:**\n\nsource    target    Effect       References\nIKBKB     CDKN2A    inhibition   ProtMapper:20152798; ProtMapper:21619050; ProtMapper:29292732; SIGNOR:20152798; iPTMnet:20152798 (+5 more)\nCDKN2A    CCND1     inhibition\nCDKN2A    CDK4      inhibition   BioGRID:10719365; BioGRID:12529334; HPRD:15232106; HPRD:17517622; HPRD:9228064 (+69 more)\nCDKN2A    CDK4      inhibition   BioGRID:10719365; BioGRID:12529334; HPRD:15232106; HPRD:17517622; HPRD:9228064 (+47 more)\nJUN       CDKN2A    stimulation\nJUN       CDKN2A    stimulation\nCDKN2A    PIK3CA    inhibition\nCDKN2A    PIK3CA    inhibition\nCDKN2A    CCND1     inhibition\nCDKN2A    CDKN1A    inhibition\nCDKN2A    CDKN1A    inhibition\nCDKN2A    NFKB1     inhibition\nCDKN2A    NFKB1     inhibition\nCDKN2A    ATM       stimulation\nCDKN2A    ATM       stimulation\nCTNNB1    CDKN2A    inhibition\nCTNNB1    CDKN2A    inhibition\nE2F2      CDKN2A    stimulation  ACSN:11883935; SPIKE:11883935; SPIKE:18319725; SPIKE_LC:11883935; SPIKE_LC:18319725\nE2F2      CDKN2A    stimulation  ACSN:11883935; SPIKE:11883935; SPIKE:18319725; SPIKE_LC:11883935; SPIKE_LC:18319725\nTP63      CDKN2A    inhibition\nTP63      CDKN2A    inhibition\nTFDP1     CDKN2A    inhibition\nCDKN2A    TFDP1     inhibition\nTFDP1     CDKN2A    inhibition\nCDKN2A    TFDP1     inhibition\nCDKN2A    BIRC5     inhibition\nCDKN2A    BIRC5     inhibition\nCDKN2A    CCND3     inhibition\nCDKN2A    VDR       inhibition\nCDKN2A    BCL2L1    inhibition   SPIKE:19049976; SPIKE_LC:19049976\nCDKN2A    CCND3     inhibition\nCDKN2A    VDR       inhibition\nCDKN2A    BCL2L1    inhibition   SPIKE:19049976; SPIKE_LC:19049976"
}

**Tool Output:**

Network reset.

**Tool Output:**

{
  "result": "Network reset."
}

**Tool Output:**

**Network created successfully!**

- **Initial genes:** TNF, TNFRSF1A, TRADD, TRAF2, RIPK1, FADD, CASP8, CFLAR, BCL2, BAX, MCL1, XIAP, BIRC2, BIRC3, IKBKB, NFKBIA, RELA, MAP3K7, MAPK8, JUN, FOS, PIK3CA, AKT1, PTEN, MTOR, CCND1, CDK4, E2F1, MYC, TP53, CDKN1A, CASP3, CASP9, APAF1
- **Total nodes:** 34
- **Total interactions:** 188

**Preview of interactions (first 100 rows):**

source    target    Effect
TNF       TNFRSF1A  stimulation
TNF       TRADD     inhibition
TNF       CASP8     stimulation
CFLAR     TNF       inhibition
TNF       IKBKB     stimulation
TNF       NFKBIA    inhibition
TNF       RELA      stimulation
TNF       MAPK8     stimulation
TNF       JUN       stimulation
FOS       TNF       stimulation
TNF       AKT1      stimulation
PTEN      TNF       inhibition
CCND1     TNF       inhibition
MYC       TNF       stimulation
TNF       CASP3     stimulation
TNFRSF1A  TRADD     stimulation
TNFRSF1A  TRAF2     stimulation
TNFRSF1A  RIPK1     stimulation
TNFRSF1A  FADD      stimulation
TNFRSF1A  CASP8     stimulation
TNFRSF1A  NFKBIA    inhibition
TNFRSF1A  RELA      stimulation
TNFRSF1A  CASP3     stimulation
TRADD     TRAF2     bimodal
TRADD     RIPK1     stimulation
TRADD     FADD      stimulation
TRADD     CASP8     stimulation
CFLAR     TRADD     inhibition
TRADD     BIRC2     stimulation
TRADD     IKBKB     stimulation
TRADD     RELA      stimulation
TRAF2     RIPK1     stimulation
TRAF2     CASP8     stimulation
TRAF2     BIRC2     stimulation
TRAF2     BIRC3     stimulation
TRAF2     IKBKB     stimulation
TRAF2     NFKBIA    stimulation
RELA      TRAF2     stimulation
TRAF2     RELA      stimulation
TRAF2     MAP3K7    stimulation
TRAF2     MAPK8     stimulation
TRAF2     TP53      stimulation
FADD      RIPK1     stimulation
CASP8     RIPK1     inhibition
CFLAR     RIPK1     inhibition
BIRC2     RIPK1     stimulation
BIRC3     RIPK1     stimulation
RIPK1     IKBKB     stimulation
RIPK1     RELA      stimulation
FADD      CASP8     stimulation
CFLAR     FADD      bimodal
BIRC2     FADD      inhibition
FADD      IKBKB     stimulation
TP53      FADD      stimulation
FADD      CASP3     stimulation
CFLAR     CASP8     inhibition
BCL2      CASP8     inhibition
BIRC2     CASP8     inhibition
BIRC3     CASP8     inhibition
CASP8     IKBKB     stimulation
RELA      CASP8     inhibition
E2F1      CASP8     stimulation
TP53      CASP8     stimulation
CASP8     CASP3     stimulation
BIRC2     CFLAR     inhibition
BIRC3     CFLAR     inhibition
MAPK8     CFLAR     inhibition
AKT1      CFLAR     inhibition
MYC       CFLAR     inhibition
TP53      CFLAR     stimulation
BCL2      BAX       inhibition
RELA      BCL2      stimulation
MAPK8     BCL2      bimodal
AKT1      BCL2      bimodal
MTOR      BCL2      stimulation
BCL2      CCND1     inhibition
E2F1      BCL2      bimodal
BCL2      MYC       stimulation
TP53      BCL2      inhibition
CASP3     BCL2      inhibition
BCL2      APAF1     inhibition
MCL1      BAX       inhibition
RELA      BAX       inhibition
MAPK8     BAX       stimulation
AKT1      BAX       inhibition
MYC       BAX       stimulation
TP53      BAX       stimulation
CASP3     BAX       stimulation
BAX       APAF1     stimulation
MAPK8     MCL1      bimodal
AKT1      MCL1      stimulation
E2F1      MCL1      inhibition
TP53      MCL1      bimodal
CASP3     MCL1      inhibition
RELA      XIAP      stimulation
XIAP      MAP3K7    stimulation
XIAP      MAPK8     stimulation
AKT1      XIAP      stimulation
XIAP      PTEN      stimulation
TP53      XIAP      stimulation

**Tool Output:**

{
  "result": "**Network created successfully!**\n\n- **Initial genes:** TNF, TNFRSF1A, TRADD, TRAF2, RIPK1, FADD, CASP8, CFLAR, BCL2, BAX, MCL1, XIAP, BIRC2, BIRC3, IKBKB, NFKBIA, RELA, MAP3K7, MAPK8, JUN, FOS, PIK3CA, AKT1, PTEN, MTOR, CCND1, CDK4, E2F1, MYC, TP53, CDKN1A, CASP3, CASP9, APAF1\n- **Total nodes:** 34\n- **Total interactions:** 188\n\n**Preview of interactions (first 100 rows):**\n\nsource    target    Effect\nTNF       TNFRSF1A  stimulation\nTNF       TRADD     inhibition\nTNF       CASP8     stimulation\nCFLAR     TNF       inhibition\nTNF       IKBKB     stimulation\nTNF       NFKBIA    inhibition\nTNF       RELA      stimulation\nTNF       MAPK8     stimulation\nTNF       JUN       stimulation\nFOS       TNF       stimulation\nTNF       AKT1      stimulation\nPTEN      TNF       inhibition\nCCND1     TNF       inhibition\nMYC       TNF       stimulation\nTNF       CASP3     stimulation\nTNFRSF1A  TRADD     stimulation\nTNFRSF1A  TRAF2     stimulation\nTNFRSF1A  RIPK1     stimulation\nTNFRSF1A  FADD      stimulation\nTNFRSF1A  CASP8     stimulation\nTNFRSF1A  NFKBIA    inhibition\nTNFRSF1A  RELA      stimulation\nTNFRSF1A  CASP3     stimulation\nTRADD     TRAF2     bimodal\nTRADD     RIPK1     stimulation\nTRADD     FADD      stimulation\nTRADD     CASP8     stimulation\nCFLAR     TRADD     inhibition\nTRADD     BIRC2     stimulation\nTRADD     IKBKB     stimulation\nTRADD     RELA      stimulation\nTRAF2     RIPK1     stimulation\nTRAF2     CASP8     stimulation\nTRAF2     BIRC2     stimulation\nTRAF2     BIRC3     stimulation\nTRAF2     IKBKB     stimulation\nTRAF2     NFKBIA    stimulation\nRELA      TRAF2     stimulation\nTRAF2     RELA      stimulation\nTRAF2     MAP3K7    stimulation\nTRAF2     MAPK8     stimulation\nTRAF2     TP53      stimulation\nFADD      RIPK1     stimulation\nCASP8     RIPK1     inhibition\nCFLAR     RIPK1     inhibition\nBIRC2     RIPK1     stimulation\nBIRC3     RIPK1     stimulation\nRIPK1     IKBKB     stimulation\nRIPK1     RELA      stimulation\nFADD      CASP8     stimulation\nCFLAR     FADD      bimodal\nBIRC2     FADD      inhibition\nFADD      IKBKB     stimulation\nTP53      FADD      stimulation\nFADD      CASP3     stimulation\nCFLAR     CASP8     inhibition\nBCL2      CASP8     inhibition\nBIRC2     CASP8     inhibition\nBIRC3     CASP8     inhibition\nCASP8     IKBKB     stimulation\nRELA      CASP8     inhibition\nE2F1      CASP8     stimulation\nTP53      CASP8     stimulation\nCASP8     CASP3     stimulation\nBIRC2     CFLAR     inhibition\nBIRC3     CFLAR     inhibition\nMAPK8     CFLAR     inhibition\nAKT1      CFLAR     inhibition\nMYC       CFLAR     inhibition\nTP53      CFLAR     stimulation\nBCL2      BAX       inhibition\nRELA      BCL2      stimulation\nMAPK8     BCL2      bimodal\nAKT1      BCL2      bimodal\nMTOR      BCL2      stimulation\nBCL2      CCND1     inhibition\nE2F1      BCL2      bimodal\nBCL2      MYC       stimulation\nTP53      BCL2      inhibition\nCASP3     BCL2      inhibition\nBCL2      APAF1     inhibition\nMCL1      BAX       inhibition\nRELA      BAX       inhibition\nMAPK8     BAX       stimulation\nAKT1      BAX       inhibition\nMYC       BAX       stimulation\nTP53      BAX       stimulation\nCASP3     BAX       stimulation\nBAX       APAF1     stimulation\nMAPK8     MCL1      bimodal\nAKT1      MCL1      stimulation\nE2F1      MCL1      inhibition\nTP53      MCL1      bimodal\nCASP3     MCL1      inhibition\nRELA      XIAP      stimulation\nXIAP      MAP3K7    stimulation\nXIAP      MAPK8     stimulation\nAKT1      XIAP      stimulation\nXIAP      PTEN      stimulation\nTP53      XIAP      stimulation"
}

**Tool Output:**

Removed 18 bimodal interactions from the network.

**Tool Output:**

{
  "result": "Removed 18 bimodal interactions from the network."
}

**Tool Output:**

All nodes are connected.

**Tool Output:**

{
  "result": "All nodes are connected."
}

**Tool Output:**

**Exported to** `Network_1.bnet`

_Preview (first 100 lines) of the BNET file:_

gene      expression
TNF       (FOS | MYC) & !(CFLAR | PTEN | CCND1)
TNFRSF1A  (TNF)
TRADD     (TNFRSF1A) & !(TNF | CFLAR)
TRAF2     (TNFRSF1A | RELA)
RIPK1     (TNFRSF1A | TRADD | TRAF2 | FADD | BIRC2 | BIRC3) & !(CASP8 | CFLAR)
FADD      (TNFRSF1A | TRADD | TP53) & !(BIRC2)
CASP8     (TNF | TNFRSF1A | TRADD | TRAF2 | FADD | E2F1 | TP53) & !(CFLAR | BCL2 | BIRC2 | BIRC3 | RELA)
CFLAR     (TP53) & !(BIRC2 | BIRC3 | MAPK8 | AKT1 | MYC)
BCL2      (RELA | MTOR) & !(TP53 | CASP3)
BAX       (MAPK8 | MYC | TP53 | CASP3) & !(BCL2 | MCL1 | RELA | AKT1)
MCL1      (AKT1) & !(E2F1 | CASP3)
XIAP      (RELA | AKT1 | TP53)
BIRC2     (TRADD | TRAF2 | BIRC3 | RELA)
BIRC3     (TRAF2 | NFKBIA | RELA) & !(TP53)
IKBKB     (TNF | TRADD | TRAF2 | RIPK1 | FADD | CASP8 | MAP3K7 | AKT1) & !(CASP3)
NFKBIA    (TRAF2 | CASP3) & !(TNF | TNFRSF1A | RELA | JUN)
RELA      (TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | IKBKB | PIK3CA | E2F1) & !(CASP3)
MAP3K7    (TRAF2 | XIAP)
MAPK8     (TNF | TRAF2 | XIAP | MAP3K7 | PIK3CA)
JUN       (TNF | RELA | MAPK8 | FOS | AKT1)
FOS       (RELA | MAPK8 | AKT1)
PIK3CA    !(PTEN)
AKT1      (TNF | MAPK8 | MTOR) & !(CASP3)
PTEN      (XIAP | TP53 | CASP3) & !(RELA | JUN | FOS | AKT1)
MTOR      (IKBKB | PIK3CA)
CCND1     (RELA | JUN | FOS | PIK3CA | MYC) & !(BCL2 | CDKN1A)
CDK4      (JUN | FOS | CCND1 | MYC) & !(CDKN1A)
E2F1      (PTEN) & !(CDKN1A)
MYC       (BCL2 | MAPK8 | PIK3CA | E2F1) & !(RELA | JUN)
TP53      (TRAF2 | XIAP | MAPK8 | E2F1) & !(JUN | FOS)
CDKN1A    (MAPK8 | JUN | CASP3) & !(MYC)
CASP3     (TNF | TNFRSF1A | FADD | CASP8 | E2F1) & !(XIAP | BIRC2 | BIRC3)
CASP9     (E2F1 | APAF1) & !(BIRC2 | BIRC3)
APAF1     (BAX | E2F1 | TP53) & !(BCL2 | XIAP | BIRC2 | BIRC3 | AKT1)

**Tool Output:**

{
  "result": "**Exported to** `Network_1.bnet`\n\n_Preview (first 100 lines) of the BNET file:_\n\ngene      expression\nTNF       (FOS | MYC) & !(CFLAR | PTEN | CCND1)\nTNFRSF1A  (TNF)\nTRADD     (TNFRSF1A) & !(TNF | CFLAR)\nTRAF2     (TNFRSF1A | RELA)\nRIPK1     (TNFRSF1A | TRADD | TRAF2 | FADD | BIRC2 | BIRC3) & !(CASP8 | CFLAR)\nFADD      (TNFRSF1A | TRADD | TP53) & !(BIRC2)\nCASP8     (TNF | TNFRSF1A | TRADD | TRAF2 | FADD | E2F1 | TP53) & !(CFLAR | BCL2 | BIRC2 | BIRC3 | RELA)\nCFLAR     (TP53) & !(BIRC2 | BIRC3 | MAPK8 | AKT1 | MYC)\nBCL2      (RELA | MTOR) & !(TP53 | CASP3)\nBAX       (MAPK8 | MYC | TP53 | CASP3) & !(BCL2 | MCL1 | RELA | AKT1)\nMCL1      (AKT1) & !(E2F1 | CASP3)\nXIAP      (RELA | AKT1 | TP53)\nBIRC2     (TRADD | TRAF2 | BIRC3 | RELA)\nBIRC3     (TRAF2 | NFKBIA | RELA) & !(TP53)\nIKBKB     (TNF | TRADD | TRAF2 | RIPK1 | FADD | CASP8 | MAP3K7 | AKT1) & !(CASP3)\nNFKBIA    (TRAF2 | CASP3) & !(TNF | TNFRSF1A | RELA | JUN)\nRELA      (TNF | TNFRSF1A | TRADD | TRAF2 | RIPK1 | IKBKB | PIK3CA | E2F1) & !(CASP3)\nMAP3K7    (TRAF2 | XIAP)\nMAPK8     (TNF | TRAF2 | XIAP | MAP3K7 | PIK3CA)\nJUN       (TNF | RELA | MAPK8 | FOS | AKT1)\nFOS       (RELA | MAPK8 | AKT1)\nPIK3CA    !(PTEN)\nAKT1      (TNF | MAPK8 | MTOR) & !(CASP3)\nPTEN      (XIAP | TP53 | CASP3) & !(RELA | JUN | FOS | AKT1)\nMTOR      (IKBKB | PIK3CA)\nCCND1     (RELA | JUN | FOS | PIK3CA | MYC) & !(BCL2 | CDKN1A)\nCDK4      (JUN | FOS | CCND1 | MYC) & !(CDKN1A)\nE2F1      (PTEN) & !(CDKN1A)\nMYC       (BCL2 | MAPK8 | PIK3CA | E2F1) & !(RELA | JUN)\nTP53      (TRAF2 | XIAP | MAPK8 | E2F1) & !(JUN | FOS)\nCDKN1A    (MAPK8 | JUN | CASP3) & !(MYC)\nCASP3     (TNF | TNFRSF1A | FADD | CASP8 | E2F1) & !(XIAP | BIRC2 | BIRC3)\nCASP9     (E2F1 | APAF1) & !(BIRC2 | BIRC3)\nAPAF1     (BAX | E2F1 | TP53) & !(BCL2 | XIAP | BIRC2 | BIRC3 | AKT1)"
}

**Tool Output:**

MaBoSS bnd and cfg files created successfully. Output files: output.bnd, output.cfg

**Tool Output:**

{
  "result": "MaBoSS bnd and cfg files created successfully. Output files: output.bnd, output.cfg"
}

**Tool Output:**

MaBoSS simulation created successfully with the following parameters:
time_tick: 0.5
max_time: 1000.0
sample_count: 10000.0
discrete_time: 0.0
use_physrandgen: 0.0
seed_pseudorandom: 0.0
display_traj: 0.0
statdist_traj_count: 0.0
statdist_cluster_threshold: 1.0
thread_count: 1.0
statdist_similarity_cache_max_size: 20000.0

**Tool Output:**

{
  "result": "MaBoSS simulation created successfully with the following parameters:\ntime_tick: 0.5\nmax_time: 1000.0\nsample_count: 10000.0\ndiscrete_time: 0.0\nuse_physrandgen: 0.0\nseed_pseudorandom: 0.0\ndisplay_traj: 0.0\nstatdist_traj_count: 0.0\nstatdist_cluster_threshold: 1.0\nthread_count: 1.0\nstatdist_similarity_cache_max_size: 20000.0"
}

**Tool Output:**

MaBoSS output nodes set successfully: ['E2F1', 'CASP3']

**Tool Output:**

{
  "result": "MaBoSS output nodes set successfully: ['E2F1', 'CASP3']"
}

**Tool Output:**

MaBoSS simulation run completed successfully.

**Tool Output:**

{
  "result": "MaBoSS simulation run completed successfully."
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory**

_Below is the probability trajectory of each state over time:_

<nil>
      1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory**\n\n_Below is the probability trajectory of each state over time:_\n\n  `<nil>`\n      1"
}

**Tool Output:**

Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.5, 1: 0.5}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})

**Tool Output:**

{
  "result": "Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.5, 1: 0.5}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})"
}

**Tool Output:**

MaBoSS simulation run completed successfully.

**Tool Output:**

{
  "result": "MaBoSS simulation run completed successfully."
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory**

_Below is the probability trajectory of each state over time:_

<nil>
      1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory**\n\n_Below is the probability trajectory of each state over time:_\n\n  `<nil>`\n      1"
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory (with Mutation)**

_Below is the probability trajectory of each state over time after mutation: {'TNF': 'ON'}_

<nil>
      1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory (with Mutation)**\n\n_Below is the probability trajectory of each state over time after mutation: {'TNF': 'ON'}_\n\n  `<nil>`\n      1"
}

**Tool Output:**

Nodes in the MaBoSS network: FOS, MYC, CFLAR, PTEN, CCND1, TNF, TNFRSF1A, TRADD, RELA, TRAF2, FADD, BIRC2, BIRC3, CASP8, RIPK1, TP53, E2F1, BCL2, MAPK8, AKT1, MTOR, CASP3, MCL1, BAX, XIAP, NFKBIA, MAP3K7, IKBKB, JUN, PIK3CA, CDKN1A, CDK4, APAF1, CASP9

**Tool Output:**

{
  "result": "Nodes in the MaBoSS network: FOS, MYC, CFLAR, PTEN, CCND1, TNF, TNFRSF1A, TRADD, RELA, TRAF2, FADD, BIRC2, BIRC3, CASP8, RIPK1, TP53, E2F1, BCL2, MAPK8, AKT1, MTOR, CASP3, MCL1, BAX, XIAP, NFKBIA, MAP3K7, IKBKB, JUN, PIK3CA, CDKN1A, CDK4, APAF1, CASP9"
}

**Tool Output:**

Initial state of the MaBoSS simulation: {'FOS': [0, 1], 'MYC': [0, 1], 'CFLAR': [0, 1], 'PTEN': [0, 1], 'CCND1': [0, 1], 'TNF': 1, 'TNFRSF1A': [0, 1], 'TRADD': [0, 1], 'RELA': [0, 1], 'TRAF2': [0, 1], 'FADD': [0, 1], 'BIRC2': [0, 1], 'BIRC3': [0, 1], 'CASP8': [0, 1], 'RIPK1': [0, 1], 'TP53': [0, 1], 'E2F1': [0, 1], 'BCL2': [0, 1], 'MAPK8': [0, 1], 'AKT1': [0, 1], 'MTOR': [0, 1], 'CASP3': [0, 1], 'MCL1': [0, 1], 'BAX': [0, 1], 'XIAP': [0, 1], 'NFKBIA': [0, 1], 'MAP3K7': [0, 1], 'IKBKB': [0, 1], 'JUN': [0, 1], 'PIK3CA': [0, 1], 'CDKN1A': [0, 1], 'CDK4': [0, 1], 'APAF1': [0, 1], 'CASP9': [0, 1]}

**Tool Output:**

{
  "result": "Initial state of the MaBoSS simulation: {'FOS': [0, 1], 'MYC': [0, 1], 'CFLAR': [0, 1], 'PTEN': [0, 1], 'CCND1': [0, 1], 'TNF': 1, 'TNFRSF1A': [0, 1], 'TRADD': [0, 1], 'RELA': [0, 1], 'TRAF2': [0, 1], 'FADD': [0, 1], 'BIRC2': [0, 1], 'BIRC3': [0, 1], 'CASP8': [0, 1], 'RIPK1': [0, 1], 'TP53': [0, 1], 'E2F1': [0, 1], 'BCL2': [0, 1], 'MAPK8': [0, 1], 'AKT1': [0, 1], 'MTOR': [0, 1], 'CASP3': [0, 1], 'MCL1': [0, 1], 'BAX': [0, 1], 'XIAP': [0, 1], 'NFKBIA': [0, 1], 'MAP3K7': [0, 1], 'IKBKB': [0, 1], 'JUN': [0, 1], 'PIK3CA': [0, 1], 'CDKN1A': [0, 1], 'CDK4': [0, 1], 'APAF1': [0, 1], 'CASP9': [0, 1]}"
}

**Tool Output:**

Logical rules of the MaBoSS simulation:
{'RELA': '(!RELA & ((TNF | (TNFRSF1A | (TRADD | (TRAF2 | (RIPK1 | (IKBKB | (PIK3CA | E2F1))))))) & !(CASP3))) | (RELA & ((TNF | (TNFRSF1A | (TRADD | (TRAF2 | (RIPK1 | (IKBKB | (PIK3CA | E2F1))))))) & !(CASP3)))', 'MAPK8': '(!MAPK8 & (TNF | (TRAF2 | (XIAP | (MAP3K7 | PIK3CA))))) | (MAPK8 & (TNF | (TRAF2 | (XIAP | (MAP3K7 | PIK3CA)))))', 'AKT1': '(!AKT1 & ((TNF | (MAPK8 | MTOR)) & !(CASP3))) | (AKT1 & ((TNF | (MAPK8 | MTOR)) & !(CASP3)))', 'FOS': '(!FOS & (RELA | (MAPK8 | AKT1))) | (FOS & (RELA | (MAPK8 | AKT1)))', 'BCL2': '(!BCL2 & ((RELA | MTOR) & !(TP53 | CASP3))) | (BCL2 & ((RELA | MTOR) & !(TP53 | CASP3)))', 'PIK3CA': '(!PIK3CA & !(PTEN)) | (PIK3CA & !(PTEN))', 'E2F1': '(!E2F1 & ((PTEN) & !(CDKN1A))) | (E2F1 & ((PTEN) & !(CDKN1A)))', 'JUN': '(!JUN & (TNF | (RELA | (MAPK8 | (FOS | AKT1))))) | (JUN & (TNF | (RELA | (MAPK8 | (FOS | AKT1)))))', 'MYC': '(!MYC & ((BCL2 | (MAPK8 | (PIK3CA | E2F1))) & !(RELA | JUN))) | (MYC & ((BCL2 | (MAPK8 | (PIK3CA | E2F1))) & !(RELA | JUN)))', 'TP53': '(!TP53 & ((TRAF2 | (XIAP | (MAPK8 | E2F1))) & !(JUN | FOS))) | (TP53 & ((TRAF2 | (XIAP | (MAPK8 | E2F1))) & !(JUN | FOS)))', 'BIRC2': '(!BIRC2 & (TRADD | (TRAF2 | (BIRC3 | RELA)))) | (BIRC2 & (TRADD | (TRAF2 | (BIRC3 | RELA))))', 'BIRC3': '(!BIRC3 & ((TRAF2 | (NFKBIA | RELA)) & !(TP53))) | (BIRC3 & ((TRAF2 | (NFKBIA | RELA)) & !(TP53)))', 'CFLAR': '(!CFLAR & ((TP53) & !(BIRC2 | (BIRC3 | (MAPK8 | (AKT1 | MYC)))))) | (CFLAR & ((TP53) & !(BIRC2 | (BIRC3 | (MAPK8 | (AKT1 | MYC))))))', 'XIAP': '(!XIAP & (RELA | (AKT1 | TP53))) | (XIAP & (RELA | (AKT1 | TP53)))', 'CASP3': '(!CASP3 & ((TNF | (TNFRSF1A | (FADD | (CASP8 | E2F1)))) & !(XIAP | (BIRC2 | BIRC3)))) | (CASP3 & ((TNF | (TNFRSF1A | (FADD | (CASP8 | E2F1)))) & !(XIAP | (BIRC2 | BIRC3))))', 'PTEN': '(!PTEN & ((XIAP | (TP53 | CASP3)) & !(RELA | (JUN | (FOS | AKT1))))) | (PTEN & ((XIAP | (TP53 | CASP3)) & !(RELA | (JUN | (FOS | AKT1)))))', 'CDKN1A': '(!CDKN1A & ((MAPK8 | (JUN | CASP3)) & !(MYC))) | (CDKN1A & ((MAPK8 | (JUN | CASP3)) & !(MYC)))', 'CCND1': '(!CCND1 & ((RELA | (JUN | (FOS | (PIK3CA | MYC)))) & !(BCL2 | CDKN1A))) | (CCND1 & ((RELA | (JUN | (FOS | (PIK3CA | MYC)))) & !(BCL2 | CDKN1A)))', 'TNF': '(!TNF & ((FOS | MYC) & !(CFLAR | (PTEN | CCND1)))) | (TNF & ((FOS | MYC) & !(CFLAR | (PTEN | CCND1))))', 'TNFRSF1A': '(!TNFRSF1A & (TNF)) | (TNFRSF1A & (TNF))', 'TRADD': '(!TRADD & ((TNFRSF1A) & !(TNF | CFLAR))) | (TRADD & ((TNFRSF1A) & !(TNF | CFLAR)))', 'TRAF2': '(!TRAF2 & (TNFRSF1A | RELA)) | (TRAF2 & (TNFRSF1A | RELA))', 'RIPK1': '(!RIPK1 & ((TNFRSF1A | (TRADD | (TRAF2 | (FADD | (BIRC2 | BIRC3))))) & !(CASP8 | CFLAR))) | (RIPK1 & ((TNFRSF1A | (TRADD | (TRAF2 | (FADD | (BIRC2 | BIRC3))))) & !(CASP8 | CFLAR)))', 'IKBKB': '(!IKBKB & ((TNF | (TRADD | (TRAF2 | (RIPK1 | (FADD | (CASP8 | (MAP3K7 | AKT1))))))) & !(CASP3))) | (IKBKB & ((TNF | (TRADD | (TRAF2 | (RIPK1 | (FADD | (CASP8 | (MAP3K7 | AKT1))))))) & !(CASP3)))', 'FADD': '(!FADD & ((TNFRSF1A | (TRADD | TP53)) & !(BIRC2))) | (FADD & ((TNFRSF1A | (TRADD | TP53)) & !(BIRC2)))', 'NFKBIA': '(!NFKBIA & ((TRAF2 | CASP3) & !(TNF | (TNFRSF1A | (RELA | JUN))))) | (NFKBIA & ((TRAF2 | CASP3) & !(TNF | (TNFRSF1A | (RELA | JUN)))))', 'CASP8': '(!CASP8 & ((TNF | (TNFRSF1A | (TRADD | (TRAF2 | (FADD | (E2F1 | TP53)))))) & !(CFLAR | (BCL2 | (BIRC2 | (BIRC3 | RELA)))))) | (CASP8 & ((TNF | (TNFRSF1A | (TRADD | (TRAF2 | (FADD | (E2F1 | TP53)))))) & !(CFLAR | (BCL2 | (BIRC2 | (BIRC3 | RELA))))))', 'MTOR': '(!MTOR & (IKBKB | PIK3CA)) | (MTOR & (IKBKB | PIK3CA))', 'MAP3K7': '(!MAP3K7 & (TRAF2 | XIAP)) | (MAP3K7 & (TRAF2 | XIAP))', 'MCL1': '(!MCL1 & ((AKT1) & !(E2F1 | CASP3))) | (MCL1 & ((AKT1) & !(E2F1 | CASP3)))', 'BAX': '(!BAX & ((MAPK8 | (MYC | (TP53 | CASP3))) & !(BCL2 | (MCL1 | (RELA | AKT1))))) | (BAX & ((MAPK8 | (MYC | (TP53 | CASP3))) & !(BCL2 | (MCL1 | (RELA | AKT1)))))', 'CDK4': '(!CDK4 & ((JUN | (FOS | (CCND1 | MYC))) & !(CDKN1A))) | (CDK4 & ((JUN | (FOS | (CCND1 | MYC))) & !(CDKN1A)))', 'APAF1': '(!APAF1 & ((BAX | (E2F1 | TP53)) & !(BCL2 | (XIAP | (BIRC2 | (BIRC3 | AKT1)))))) | (APAF1 & ((BAX | (E2F1 | TP53)) & !(BCL2 | (XIAP | (BIRC2 | (BIRC3 | AKT1))))))', 'CASP9': '(!CASP9 & ((E2F1 | APAF1) & !(BIRC2 | BIRC3))) | (CASP9 & ((E2F1 | APAF1) & !(BIRC2 | BIRC3)))'}

**Tool Output:**

{
  "result": "Logical rules of the MaBoSS simulation:\n{'RELA': '(!RELA & ((TNF | (TNFRSF1A | (TRADD | (TRAF2 | (RIPK1 | (IKBKB | (PIK3CA | E2F1))))))) & !(CASP3))) | (RELA & ((TNF | (TNFRSF1A | (TRADD | (TRAF2 | (RIPK1 | (IKBKB | (PIK3CA | E2F1))))))) & !(CASP3)))', 'MAPK8': '(!MAPK8 & (TNF | (TRAF2 | (XIAP | (MAP3K7 | PIK3CA))))) | (MAPK8 & (TNF | (TRAF2 | (XIAP | (MAP3K7 | PIK3CA)))))', 'AKT1': '(!AKT1 & ((TNF | (MAPK8 | MTOR)) & !(CASP3))) | (AKT1 & ((TNF | (MAPK8 | MTOR)) & !(CASP3)))', 'FOS': '(!FOS & (RELA | (MAPK8 | AKT1))) | (FOS & (RELA | (MAPK8 | AKT1)))', 'BCL2': '(!BCL2 & ((RELA | MTOR) & !(TP53 | CASP3))) | (BCL2 & ((RELA | MTOR) & !(TP53 | CASP3)))', 'PIK3CA': '(!PIK3CA & !(PTEN)) | (PIK3CA & !(PTEN))', 'E2F1': '(!E2F1 & ((PTEN) & !(CDKN1A))) | (E2F1 & ((PTEN) & !(CDKN1A)))', 'JUN': '(!JUN & (TNF | (RELA | (MAPK8 | (FOS | AKT1))))) | (JUN & (TNF | (RELA | (MAPK8 | (FOS | AKT1)))))', 'MYC': '(!MYC & ((BCL2 | (MAPK8 | (PIK3CA | E2F1))) & !(RELA | JUN))) | (MYC & ((BCL2 | (MAPK8 | (PIK3CA | E2F1))) & !(RELA | JUN)))', 'TP53': '(!TP53 & ((TRAF2 | (XIAP | (MAPK8 | E2F1))) & !(JUN | FOS))) | (TP53 & ((TRAF2 | (XIAP | (MAPK8 | E2F1))) & !(JUN | FOS)))', 'BIRC2': '(!BIRC2 & (TRADD | (TRAF2 | (BIRC3 | RELA)))) | (BIRC2 & (TRADD | (TRAF2 | (BIRC3 | RELA))))', 'BIRC3': '(!BIRC3 & ((TRAF2 | (NFKBIA | RELA)) & !(TP53))) | (BIRC3 & ((TRAF2 | (NFKBIA | RELA)) & !(TP53)))', 'CFLAR': '(!CFLAR & ((TP53) & !(BIRC2 | (BIRC3 | (MAPK8 | (AKT1 | MYC)))))) | (CFLAR & ((TP53) & !(BIRC2 | (BIRC3 | (MAPK8 | (AKT1 | MYC))))))', 'XIAP': '(!XIAP & (RELA | (AKT1 | TP53))) | (XIAP & (RELA | (AKT1 | TP53)))', 'CASP3': '(!CASP3 & ((TNF | (TNFRSF1A | (FADD | (CASP8 | E2F1)))) & !(XIAP | (BIRC2 | BIRC3)))) | (CASP3 & ((TNF | (TNFRSF1A | (FADD | (CASP8 | E2F1)))) & !(XIAP | (BIRC2 | BIRC3))))', 'PTEN': '(!PTEN & ((XIAP | (TP53 | CASP3)) & !(RELA | (JUN | (FOS | AKT1))))) | (PTEN & ((XIAP | (TP53 | CASP3)) & !(RELA | (JUN | (FOS | AKT1)))))', 'CDKN1A': '(!CDKN1A & ((MAPK8 | (JUN | CASP3)) & !(MYC))) | (CDKN1A & ((MAPK8 | (JUN | CASP3)) & !(MYC)))', 'CCND1': '(!CCND1 & ((RELA | (JUN | (FOS | (PIK3CA | MYC)))) & !(BCL2 | CDKN1A))) | (CCND1 & ((RELA | (JUN | (FOS | (PIK3CA | MYC)))) & !(BCL2 | CDKN1A)))', 'TNF': '(!TNF & ((FOS | MYC) & !(CFLAR | (PTEN | CCND1)))) | (TNF & ((FOS | MYC) & !(CFLAR | (PTEN | CCND1))))', 'TNFRSF1A': '(!TNFRSF1A & (TNF)) | (TNFRSF1A & (TNF))', 'TRADD': '(!TRADD & ((TNFRSF1A) & !(TNF | CFLAR))) | (TRADD & ((TNFRSF1A) & !(TNF | CFLAR)))', 'TRAF2': '(!TRAF2 & (TNFRSF1A | RELA)) | (TRAF2 & (TNFRSF1A | RELA))', 'RIPK1': '(!RIPK1 & ((TNFRSF1A | (TRADD | (TRAF2 | (FADD | (BIRC2 | BIRC3))))) & !(CASP8 | CFLAR))) | (RIPK1 & ((TNFRSF1A | (TRADD | (TRAF2 | (FADD | (BIRC2 | BIRC3))))) & !(CASP8 | CFLAR)))', 'IKBKB': '(!IKBKB & ((TNF | (TRADD | (TRAF2 | (RIPK1 | (FADD | (CASP8 | (MAP3K7 | AKT1))))))) & !(CASP3))) | (IKBKB & ((TNF | (TRADD | (TRAF2 | (RIPK1 | (FADD | (CASP8 | (MAP3K7 | AKT1))))))) & !(CASP3)))', 'FADD': '(!FADD & ((TNFRSF1A | (TRADD | TP53)) & !(BIRC2))) | (FADD & ((TNFRSF1A | (TRADD | TP53)) & !(BIRC2)))', 'NFKBIA': '(!NFKBIA & ((TRAF2 | CASP3) & !(TNF | (TNFRSF1A | (RELA | JUN))))) | (NFKBIA & ((TRAF2 | CASP3) & !(TNF | (TNFRSF1A | (RELA | JUN)))))', 'CASP8': '(!CASP8 & ((TNF | (TNFRSF1A | (TRADD | (TRAF2 | (FADD | (E2F1 | TP53)))))) & !(CFLAR | (BCL2 | (BIRC2 | (BIRC3 | RELA)))))) | (CASP8 & ((TNF | (TNFRSF1A | (TRADD | (TRAF2 | (FADD | (E2F1 | TP53)))))) & !(CFLAR | (BCL2 | (BIRC2 | (BIRC3 | RELA))))))', 'MTOR': '(!MTOR & (IKBKB | PIK3CA)) | (MTOR & (IKBKB | PIK3CA))', 'MAP3K7': '(!MAP3K7 & (TRAF2 | XIAP)) | (MAP3K7 & (TRAF2 | XIAP))', 'MCL1': '(!MCL1 & ((AKT1) & !(E2F1 | CASP3))) | (MCL1 & ((AKT1) & !(E2F1 | CASP3)))', 'BAX': '(!BAX & ((MAPK8 | (MYC | (TP53 | CASP3))) & !(BCL2 | (MCL1 | (RELA | AKT1))))) | (BAX & ((MAPK8 | (MYC | (TP53 | CASP3))) & !(BCL2 | (MCL1 | (RELA | AKT1)))))', 'CDK4': '(!CDK4 & ((JUN | (FOS | (CCND1 | MYC))) & !(CDKN1A))) | (CDK4 & ((JUN | (FOS | (CCND1 | MYC))) & !(CDKN1A)))', 'APAF1': '(!APAF1 & ((BAX | (E2F1 | TP53)) & !(BCL2 | (XIAP | (BIRC2 | (BIRC3 | AKT1)))))) | (APAF1 & ((BAX | (E2F1 | TP53)) & !(BCL2 | (XIAP | (BIRC2 | (BIRC3 | AKT1))))))', 'CASP9': '(!CASP9 & ((E2F1 | APAF1) & !(BIRC2 | BIRC3))) | (CASP9 & ((E2F1 | APAF1) & !(BIRC2 | BIRC3)))'}"
}

**Tool Output:**

MaBoSS parameters updated successfully.

**Tool Output:**

{
  "result": "MaBoSS parameters updated successfully."
}

**Tool Output:**

MaBoSS simulation run completed successfully.

**Tool Output:**

{
  "result": "MaBoSS simulation run completed successfully."
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory**

_Below is the probability trajectory of each state over time:_

<nil>
      1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory**\n\n_Below is the probability trajectory of each state over time:_\n\n  `<nil>`\n      1"
}

**Tool Output:**

MaBoSS parameters updated successfully.

**Tool Output:**

{
  "result": "MaBoSS parameters updated successfully."
}

**Tool Output:**

MaBoSS simulation run completed successfully.

**Tool Output:**

{
  "result": "MaBoSS simulation run completed successfully."
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory**

_Below is the probability trajectory of each state over time:_

<nil>
      1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory**\n\n_Below is the probability trajectory of each state over time:_\n\n  `<nil>`\n      1"
}

**Tool Output:**

Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 1.0, 1: 0.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.5, 1: 0.5}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})

**Tool Output:**

{
  "result": "Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 1.0, 1: 0.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.5, 1: 0.5}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})"
}

**Tool Output:**

MaBoSS simulation run completed successfully.

**Tool Output:**

{
  "result": "MaBoSS simulation run completed successfully."
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory**

_Below is the probability trajectory of each state over time:_

<nil>
      1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory**\n\n_Below is the probability trajectory of each state over time:_\n\n  `<nil>`\n      1"
}

**Tool Output:**

Network trajectory plot saved: network_trajectory.png
You can open it with your image viewer.

**Tool Output:**

{
  "result": "Network trajectory plot saved: network_trajectory.png\nYou can open it with your image viewer."
}

**Tool Output:**

MaBoSS output nodes set successfully: ['TNF', 'TNFRSF1A', 'RELA', 'E2F1', 'CASP3']

**Tool Output:**

{
  "result": "MaBoSS output nodes set successfully: ['TNF', 'TNFRSF1A', 'RELA', 'E2F1', 'CASP3']"
}

**Tool Output:**

MaBoSS parameters updated successfully.

**Tool Output:**

{
  "result": "MaBoSS parameters updated successfully."
}

**Tool Output:**

Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 1.0, 1: 0.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.5, 1: 0.5}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})

**Tool Output:**

{
  "result": "Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 1.0, 1: 0.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.5, 1: 0.5}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})"
}

**Tool Output:**

MaBoSS simulation run completed successfully.

**Tool Output:**

{
  "result": "MaBoSS simulation run completed successfully."
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory**

_Below is the probability trajectory of each state over time:_

  RELA -- TNF -- TNFRSF1A
                        1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory**\n\n_Below is the probability trajectory of each state over time:_\n\n  RELA -- TNF -- TNFRSF1A\n                        1"
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory (with Mutation)**

_Below is the probability trajectory of each state over time after mutation: {'XIAP': 'OFF'}_

  E2F1 -- CASP3    RELA -- TNF -- TNFRSF1A
        0.00564                    0.99436

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory (with Mutation)**\n\n_Below is the probability trajectory of each state over time after mutation: {'XIAP': 'OFF'}_\n\n  E2F1 -- CASP3    RELA -- TNF -- TNFRSF1A\n        0.00564                    0.99436"
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory (with Mutation)**

_Below is the probability trajectory of each state over time after mutation: {'BCL2': 'OFF'}_

  RELA -- TNF -- TNFRSF1A
                        1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory (with Mutation)**\n\n_Below is the probability trajectory of each state over time after mutation: {'BCL2': 'OFF'}_\n\n  RELA -- TNF -- TNFRSF1A\n                        1"
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory (with Mutation)**

_Below is the probability trajectory of each state over time after mutation: {'CASP8': 'ON'}_

  RELA -- TNF -- TNFRSF1A
                        1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory (with Mutation)**\n\n_Below is the probability trajectory of each state over time after mutation: {'CASP8': 'ON'}_\n\n  RELA -- TNF -- TNFRSF1A\n                        1"
}

**User Request:**

@agent Continue: "Continue to iterate?"

**Tool Output:**

MaBoSS parameters updated successfully.

**Tool Output:**

{
  "result": "MaBoSS parameters updated successfully."
}

**Tool Output:**

Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.5, 1: 0.5}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})

**Tool Output:**

{
  "result": "Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.5, 1: 0.5}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})"
}

**Tool Output:**

Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.1, 1: 0.9}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})

**Tool Output:**

{
  "result": "Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.1, 1: 0.9}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.5, 1: 0.5}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})"
}

**Tool Output:**

Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.1, 1: 0.9}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.1, 1: 0.9}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})

**Tool Output:**

{
  "result": "Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.1, 1: 0.9}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.5, 1: 0.5}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.1, 1: 0.9}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})"
}

**Tool Output:**

Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.1, 1: 0.9}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.1, 1: 0.9}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.1, 1: 0.9}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})

**Tool Output:**

{
  "result": "Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.5, 1: 0.5}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.1, 1: 0.9}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.1, 1: 0.9}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.1, 1: 0.9}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})"
}

**Tool Output:**

Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.1, 1: 0.9}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.1, 1: 0.9}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.1, 1: 0.9}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.1, 1: 0.9}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})

**Tool Output:**

{
  "result": "Initial state set for MaBoSS simulation: OrderedDict({'FOS': {0: 0.5, 1: 0.5}, 'MYC': {0: 0.5, 1: 0.5}, 'CFLAR': {0: 0.1, 1: 0.9}, 'PTEN': {0: 0.5, 1: 0.5}, 'CCND1': {0: 0.5, 1: 0.5}, 'TNF': {0: 0.0, 1: 1.0}, 'TNFRSF1A': {0: 0.5, 1: 0.5}, 'TRADD': {0: 0.5, 1: 0.5}, 'RELA': {0: 0.5, 1: 0.5}, 'TRAF2': {0: 0.5, 1: 0.5}, 'FADD': {0: 0.5, 1: 0.5}, 'BIRC2': {0: 0.5, 1: 0.5}, 'BIRC3': {0: 0.5, 1: 0.5}, 'CASP8': {0: 0.5, 1: 0.5}, 'RIPK1': {0: 0.5, 1: 0.5}, 'TP53': {0: 0.5, 1: 0.5}, 'E2F1': {0: 0.5, 1: 0.5}, 'BCL2': {0: 0.1, 1: 0.9}, 'MAPK8': {0: 0.5, 1: 0.5}, 'AKT1': {0: 0.5, 1: 0.5}, 'MTOR': {0: 0.5, 1: 0.5}, 'CASP3': {0: 0.5, 1: 0.5}, 'MCL1': {0: 0.1, 1: 0.9}, 'BAX': {0: 0.5, 1: 0.5}, 'XIAP': {0: 0.1, 1: 0.9}, 'NFKBIA': {0: 0.5, 1: 0.5}, 'MAP3K7': {0: 0.5, 1: 0.5}, 'IKBKB': {0: 0.5, 1: 0.5}, 'JUN': {0: 0.5, 1: 0.5}, 'PIK3CA': {0: 0.5, 1: 0.5}, 'CDKN1A': {0: 0.5, 1: 0.5}, 'CDK4': {0: 0.5, 1: 0.5}, 'APAF1': {0: 0.5, 1: 0.5}, 'CASP9': {0: 0.5, 1: 0.5}})"
}

**Tool Output:**

MaBoSS simulation run completed successfully.

**Tool Output:**

{
  "result": "MaBoSS simulation run completed successfully."
}

**Tool Output:**

**MaBoSS Simulation: State Probability Trajectory**

_Below is the probability trajectory of each state over time:_

  RELA -- TNF -- TNFRSF1A
                        1

**Tool Output:**

{
  "result": "**MaBoSS Simulation: State Probability Trajectory**\n\n_Below is the probability trajectory of each state over time:_\n\n  RELA -- TNF -- TNFRSF1A\n                        1"
}

**GitHub Copilot Response:**

Done. Summary of part 1 (saved under gpt_5/Scenario_1):

- Built OmniPath network from seed genes, removed bimodal interactions, connectivity OK.
- Exported to Network_1.bnet; generated MaBoSS output.bnd/output.cfg.
- Set outputs: apoptosis=CASP3, proliferation=E2F1.
- Baseline (TNF=ON) converges to RELA -- TNF -- TNFRSF1A (NF-κB survival); CASP3/E2F1 remain OFF.
- Sanity checks: XIAP OFF yields small apoptosis (~0.56%); BCL2 OFF or CASP8 ON didn’t flip fate (XIAP/RELA keep survival).

Next:

- Calibrate to reveal apoptotic/proliferative attractors (e.g., lower XIAP/BCL2/MCL1/CFLAR or inhibit RELA/IKK), or
- Proceed to PhysiCell: add TNF substrate, cancer cell type, attach PhysiBoSS with BND/CFG, map TNF→TNFRSF1A input, map CASP3→apoptosis and E2F1→proliferation.

Choose “tune MaBoSS” or “proceed to PhysiCell.”

**User Request:**

Let's proceed with PhysiCell

**Tool Output:**

BND files: output.bnd
CFG files: output.cfg

**Tool Output:**

{
  "result": "BND files: output.bnd\nCFG files: output.cfg"
}

**Tool Output:**

**Session created:** 8115b1a7... (tnf_fate_s1)
**Next steps:**

1. `analyze_biological_scenario()` - Set your biological context
2. `create_simulation_domain()` - Define spatial framework
3. Use `get_workflow_status()` to track progress

**ol Output:**

{
  "result": "**Session created:** 8115b1a7... (tnf_fate_s1)\n**Next steps:**\n1. `analyze_biological_scenario()` - Set your biological context\n2. `create_simulation_domain()` - Define spatial framework\n3. Use `get_workflow_status()` to track progress"
}


**Tool Output:**

**Biological scenario stored:** TNF diffuses in tumor microenvironment; cancer cells sense TNF via TNFRSF1A and trigger intracellular TNF-fate Boolean network (MaBoSS). CASP3 high => apoptosis; E2F1 high => proliferation. We will simulate 2D monolayer (thin 3D slab), uniform initial TNF=0 that can be introduced later.
**Next step:** Use `create_simulation_domain()` to set up the spatial framework.

**Tool Output:**

{
  "result": "**Biological scenario stored:** TNF diffuses in tumor microenvironment; cancer cells sense TNF via TNFRSF1A and trigger intracellular TNF-fate Boolean network (MaBoSS). CASP3 high => apoptosis; E2F1 high => proliferation. We will simulate 2D monolayer (thin 3D slab), uniform initial TNF=0 that can be introduced later.\n**Next step:** Use `create_simulation_domain()` to set up the spatial framework."
}

**Tool Output:**

**Simulation domain created:**

- Domain: 1000.0×1000.0×20.0 μm
- Mesh: 20.0 μm
- Duration: 24.0 hours
- Progress: 40%
  **Next step:** Use `add_single_substrate()` to add oxygen, nutrients, or drugs.

**Tool Output:**

{
  "result": "**Simulation domain created:**\n- Domain: 1000.0×1000.0×20.0 μm\n- Mesh: 20.0 μm\n- Duration: 24.0 hours\n- Progress: 40%\n**Next step:** Use `add_single_substrate()` to add oxygen, nutrients, or drugs."
}

**Tool Output:**

**Substrate added:** TNF

- Diffusion: 100000 μm²/min
- Decay: 0.01 min⁻¹
- Initial: 0 dimensionless
- Progress: 60%
  **Next step:** Use `add_single_cell_type()` to add cancer cells, immune cells, etc.

**Tool Output:**

{
  "result": "**Substrate added:** TNF\n- Diffusion: 100000 μm²/min\n- Decay: 0.01 min⁻¹\n- Initial: 0 dimensionless\n- Progress: 60%\n**Next step:** Use `add_single_cell_type()` to add cancer cells, immune cells, etc."
}

**Tool Output:**

**Cell type added:** cancer_cell

- Cycle model: Ki67_basic
- Progress: 57%
  **Next step:** Use `add_single_cell_rule()` to create cell behavior rules.
  First, use `list_all_available_signals()` and `list_all_available_behaviors()` to see options.

**Tool Output:**

{
  "result": "**Cell type added:** cancer_cell\n- Cycle model: Ki67_basic\n- Progress: 57%\n**Next step:** Use `add_single_cell_rule()` to create cell behavior rules.\nFirst, use `list_all_available_signals()` and `list_all_available_behaviors()` to see options."
}

**Tool Output:**

**PhysiBoSS model added to cancer_cell:**

- Model file: output.bnd
- Config file: output.cfg
- Progress: 50%
  **Next step:** Use `configure_physiboss_settings()` to set intracellular parameters.

**Tool Output:**

{
  "result": "**PhysiBoSS model added to cancer_cell:**\n- Model file: output.bnd\n- Config file: output.cfg\n- Progress: 50%\n**Next step:** Use `configure_physiboss_settings()` to set intracellular parameters."
}

**Tool Output:**

**Configured parameters for cancer_cell:**

- **Volume:** 2500 μm³ (nuclear: 500 μm³)
- **Motility:** 0.5 μm/min (persistence: 5 min)
- **Death rates:** apoptosis 0.0001, necrosis 0.0001 min⁻¹

**Tool Output:**

{
  "result": "**Configured parameters for cancer_cell:**\n- **Volume:** 2500 μm³ (nuclear: 500 μm³)\n- **Motility:** 0.5 μm/min (persistence: 5 min)\n- **Death rates:** apoptosis 0.0001, necrosis 0.0001 min⁻¹"
}

**Tool Output:**

**PhysiBoSS settings configured for cancer_cell:**

- Time step: 6.0 min
- Stochasticity: 0
- Scaling: 1.0
- Start time: 0.0 min
- Global inheritance: False
- Progress: 60%
  **Next step:** Use `add_physiboss_input_link()` to connect PhysiCell signals to boolean nodes.

**Tool Output:**

{
  "result": "**PhysiBoSS settings configured for cancer_cell:**\n- Time step: 6.0 min\n- Stochasticity: 0\n- Scaling: 1.0\n- Start time: 0.0 min\n- Global inheritance: False\n- Progress: 60%\n**Next step:** Use `add_physiboss_input_link()` to connect PhysiCell signals to boolean nodes."
}

**Tool Output:**

**PhysiBoSS input:** TNF → TNF

- Action: activation
- Threshold: 0.1
- Smoothing: 0
- Progress: 70%
  **Next step:** Use `add_physiboss_output_link()` to connect boolean nodes to cell behaviors.

**Tool Output:**

{
  "result": "**PhysiBoSS input:** TNF → TNF\n- Action: activation\n- Threshold: 0.1\n- Smoothing: 0\n- Progress: 70%\n**Next step:** Use `add_physiboss_output_link()` to connect boolean nodes to cell behaviors."
}

**Tool Output:**

**PhysiBoSS output:** CASP3 → apoptosis_rate

- Action: activation
- Active value: 0.02
- Base value: 0.0001
- Smoothing: 0
- Progress: 80%
  **Next step:** Use `apply_physiboss_mutation()` for genetic perturbations

**Tool Output:**

{
  "result": "**PhysiBoSS output:** CASP3 → apoptosis_rate\n- Action: activation\n- Active value: 0.02\n- Base value: 0.0001\n- Smoothing: 0\n- Progress: 80%\n**Next step:** Use `apply_physiboss_mutation()` for genetic perturbations"
}

**Tool Output:**

**PhysiBoSS output:** E2F1 → proliferation_rate

- Action: activation
- Active value: 0.02
- Base value: 0.001
- Smoothing: 0
- Progress: 80%
  **Next step:** Use `apply_physiboss_mutation()` for genetic perturbations

**Tool Output:**

{
  "result": "**PhysiBoSS output:** E2F1 → proliferation_rate\n- Action: activation\n- Active value: 0.02\n- Base value: 0.001\n- Smoothing: 0\n- Progress: 80%\n**Next step:** Use `apply_physiboss_mutation()` for genetic perturbations"
}

**Tool Output:**

No XML configuration loaded. Use load_xml_configuration() first.

**Tool Output:**

{
  "result": "No XML configuration loaded. Use load_xml_configuration() first."
}

**Tool Output:**

## Simulation Summary

**Session:** 8115b1a7...
**Progress:** 80%

**Scenario:** TNF diffuses in tumor microenvironment; cancer cells sense TNF via TNFRSF1A and trigger intracellular TNF-fate Boolean network (MaBoSS). CASP3 high => apoptosis; E2F1 high => proliferation. We will simulate 2D monolayer (thin 3D slab), uniform initial TNF=0 that can be introduced later.

**Components:**

- **Substrates (1):** TNF
- **Cell Types (1):** cancer_cell
- **Rules:** 0
- **PhysiBoSS Models:** 1

**Completed Steps:**
Substrates Added
Cell Types Added
Physiboss Settings Configured
Domain Setup
Physiboss Models Added
Physiboss Outputs Linked
Scenario Analysis
Physiboss Inputs Linked

**Next Steps:**
• configure_cell_parameters - Set cell volumes, motility, death rates

**Ready for export!** Use `export_xml_configuration()` to generate files.

**Tool Output:**

{
  "result": "## Simulation Summary\n\n**Session:** 8115b1a7...\n**Progress:** 80%\n\n**Scenario:** TNF diffuses in tumor microenvironment; cancer cells sense TNF via TNFRSF1A and trigger intracellular TNF-fate Boolean network (MaBoSS). CASP3 high => apoptosis; E2F1 high => proliferation. We will simulate 2D monolayer (thin 3D slab), uniform initial TNF=0 that can be introduced later.\n\n**Components:**\n- **Substrates (1):** TNF\n- **Cell Types (1):** cancer_cell\n- **Rules:** 0\n- **PhysiBoSS Models:** 1\n\n**Completed Steps:**\nSubstrates Added\nCell Types Added\nPhysiboss Settings Configured\nDomain Setup\nPhysiboss Models Added\nPhysiboss Outputs Linked\nScenario Analysis\nPhysiboss Inputs Linked\n\n**Next Steps:**\n• configure_cell_parameters - Set cell volumes, motility, death rates\n\n**Ready for export!** Use `export_xml_configuration()` to generate files."
}

**Tool Output:**

## XML Configuration Exported

**File:** PhysiCell_settings.xml (11KB)
**Source:** Created from scratch
**Substrates:** 1 (TNF)
**Cell Types:** 1 (cancer_cell)
**Progress:** 80%

**Next step:** Copy to PhysiCell project directory and run:

```bash
./myproject PhysiCell_settings.xml
```

**Tool Output:**

{
  "result": "## XML Configuration Exported\n\n**File:** PhysiCell_settings.xml (11KB)\n**Source:** Created from scratch\n**Substrates:** 1 (TNF)\n**Cell Types:** 1 (cancer_cell)\n**Progress:** 80%\n\n**Next step:** Copy to PhysiCell project directory and run:\n ``bash\n./myproject PhysiCell_settings.xml\n``"
}

**Tool Output:**

**No cell rules to export**

Use add_single_cell_rule() to create signal-behavior relationships first.

**Tool Output:**

{
  "result": "**No cell rules to export**\n\nUse add_single_cell_rule() to create signal-behavior relationships first."
}

**GitHub Copilot Response:**

Great. I added PhysiBoSS to a cancer cell type and wired TNF→TNF input and CASP3/E2F1 to apoptosis/proliferation. Exported files are ready.

What I configured

- Domain: 1000 x 1000 x 20 µm, dx=20, duration=24 h.
- Substrate: TNF (D=1e5 µm²/min, decay=0.01, initial=0).
- Cell type: cancer_cell (Ki67_basic).
- PhysiBoSS model: output.bnd/output.cfg attached to cancer_cell.
- Intracellular settings: dt=6 min, scaling=1, inheritance_global=false.
- Links:
  - Input: TNF signal activates boolean node TNF (threshold 0.1).
  - Outputs: CASP3 → apoptosis_rate (base 1e-4, active 0.02), E2F1 → proliferation_rate (base 0.001, active 0.02).
- Exported:
  ---------

**GitHub Copilot Response:**

- No cell_rules.csv (none defined yet)

Next options

- Add an external TNF source: boundary Dirichlet, uniform pulse, or secreting agents.
- Seed initial cell population and TNF pulse schedule.
- Export cell behavior rules CSV or keep rules embedded.

Tell me:

- How many initial cancer cells and seeding pattern (e.g., center 200 cells, random disk radius 200 µm)?
- TNF delivery (constant boundary at edges, central injection at t=60 min, or uniform pulse concentration)?
- Save outputs under gpt_5/Scenario_1?

**User Request:**

Let's assume the TNF diffuses slowly from the edge of the simulation toward the center. Adjust the parameters, then export again the simulation and provide me a summary of the model and of you achieved globally.

**Tool Output:**

**Substrate added:** TNF

- Diffusion: 10000 μm²/min
- Decay: 0.01 min⁻¹
- Initial: 0 dimensionless
- Boundary: 1 dimensionless
- Progress: 80%
  **Next step:** Use `add_single_cell_type()` to add cancer cells, immune cells, etc.

**Tool Output:**

{
  "result": "**Substrate added:** TNF\n- Diffusion: 10000 μm²/min\n- Decay: 0.01 min⁻¹\n- Initial: 0 dimensionless\n- Boundary: 1 dimensionless\n- Progress: 80%\n**Next step:** Use `add_single_cell_type()` to add cancer cells, immune cells, etc."
}

**Tool Output:**

**Substrate interaction set:** cancer_cell ↔ TNF (secretion: 0, uptake: 0.01 min⁻¹)

**Tool Output:**

{
  "result": "**Substrate interaction set:** cancer_cell ↔ TNF (secretion: 0, uptake: 0.01 min⁻¹)"
}

**Tool Output:**

## Simulation Summary

**Session:** 8115b1a7...
**Progress:** 80%

**Scenario:** TNF diffuses in tumor microenvironment; cancer cells sense TNF via TNFRSF1A and trigger intracellular TNF-fate Boolean network (MaBoSS). CASP3 high => apoptosis; E2F1 high => proliferation. We will simulate 2D monolayer (thin 3D slab), uniform initial TNF=0 that can be introduced later.

**Components:**

- **Substrates (1):** TNF
- **Cell Types (1):** cancer_cell
- **Rules:** 0
- **PhysiBoSS Models:** 1

**Completed Steps:**
Substrates Added
Cell Types Added
Physiboss Settings Configured
Domain Setup
Physiboss Models Added
Physiboss Outputs Linked
Scenario Analysis
Physiboss Inputs Linked

**Next Steps:**
• configure_cell_parameters - Set cell volumes, motility, death rates

**Ready for export!** Use `export_xml_configuration()` to generate files.

**Tool Output:**

{
  "result": "## Simulation Summary\n\n**Session:** 8115b1a7...\n**Progress:** 80%\n\n**Scenario:** TNF diffuses in tumor microenvironment; cancer cells sense TNF via TNFRSF1A and trigger intracellular TNF-fate Boolean network (MaBoSS). CASP3 high => apoptosis; E2F1 high => proliferation. We will simulate 2D monolayer (thin 3D slab), uniform initial TNF=0 that can be introduced later.\n\n**Components:**\n- **Substrates (1):** TNF\n- **Cell Types (1):** cancer_cell\n- **Rules:** 0\n- **PhysiBoSS Models:** 1\n\n**Completed Steps:**\nSubstrates Added\nCell Types Added\nPhysiboss Settings Configured\nDomain Setup\nPhysiboss Models Added\nPhysiboss Outputs Linked\nScenario Analysis\nPhysiboss Inputs Linked\n\n**Next Steps:**\n• configure_cell_parameters - Set cell volumes, motility, death rates\n\n**Ready for export!** Use `export_xml_configuration()` to generate files."
}

**Tool Output:**

Error exporting XML configuration: [Errno 2] No such file or directory: 'gpt_5/Scenario_1/PhysiCell_settings.xml'

**Tool Output:**

{
  "result": "Error exporting XML configuration: [Errno 2] No such file or directory: 'gpt_5/Scenario_1/PhysiCell_settings.xml'"
}

**Tool Output:**

Error exporting XML configuration: [Errno 2] No such file or directory: 'gpt_5/Scenario_1/PhysiCell_settings.xml'

**Tool Output:**

{
  "result": "Error exporting XML configuration: [Errno 2] No such file or directory: 'gpt_5/Scenario_1/PhysiCell_settings.xml'"
}

**Tool Output:**

## XML Configuration Exported

**File:** PhysiCell_settings.xml (11KB)
**Source:** Created from scratch
**Substrates:** 1 (TNF)
**Cell Types:** 1 (cancer_cell)
**Progress:** 80%

**Next step:** Copy to PhysiCell project directory and run:

```bash
./myproject PhysiCell_settings.xml
```

**Tool Output:**

{
  "result": "## XML Configuration Exported\n\n**File:** PhysiCell_settings.xml (11KB)\n**Source:** Created from scratch\n**Substrates:** 1 (TNF)\n**Cell Types:** 1 (cancer_cell)\n**Progress:** 80%\n\n**Next step:** Copy to PhysiCell project directory and run:\n ``bash\n./myproject PhysiCell_settings.xml\n``"
}

**GitHub Copilot Response:**

Here’s what I changed and exported.

TNF diffusion from edges

- TNF substrate: diffusion_coefficient=10000 µm²/min (slower), decay_rate=0.01 1/min, initial=0.
- Edge source: Dirichlet boundary enabled, boundary value=1.0 (TNF enters from domain edges and diffuses inward).
- Cancer cells: TNF uptake_rate=0.01 1/min; no secretion.

PhysiBoSS coupling (unchanged)

- Input link: TNF signal → boolean node TNF (threshold=0.1).
- Output links: CASP3 → apoptosis_rate (base 1e-4, active 0.02); E2F1 → proliferation_rate (base 0.001, active 0.02).
- Intracellular: dt=6 min, scaling=1, inheritance_global=false.

Domain and run

- Size: 1000 x 1000 x 20 µm, dx=20; 2D slab; duration: 24 h.
- Cell type: cancer_cell (Ki67_basic) with default volumes/motility; PhysiBoSS model attached (output.bnd/output.cfg).

Exports and files

- MaBoSS: output.bnd, output.cfg (already in workspace).
- PhysiCell XML:

**GitHub Copilot Response:**

 (exported at project root). Use this file with your simulator; if you want it in gpt_5/Scenario_1, I can place a copy there.

Global summary of what we achieved

- Built an OmniPath TNF-fate network, removed bimodal edges, verified connectivity, exported .bnet, generated MaBoSS .bnd/.cfg.
- Selected outputs (CASP3=apoptosis, E2F1=proliferation), ran MaBoSS; baseline under TNF favored NF-κB survival; mutations (e.g., XIAP OFF) modestly increased apoptosis.
- Created a PhysiCell session, added TNF substrate and a cancer cell type, integrated the MaBoSS model via PhysiBoSS, wired TNF signal to the network and network outputs to cell behaviors.
- Adjusted transport to model slow TNF diffusion from edges toward the center; exported an XML ready to run.

Want me to:

- Copy the exported XML into gpt_5/Scenario_1 and add a basic seeding (e.g., 200 cells in a central disk)?
- Add a gentle TNF boundary value (e.g., 0.2 instead of 1.0) or time-varying pulse?
