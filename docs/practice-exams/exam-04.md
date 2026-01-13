# Practice Exam 04 (Bonus Questions)

!!! info "Exam Details"
    - **Total Questions**: 6
    - **Estimated Time**: ~12 minutes
    - **Passing Score**: 72%

## Question 1

A company is planning to create an internal-only chat interface to help employees handle customer queries. Currently, the employees need to refer to a massive knowledge base of internal documents to address customer issues. The new solution must be serverless. Which combination of steps will meet these requirements?

- **A.** Set up Amazon Bedrock with the Anthropic Claude foundation model.
- **B.** Set up Amazon SageMaker JumpStart with the Llama foundation model.
- **C.** Use Amazon EC2 instances with Amazon API Gateway to invoke the model API.
- **D.** Use AWS Lambda functions with Amazon API Gateway to invoke the model API.
- **E.** Use an Amazon S3 bucket to store vector database dumps and embeddings. * F. Use Amazon RDS for MySQL to store vector database dumps and embeddings.

??? success "Reveal Answer"
    **Correct Answer: A**

    Câu hỏi yêu cầu một giải pháp hoàn toàn Serverless (không máy chủ) cho ứng dụng Chatbot RAG. Dưới đây là lý do chọn bộ ba này: Tại sao chọn A (Amazon Bedrock): o Amazon Bedrock là dịch vụ Serverless hoàn toàn (Fully Managed), cung cấp quyền truy cập vào các mô hình nền tảng (Foundation Models) như Claude thông qua API. Bạn không cần quản lý máy chủ hay endpoint như SageMaker (trừ khi dùng Serverless Inference, nhưng Bedrock là lựa chọn native hơn cho GenAI API). Tại sao chọn D (Lambda + API Gateway): o Đây là cặp đôi kinh điển của kiến trúc Serverless Compute trên AWS. API Gateway cung cấp điểm cuối REST/WebSocket để chat client kết nối, và AWS Lambda thực thi logic nghiệp vụ (gọi Bedrock API, xử lý context) mà không cần chạy server EC2 liên tục. Tại sao chọn E (Amazon S3): o Amazon S3 là dịch vụ lưu trữ đối tượng Serverless. Trong kiến trúc RAG (Retrieval-Augmented Generation), S3 thường được dùng làm "Data Source" để chứa các tài liệu nội bộ (Knowledge Base). (Lưu ý: Mặc dù cần một Vector Database để search, nhưng S3 là nơi lưu trữ dữ liệu gốc bền vững và serverless nhất trong các lựa chọn lưu trữ được đưa ra). Tại sao không chọn B (SageMaker JumpStart): Mặc dù JumpStart giúp triển khai model nhanh, nhưng nó thường triển khai lên SageMaker Real-time Endpoints (dựa trên EC2 instances), nghĩa là bạn phải trả tiền theo giờ cho instance chạy, không phải là Serverless thực thụ. Tại sao không chọn C (EC2): EC2 là IaaS (Infrastructure as a Service), yêu cầu quản lý server, vá lỗi, scaling thủ công. Nó vi phạm yêu cầu "Serverless". Tại sao không chọn F (RDS MySQL): Amazon RDS truyền thống yêu cầu provision instance. Dù có Aurora Serverless, nhưng trong ngữ cảnh RAG, S3 (cho raw docs) hoặc OpenSearch Serverless (cho vector) thường được ưu tiên hơn RDS MySQL tiêu chuẩn.

---

## Question 2

An ML engineer needs to deploy a trained model that is based on a genetic algorithm. The algorithm solves a complex problem and can take several minutes to generate predictions. When the model is deployed, the model needs to access large amounts of data to process requests. The requests can involve as much as 100 MB of data. Which deployment solution will meet these requirements with the LEAST operational overhead?

