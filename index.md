# From catalogue records to research data

**A repeatable workflow for refining bibliographic metadata**  
*Learning material draft · Harmonisation, validation and dissemination*  
*Case study: publication years and places in the English Short Title Catalogue (ESTC)*

*![An ESTC date statement \[1787?\] becomes year 1787 and an explicit uncertainty flag while retaining its original text. An editorial timeline shows understanding, planning, refinement, evaluation and publication, with evaluation returning to planning. Typeset in Source Sans 3 and Ibarra Real Nova.][image1]*

*Figure 1\. A repeatable workflow for bibliographic refinement. Evaluation informs revision, while source evidence and uncertainty remain available in the resulting dataset.*

## Introduction

Bibliographic metadata supports the description, discovery and interpretation of published material. Using it for new purposes—such as analysing publishing patterns, connecting collections or preparing reusable datasets—requires understanding how records were created and how their information can be transformed. This material presents a repeatable workflow for assessing, refining, validating and publishing bibliographic metadata while preserving its source evidence and uncertainty.

The material is intended for researchers, librarians, cataloguers, metadata and research-data specialists, and others interested in working with bibliographic data. These readers bring complementary expertise: knowledge of collections and cataloguing practices, historical and subject knowledge, and experience with data modelling and processing. The workflow provides a common framework for making decisions and evaluating results across these roles.

Publication years and places in the English Short Title Catalogue (ESTC) provide the worked examples. They demonstrate how to inspect source records, define an output structure, organise connected processing tasks, evaluate transformations and prepare a documented release. The principles can be adapted to other catalogues and purposes. Familiarity with tables is helpful; MARC fields and other technical concepts are introduced where they are needed.

### Learning outcomes

By the end of this lesson, you should be able to:

* Explain how a catalogue’s purpose, coverage and cataloguing history affect its use in research.  
* Define a research or data-reuse objective, identify relevant source fields and specify what each output row represents.  
* Organise refinement into clearly documented tasks with distinct responsibilities and dependencies.  
* Understand the example cases of: Refining dates and places while retaining source statements, uncertainty and unresolved cases.
* Distinguish structural validation from evaluation of the accuracy of he results.  
* Prepare a versioned dataset with sufficient documentation for others to assess and reuse it.

## An iterative workflow

Refining a large dataset is an iterative process. For example, work on publication years may reveal a need to distinguish date ranges; place processing may expose uncertainty in imprints or differences in cataloguing practice. These findings may lead to changes in the output structure, processing rules or research question. Keeping successive versions to make those changes traceable. The following steps describe a sensible approach to such a task:

1. **Map and plan.** Understand the source fields and decide what the research-ready output should represent.  
2. **Plan the work.** Agree and set shared conventions, divide tasks and identify which steps rely on earlier results.  
3. **Extract and refine.** Transform one field at a time, retaining evidence and unresolved cases.  
4. **Validate and publish.** Test the results and publish them with code, documentation and a clear statement of scope.

Data and research publications can progress in tandem: E.g. a first data publication can contain the refined year table and place links while actor identification continues. Number the release and document its source snapshot and the versions of its year and place tables. Actor data can be added in a later version, noting changes to the earlier tables. Researchers can cite the version they used (see publication section below), and work with the data at each stage as methods and evidence develop.

# Reading the examples

Bibliographic metadata describes publications and related entities, such as people, places and surviving copies. A catalogue record brings together several kinds of information, but records, works, editions and physical copies are different units. Counting one does not necessarily measure another.

MARC 21 is a structured format for bibliographic records. Its numbered fields contain information divided into subfields. For example, 260 \$c identifies subfield \$c of field 260, used here as a source of publication-date statements. You do not need to memorise these codes: the examples explain the ones they use.

Harmonisation makes differently expressed information comparable while retaining meaningful distinctions. A date statement can be represented by numerical values for analysis while its original wording and uncertainty remain available.

A stable identifier connects information about the same record across tables. A link table stores relationships: for example, a record associated with two places has two record–place links. An authority resource supplies identifiers and descriptions for entities such as people or places. It can help connect variant names, but a proposed match still needs evaluation.

## 1\. Map the source and plan the output

Before writing transformation rules, examine the source, its history and the intended use. The ESTC brings together records created over an extended period by different contributing institutions. Cataloguing conventions have varied across institutions and over time. An apparent inconsistency may reflect historical variation, a cataloguing decision or an error; examine the record before changing it.

