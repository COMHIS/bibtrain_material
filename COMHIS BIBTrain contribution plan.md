# BIBTrain training material contribution

## What we promised

**Training Material 7**

**Topic:** Refinement, evaluation and publication workflow for bibliography metadata

**Author:** Ville Vaara, Mikko Tolonen, Eetu Mäkelä, Iiro Tiihonen

**Classification:** Harmonization, Validation, Dissemination

**Short description:** We present a workflow for harmonizing, validating, and publishing a bibliographic metadata dataset as an example of a generalizable data refinement process. The focus is on developing a repeatable and extensible workflow for producing research-ready datasets and for assessing the quality of the refinement process. The article provides clear, step-by-step guidance for applying the approach to comparable raw datasets, along with access to the refinement scripts that can serve as a starting point for replicating and adapting the workflow.

## Platform

Material to be produced for DARIAH Campus platform. e.g. [https\://campus.dariah.eu/curricula/automatic-text-recognition-made-easy](https://campus.dariah.eu/curricula/automatic-text-recognition-made-easy) 

First half of an ESTC article, focusing on the workflow of producing a refined dataset out of the MARC21 ESTC dump.

(The eventual article covers: 1\) workflow and refinement process and 2\) data itself, its structure and description of its contents)

This part will be covering:

* breaking down the work in the project to different digestible bits (different fields, etc given as responsibility to different contributors)  
* tracking the workflow, interdependencies  
* philosophy around data publication, possible licensing issues and choices

The second part (not in this BIBTrain training material) will contain, e.g.:

* references to research applications where the data has been used

# Content

## ESTC MARC records to unified linked data format

## Sections:

1. pre-evaluation of the data  
   1. complexity assessment for different facets  
   2. how internally coherent and systematic the use of the origin model has been  
   3. planning the end product \- should the data model be rehashed for the intended use? Does the existing model serve research needs  
   4. What has been included in the data, what kind of assumptions have been made  
   5.   
2. work segmentation  
3. harmonizing  
4. validating  
5. publishing

Notes:

* When to use generative AI  
* Traditional processing makes sense vs generative model  
* What could be done with generative / machine learning AI?  
* Using multiple data sources, eg. actor information  
* Interdependencies and internal workflow in the data processing  
  * E.g. actors depend on publication year and place

Workflow for different sections

* Understanding what is there, in terms of context- both library practices, as well as the historical practices  
* Understanding what is there, in terms of data- overviews, data statistics, how same information can be broken up into several parts of a MARC record

Essentially, such a project is about moving the data from one model to another

# General notes for the below:

* *Emphasize work segmentation, coordination of data, documentation, pipeline / workflow / interlinked modules \-thinking, working with data and code publication in mind.*


# Refinement, evaluation and publication workflow for bibliography metadata

## Introduction

This module\[some other term?\] describes the process and considerations involved in taking a bibliographic dataset produced and used in a library, and refining it into a format that can then be used as data for historical research. The workflow is based on work done on the English Short Title Catalogue (ESTC), and examples are pulled from that process, but it applies more broadly to a wide variety of bibliographic data.

The main focus in the module is in the process, from data evaluation to publication, and iterating over multiple versions of a dataset. The module has been written with a collaborative workflow in mind, but applies equally well to a project with just one initial contributor. The realization, again and again, with metadata refinement work has been that the work is by necessity iterative and modular by nature, and best approached as such. The initial need might be to refine a part of a dataset for a specific research need, but more often than not, additional avenues of inquiry present themselves. Therefore, the work usually proceeds from milestone to milestone, and keeping this nature of the work in mind can be very beneficial for its overall organization. In the below examples, we’ll cover the critical aspects to keep in mind in this kind of work: Evaluation of the initial data, working with modularity and eventual data publications in mind from the get go, ensuring ease of collaborative and iterative work (with others, or with the sole researcher’s future self). 

## Evaluation of the initial data

1. complexity assessment for different facets  
   2. how internally coherent and systematic the use of the origin model has been  
   3. planning the end product \- should the data model be rehashed for the intended use? Does the existing model serve research needs  
   4. What has been included in the data, what kind of assumptions have been made

### Motivation for the evaluation

Refining bibliographic metadata involves decisions about what the data represents and what researchers will count. Before processing individual fields, one should distinguish catalogue records, editions, works and surviving copies, and identify which of these the proposed output describes. Historical variation should also be distinguished from inconsistency introduced during cataloguing: an unusual spelling or an apparently contradictory date may carry information worth preserving. The original value should therefore remain recoverable alongside its harmonised interpretation. This makes refinement an explicit part of historical source criticism, following the approach developed in our work on bibliographic data science and the history of the book.