- **A.** Deploy the model to Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer.
- **B.** Deploy the model to an Amazon SageMaker real-time endpoint.
- **C.** Deploy the model to an Amazon SageMaker Asynchronous Inference endpoint.
- **D.** Package the model as a container. Deploy the model to Amazon Elastic Container Service (Amazon ECS) on Amazon EC2 instances.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Asynchronous Inference): o Xử lý Payload Lớn (100 MB): SageMaker Asynchronous Inference được thiết kế đặc biệt để xử lý các payload input có kích thước lớn (lên đến 1 GB) bằng cách upload dữ liệu lên Amazon S3 trước khi xử lý, thay vì gửi trực tiếp qua HTTP body như Real-time endpoint (thường giới hạn ở mức 6MB). o Thời gian xử lý dài (Long Prediction Times): Thuật toán di truyền trong đề bài mất "vài phút" để chạy. Real-time Endpoint có giới hạn timeout (mặc định 60s), nên kết nối sẽ bị ngắt trước khi model chạy xong. Async Inference cho phép thời gian xử lý lên tới 1 giờ, phù hợp hoàn hảo cho các tác vụ tốn thời gian. o Tối ưu vận hành (Least Operational Overhead): Đây là dịch vụ được quản lý hoàn toàn (fully managed), có sẵn tính năng hàng đợi (queuing) và autoscaling (thậm chí scale về 0 khi không dùng), giúp bạn không phải tự xây dựng hệ thống queue hay quản lý server EC2 thủ công. Tại sao không chọn A (EC2) và D (ECS): Cả hai giải pháp này đều là "Self-managed" (Tự quản lý). Bạn sẽ phải tự cấu hình Load Balancer, tự viết code để xử lý hàng đợi (queue) cho các request lâu, và tự lo phần scaling hạ tầng. Điều này tốn nhiều công sức vận hành hơn nhiều so với giải pháp có sẵn của SageMaker. Tại sao không chọn B (Real-time Endpoint): Real-time endpoint không hỗ trợ payload 100MB và không phù hợp cho các request kéo dài vài phút (sẽ gây timeout lỗi client).

---

## Question 3

An ML engineer wants to use a set of survey responses as training data for an ML classifier. All the survey responses are either "yes" or "no." The ML engineer needs to convert the responses into a feature that will produce better model training results. The ML engineer must not increase the dimensionality of the dataset. Which methods will meet these requirements? (Choose two.)

- **A.** Binary encoding
- **B.** Label encoding
- **C.** One-hot encoding
- **D.** Statistical imputation
- **E.** Tokenization

??? success "Reveal Answer"
    **Correct Answer: A**

    Câu hỏi đặt ra hai yêu cầu chính: chuyển đổi dữ liệu dạng văn bản ("yes"/"no") sang dạng số để mô hình hiểu được, và quan trọng nhất là không được làm tăng số chiều (dimensionality) của tập dữ liệu. Tại sao chọn B (Label encoding): Label encoding gán một số nguyên duy nhất cho mỗi nhãn. Với dữ liệu nhị phân "yes"/"no", nó sẽ chuyển thành 0 và 1 (ví dụ: No=0, Yes=1). Quá trình này thay thế 1 cột văn bản bằng 1 cột số, do đó số chiều của dữ liệu được giữ nguyên (1 column -> 1 column). Đây là cách đơn giản và hiệu quả nhất cho biến nhị phân. Tại sao chọn A (Binary encoding): Mặc dù với các biến có nhiều giá trị (high cardinality), Binary encoding thường tạo ra nhiều cột (logarit cơ số 2 của số lượng nhãn), nhưng với trường hợp đặc biệt chỉ có 2 giá trị ("yes"/"no"), Binary encoding hoạt động tương tự như Label encoding. Nó chuyển nhãn thành chuỗi nhị phân (0 hoặc 1) và lưu trong một cột duy nhất. Do đó, nó cũng thỏa mãn điều kiện không tăng số chiều. Tại sao không chọn C (One-hot encoding): One-hot encoding sẽ tạo ra một cột mới cho mỗi giá trị duy nhất. Với "yes" và "no", nó sẽ tạo ra 2 cột mới (ví dụ: is_yes và is_no). Việc biến 1 cột thành 2 cột vi phạm yêu cầu "must not increase the dimensionality". Tại sao không chọn D (Statistical imputation): Đây là kỹ thuật để điền các giá trị bị thiếu (missing values), không phải là kỹ thuật mã hóa (encoding) dữ liệu văn bản sang số. Tại sao không chọn E (Tokenization): Tokenization là bước tách văn bản thành các từ/token (thường dùng trong NLP). Bản thân nó chưa tạo ra feature số (cần qua bước vectorization như TF-IDF hay Embedding), và các bước sau đó thường làm tăng số chiều dữ liệu lên rất nhiều.

