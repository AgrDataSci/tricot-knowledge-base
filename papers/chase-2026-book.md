---
id: chase-2026-book
title: Product testing with users in agriculture and food. Decentralized on-farm evaluation, breeding product validation, consumer testing and other applications using the tricot approach
authors: Chase R, de Sousa K, Laporte MA, Acuña S, Angudubo S, Benavente G, Cairns J, Clements L, Cremaschi A, Dorado-Betancourt H, Gandhi H, Londoño JM, Madriz B, Manrow-Villalobos M, Mbugua Gitonga A, Müller A, Steinke J, Stern R, Teeken B, van Heerwaarden J, Zaman-Allah M, van Etten J
year: 2026
journal: Bioversity International (book, 1st edition)
journal_short: Book
article: 1st ed., Montpellier, France
type: book
source: team
peer_reviewed: no
curated_card: yes
doi: https://doi.org/10.5281/zenodo.20042955
open_copy: https://learn.climmob.net
license: see Zenodo record
data: none (links to sample-size, seed and costing calculators, SOPs, trait illustration images and the farmer feedback package)
software: ClimMob 3, ODK Collect, Enketo, R-Instat, PlackettLuce, gosset, ClimMobTools, climatrends, chirps (check CRAN for current versions)
crops: many (cereals, legumes, roots and tubers, vegetables, cacao), with SOPs for amaranth, bambara groundnut, cowpea, finger millet, jute mallow, leafy vegetables, maize, pearl millet, pumpkin, sesame and sweetpotato
region: global, with African case studies (Ethiopia, Ghana, Kenya, Nigeria, Rwanda, Tanzania, Uganda)
keywords: tricot handbook, ten steps, target product profile, task groups, gender, sample size, plot size, SOPs, ClimMob, Plackett-Luce, feedback workshop, case studies
gist: Step-by-step tricot handbook with planning defaults (8 to 12 options, at least 30 replicates per option, 100 to 200 farms), ClimMob workflows and eight African case studies
not_established: a universal sample size for every tricot trial (the numbers are planning defaults); that tricot caused the variety releases described in the case studies (these are practitioner interviews, not impact evaluations); that gender differences in preferences are absent (tricot analyses have not consistently detected them, and the book suggests unmeasured social variables as one possible reason); that tricot suits farming practices as well as varieties (one case study found practices harder to test)
relations:
  - updates: vanetten-2020-guide  # several chapters reuse the 2020 guide, updated and extended
  - updates: vanetten-2020-rtbwp  # the Dissemination section reproduces its page 13
  - updates: steinke-2016-guide
  - citesAsDataSource: occelli-2024-agecon  # the FAQ says about a quarter cheaper than PVS and nearly twice as many farmers reached; the source reports 28% cheaper
  - discusses: quiros-2024-compag  # ClimMob chapters
  - discusses: daudi-2026-fes  # groundnut case study interview
  - discusses: moyo-2021-fsufs  # sweetpotato case study interview
  - discusses: kadege-2026-fsufs  # common bean case study interview
---

## Questions this book answers

- What is the current, complete guidance on running a tricot trial, step by step?
- How do I set objectives, choose options and traits, and cost a trial?
- How should participants be sampled to represent social, gender and task groups?
- How many participants, replicates and locations, and how much seed and plot space, does a trial need?
- What SOPs, metadata and ethics rules apply to a tricot trial in ClimMob?
- How are tricot rankings analysed, and how do I give results back to farmers?
- What have breeders and seed-sector practitioners in Africa learned from using tricot?

## Summary

This book is the current guide to tricot, written by the tricot team and partners under the 1000FARMS project (Gates Foundation) and BOLD WP7 (Norad through the Crop Trust). Each chapter downloads as a PDF, and the book is versioned on Zenodo.

The book presents tricot, conceived in 2011, as a citizen science approach for testing technology options in their use environments. Many participants each run a small experiment with three randomly assigned options, and their rankings add up to answer a larger question. Five features define it, namely small incomplete blocks that lower the barrier to participation, rankings and simple measurements that need little training, limited control of conditions to maximize external validity, a streamlined digital workflow in ClimMob, and early feedback to participants. Applications now span on-farm variety testing, consumer testing, product concept testing, fertilizers, clonal crops, vegetables and cacao.

The chapters follow the ten tricot steps. Preparation covers objectives, stakeholder engagement, standardized costing templates, an introduction to ClimMob and a planning checklist. Design is the longest chapter. It covers target product profiles, task-group sampling with an explicit gender lens, ethics and access-and-benefit-sharing, trial size with interactive sample-size and seed calculators, plot size, crop SOPs, ClimMob project setup, eight trial-documentation forms built on DataCite, CRediT and GloMIP vocabularies, and a full bean trial protocol. Recruitment, distribution, execution and observation reuse and update the 2020 guide, adding ClimMob how-tos for field agents, registration, trial packages and data collection. Compilation covers ODK, Enketo and project closure. Analysis reviews the Plackett-Luce model and its extensions with covariates, climate, genomic and on-station data, then the ClimMob report, R-Instat and the R package suite. Feedback describes a results workshop with feedback sheets and certificates, open data publication, and project sharing. Evaluation lists four indicators of success. The back matter holds curated resources, FAQs, the 1000FARMS Community of Practice, tools in development (an online course, Sikia and a registration app) and a glossary.