The initial consideration is understanding the nature of the dataset in question. Bibliographic datasets, as produced by libraries and other memory organisations have not been produced with research use in mind, and they typically have a lot of historical baggage in their format baked in. The ESTC for example, follows the MARC21 format, which has its roots in the move from card catalogues in libraries to electronic cataloguing systems, and therefore follows a relatively archaic data structure. This is further complicated by a natural process with a widely adapted, and at this point old data format: various additions and options have been baked into the data structure, and while the MARC format is well documented (see [https\://www\.loc.gov/marc/bibliographic/](https://www.loc.gov/marc/bibliographic/) ), its wide offering of fields (each data point in a MARC catalogue entry has a field, subfield and various indicator codes) often allows entering the same information in different places in varying forms- more on this later.

### Dataset internal coherence?

In order to get the bibliographic data research ready, the first step in a process like this is conducting wide enough analysis of the dataset. What kind of information does it hold in its various structures, how long has it been under construction, and how have the practices of collecting entries in it changed over the years, how internally coherent and systematic has the entry of information into it been? Do these considerations vary- the ESTC for example is a catalogue that has been collected from various contributing libraries, and combined together by the British Library- and although broad overall practices have been more or less similar in the contributing libraries, there are differences- subtle, or less subtle, and if they are not taken under consideration a lot of data can go missing.

### End product planning

Bibliographical data can be complex and multifaceted. The main question should always be, “What are the critical data facets for the needs of this research project?” It is very easy to get lost in an attempt to  A sensible approach is to both A) to go for the low hanging fruit- the easiest data facets to get to a usable state, and to B) plan for an iterative process of gradually expanding the scope of the final ‘product’, and to account for a possibility of such expansion in the planned model for the output. 