Also consider what the catalogue covers. The absence of a record does not establish that a publication never existed. Likewise, information absent from a catalogue record may be present in the physical object or another source. Refinement should make available evidence easier to use without concealing these limits.

### Choose the unit of analysis - standardising the research inputs

Reserch, especially quantitative approaches, needs data units that represents similar items. With biblographic data this might not be the case: Decide whether each output row represents a catalogue record, an edition, a work or a surviving copy. In these ESTC examples, a decision was made to equate an ESTC MARC record with an edition of a work, even though this is not always the case in the catalogue, but explicitly stating such choices will help with resolving ambiguity present in the source data. The year table presented in the below examples has one row per record identifier. Place data uses a separate link for each record–place association.

In rare cases, data does not conform to expectations: For example, the record T146309 has links to both London and Paris in the place-link file. It counts once in the master record table and twice in the place-link table. Joining the links to the record table produces two rows for that record. Whether this is appropriate depends on what is being counted.

Looking at the year table output, we see that it keeps the original transcription and adds parsed values:

| estc\_id | original | publication\_year\_from | publication\_year\_till | publication\_year | uncertain | circa | range |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| N72335 | \[1787?\] | 1787 | NA | 1787 | TRUE | FALSE | FALSE |
| T146309 | 1711\. | 1711 | NA | 1711 | FALSE | FALSE | FALSE |
| N62219 | ca. 1785-1800\] | 1785 | 1800 | 1785 | FALSE | TRUE | TRUE |

The question mark in \[1787?\] sets the uncertain \-flag, while the single year is kept. ca. 1785-1800\] gives both endpoints and sets circa and range; publication\_year takes the first endpoint. Keeping the table at one row per identifier ensures that it can be joined to the record core without multiplying rows.

The place link table excerpt below has one row for each record–place association. As mentioned, record T146309 has two links in the file:

| estc\_id | geo\_id |
| :---- | :---- |
| T146309 | \<http\://vocab.getty.edu/tgn/7011781\> (London, England, Great Britain) |
| T146309 | \<http\://vocab.getty.edu/tgn/7008038\> (Paris, France) |

### Build a field map \- how the source matches the output

Identify where the source records contain evidence for each concept needed by the project. A concept may appear in several MARC fields, and one field may contain several kinds of information, as illustrated by the examples below.

**Publication year**: the worked example begins with field 260 \$c. Roman numerals, brackets, uncertainty, approximate dates and wording are all encoded in the same field. Some examples from the year data:

| Encoding | Example value | Record |
| :---- | :---- | :---- |
| Plain year | \[1708\] | N72338 |
| Uncertain (question mark) | \[1787?\] | N72335 |
| Roman numerals with a bracketed year | M.DCC.LXVI. \[1766\] | N71014 |
| Roman numerals, no brackets | MDCCLXXIV. 1774\. | N10003 |
| Circa | \[ca. 1740\] | N71861 |
| Circa and uncertain | \[ca. 1719?\] | N34110 |
| Range | \[1791 \- 1839\] | N71524 |
| Range in words | between 1760 and 1800\] | N71859 |

Related dates elsewhere in the record may describe something different: for example, 240 \$f supplies a date associated with a work.

Publication place: The below table illustrates the input values of the place name processing code. Note how, even if the source data is more structured, there still is considerable variation in its form and content.

| Field | Example value |
| :---- | :---- |
| 752 \$a, \$b, \$d | Great Britain, England, London. |
| 752 \$c, \$f | Dorset, Dorchester. (\$c county, \$d town) and Westminster. (\$f) |
| 752 with no \$b or \$c | Ireland, Dublin. |
| 260 \$a imprint place | Westminster :, Dorchester : |
| 260 \$a in brackets | \[London\] : |
| 500 \$a note on the imprint | Imprint from colophon. |
| 500 \$a note on a pseudonym | Isaac Bickerstaff is a pseudonym, and this is possibly a pastiche. |
| 008 country code | enk (England), ie (Ireland) |

### Design an output that can grow

Use the research question or intended use to define a concise output structure. Keep source statements available alongside interpreted values and connect them through stable identifiers. Store repeated values in linked tables, and distinguish absent information from information that is present but unresolved.

### Planning exercise

For a record associated with two publication places, decide whether the intended analysis counts one record or two record–place associations. Explain the difference and document the choice.

## 2\. Plan a repeatable workflow