Planning guidance is concrete. Start with 8 to 12 options and no more than ten evaluation criteria. Aim for at least 30 replicates per option, which detects a 0.7 standard-deviation difference in a measured trait with 95% probability. Rank-based estimates are unreliable with too few replicates, and rankings need about twice as many replicates for equal power. Aim also for at least 10 replicates per location. For about 12 entries, 100 to 200 farms detect effect sizes of 0.7 to 1 standard deviation with 95% probability. Give each variety the same number of seeds rather than the same weight, keep plots small but large enough to avoid edge effects, and hold training workshops of at most 20 farmers about four weeks before planting.

A case-study chapter comes near the end. Eight breeders and trial managers from CIMMYT, One Acre Fund, TARI, Bayer, CIP, SARI, IITA and ISSD Ethiopia describe how tricot informed product profiles, market segments, release proposals and zone-specific recommendations, and they name recurring constraints such as seed multiplication, language, field-agent training and the weak handling of quantitative data.

## Chapter by chapter

Each section below gives the chapter authors, the PDF pages of the version checked (the 315-page PDF in `papers-pdf/`), the questions it answers, a summary and the practical guidance a user is most likely to need. Chapters marked "from the 2020 guide" carry the byline "Taken from van Etten et al. (2020)" with a page number, so cite the book for current practice and the guide for the original wording.

### 1. Introduction and the ten steps

**Authors.** Introduction by Jacob van Etten, Jonathan Steinke and Kauê de Sousa. The ten-steps section has no byline and follows the Tricot Short Guide (van Etten et al. 2020). PDF pages 4 to 19.

**Questions.** What is tricot and what makes it different from other participatory formats? Where has it been used? What are the ten steps?

The introduction defines tricot (triadic comparisons of technologies) as citizen science in which non-scientists generate and interpret experimental data. It addresses a known weakness of on-farm testing, which is capturing the full socio-economic and environmental heterogeneity of use contexts, and it argues that testing in use environments matters for external validity. The method was first implemented and tested between 2013 and 2016, much of it in the Seeds for Needs initiative on cereals and grain legumes, then spread to public and private actors, to food products, product concepts and fertilizers, and to cassava, sweetpotato, potato, vegetables and cacao. Its novelty lies in combining older participatory elements into one standardized format supported by ClimMob.

The chapter lists five uses. On-farm testing links farmer-reported outcomes to environmental, socio-economic and DNA metadata. Consumer testing assesses taste, cooking quality and shelf life. Concept testing compares broader ideas such as farming practices or agroforestry designs. Scaling and adaptation rest on the method's simplicity. The claimed outcomes are greater crop diversity (citing Gotor et al. 2021), faster adoption (citing Occelli et al. 2024) and more inclusive innovation (no citation). The book presents no new evidence for them.

The ten steps are preparation, design, recruitment, distribution, execution, observation, compilation, analysis, feedback and evaluation. Researchers define objectives and typically 8 to 12 options. Implementers design the project in ClimMob and prepare packages of three randomized options identified by QR codes. Implementers recruit farmers, and the number of farmers needed depends on the number of options. Field agents support groups of farmers and collect data with ODK Collect. Farmers plant blind, rank options on an observation card, and later receive the option names, the best options for their farm and certificates. Each cycle ends with a joint evaluation.

**Practical guidance.**
- Use ClimMob from the very start and train implementers in it, or the workflow breaks.
- Keep option names hidden from farmers until all data are collected.
- Treat tricot as iterative, with each cycle refining the option pool.

### 2. Preparation

**Authors.** Objective setting by Jacob van Etten, Rachel Chase and Kauê de Sousa. Stakeholder engagement from the 2020 guide. Budgeting by Stephen Angudubo and Grecia Benavente. Introducing ClimMob by Sofía Acuña, Marilyn Manrow, Brandon Madriz and Kauê de Sousa. PDF pages 20 to 41.

**Questions.** What questions can tricot answer? How many options and traits should I include? Who should participate, how many, and should they be rewarded? How do I cost a trial? What is ClimMob?

Objective setting starts from the main question, which may be agronomic (yield, drought tolerance, disease resistance), social (gender-differentiated trait preferences) or climatic (G×E modelled with gridded weather data). Options should solve local problems and be easy to adopt, and focus groups with farmers from diverse locations help narrow a larger pool. A local check can be planted nearby or included as one of the three options, never as a fourth option. Evaluation aspects are chosen with field agents and future users of all ages and both sexes, capped at ten, and always include overall performance and an open question on why the best option was preferred. Data are collected with ODK Collect on Android, with Enketo as a browser alternative, and the trial area should match the target environment and the relevant target product profile.

Stakeholder engagement asks who should participate, noting that subsistence and market-oriented households need different things and that processors and consumers may hold relevant knowledge. A field agent can support up to 25 farmers, and a first project should involve about 100 to 200 farmers. RHoMIS questions, available in ClimMob, characterize households. Rewards need care, since some undermine curiosity, and the chapter favours extra seed of the farmer's preferred variety.

Budgeting introduces two standardized costing templates, one for grain crops and one for root, tuber and banana crops, which differ in how seed multiplication is costed. They make costs transparent and comparable across countries and expose cost drivers such as excessive farm visits.

The ClimMob section describes the free, open-source platform (version 3), its component-based architecture built on ODK, ODK Tools and PyUtilib, its R-based analysis, its three user types (implementers, field agents, testers) and its libraries of field agents, technologies and multilingual questions from the 1000FARMS team. Designing a trial needs a computer with internet, and field data collection needs an Android phone or tablet. Data can also be uploaded from Excel templates. A step-by-step checklist assigns each task in the ten steps to researchers, implementers, field agents or farmers.