\[something more about modularity in structure, how ESTC records are joined by ESTCids, etc

Moving target? Iterative work, setting checkpoints for research publications, and sufficient data release for work up to that point.

### Historian’s default question: scope, process of data formation **\[more sensible title here\]**

\[Cover the questions of: what kind of material was preserved for cataloguing in the first place, what was seemed as worthwhile to catalogue, what were the aspects of the data that were ‘lost in translation’ when cataloguing from the physical objects, or microfilm, or something similar into the digital entries. E.g. truncated publisher statements in ESTC.\]

## Work segmentation

This section covers slicing up a large project, like processing the ESTC, into smaller tangible realistic-for-one-person-to-do bits.

* How to section the work  
* Is an initial common cleaning pass needed? E.g. Duplicated ids in ESTC.  
* Making sure that everyone uses common start off point, and that any processed data that is needed in further downstream tasks is held in a centralised location \--- so the common data items need a shared location (possible with versioning) to ensure that everyone is working off the same data, but the pipelines can be separate and isolated to enable easier work on different parts.  
* and how to account for the fact that some parts depend on others (e.g. publisher statements and publication years and places), how to keep track of this  
* Interface between different parts: separate code repositories that export and import commonly agreed data formats (csv, json), or one gigantic system?  
* Stitching it all back together again: using a common id format for joining exploded records  
* Figuring out which parts of the initial data feed into which parts of the final output.

A practical way to organise the project is to give each processing module an agreed input, output, responsible contributor and validation procedure. Publication dates, places, physical descriptions and actors can then be developed separately while remaining connected through stable ESTC identifiers. These modules also need an explicit dependency map: identifying an actor may depend on an already harmonised publication place and date, while a subsequent correction to either may require the actor matching to be revisited. Each output should record the versions of its inputs, so that improvements can be propagated without silently combining incompatible stages of the dataset. Our Best Practices in Bibliographic Data Science already illustrates these dependencies in the ESTC workflow; this training material could turn that principle into a practical planning exercise.

One of the major benefits of modular and iterative structure in the data that is being produced is the ability to utilize it for research along the way. The data processing work does not need to be exhaustively completed to be useful for research articles, but by focusing on e.g. prices of publications, or their genres, it has been possible in our ESTC related projects to get meaningful historical knowledge out of the dataset even if some other parts of the data unification have still been under work. see e.g. (\[Iiro’s price article\], \[the old canon article/book section\]). Then, as further data work is completed, or old work is refined to a better or more nuanced level, the benefits from the interlinked and interoperable nature of the dataset start cascading. More nuanced historical inquiries can be made, when the phenomena under focus can be approached from multiple interlinked points of view stemming from the accumulating interlinked refined data. \[Example of an article using multiple aspects of refined ESTC?\]

***Emphasize: good workflow between parts, ease of updating data internally, consistency in naming conventions, ensuring everyone is working on same data version / from same source***

*The above could be a separate workflow planning section, and go into some detail:what file formats to use (cvs, json, parquet), how to keep up-to-date accessible common data source (git), separators in csv files, common understanding of practices and documentation (lack of, or too much: dangers of bloated confusing documentation with agentic workflows).*

The ESTC work was partitioned by historical aspects of book production, that overlap with specific MARC fields in the raw data, but do not line up with them one-to-one. Some parts were relatively simple: (Short) titles and publication years were quite quick to process, but other facets, such as author and booktrade actor data, book prices or topic keywords took multiple passes, and a considerable effort. As examples below, we’ll focus on **publication years** and **publication locations**. 

The most important points to keep in mind for the segment below are these principles:

* **Using a common storage location**: The data, both the starting raw data, as well as the outputs of the processing pipelines, are kept in a **single shared Git** **repository**. This ensures that all workflows start from a common point, as long as the repository is periodically checked. The use of such established automated practices is heavily recommended: they sidestep the need to manually check a Google Drive folder or other similar solution for an up-to-date version, take care of versioning automatically, and offer a solution to keep all related documentation connected with the data.  
* Use of repositories and **versioning for processing code, documenting** the code well enough along the way, and keeping processing code for different sections of the data isolated from each other. This ensures reproducibility, possibility of taking up the work again after a pause in work in a specific section, and possibility of passing on the responsibility of a section of the workflow to another researcher.  
* Ensuring that **common data practices** are followed in different workflows. This covers agreeing on file formats to use (csv and json are universally good and accepted, but even there details might need to be covered: E.g.: What kind of separators are used in csv tables, how empty values are stored, and how multiple values in a single field are stored? A good starting point here might be following the FAIR data principles, see [https\://www\.gofair.foundation/fair-principles](https://www.gofair.foundation/fair-principles) ). Another important point here is to make sure that internal linking of the data works seamlessly: The style of unique identifiers to link parts of the data back together should be set, and followed.  
* Keeping the possibility, or aim, of **data publication** in mind from the start of the project. Even if it might not be the end goal of the project, open data publication is more and more seen as a merit in the scientific community, and besides possible other users in the research field, even the researcher’s (or research group’s) own internal use will benefit greatly from keeping the quality bar high enough, so that the data could be published at some point. This ensures that both the content of the processed data, and the workflow is documented well enough, and the data is understandable even after it has been unused for a while, and the choices made are not anymore in immediate memory.

Another section on coordination, communication and documentation? Best practices / this might work…

## Harmonizing

\[Examples of data harmonization workflows, by “thread”- e.g. publication year, price, location, actors\]

In the ESTC project, different subsections of the dataset needed vastly different amounts of work, and crucially, many of them could be worked on independently of each other, as outlined in the previous section. Below we’ll look at three examples of data harmonisation workflows: Publication year, publication location and actors related to each title (authors, publishers, printers).

#### External data

In multiple places in the ESTC workflows, additional external data sources are used with the unification process. The location processing code uses data from the Getty Thesaurus of Geographic Names, and the actor pipeline uses multiple external data sources, including VIAF (The Virtual International Authority File), Wikidata, and others. External authority resources provide valuable evidence for harmonisation, but their suitability needs to be assessed for each task. A standardised place name may conceal historical changes, and an authority record for a person may not establish which role that person performed in a particular publication. Matching should therefore retain the original statement, the proposed identification, the supporting source and any unresolved alternatives. Printer, publisher and bookseller roles should remain distinct wherever the evidence permits. Unmatched or uncertain cases should be represented explicitly, allowing later work to improve the identification without losing the earlier evidence. 

### Publication years

### Places

### Actors

## Evaluation

Validation should accompany each module and also examine the assembled dataset. Automated checks can establish whether identifiers remain unique where required, relationships point to existing records, and transformations have unexpectedly removed information or multiplied records. Historical validation asks a different question: whether the interpretation is supported by the catalogue statement or other evidence. For the training exercise, participants could construct a small, manually reviewed reference set containing both common and difficult cases, then reserve a separate sample for evaluation. Reviewing difficult cases helps improve the method, while a representative sample is needed to estimate how often errors occur across the dataset. Changes in aggregate distributions can flag problems for investigation, but cannot alone establish correctness.

GENERATIVE AI

The choice between explicit rules, machine learning and generative AI should follow the problem being solved. Regular, well-understood patterns are suitable for reproducible parsing rules; ambiguous statements may benefit from models that propose structured interpretations for review. Model outputs should retain their supporting source text and pass the same validation requirements as other transformations. When models are used, record the model version, instructions and review procedure, and evaluate the results against examples that were not used to develop the method. For teaching purposes, applying a rule and a model to the same small set of statements would make their different strengths and failure modes visible.

## Publication

Publication can be treated as a recurring checkpoint throughout the project. Each release should identify its source snapshot, processing-code version, included modules, validation results and known limitations, enabling researchers to cite and reproduce the particular dataset they used. A release can be useful while some fields remain unfinished, provided its scope and uncertainty are clear. The training material could conclude with participants preparing a small release package containing the refined data, a field dictionary, a transformation record and an evaluation summary, together with clear reuse conditions. This would extend the iterative relationship between harmonisation, analysis and validation described in [Open Bibliographical Data Workflows and the Multilinguality Challenge](https://doi.org/10.5334/johd.190) into a concrete, assessable learning outcome.

* Licensing \- is the more permissive better?  
* Keeping publication in mind while working on the data- leading to more benefits down the line, pre-emptive need to make messy “good enough for research” data publication ready, and as a side effect keeping the workflow cleaner too.  
* Publishing data, code, both?  
* Publishing platforms: zenodo, Harvard dataverse, university repositories, git (hub)  
* Doi for publication, DOIs for versions of publication.  
* Subsections of data: publication separately, or one package that gets updated? Both with references?