Divide the work into parts that can be developed and checked independently. For each part, specify its source data, expected result, responsible contributor, transformations and checks. Contributors can then work on different fields while using agreed identifiers and compatible inputs.

Separate the shared data arrangement from the organisation of the code. Keep an identifiable, versioned source snapshot and checked component outputs in a shared data location. Keep processing code and run instructions in version-controlled repositories. One repository or several can work, provided contributors know which inputs to use and how their outputs will connect. Large or restricted datasets need an appropriate data store; they need not be placed in the code repository.

Before processing, agree on:

* Identifiers, file formats, column names, separators and character encodings.  
* How missing, uncertain and multiple values will be represented.  
* Where approved inputs and outputs can be found, and how their versions are identified.  
* How each processing step is run and checked.  
* Which steps depend on earlier results.  
* How corrections are communicated and incorporated into later releases.

Dependencies matter. In the ESTC workflow, actor identification uses harmonised titles, places and years. A correction to these inputs may require actor matching to be revisited. Record the input versions used by each component so that these consequences can be identified.

A checked subset can be released while other components remain unfinished. Document the included fields, unfinished work, source snapshot and processing version. Later releases should explain changes to existing tables as well as additions.

## 3\. Extract, refine and unify the fields

Begin with a small sample and inspect values in context. Record the rules before applying them more widely, and retain source statements alongside derived values.

The examples below describe choices in an ESTC implementation. They demonstrate how to make decisions explicit, but those decisions should be reassessed when the data or intended use changes. Distinguish source evidence, its interpretation and any additional grouping introduced for analysis.

### Worked example A: publication years

The year table begins with the transcription from 260 \$c, stored unchanged in an original column and connected to the ESTC identifier. Parsed values can therefore be checked against the catalogue text.

The examples illustrate several patterns:

* 1711\. supplies a single year, 1711\.  
* \[1787?\] supplies a year while retaining the question mark as an uncertainty flag.  
* ca. 1785-1800\] supplies two endpoints and retains both approximation and range flags.  
* between 1700 and 1799\] supplies an interval whose endpoints should remain available.

These distinctions affect interpretation. A range is not equivalent to a precisely dated publication, and an approximate date is not the same as an unqualified one. Missing or unparsed values should remain identifiable rather than being silently converted into apparently exact dates.

Before analysing intervals, decide how they will be treated. Selecting one endpoint can simplify aggregation, but it also affects the apparent distribution of publications over time. A record dated between 1700 and 1799 cannot confidently be assigned to the first decade of that century.

**Technical note: the year table**

The implementation described in the project draft includes estc\_id, original, publication\_year\_from, publication\_year\_till, publication\_year, uncertain, circa and range. The flags can overlap.

Its publication\_year field takes the first endpoint when available, otherwise the last. Decade and century fields are derived from that selected value. These are processing conventions rather than additional evidence about publication. Analyses should explain whether they use this value, exclude ranges or handle intervals through another method.

The source file described in the draft is tab-separated despite its .csv extension. Check the delimiter, field types and identifier uniqueness when loading it. A one-row-per-identifier year table can be joined to a one-row-per-identifier record core without multiplying records. Identify the exact data and code versions when reproducing this implementation.

### Worked example B: publication places

The place workflow brings together structured place information, imprint statements and relevant notes. It begins with MARC 752, retaining country, state or region, and place components. A record may have more than one such statement, so the output must preserve multiple associations.

The implementation applies explicit rules to these components. Examples include removing punctuation from matching values, expanding abbreviations, reorganising country and state information, and mapping variant place names. Keep the unmodified source values so that each transformation remains inspectable.

Some rules standardise expression; others introduce analytical categories. Expanding St Andrews to Saint Andrews differs from grouping Twickenham or Croydon under London. The latter may support a study of a wider publishing area while obscuring distinctions needed for local history. Preserve the more specific source place and document the grouping separately. Decisions about historical names and geographical hierarchies should likewise state their purpose.

Notes can supply evidence that differs from the imprint. In the ESTC example, a script selects notes containing both “false” and “imprint” for manual curation. Such a search identifies a particular set of candidate notes; it does not establish that every false imprint has been found. Retain the stated imprint place, the proposed corrective place and the evidence for their relationship.

Uncertainty expressions should also remain available. A bracketed place, a question mark and a correction introduced by “i.e.” are different features. Recording them helps readers examine interpretations, but simply counting the features does not establish a calibrated scale of confidence.