**Practical guidance.**
- Start with 8 to 12 options and no more than ten criteria, always including overall performance.
- Plan for about 100 to 200 farmers in a first cycle and no more than field agents can support.
- Cost the trial with the template that fits the crop type before committing to numbers.

### 3. Design

**Authors.** Product management by Harish Gandhi and Agnes Mbugua Gitonga. Sampling by Béla Teeken, Jill Cairns and Mainassara Zaman-Allah. Trial size by Joost van Heerwaarden and Marie-Angélique Laporte. SOPs by Almendra Cremaschi and Marie-Angélique Laporte. Project setup and trial documentation by Sofía Acuña, Marilyn Manrow and Brandon Madriz (with Kauê de Sousa for setup). Bean protocol by Kauê de Sousa. PDF pages 42 to 135.

Design spans PDF pages 42 to 135, nearly a third of the book. The subsections below follow its parts.

#### 3a. Product management

**Questions.** What is a target product profile, and how does it guide a tricot trial?

A target product profile (TPP) is the formal blueprint of the traits and performance benchmarks a new product needs to succeed in one market segment. The standard template lists required traits, measurement scales, minimum thresholds, priority, breeding objective, seed production needs, registration traits and benchmarks against market leaders. Essential traits split into improve traits, actively enhanced, and threshold traits, maintained at current levels, while nice-to-have traits add competitive edge. TPPs guide product advancement, parent selection and market differentiation. They start with incomplete information and improve iteratively as market intelligence fills gaps, as in concept testing of groundnut market segments in Tanzania. A useful TPP needs a market segment that is neither too broad nor too narrow and a multidisciplinary team. TPPs are published on GloMIP.

#### 3b. Sampling, inclusion and ethics

**Questions.** How do I choose participants who represent real users? How should gender be handled? What ethics, privacy and ABS rules apply?

The sampling section argues that tricot's statistical power comes from replication across space and seasons, so sampling must capture who farms where and under what constraints. It criticizes recruitment by broad demographic categories or equal numbers of men and women regardless of experience, and recruitment of people who are simply comfortable speaking to researchers. tricot instead uses purposive sampling by task groups, meaning people who perform similar crop tasks (cultivation, processing, marketing) within locally defined social groups, with gender analysed afterwards within and across task groups rather than imposed upfront.

The practical sequence is to identify relevant tasks, identify local social groups with leaders, key informants and transect walks while guarding against elite capture, map tasks within groups, exclude groups not involved in the crop, organize participants under a lead farmer, and agree modest compensation. Participants should represent local social groups roughly in proportion to their presence in the community and are chosen for tasks and skills rather than age. In Nigerian cassava trials, ten participants per community worked under a lead farmer they chose themselves, and a worked example shows seven local social groups in a southwest Nigerian village (numbered i to viii, with vi missing), and the ten participants selected came from four of them. Participant teams are prepared one to two months before planting material arrives, and drop-outs are replaced by people from similar groups. Lead-farmer trainings, ideally after plot installation and at state level in Nigeria, use a guide of four to five farmer-defined parameters. A short RHoMIS questionnaire is administered to every participant.

The inclusion discussion notes that tricot analyses have not consistently detected strong differences between men and women, even though trait-prioritization studies often do, and attributes this partly to gender interacting with income, occupation, migration or ethnicity, which are rarely measured.

On ethics, tricot needs institutional and possibly national ethics clearance, GDPR-compliant data handling, informed consent, the right to withdraw participation and data, and an opt-in to be named in publications. Using traditional varieties as checks is usually outside ABS rules but may fall under national ABS law, depending on how the country defines utilization, or under the Plant Treaty's multilateral system (SMTA, with no monetary benefit-sharing obligation if the varieties are not bred, but any onward transfer must follow SMTA terms). The new knowledge farmers produce in trials would usually fall outside national ABS laws but may still be subject to rules on working with indigenous and local communities, so the book recommends following CBD and Nagoya principles as best practice and returning non-monetary benefits. The chapter also lists features ClimMob should provide, such as an auto-generated IRB request, short consent forms (signature, photo or audio) and automatic detection of personal information before data export.

#### 3c. Trial size and plot size

**Questions.** How many replicates, farms and locations do I need? How much seed? How big should plots be?

