# hackillinois-summarization
### About
Built an interactive website that allow users to upload multiple source materials(lecture notes, videos, articles...) and provide aggregated summary of multiple sources. Users can read the summary on the website and nevigate back to the original source by clicking on the sentence of the summary.\n
Further details can be found in below link:
https://devpost.com/software/cramberry

### Implementation
This is a summarization code on the flask server side. The overall architecture is as follows./n
1. Parse the multiple input video/audio/pdf source to text and metadata(video timeline, pdf page...)./n
2. Using the merged text from multiple source text, create a multi document summary. Each sentence in the summary has source type and according metadata to trace back to its original source./n
3. Refine the summary with openAI API call to chatgpt.
4. Respond to the server request with generated summary./n

### Graph based multi document summarization
As we needed to trace back the generated summary sentences to its original source, we used graph based summarization algorithm. Each sentence of the original text became nodes and the cosine similarity between sentences became weighted edges. A pagerank algorithm was used to generate important sentences from the graph, thus a summary.