The workflow connects harmonised place descriptions to Getty Thesaurus of Geographic Names (TGN) identifiers where a suitable match is available. Authority resources support identification; shared names and plausible coordinates alone do not guarantee that a match is correct.

The output separates three functions: describing places, connecting records to places, and recording attributes of each catalogue record. This supports different questions without making one table serve every purpose.

**Technical note: the place tables**

The implementation described in the project draft produces:

* estc\_geo\_identifiers.tsv: place descriptions, identifiers, coordinates and matching-related information.  
* estc\_edition\_to\_place\_geo\_links\_post\_evaluation\_fixes.tsv: record–place associations incorporating the documented evaluation corrections.  
* estc\_places\_edition\_attributes.tsv: record-level attributes, including numbers of related places and imprint-related flags.

Despite “edition” in the filenames, check what the identifiers and rows actually represent before interpreting them as edition-level evidence.

The matching script queries preferred and alternative labels in TGN, including language-tagged searches, and saves results for reuse. Its geo\_score ranks candidates using the number of alternative place types recorded in TGN. This measures a feature of the authority description; it is not a calibrated probability that an identification is correct. Evaluate ambiguous matches independently.

Joining the place-link table to either place descriptions or record attributes retains one row per record–place association. A record linked to two places still has two rows. To obtain one row per catalogue record, use the record-level table or explicitly aggregate the links.

### Make decisions inspectable

For derived values, retain or link to the source statement, transformation rule, supporting resource and unresolved alternatives. Record external-resource versions where available, or the retrieval date and query details where the resource changes over time.

Explicit parsing rules suit regular, well-understood patterns. Machine-learning or generative-AI systems can propose interpretations of ambiguous statements, but their outputs require evaluation. Record the model version, instructions and review procedure, preserve the input evidence, and use evaluation examples that were not used to develop the method. These are possible extensions of the workflow, not prerequisites for following this lesson.

## 4\. Validate and evaluate

Validate each component as it is developed, then check the assembled tables. Structural validation asks whether the data follow their declared organisation. Evaluation of interpretation asks whether derived values are supported by the source evidence. Both are necessary.

Structural checks include:

* Required fields and expected data types.  
* Unique identifiers where one row per identifier is required.  
* Valid links between tables.  
* Expected row counts before and after joins.  
* Unexpected changes in value distributions or missing information.  
* Traceability from derived values to source evidence.

Interpretive evaluation requires reviewed examples. Include ordinary and difficult cases when developing the method, and use a separate representative sample when estimating performance across the dataset. A collection of difficult examples is useful for finding weaknesses, but it does not by itself measure how frequently those weaknesses occur.

Define what counts as correct, incorrect, partly correct or unresolved. For a place match, distinguish correct interpretation of the catalogue statement from correct identification of the historical publication place. Agreement with the catalogue does not independently establish historical truth.

### Evaluation example: publication places

The project draft describes a comparison of raw and processed place information for a random sample of 300 records. A separate review of 100 TGN identifiers found four incorrect identifications, which were corrected. These observations illustrate why field transformations and authority matching need separate checks.

A published evaluation should identify the tested data and code versions, sampling procedure, review criteria and results before corrections. Explain how corrections were incorporated and whether a further evaluation was performed. Report information loss with a clear definition and denominator. Results describe the tested version and sample; corrected examples alone do not establish the accuracy of the full release.

## 5\. Publish a documented dataset

Plan for publication from the beginning so that decisions, code and data remain understandable as the work progresses. A partial dataset can be useful when its scope, status and limitations are explicit.

A release should include:

* Refined tables and a field dictionary explaining identifiers, units and relationships.  
* Source-snapshot and processing-code versions.  
* External authority-resource versions or retrieval information.  
* Code or processing instructions, with key decisions documented.  
* A validation and evaluation summary.  
* Known limitations, unresolved cases and unfinished components.  
* Access conditions, reuse conditions and licensing information for data and code.  
* A citation identifying the particular release.

Choose a repository according to preservation needs, access conditions and institutional or funder requirements. Options include general-purpose repositories such as Zenodo, Dataverse repositories and institutional services. Library and research-data support colleagues can help assess the appropriate route. Use a code repository for active development and connect it to the archived release where appropriate.

A persistent identifier helps users locate and cite a release, but does not itself establish data quality. Clearly identify the files and versions used in an analysis, and explain changes between releases. Check source terms and third-party material before selecting reuse conditions.