Statistical power rises with replicates per option (n). Detecting a difference of 0.7 residual standard deviations (Cohen's d) with 95% probability needs about 30 replicates per option for measurements, and rankings need about twice as many for equal power. Rank-based estimates are unreliable when n is too small, so the chapter sets 30 replicates as the minimum to aim for. Because designs are balanced, plots equal farms times three, which equals options times n.

An interactive sample-size calculator (based on Talsma 2018, blocks of three, alpha and beta of 0.05, no allowance for data return) and a seed calculator (default 12 options, 30 replicates, 0.2 kg per plot, 10% buffer, giving 120 participants, 360 plots and 72 kg of seed, or 79.2 kg with the buffer) support planning. With its default inputs (Cohen's d of 0.7, 12 options) the sample-size calculator returns 187 participants and 561 plots, which is about 47 replicates per option (card's calculation). Suggested effect sizes are 0.7 to 1.0 for a single-season agronomic trial and 0.2 to 0.5 for consumer preference tests.

For multiple areas, aim for 10 to 20 replicates per geographical area and at least 10 per location. ClimMob designs stay sequentially balanced when each location gets the same number of farms, and a prototype sampling tool plans multi-location designs with shortest travel routes (an example with 20 options and 7 locations needs 467 farms, 67 per location). For about 12 entries, 100 to 200 farms give a 95% probability of detecting effect sizes of 0.7 to 1 standard deviation, with more farms needed for more agro-ecological environments and to allow for attrition over seasons. The chapter says this range matches earlier on-farm cereal trials and that future studies should give better guidance on trial dimensions. Simulations show that with 3 replicates per environment, ranking data cannot estimate option-by-environment variation, while with 18 per environment the estimates roughly follow the true values (read from a chart, approximate).

Plots should be small, so that more and smaller farms can take part, which adds variation between farms but no systematic bias. They should not be so small that edge effects dominate or that processing and cooking tests lack material. Interplot competition seems unimportant for yield in potato ridges (Connolly 1993, as cited), extends beyond the first row in cassava (Elias 2018, as cited) and is thought to be substantial in sweetpotato, where Grüneberg 2019 (as cited) recommends 30 m² plots with 100 vine cuttings on farm, but a Ghana tricot used 6 m² plots with 20 vines. Seed should be given by number rather than weight, so small-seeded varieties are not planted at higher density.

#### 3d. Standard operating procedures

**Questions.** What is a tricot SOP, what does it contain, and how is one developed and used in ClimMob?

SOPs are validated descriptions of what to record, how and when, developed with crop breeding teams so data from thousands of farmer-managed plots stay comparable. The chapter frames their value as practical, methodological, attributional and communicational, and adds that SOPs embed consent, data protection and PII handling at protocol level, reducing the need for trial-by-trial ethical clearance. All SOPs share four elements (trial and household characterization, growth-stage modules with trait measurements including yield, paired best and worst ranking questions aligned with TPPs, and RHoMIS socio-economic surveys), with an optional consumer evaluation of taste, aroma, texture and acceptability. Universal ranking traits are germination, vigor, pest and disease tolerance, abiotic stress tolerance, yield and overall preference, and crop-specific traits follow (panicle length and malting quality for millet, regrowth and livestock preference for forages). Leafy vegetables get repeated harvest modules.

SOPs are developed in four steps, namely identify trait priorities, define variables and units using a core question set and a curated library, pilot in ClimMob, then adjust and publish openly with versions. They are linked to Crop Ontology for machine-readable interoperability. In ClimMob, choosing an SOP template configures the registration form, growth-stage modules and ranking questions as ODK forms for field agents, with multilingual support (up to four languages per project). SOPs are listed for amaranth, bambara groundnut, cowpea, finger millet, jute mallow, leafy vegetables, maize, pearl millet, pumpkin, sesame and sweetpotato.

#### 3e. ClimMob project setup and trial documentation

**Questions.** How do I create a project, choose options, build forms and randomize packages? What metadata should I record?

Project setup walks through naming (technology, year and location, as in Bean_Honduras_2019_season1), the number of participants (better slightly too high), the fixed three options per participant with renameable labels, the project type (training or real; on-farm, home or public space), an optional SOP template and up to four languages. Users then add options from the technology library, build data-collection moments by dragging questions from the library, and generate packages. Randomization defaults to equal packages per option, any change must be rebalanced, and the list must be confirmed or it is lost. ClimMob then provides QR-code labels and the randomized package list.

Trial documentation is a set of eight forms that must be complete before analysis, covering contributors (roles from DataCite, activities from CRediT), funders, experimental design (plot size, design, market segments and TPP IDs from GloMIP), genotypes (entry type, release and crossing year, origin, target traits), participant recruitment (sample-size method, selection criteria, recruitment approach and location, how consent was formalized), capacity building (how tricot was explained, instructions, training setup, follow-up, inputs provided), data collection (method and input channel) and results communication (channels and feedback methods). Each form offers multi-select, "Other" and "Non-applicable" options. Entry types include historical, farmer, commercial and comparative checks, evaluation entries, release candidates and replacement candidates.

#### 3f. Design example, bean protocol

**Questions.** What does a complete tricot protocol look like for one crop?

The bean protocol lists data-collection moments (registration at package distribution, early agronomic performance at 15 days, maturity at 40 days, harvest at 60 to 90 days and post-harvest at 90 to 150 days, with RHoMIS at any time) and the characterization and ranking questions at each. Registration records consent, package code, delivery GPS, age, sex, education, administrative units and experience with the crop and with tricot. Later moments record plot conditions, management, plot loss, disease, inputs and yield, and ranking pairs cover germination time and rate, pest, disease and abiotic stress tolerance, maturity, yield, seed size (also for the target use or market), leaf quality for consumption, taste, marketability, storage problems, storability, overall preference and comparison with the local variety. A separate bean consumer SOP is planned.

**Practical guidance for Design.**
- Write or adopt a TPP before choosing options and traits.
- Recruit by task groups within local social groups, replace drop-outs like for like, and run RHoMIS on every participant.
- Plan at least 30 replicates per option and 10 per location, then check numbers with the calculators.
- Give equal seed numbers, keep plots small, and do not harvest border rows where edge effects matter.
- Reuse SOP and library questions before writing new ones, and complete all eight documentation forms.

### 4. Recruitment

**Authors.** Recruitment from the 2020 guide. Field agents and registration by Sofía Acuña, Marilyn Manrow, Brandon Madriz and Kauê de Sousa. PDF pages 136 to 143.

**Questions.** Who can take part and how do I find them? Can groups run trials? How do I add field agents and registration questions in ClimMob?

Anyone may participate, and field agents, posters in shops and village halls help find volunteers who will commit time, enjoy experimenting and include women and men in roughly equal numbers. Existing groups such as committees, credit cooperatives or religious groups can run a joint trial on a host farm, and women's research groups can raise women's participation. Trusted local networks, extension officers and a shared WhatsApp group linking lead farmers with researchers strengthen communication. Farmers should take part over several cycles, so newcomers can learn from experienced peers and everyone tests new sets of options.

In ClimMob, implementers add field agents from the library (each needs a username and password for ODK Collect) and build the registration form from library questions, which serve both administration and later analysis, such as whether younger participants adopt a technology faster or whether female participants prefer certain options. RHoMIS can be added for deeper household data.

### 5. Distribution

**Authors.** Training workshop from the 2020 guide. Trial packages by Sofía Acuña, Marilyn Manrow, Brandon Madriz and Kauê de Sousa. PDF pages 144 to 151.

**Questions.** How should the training workshop run? What goes in a trial package, and how are participants registered?

The training and distribution workshop takes place about four weeks before the trial, with at most 20 farmers at a time and men and women in equal numbers where possible. Implementers and field agents explain the purpose, benefits and responsibilities, show a demonstration plot or video, hand out a pictorial guide and practise filling in the observation card.

Each package has a QR code that farmers keep for the whole trial, three bags with equal quantities of the assigned options (or instructions for non-material options), an observation card and a brochure. Registration uses ODK Collect, scanning the QR code to link the package to the participant, with at minimum the QR code and the participant's name. Paper registration followed by Excel upload is possible but discouraged as slower and more error-prone. Finishing registration in ClimMob cannot be undone.

### 6. Execution

**Authors.** From the 2020 guide. PDF pages 152 to 154.

**Questions.** How should farmers plant and manage their trial?

Farmers plant and manage their own trial and deserve respect as experts. Two principles govern execution. The trial should reflect real production conditions, so the plot sits next to or within the regular field in an average spot and receives exactly the usual management, including intercropping, with neither extra care nor neglect, unless the options tested are themselves management practices. The trial should also allow a fair comparison, so the three options sit side by side in equal sub-plots (for example six rows of five metres) with A on the left, B in the middle and C on the right, borders marked and options never mixed.

### 7. Observation

**Authors.** From the 2020 guide. PDF pages 155 to 158.

**Questions.** How should farmers evaluate their options, and how do I design an observation card?

Farmers often find it hard to rank on one criterion while ignoring their overall impression, so the chapter stresses judging one criterion at a time. Evaluations usually happen in three stages, namely early criteria such as foliage, later criteria such as disease, and post-harvest criteria such as yield or market value, with dates suggested by implementers. Phone follow-up reminds farmers, answers questions and can double as data compilation. Observation cards always ask for the best and worst option in as few words as possible ("Best foliage?"), with images, and are built by defining data-collection moments (for beans, sowing, 30 days after sowing and harvest) and one question per observation.

### 8. Compilation

**Authors.** Data collection by Sofía Acuña, Marilyn Manrow, Brandon Madriz and Kauê de Sousa. Closing a project by Sofía Acuña, Marilyn Manrow and Brandon Madriz. PDF pages 159 to 170.

**Questions.** How do field agents collect and submit data? Can data be entered from a browser? How and when do I close a project?

ClimMob generates a form for each data-collection moment. Field agents fill and send forms in ODK Collect (recommended), the administrator checks and corrects data, closes the moment and opens the next. Cancelling a form in ODK deletes it permanently. Excel upload is possible but not recommended. Enketo lets registered field agents submit from a browser, and in that case the QR code is replaced by a typed code combining the owner's username, the package number and the project code, ending with a tilde.

Closing a project turns it into a permanent read-only record. A project can be closed at any time, but only by the owner, and ideally once data are verified and trial documentation is complete. Documentation is not needed to close, but the analysis module needs it, along with enough data and no submission conflicts, and conflicts cannot be resolved after closing. After closing, edits return an access-restricted message and the owner and 1000FARMS administrators are notified.

### 9. Analysis

**Authors.** Statistical models by Kauê de Sousa, Joost van Heerwaarden and Hugo Dorado. ClimMob report by Sofía Acuña, Marilyn Manrow, Brandon Madriz and Kauê de Sousa. R-Instat by Lily Clements, Roger Stern and Rachel Chase. Advanced analysis in R by Kauê de Sousa. PDF pages 171 to 187.

**Questions.** Which models suit tricot rankings and measurements? How can analysis bring in climate, genomic, on-station or lab data? What tools can non-coders and coders use?

The Plackett-Luce model, derived from Luce's choice axiom, estimates a worth parameter per item from rankings. It suits tricot because it handles partial rankings in incomplete, unbalanced designs, models ordinal data directly, gives intuitive outputs (probabilities of outperforming others, expected ranks) and accepts covariates and hierarchical extensions. Rankings are fast, locally adaptable and need little calibration.

A widely used way to model heterogeneity is the Plackett-Luce tree (model-based recursive partitioning on environmental or social covariates), which reveals G×E and helps define target populations of environments, as in the Nicaragua bean example where maximum night temperature split the data. Plackett-Luce regression adds linear covariates, including option-level ones such as trait, genomic or food-lab data. Continuous data such as yield go to linear or generalized linear mixed models that partition variance and estimate heritability, with rankings and measurements analysed in parallel and combined at interpretation while joint ordinal-continuous models are under development. Further extensions link trials to seasonal climate for location-specific recommendations, synthesize rankings across trials, add genomic relatedness to raise predictive accuracy, express results as probability of superiority over checks, and integrate on-station genotypic values (potato in Rwanda) or instrumental lab data (gari, a cassava product) as item covariates. Future work targets multi-level, multi-environment, multi-trait and genomic models.

ClimMob produces an automatic report ranking options and comparing selected variables. R-Instat offers a graphical interface for Plackett-Luce analysis, visualization and daily climate data as covariates, supported by IDEMS eCampus courses. For coders, ClimMobTools (API access), gosset (ranking analysis, trait prioritization, synthesis), climatrends (agroclimatic indices), chirps (CHIRPS and CHIRTS data) and PlackettLuce form the R suite, with worked examples on bean trait prioritization and gari consumer testing.

### 10. Feedback

**Authors.** Trial feedback by Anna Müller and Juan Manuel Londoño. Dissemination from the 2020 RTB working paper (van Etten et al. 2020, vanetten-2020-rtbwp). Project sharing by Sofía Acuña, Marilyn Manrow and Brandon Madriz. PDF pages 188 to 200.

**Questions.** How should results go back to farmers? What materials exist? Should data be published, and where?

Farmers are data producers and partners, so every trial ends with a feedback workshop of at least half a day, for about 20 to 25 people. The recommended agenda runs 75 to 110 minutes, from welcome and a recap of the trial, through handing over and explaining personal feedback sheets, small-group discussion of five to seven people by preferred option, a group-level results presentation that stresses there is no single best option, certificates and an optional 0 to 10 usefulness score, to next steps. Field agents note farmers' comments. ClimMob generates the feedback sheet, and a feedback package provides sheet and certificate templates, data frames, icons and manuals. IITA's state-level feedback handbooks from Nigeria serve as examples. Teams should budget time and money for feedback workshops from the start and debrief afterwards to improve the next trials.

Dissemination argues for open publication of trial data to avoid the file-drawer problem and the poor documentation common in on-farm trials, through standardized metadata (including plot history), automated anonymization and repositories such as Dataverse, Zenodo or CGSpace. ClimMob projects can be shared with admin, editor or read-only member roles.

### 11. Evaluation

**Authors.** From the 2020 guide. PDF pages 201 to 203.

**Questions.** How do I judge whether a cycle worked and improve the next one?

Implementers, researchers and field agents review each cycle, listening first to farmers, and aim to include more farmers every cycle. The lowest-ranked or poorly adapted options are replaced with new ones to refresh the pool. Four indicators can be tracked in ClimMob, namely the rate of completed trials (and whether losses came from weather or from management such as QR-code errors), gender balance relative to the population growing the crop, the share of returning farmers, and whether farmers intend to keep using a tested option.

### 12. Resources, FAQs and back matter

**Authors.** Community of Practice by Rachel Chase. Spousal information letter prepared by Emily Amondo. Other sections unattributed. PDF pages 204 to 274 and 302 to 315.

**Questions.** Where are the key publications, videos, templates, SOPs and farmer materials? What do new users usually ask? What tools are coming?

The resources chapter lists the main tricot publications with links, training video playlists (introduction, ClimMob, R analysis), the costing templates and guidelines, the crop SOPs, downloadable trait illustration images for beans, cassava, cocoa, cowpea, millet, potato, sorghum and soybean, a tricot guidance sheet for farmers, a spousal information letter that helps reach women in dual-adult households, and the farmer feedback package. The 1000FARMS Community of Practice is an open Discourse forum with webinars, announcements and a methods space.

The FAQs answer common doubts. Farmers need no smartphone, only field agents do. Ties are not allowed, so farmers are asked to look again for small differences. Results can be disaggregated by environment from GPS and environmental layers. A local control can be compared by an extra question or included blind in the pool. Field agents often care for 10 to 20 growers. More than three options can be tested, since each grower receives a randomized subset of three from a larger pool (the glossary recommends 8 to 12 for a first experiment). Projects can be merged when they share at least one option. ODK Collect works offline but not on iOS. Compared with PVS in Central America, tricot was about a quarter cheaper and reached nearly twice as many farmers.

Tools in development include an open online tricot course with a certificate, Sikia (offline-first speech and image analysis of open-ended farmer interviews, tested on 1000FARMS tricot trials, including a Tanzanian bean trial (n = 480), where it picked up gendered preferences, with women stressing taste and men yield and climate) and a browser-based ClimMob registration app. A glossary defines terms such as sequentially balanced randomization, incomplete block design, infosheet and observation card.

### 13. African crop case studies

**Authors.** Happy Daudi, Elysé Tuyishime, Edith Kadege, Jamlick Mwathi, Reuben Ssali, Richard Oteng-Frimpong, Patrick Ongom, Mohammed Hassena. PDF pages 275 to 301.

**Questions.** How have breeders and seed-sector actors in Africa used tricot, what changed in their decisions, and what problems did they hit?

The chapter consists of interviews, so its evidence is practitioner experience, not designed comparisons.

- **Groundnut, Kenya and Tanzania (Happy Daudi, CIMMYT).** tricot data supported a variety release proposal and a groundnut product profile, allowed on-farm genetic gain estimates and showed that selection traits differ by zone. Constraints were seed for many farmers, English-only software and weak handling of quantitative data. Linked paper daudi-2026-fes.
- **Maize, Rwanda (Elysé Tuyishime, One Acre Fund).** Up to 15 varieties tested in one season with fewer farm visits, blind testing raised curiosity, rankings exposed grain size as a driver, zone maps showed which varieties to recommend where, and the long list was narrowed to one to three candidates for scaling. Testing farming practices proved harder than testing varieties.
- **Common bean, Tanzania (Edith Kadege, TARI).** Farmers prioritized yield, market acceptance and disease resistance, anthracnose varied by agro-ecological zone, women stressed post-harvest traits, men agronomic traits and youth marketability. Real-time ODK data allowed in-season corrections. Collecting and managing quantitative data, such as disease levels, was harder in ClimMob than rankings. Linked paper kadege-2026-fsufs.
- **Maize, Kenya (Jamlick Mwathi, Bayer).** Farmers valued grain size and colour beyond yield and preferred a hybrid the breeders had ranked lower, which entered the programme, and two areas assumed similar proved different.
- **Sweetpotato, Uganda (Reuben Ssali, CIP).** tricot reached more farmers regardless of education, validated survey-based trait priorities and showed some farmers accept mealiness when other traits are strong. Varieties must be multiplied before the trial, and rankings do not reveal trade-offs. Linked paper moyo-2021-fsufs.
- **Groundnut, Ghana (Richard Oteng-Frimpong, SARI).** Fifteen lines reached previously inaccessible farmers, female farmers preferred early maturity, and seed size, colour and fast maturity fed into product profiles. Seed had to be multiplied off-season and field agents translated across languages.
- **Cowpea, Nigeria (Patrick Ongom, IITA).** Grain colour, seed size and pest and disease resistance shaped product profiles and release decisions, and the pipeline was restructured by market class. Poorly trained field agents caused technical problems, so early supervision is needed, and some farmers' data were uploaded twice, which ClimMob can correct.
- **Seed systems, Ethiopia (Mohammed Hassena, ISSD).** tricot brought new varieties to isolated farmers through local partners and builds familiarity before release, but companies may resist unfavourable results on released varieties, and renaming varieties at release confuses farmers.

## Methods in brief

- **Structure.** Thirteen chapters (an introduction, ten chapters for the ten tricot steps, resources and African case studies), plus FAQs, a Community of Practice page, tools in development and a glossary, written by specialist authors and partly reused from the 2020 guide.
- **Tools.** Sample-size calculator (blocks of three, alpha and beta 0.05), seed calculator, prototype multi-location sampling tool, grain and RTB costing templates, planning checklist, crop SOP templates, trait illustration images, farmer feedback package and spousal information letter.
- **Standards.** SOPs linked to Crop Ontology, trial-documentation forms using DataCite, CRediT and GloMIP vocabularies, RHoMIS for household data.
- **Analysis.** Plackett-Luce models, trees and regression, mixed models for continuous traits, climate and genomic covariates, data synthesis across trials, ClimMob reports, R-Instat and the R package suite.

## Stated limitations

- Rankings carry roughly half the information of measurements, and rank-based estimates are unreliable with too few replicates.
- The sample-size calculator ignores data return rates, and trial numbers shrink over seasons, so plans need a margin.
- Better guidance on optimal trial dimensions across environments awaits future studies.
- tricot analyses have not consistently detected strong gender differences in preferences. One possible reason is that gender interacts with social variables such as income, occupation, migration status or ethnicity, which are rarely measured.
- Free-listing exercises reflect what is salient in discourse more than the relative importance of traits in real decisions.
- Small plots do not suit every crop or trait, especially where interplot competition is strong or produce is needed for processing and cooking tests.
- Rankings alone do not reveal which trade-offs farmers make, and current software handles quantitative data less well than rankings (case studies).
- tricot proved harder to apply to farming practices than to varieties in one case study.

## Key numbers

| Number | Context | Primary source |
|---|---|---|
| 2011 | Year tricot was conceived | van Etten 2011, cited in this book |
| 2013–2016 | First implementation and testing for on-farm variety testing | van Etten et al. 2019, cited in this book |
| 8–12 | Options recommended for a trial, especially a first one | This book |
| ≤10 | Evaluation aspects per trial (glossary gives 5 to 10) | This book |
| 4–5 | Farmer-defined parameters in the lead-farmer evaluation guide (Nigeria) | This book |
| 10 | Participants per community under one lead farmer, Nigerian cassava trials | This book |
| 1–2 months | Lead time to prepare participant teams before planting material arrives | This book |
| ~30 | Replicates per option to detect Cohen's d of 0.7 in a measured trait with 95% probability, and the minimum to aim for | This book |
| ~2× | Replicates needed with rankings for power equal to measurements | This book |
| 0.7–1.0 / 0.2–0.5 | Suggested effect sizes for agronomic trials / consumer preference tests | This book |
| 12 × 30 | Seed-calculator default (options × replicates), giving 120 participants and 360 plots | This book |
| 72 kg (79.2 kg) | Seed at 0.2 kg per plot, without (with) a 10% buffer | This book |
| 10–20 / ≥10 | Replicates per geographical area / per location | This book |
| 467 farms, 67 per location | Sampling-tool example with 20 options and 7 locations | This book |
| 100–200 farms | Solid results for about 12 entries, and advised size for a first project | This book |
| 6 m², 20 vines vs 30 m², 100 vines | Ghana sweetpotato tricot plots vs recommended on-farm plots | This book; Grüneberg 2019 |
| ≤25 / 10–20 | Farmers per field agent (stakeholder chapter / FAQ and glossary) | This book |
| 20–30 | Field agents a tricot project might employ | This book |
| ≤20, ~4 weeks | Farmers per training workshop, and its timing before the trial | This book |
| 3 | Options per participant, fixed in ClimMob | This book |
| ≤4 | Languages for participant forms in a ClimMob project | This book |
| 8 | Trial-documentation forms required before analysis | This book |
| 2 | Costing templates (grain crops, RTB crops) | This book |
| 60–90 / 90–150 days | Harvest / post-harvest data-collection windows in the bean protocol | This book |
| 75–110 min | Recommended feedback workshop agenda, for 20 to 25 people | This book |
| 5–7 | People per small discussion group at feedback workshops | This book |
| 4 | Indicators of success for evaluating a cycle | This book |
| ~25% cheaper, ~2× farmers | tricot vs PVS for common bean in Central America | Occelli et al. 2024 (reports 28% cheaper) |
| 15 | Maize varieties (One Acre Fund) and groundnut lines (SARI) tested in one trial | This book (case studies) |
| 480 | n in the Tanzanian bean trial used to test Sikia (unit not stated) | This book |
| ~170 USD vs 0.7 USD | Cost per in-depth household interview vs per SMS respondent, cited for Sikia | This book |

## Notes

- The PDF lists Béla Teeken twice in the citation, and gives the length as 298 pages, while the PDF checked has 315 pages. The concept DOI is 10.5281/zenodo.20042955. The documentation repository's README cites version DOI 10.5281/zenodo.20043167. Check the author list and version on Zenodo before citing.
- Name spellings differ in the source. The citation (PDF 3) and the feedback byline (PDF 188) spell "Muller", without the umlaut, while other reference lists in the book use Müller, which this card keeps. The chapter bylines give "Marilyn Manrow" and "Hugo Dorado", while the citation gives Manrow-Villalobos M and Dorado-Betancourt H. The authors field follows the citation and the chapter sections follow the bylines. The case-study byline spells "Reuban Ssali", while the interview uses Reuben (PDF 275, 289).
- The book is versioned ("Version: current" on each chapter), so wording and numbers can change. The online site and the latest version are not named in the PDF (the online edition is at learn.climmob.net, from outside the PDF). Check the live site or Zenodo for the latest version.
- Several chapters reuse 2020 guide material, and the ClimMob features described are those of this version. This is a curator caveat, not a limitation the authors state.
- Field agent load differs between chapters (up to 25 farmers in stakeholder engagement, 10 to 20 in the FAQ and glossary). Report the range.
- The Design chapter gives mixed minimum-replicate guidance. It says to aim for at least 30 replicates per option (PDF 57), calls rank estimates unreliable below 20 (PDF 61), and its own calculator returns about 47 per option for d = 0.7 with 12 options (PDF 59, card's calculation). 100 farms with 12 entries gives only 25 replicates per option.
- The sampling-tool example gives 467 farms and 67 per location across 7 locations. 467 divided by 7 is 66.7, so the per-location figure is rounded (7 times 67 would be 469).
- The trial-size Figure 1 caption gives the same colour (red) for quantitative and ranking data, so read the series from the plot (PDF 63).
- The plot-size section calls the Ghana sweetpotato plots (6 m²) two thirds of the recommended on-station size, while the recommendation it cites is 30 m² for on-farm trials. Use the m² figures, not the fraction.
- The Nigerian social-group table numbers groups i to viii but lists seven, and its grey shading does not match the caption (PDF 50 to 51).
- The bean protocol example contains wording carried over from other crop templates (planting "tubers", leaf quality), so check the current bean SOP before reuse (PDF 118 to 133).
- The ten-steps overview gives recruitment to implementers (PDF 15), and the checklist gives it to field agents (PDF 37).
- The Recruitment chapter is marked as taken from the 2020 guide, but its paragraph on extension officers and WhatsApp groups is not in the guide, and its claim about group solidarity has no reference (PDF 137).
- The Observation chapter's example questions (PDF 157) do not follow its own short best-and-worst format (PDF 156 to 157).
- The Dissemination section is labelled "van Etten et al. (2020)" but reproduces the 2020 RTB working paper (vanetten-2020-rtbwp, page 13), not the 2020 guide. It updates the working paper's "forthcoming" Valle citation to Valle (2021) and adds a list of places to share data.
- ClimMob cost differs between FAQs (free for CGIAR and NARES with a fee for private companies, versus free for anyone). The groundnut case study says ClimMob was only available in English, so extension officers translated for farmers (PDF 277). The setup chapter allows participant forms in up to four languages (PDF 82). The case study may refer to the software interface or to an earlier version, so check before citing either as current.
- The Kadege case study gives its associated paper a 2026 date with volume 9 and a 2025 DOI, and expands TARI as "Tanzania Research Institute" (PDF 283 to 284). See kadege-2026-fsufs for the paper details.
- The FAQ's cost comparison with PVS cites occelli-2024-agecon, which reports 28% lower cost than group PVS. Cite the source figure.
- Sikia, listed here as in development, is now integrated with ClimMob (goormachtigh-2026-flyer).
- Related cards include vanetten-2020-guide, vanetten-2020-rtbwp and steinke-2016-guide (earlier guides), quiros-2024-compag (ClimMob), desousa-2024-asd (retrospective and scaling), occelli-2024-agecon (costs), cairns-2026-jxb (inclusive sampling), muller-2025-ux and schumann-2024-ux (feedback design), turner-2020-compstat (PlackettLuce), dorado-2026-tag (genetic parameters from rankings), nabateregga-2025-eja (farmer-measured yield), kang-2025-expagric and alamu-2023-jsfa (item covariates), daudi-2026-fes, kadege-2026-fsufs and moyo-2021-fsufs (case-study papers).