---

## Question 4

Question 139

!!! info "Matching"


??? success "Reveal Answer"
    **Correct Answer: D**

    Sequence-to-Sequence (seq2seq): Thuật toán này chuyên dùng cho các bài toán đầu vào là một chuỗi và đầu ra là một chuỗi, điển hình như dịch máy (Machine Translation) và tóm tắt văn bản (Text Summarization). Semantic segmentation: Đây là thuật toán thị giác máy tính phân loại từng pixel (pixel-level classification) trong ảnh. Nó rất quan trọng cho xe tự lái để phân biệt chính xác đâu là đường, vỉa hè, hay người đi bộ ở cấp độ chi tiết nhất. Random Cut Forest (RCF): Là thuật toán học không giám sát (unsupervised learning) chuyên dùng để phát hiện bất thường (Anomaly Detection). Nó rất hiệu quả trong việc tìm ra các điểm dữ liệu dị biệt (abnormal/outliers) trong tập dữ liệu.

---

## Question 5

A company is planning to use an Amazon SageMaker prebuilt algorithm to create a recommendation model. The algorithm must be able to make predictions on high- dimensional sparse data. Which SageMaker algorithm should the company choose for the recommendation model?

- **A.** K-nearest neighbors (k-NN)
- **B.** Factorization Machines
- **C.** Principal component analysis (PCA)
- **D.** Sequence-to-Sequence (seq2seq)

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Factorization Machines): o High-dimensional sparse data: Thuật toán Factorization Machines (FM) trong Amazon SageMaker được thiết kế đặc biệt để xử lý các bộ dữ liệu thưa (sparse) và nhiều chiều (high-dimensional). o Recommendation Model: Đây là thuật toán tiêu chuẩn cho các hệ thống gợi ý (Recommender Systems), ví dụ như dự đoán người dùng có click vào quảng cáo hay không (Click-through rate prediction) hoặc dự đoán xếp hạng item, nơi mà ma trận tương tác giữa người dùng và sản phẩm thường rất thưa thớt (rất nhiều số 0). Tại sao không chọn A (K-nearest neighbors - k-NN): o Mặc dù k-NN có thể dùng cho gợi ý (dựa trên sự tương đồng), nhưng nó thường gặp khó khăn về hiệu năng (curse of dimensionality) khi làm việc với dữ liệu quá nhiều chiều và thưa thớt so với Factorization Machines. Trong SageMaker, k-NN thường được dùng cho classification hoặc regression dựa trên chỉ mục (index-based). Tại sao không chọn C (Principal component analysis - PCA): o PCA là thuật toán giảm chiều dữ liệu (Dimensionality Reduction), không phải là thuật toán để xây dựng mô hình dự đoán hay gợi ý trực tiếp. Nó thường được dùng ở bước tiền xử lý (preprocessing). Tại sao không chọn D (Sequence-to-Sequence - seq2seq): o Seq2Seq là thuật toán học có giám sát chuyên dùng cho xử lý ngôn ngữ tự nhiên (NLP) như dịch máy, tóm tắt văn bản, nơi đầu vào và đầu ra là các chuỗi (sequences). Nó không phù hợp cho dữ liệu bảng thưa thớt của bài toán gợi ý thông thường.

---

## Question 6

ssss A company has several teams that have developed separate prediction models on their own laptops. The teams developed the models by using Python with scikit-learn and TensorFlow frameworks. The company must rebuild the models and must integrate the models into an ML infrastructure that the company manages by using Amazon SageMaker. The company also must incorporate the models into a model registry. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Export the models from the laptops to an Amazon S3 bucket. Use an Amazon API Gateway REST API and AWS Lambda functions with SageMaker endpoints to access the models. Register the models in the SageMaker Model Registry.
- **B.** Import the models into the SageMaker Model Registry. Use SageMaker to run the imported models.
- **C.** Use code from the laptops to create containers for the models. Use the bring your own container (BYOC) functionality of SageMaker to import and use the models. Register the models in the SageMaker Model Registry.

??? success "Reveal Answer"
    **Correct Answer: ?**

    No detailed explanation provided.

---