For an ESTC release, document how the refined tables relate to the source catalogue and to the COMHIS/estcr harmonised data used by the project. Identify the actual source and transformation versions rather than assuming that similarly named files are equivalent. The supplied examples describe a particular workflow and should not be presented as documentation of every subsequent release.

## Practical exercise

Work with a small supplied selection of ESTC records, or a comparable sample from another catalogue. State the intended use and identify what each output row represents. Include straightforward cases and cases involving uncertainty, date ranges or multiple places.

## **Route A: inspect and evaluate**

Use source records and prepared output tables without running code. Identify the evidence supporting each interpreted date or place. Examine whether uncertainty and multiple values have been preserved, and propose corrections or alternative interpretations where necessary. Check how a record with two places affects totals before and after tables are joined. Record which decisions require cataloguing knowledge, subject knowledge or further evidence.

## **Route B: implement and evaluate**

Run or adapt the supplied processing instructions for the same sample. Retain identifiers and original statements, document transformation rules and produce the output tables. Check identifiers, links and row counts, then compare interpreted values with the source evidence. Record failures and unresolved cases as well as successful transformations.

Both routes produce a small documented result: an output table or annotated evaluation, a description of fields and relationships, a record of decisions and a short validation summary. Identify source and processing versions where applicable, and explain what another user would need to assess or reuse the result.

## **Questions for discussion**

How do the choices affect counts of publication years or places? Which decisions could be automated reliably, and which require review? What information should remain available so that another person can reach a different interpretation? What knowledge did different participants contribute? 

## Conclusion

Refining bibliographic metadata connects knowledge of catalogues and collections with data modelling, evaluation and interpretation. Define what the data represent, distinguish source evidence from derived values, and record the decisions connecting them.

Researchers, library professionals and other contributors can participate at different points in this workflow. Shared identifiers, documented dependencies and evaluated releases allow their contributions to accumulate. The aim is to produce data whose meaning, transformations and limitations remain understandable to its next users.

**References and working materials**

**Bibliographic data and workflows**

Lahti, Leo, Jani Marjanen, Hege Roivainen and Mikko Tolonen. “Bibliographic Data Science and the History of the Book (c. 1500–1800).” Cataloging & Classification Quarterly 57(1) (2019), 5–23. https\://doi.org/10.1080/01639374.2018.1543747

Lahti, Leo, Ville Vaara, Jani Marjanen and Mikko Tolonen. “Best practices in bibliographic data science.” Proceedings of the Research Data and Humanities (RDHUM) 2019 Conference, 57–65. https\://www\.utupub.fi/server/api/core/bitstreams/3e17b694-fb6e-47e5-8596-41613cc7138d/content

“Open Bibliographical Data Workflows and the Multilinguality Challenge.” https\://doi.org/10.5334/johd.190

**Research using ESTC data**

Tiihonen, Iiro, and Kira Hinderks. “Genre Classification Workflow for the English Short Title Catalogue (ESTC).” Transformations: A DARIAH Journal, “Metadata-based workflows” (2025). https\://doi.org/10.46298/transformations.14754

Tiihonen, Iiro, Leo Lahti and Mikko Tolonen. “Print culture and economic constraints: A quantitative analysis of book prices in eighteenth-century Britain.” Explorations in Economic History 94 (2024), article 101614\. https\://doi.org/10.1016/j.eeh.2024.101614

**Standards and project materials**

MARC 21 Format for Bibliographic Data: https\://www\.loc.gov/marc/bibliographic/

COMHIS/estcr harmonised ESTC project: https\://github.com/COMHIS/estcr

FAIR principles: findability, accessibility, interoperability and reusability.

ESTC concept–MARC field mapping and the versioned project scripts accompanying the examples.

Draft for discussion and adaptation for DARIAH-Campus. ESTC is used as a case study; field structures and cataloguing practices vary across catalogues.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAjAAAAFUCAYAAAA6fAa+AAA6e0lEQVR4Xu3d368lVZ338f4vuPDGmybhQq860QsTE4hcwBWJCV6YQNoMXjj0j8BosBtRZhwydngwD2ZmGgRM/NE/YEAx6dMwTCJgNzrjiJFGRJ44QzeJiUBCzwRvz3M++5zPPt/9Patq1/69197vV1I5VatWrapaVbXqu1fV2XvfJgAAQGX25QQAAIBlRwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqM7cA5sSDD/WH02eeyrNbXfORj24t9+2c3KN5GuL4LZ/9XMrVXd62WD4AAFgOcwtgHAjkoYuuAYw05esqb9PpM09unjv//EAaAABYrLkHMHn66tWrmxsbz20e+OSn+vM0HqcdwHiZU2efHJjnctXzouVOPvp4f756fJznypUrvTSt02mHjtzVz6tllRbXn7dFcnkS96G0nXLp0uu9PFq/5fK9bO5Fuva6jw/sq3lZzwcA1OXzXzwyMOT0bz74nWK+p396vpeu+U57+8o7/eW9THT0q/f3/8ZBfvfmW738//y9H/Xzl9K8vpiWy5qHhQcwl7eCAPVylObl6TjkeeIAxL0wMXjRcOATgwGGBwcUOT2XX8pz6OjdvXTvQx4ypcXgpFfGThCVl3XPT06P5Wo87icAoC45yBAFCR9++Jfe+MkQKEjM/+67728euWc3aHj62e2gxu44ck+/HHGA8e577/cHl+dy7jh6z3aeUPYRL7eVpqAm5pNjf3uiX968zD2AUcBy8tHHBm64XQKY2w7+VW98/3Uf6007CIh5cwCTy7H4SEjz91/38d543g7Pd5rWmbfL01522LpjuurC48fv+8ZAfu+L81nbNgAA6lMKYI4cu38g8Ihi/tKykQKWmCf3kJSW/+/L7+xZ94sXfzkwLede+Fl/3L1B87QvJ8yKb7Rx8COYHDjkm7LGHRjoUU2cH8dLAUzpnRgHC3GQvB3StK48nZfNee2DncdXtx+8ox+MSd6euPyFi68U071caR8BAHXw458cTKjXQ2nvpV6NUQIYzVevifPFAEbpfy70mOQyNf1SCGAUzOQ09fQoiMnLztLcA5iSYTf/eJO+88jdvekbPnPTnrylAMa9K5HSL1z8RX/cy+ftyPNL29W0bM4beZ4GPz6KPS6Z0v3469DRu/ashwAGAOo17Kaf548awIiCDgVCMYCJj4DsqWc3ikGNgp3zL7y4J+2NP2w/TrK/23lfZx6WIoBxr0QezNO+yZfmSSmAiYMev4yyrlx+27KjBDB+DJTnO80vI+cgq2n/CWAAoF6lIOT//ONj/XG/f2IxvwKO2BMSxyUHOzGAyetVWXp8ZApQoh+ceWZPmnpdYlouc5aWIoCRGHzccONNe27S/qsh/vePA4fTZ5/aE8CIy9LggCDmy9vlHp68TvN7KxpOnd39zphRAhhpmu90DX652C/pxvd+Yn4CGACol276ccjpfmk2pkcKPJw3v7sS82peWwBT2g69QKxxvaSb8/m/o2JaqfdmVuYWwGCbgigHKA6oAADAaAhg5iz2sAAAgPEQwAAAgOoQwAAAgOoQwAAAgOoQwAAAgOoQwAAAgOoQwAAAgOoQwAAAgOrMJYC55tMHGRgYGBgYGNZkmIe5BDAAAADTRAADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqQwADAACqM/cA5tzLv9688Orvc/JYrvn0wZwEYI4O3PrlnNSja1PD6Y2fb5588l/z7AFN13FTOgDIXAMYNUiX//Tu5mtvvT20cTr0wOM5aY9hZcxDl2DsxBM/yUlzsbEVLGI5dTl3bzn8rZw0c122KyoFMLrGTzzx45zcqGmdTekAIHMLYNoaI31KO3DrVzZPbf2Vk08+35vWjd+f3px25U/v9ZfLZd5y+B/25BGlHXrgsV55Dibip8IcYFz/ha833jxUjsoTBQhaZyxXAU3clw/+98PNG7bKi3mubqVpubgOz9OyWr+4XjLvj3nZXGbeNiyPeO7q+Oic0HG//djDvTQFAftv/uuBa0DyuRmPvc69eB7Fc+S1ty7382ld4nPV14uW1Xbpr9NyHvO5Vgpgjj98qjdf14D249LWBxYrlZevY83X9R7TVU68rgBgKQIYi3ma8m83sNuf7pryq6FzI92c52+K6U3joobZ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>