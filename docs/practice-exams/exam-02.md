# Practice Exam 02

!!! info "Exam Details"
    - **Total Questions**: 65
    - **Estimated Time**: ~130 minutes
    - **Passing Score**: 72%

## Question 1

Case Study - A company is building a web-based AI application by using Amazon SageMaker. The application will provide the following capabilities and features: ML experimentation, training, a central model registry, model deployment, and model monitoring. The application must ensure secure and isolated use of training data during the ML lifecycle. The training data is stored in Amazon S3. The company needs to use the central model registry to manage different versions of models in the application. Which action will meet this requirement with the LEAST operational overhead?

- **A.** Create a separate Amazon Elastic Container Registry (Amazon ECR) repository for each model.
- **B.** Use Amazon Elastic Container Registry (Amazon ECR) and unique tags for each model version.
- **C.** Use the SageMaker Model Registry and model groups to catalog the models.
- **D.** Use the SageMaker Model Registry and unique tags for each model version.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Use the SageMaker Model Registry and model groups): Đây là đáp án chính xác nhất vì Amazon SageMaker Model Registry là tính năng được thiết kế chuyên biệt (purpose-built) để quản lý vòng đời của mô hình. Khái niệm "Model Group" (Nhóm mô hình) trong Model Registry cho phép bạn gộp các phiên bản khác nhau của cùng một mô hình lại với nhau. Khi bạn đăng ký một mô hình mới vào một Model Group, SageMaker sẽ tự động đánh số phiên bản (version 1, 2, 3...) mà không cần thao tác thủ công phức tạp. Điều này đáp ứng hoàn hảo yêu cầu "LEAST operational overhead" (ít chi phí vận hành nhất). Tại sao không chọn A (Create a separate Amazon ECR repository for each model): Amazon ECR (Elastic Container Registry) là nơi lưu trữ Docker container images, không phải là nơi chuyên dụng để quản lý các artifact của mô hình ML hay metadata (như độ chính xác, tham số huấn luyện). Việc tạo một repo riêng cho từng mô hình sẽ gây ra sự lộn xộn, khó quản lý (management sprawl) và tốn rất nhiều công sức vận hành để theo dõi phiên bản, hoàn toàn đi ngược lại yêu cầu "ít chi phí vận hành". Tại sao không chọn B (Use Amazon ECR and unique tags): Mặc dù ECR hỗ trợ tags để đánh dấu phiên bản image, nhưng nó vẫn chỉ là nơi lưu trữ container image. Nó thiếu các tính năng cốt lõi của một Model Registry như: quy trình phê duyệt (approval workflows), theo dõi nguồn gốc (lineage tracking), và liên kết metadata của mô hình. Sử dụng ECR để thay thế Model Registry đòi hỏi phải xây dựng thêm các công cụ tùy chỉnh, gây tốn kém chi phí vận hành. Tại sao không chọn D (Use the SageMaker Model Registry and unique tags): Mặc dù sử dụng đúng dịch vụ là SageMaker Model Registry, nhưng cách dùng "unique tags" để quản lý phiên bản là không chính xác về mặt kỹ thuật và quy trình. Trong SageMaker Model Registry, cơ chế quản lý phiên bản chuẩn là thông qua Model Groups. Tags thường được dùng để thêm metadata (ví dụ: stage: production, project: alpha) chứ không phải là cơ chế chính để catalog các phiên bản mô h...

---

## Question 2

Case Study - A company is building a web-based AI application by using Amazon SageMaker. The application will provide the following capabilities and features: ML experimentation, training, a central model registry, model deployment, and model monitoring. The application must ensure secure and isolated use of training data during the ML lifecycle. The training data is stored in Amazon S3. The company is experimenting with consecutive training jobs. How can the company MINIMIZE infrastructure startup times for these jobs?

- **A.** Use Managed Spot Training.
- **B.** Use SageMaker managed warm pools.
- **C.** Use SageMaker Training Compiler.
- **D.** Use the SageMaker distributed data parallelism (SMDDP) library.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Use SageMaker managed warm pools): Đây là đáp án chính xác vì tính năng SageMaker managed warm pools cho phép giữ lại các instance (máy chủ) và tài nguyên đã được provision (cấp phát) ở trạng thái "sẵn sàng" (warm) sau khi một training job kết thúc. Khi chạy các job liên tiếp (consecutive training jobs), SageMaker có thể tái sử dụng ngay các instance này mà không cần tốn thời gian khởi động lại, tải container image hay cài đặt thư viện, giúp giảm đáng kể thời gian khởi động hạ tầng (infrastructure startup times). Tại sao không chọn A (Use Managed Spot Training): Managed Spot Training sử dụng dung lượng dư thừa của AWS EC2 để tiết kiệm chi phí (cost optimization). Tuy nhiên, nó không đảm bảo về thời gian khởi động và thậm chí có thể làm tăng thời gian chờ đợi nếu không có sẵn dung lượng Spot hoặc bị gián đoạn giữa chừng. Mục tiêu của Spot là "giá rẻ", không phải "khởi động nhanh". Tại sao không chọn C (Use SageMaker Training Compiler): SageMaker Training Compiler là một trình biên dịch giúp tối ưu hóa mã nguồn mô hình (model code) để tăng tốc độ huấn luyện (training throughput) bằng cách sử dụng hiệu quả hơn phần cứng GPU. Nó tập trung vào việc làm cho quá trình huấn luyện nhanh hơn, chứ không giúp giảm thời gian khởi động hạ tầng (provisioning phase). Tại sao không chọn D (Use the SageMaker distributed data parallelism library): Thư viện SMDDP được dùng để phân tán dữ liệu huấn luyện trên nhiều GPU/instance để huấn luyện nhanh hơn (parallel processing). Tương tự như đáp án C, nó giải quyết bài toán về tốc độ xử lý dữ liệu trong khi train, chứ không giải quyết vấn đề độ trễ khi khởi tạo tài nguyên ban đầu.

---

## Question 3

Case Study - A company is building a web-based AI application by using Amazon SageMaker. The application will provide the following capabilities and features: ML experimentation, training, a central model registry, model deployment, and model monitoring. The application must ensure secure and isolated use of training data during the ML lifecycle. The training data is stored in Amazon S3. The company must implement a manual approval-based workflow to ensure that only approved models can be deployed to production endpoints. Which solution will meet this requirement?

- **A.** Use SageMaker Experiments to facilitate the approval process during model registration.
- **B.** Use SageMaker ML Lineage Tracking on the central model registry. Create tracking entities for the approval process.
- **C.** Use SageMaker Model Monitor to evaluate the performance of the model and to manage the approval.
- **D.** Use SageMaker Pipelines. When a model version is registered, use the AWS SDK to change the approval status to "Approved."

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (SageMaker Pipelines & Model Registry Approval): o Đề bài yêu cầu một quy trình phê duyệt thủ công (manual approval-based workflow) để kiểm soát việc deploy model. Trong kiến trúc MLOps của AWS, SageMaker Model Registry là thành phần trung tâm lưu trữ các phiên bản model (Model Versions). o Mỗi phiên bản model trong Registry có thuộc tính ModelApprovalStatus. Giá trị mặc định thường là PendingManualApproval. Để deploy model ra production, trạng thái này phải được chuyển sang Approved. o Đáp án D chính xác về mặt kỹ thuật vì việc thay đổi trạng thái này có thể thực hiện thông qua AWS SDK (sử dụng API UpdateModelPackage) hoặc qua giao diện SageMaker Studio. Đây là "trigger" chuẩn để các pipeline CI/CD (như EventBridge + CodePipeline) bắt sự kiện và thực hiện deploy. Tại sao không chọn A (SageMaker Experiments): o SageMaker Experiments được thiết kế để theo dõi các lần chạy huấn luyện (training runs), so sánh metrics và hyperparameters giữa các thử nghiệm. Nó giúp Data Scientist chọn ra model tốt nhất nhưng không có tính năng quản lý trạng thái phê duyệt (approval status) hay cơ chế Gatekeeper để chặn deploy như Model Registry. Tại sao không chọn B (SageMaker ML Lineage Tracking): o SageMaker ML Lineage Tracking dùng để truy vết nguồn gốc (lineage) của dữ liệu và model (ví dụ: Model A được train từ Dataset B bởi User C). Nó là công cụ để audit (kiểm toán) lịch sử, không phải là công cụ để thực thi workflow phê duyệt (operational workflow). Việc tạo "tracking entities" không thay đổi được trạng thái logic để cho phép deploy. Tại sao không chọn C (SageMaker Model Monitor): o SageMaker Model Monitor là dịch vụ giám sát model sau khi đã deploy (theo dõi Data Drift, Model Quality Drift). Nó hoạt động ở giai đoạn vận hành (Operation), không tham gia vào quy trình phê duyệt model (Registration & Approval) trước khi deploy.

---

## Question 4

Case Study - A company is building a web-based AI application by using Amazon SageMaker. The application will provide the following capabilities and features: ML experimentation, training, a central model registry, model deployment, and model monitoring. The application must ensure secure and isolated use of training data during the ML lifecycle. The training data is stored in Amazon S3. The company needs to run an on-demand workflow to monitor bias drift for models that are deployed to real-time endpoints from the application. Which action will meet this requirement?

- **A.** Configure the application to invoke an AWS Lambda function that runs a SageMaker Clarify job.
- **B.** Invoke an AWS Lambda function to pull the sagemaker-model-monitor-analyzer built-in SageMaker image.
- **C.** Use AWS Glue Data Quality to monitor bias.
- **D.** Use SageMaker notebooks to compare the bias.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (SageMaker Clarify & Lambda): o Giải quyết vấn đề "Bias Drift": Trong hệ sinh thái AWS, SageMaker Clarify là công cụ chuyên biệt để phát hiện các loại thiên kiến (bias) trong dữ liệu và mô hình (cả trước và sau khi huấn luyện). Nó có thể tính toán các chỉ số bias (như Class Imbalance, Difference in Proportions, v.v.) dựa trên dữ liệu thực tế thu thập từ endpoint. o Giải quyết vấn đề "On-demand Workflow": Đề bài yêu cầu quy trình chạy "theo yêu cầu" (on-demand) từ ứng dụng web, chứ không phải chạy theo lịch trình cố định (scheduled). AWS Lambda là giải pháp hoàn hảo để làm cầu nối: Ứng dụng gọi Lambda -> Lambda gọi API CreateProcessingJob để khởi chạy SageMaker Clarify job. Tại sao không chọn B (sagemaker-model-monitor-analyzer image): o Hình ảnh container sagemaker-model-monitor-analyzer chủ yếu được sử dụng bởi SageMaker Model Monitor để giám sát Data Quality (chất lượng dữ liệu) và Model Quality (độ chính xác, ví dụ: RMSE, Accuracy). o Đối với Bias Drift, SageMaker Model Monitor thực tế sử dụng container của Clarify bên dưới. Quan trọng hơn, hành động "pull image" (tải image về) không giải quyết được vấn đề; bạn cần phải chạy một job xử lý (Processing Job) với image đó, chứ không chỉ đơn thuần là tải nó về. Tại sao không chọn C (AWS Glue Data Quality): o AWS Glue Data Quality được thiết kế để kiểm tra chất lượng dữ liệu trong các pipeline ETL (ví dụ: kiểm tra null, định dạng dữ liệu trong S3 hoặc Glue Data Catalog). Nó không có khả năng phân tích các đặc tính chuyên sâu của ML Model như Bias (sự thiên vị của thuật toán) hay Model Drift. Tại sao không chọn D (SageMaker notebooks): o SageMaker Notebooks là môi trường phát triển tương tác (Interactive Development) dành cho Data Scientist để thử nghiệm code. Nó không phải là một giải pháp vận hành (Operational Solution) để tích hợp vào ứng dụng web chạy tự động. Bạn không thể dùng Notebook để đáp ứng yêu cầu "on- demand workflow" cho production một cách ổn định và tự động hóa.

---

## Question 5

A company stores historical data in .csv files in Amazon S3. Only some of the rows and columns in the .csv files are populated. The columns are not labeled. An ML engineer needs to prepare and store the data so that the company can use the data to train ML models. Task: Select and order the correct steps from the following list to perform this task. (Select three and place them in the correct order).

!!! info "Ordering"


??? success "Reveal Answer"
    **Correct Answer: 1,2,3**

    Bước 1: Use AWS Glue crawlers to infer the schemas and available columns. o Lý do chọn: Dữ liệu đầu vào là CSV thô, thiếu nhãn cột (columns are not labeled) và không đồng nhất. Để xử lý, hệ thống cần hiểu cấu trúc dữ liệu (metadata/schema). AWS Glue Crawler là dịch vụ chuyên dụng để quét S3, tự động nhận diện định dạng, suy luận schema và tạo bảng trong AWS Glue Data Catalog. Đây là bước tiền đề để các công cụ khác (như DataBrew) có thể hiểu dữ liệu đầu vào. o Tại sao không dùng Amazon Athena: Athena dùng để truy vấn dữ liệu bằng SQL dựa trên schema đã có (thường do Glue Crawler tạo ra). Athena không phải là công cụ tối ưu để "infer schema" và lưu trữ metadata cho quy trình ETL. Bước 2: Use AWS Glue DataBrew for data cleaning and feature engineering. o Lý do chọn: Đề bài mô tả dữ liệu rất "bẩn" (missing rows, missing columns, unlabelled). AWS Glue DataBrew là công cụ visual data preparation (no-code), cho phép người dùng nhìn thấy trực quan dữ liệu, dễ dàng thực hiện các thao tác như làm sạch (cleaning), điền giá trị thiếu (imputation), và gắn nhãn cột mà không cần viết code phức tạp. o Tại sao không dùng SageMaker Batch Transform: Batch Transform dùng để chạy suy luận (inference) trên hàng loạt dữ liệu bằng một model đã được huấn luyện. Nó không dùng để làm sạch dữ liệu thô ban đầu. Bước 3: Store the resulting data back in Amazon S3. o Lý do chọn: Sau khi dữ liệu đã được làm sạch và chuẩn hóa (Prepared Data), nó cần được lưu trữ lại vào một vị trí bền vững để SageMaker có thể truy cập cho việc Training. Amazon S3 là nơi lưu trữ tiêu chuẩn cho dữ liệu huấn luyện ML.

---

## Question 6

An ML engineer needs to use Amazon SageMaker Feature Store to create and manage features to train a model. Task: Select and order the steps from the following list to create and use the features in Feature Store. (Select three and place them in the correct order).

!!! info "Ordering"


??? success "Reveal Answer"
    **Correct Answer: 1,2,3**

    Bước 1: Create a feature group. o Lý do: Trước khi lưu trữ bất kỳ dữ liệu nào, bạn bắt buộc phải định nghĩa "Feature Group". Đây là bước thiết lập schema (tên cột, kiểu dữ liệu) và cấu hình hạ tầng lưu trữ (Online/Offline store). Không có Feature Group thì không có chỗ để chứa dữ liệu. Bước 2: Ingest the records. o Lý do: Sau khi đã có "thùng chứa" (Feature Group), bước tiếp theo là nạp dữ liệu (Ingestion) vào đó. Dữ liệu được đưa vào thông qua API PutRecord hoặc streaming. Bước 3: Access the store to build datasets for training. o Lý do: Khi dữ liệu đã nằm trong Store, bạn mới có thể truy xuất (Retrieve/Query) nó để tạo thành các tập dữ liệu huấn luyện (Training Datasets) hoặc phục vụ cho suy luận (Inference).

---

## Question 7

A company wants to host an ML model on Amazon SageMaker. An ML engineer is configuring a continuous integration and continuous delivery (CI/CD) pipeline in AWS CodePipeline to deploy the model. The pipeline must run automatically when new training data for the model is uploaded to an Amazon S3 bucket. Task: Select and order the pipeline's correct steps from the following list. Each step should be selected one time or not at all. (Select and order three.)

!!! info "Ordering"


??? success "Reveal Answer"
    **Correct Answer: 1,2,3**

    Bước 1: An S3 event notification invokes the pipeline when new data is uploaded. o Tại sao chọn: Để tự động hóa quy trình khi có "new training data", chúng ta cần một cơ chế Trigger (kích hoạt). AWS CodePipeline hỗ trợ trực tiếp S3 Source Action. Khi có object mới được upload (PutObject), S3 sẽ gửi event notification (thông qua EventBridge hoặc trực tiếp) để khởi động Pipeline. o Tại sao không chọn S3 Lifecycle rule: S3 Lifecycle chỉ dùng để quản lý vòng đời lưu trữ (ví dụ: chuyển sang Glacier sau 30 ngày, xóa sau 1 năm), hoàn toàn không có chức năng trigger CI/CD pipeline. Bước 2: SageMaker retrains the model by using the data in the S3 bucket. o Tại sao chọn: Mục đích của việc upload dữ liệu mới là để cập nhật model. Do đó, bước logic tiếp theo sau khi pipeline chạy là phải gọi SageMaker Training Job để huấn luyện lại (Retrain) model trên dữ liệu mới đó. Bước 3: The pipeline deploys the model to a SageMaker endpoint. o Tại sao chọn: Đề bài nêu rõ mục tiêu là "host an ML model" và "deploy the model". Để model có thể phục vụ suy luận (inference), nó phải được deploy ra một SageMaker Endpoint (Real-time hoặc Serverless). Đây là đích đến cuối cùng của quy trình CD (Continuous Delivery). o Tại sao không chọn Model Registry: Mặc dù Model Registry là một bước quan trọng trong MLOps (để quản lý phiên bản), nhưng việc đưa model vào Registry chỉ là "lưu trữ/đăng ký" (Register), chưa phải là "triển khai để chạy" (Deploy/Host). Vì đề bài yêu cầu chỉ chọn 3 bước để hoàn thành việc "host", nên Endpoint là đáp án chính xác hơn để thỏa mãn yêu cầu kinh doanh.

---

## Question 8

An ML engineer is building a generative AI application on Amazon Bedrock by using large language models (LLMs). Task: Select the correct generative AI term from the following list for each description. Each term should be selected one time or not at all. (Select three.)

!!! info "Matching"


??? success "Reveal Answer"
    **Correct Answer: ?**

    Token: o Định nghĩa: Là đơn vị văn bản nhỏ nhất mà LLM có thể xử lý. Một token có thể là một từ, một phần của từ, hoặc một dấu câu (ví dụ: từ "Amazon" có thể là 1 token, nhưng "antidisestablishmentarianism" có thể bị tách thành nhiều token). o Tại sao chọn: Bất cứ khi nào đề cập đến "unit of text", "processing unit", hoặc chi phí tính tiền (billing based on input/output count), đó chính là Token. Embedding: o Định nghĩa: Là kỹ thuật chuyển đổi văn bản (text) thành các dãy số thực (vectors) trong không gian nhiều chiều. Các vector này giúp máy tính hiểu được "ý nghĩa ngữ nghĩa" (semantic meaning). Các từ có nghĩa gần nhau sẽ có vector nằm gần nhau. o Tại sao chọn: Từ khóa nhận diện là "Vector", "High-dimensional", "Semantic meaning", hoặc "Numerical representation". Retrieval Augmented Generation (RAG): o Định nghĩa: Là kiến trúc kết hợp sức mạnh của LLM với dữ liệu bên ngoài (External Knowledge Base). Trước khi gửi câu hỏi cho LLM, hệ thống sẽ tìm kiếm thông tin liên quan từ cơ sở dữ liệu riêng, kẹp thông tin đó vào prompt để LLM trả lời chính xác hơn. o Tại sao chọn: Từ khóa là "External data", "Knowledge base", "Augment response", hoặc "Context". Tại sao không chọn Temperature: o Định nghĩa: Đây là một siêu tham số (hyperparameter) cấu hình độ "sáng tạo" hoặc "ngẫu nhiên" của model (giá trị từ 0 đến 1). Temperature thấp (gần 0) cho kết quả nhất quán, chính xác; Temperature cao (gần 1) cho kết quả đa dạng, sáng tạo hơn. o Đề bài chỉ yêu cầu chọn 3 thuật ngữ tương ứng với 3 mô tả về cấu trúc/kỹ thuật, không hỏi về tham số cấu hình.

---

## Question 9

An ML engineer is working on an ML model to predict the prices of similarly sized homes. The model will base predictions on several features. The ML engineer will use the following feature engineering techniques to estimate the prices of the homes. Task: Select the correct feature engineering techniques for the following list of features. Each feature engineering technique should be selected one time or not at all (Select three). Techniques List: * Feature splitting * Logarithmic transformation * One-hot encoding * Standardized distribution Features to Map (Reconstructed): 1. City (Name): (e.g., "Seattle", "Austin", "Boston") 2. Type_Year: (e.g., "Apartment_2015", "House_1998") 3. Size of the building: (e.g., Square feet or Square Meters)


??? success "Reveal Answer"
    **Correct Answer: ?**

    1. City (Name) → One-hot encoding: o Tại sao: "City" là dữ liệu định danh (Categorical/Nominal data) không có thứ tự tự nhiên (ví dụ: Hà Nội không lớn hơn hay nhỏ hơn TP.HCM về mặt số học). Để đưa vào mô hình ML, ta không thể dùng Label Encoding (gán 1, 2, 3...) vì sẽ tạo ra thứ tự giả tạo. One-hot encoding là kỹ thuật chuẩn để biến mỗi thành phố thành một vector nhị phân (0/1), giúp mô hình đối xử bình đẳng với các thành phố. 2. Type_Year → Feature splitting: o Tại sao: Đây là một thuộc tính ghép (Composite Feature) chứa hai thông tin hoàn toàn khác nhau: "Loại nhà" (Categorical) và "Năm xây dựng" (Numerical/Time). Để mô hình học hiệu quả, chúng ta cần tách (Split) chuỗi này ra thành hai cột riêng biệt. Sau đó mới xử lý tiếp (ví dụ: Type thì One-hot, Year thì tính tuổi nhà). 3. Size of the building → Standardized distribution: o Tại sao: Diện tích nhà là biến số liên tục (Numerical Continuous). Trong các thuật toán hồi quy (Regression) để dự đoán giá nhà, việc các biến số có đơn vị khác nhau (ví dụ: diện tích là hàng ngàn m2, trong khi số phòng ngủ chỉ là 1-5) sẽ làm mô hình khó hội tụ. Standardized distribution (chuẩn hóa Z- score về Mean=0, Std=1) giúp đưa dữ liệu về cùng một tỷ lệ. o Tại sao không chọn Logarithmic transformation: Mặc dù Log transform thường dùng cho diện tích (do phân phối lệch phải), nhưng đề bài có từ khóa quan trọng: "similarly sized homes" (các ngôi nhà có kích thước tương đồng). Điều này ám chỉ dữ liệu diện tích không bị lệch quá nhiều (skewness thấp), nên việc chuẩn hóa (Standardization) là ưu tiên hợp lý hơn để cải thiện tốc độ huấn luyện.

---

## Question 10

Case study - An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3. The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data. Which AWS service or feature can aggregate the data from the various data sources?

- **A.** Amazon EMR Spark jobs
- **B.** Amazon Kinesis Data Streams
- **C.** Amazon DynamoDB
- **D.** AWS Lake Formation

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (EMR Spark jobs): Đề bài đề cập đến việc dữ liệu có vấn đề về "mất cân bằng lớp" (class imbalance) và các đặc trưng có "sự phụ thuộc lẫn nhau" (interdependencies). Để giải quyết vấn đề này nhằm giúp thuật toán nắm bắt được pattern, kỹ sư ML cần thực hiện Feature Engineering (Kỹ thuật đặc trưng) và Data Transformation phức tạp (như SMOTE để cân bằng lớp, hoặc Join các bảng để tạo đặc trưng tổng hợp). Apache Spark trên Amazon EMR là công cụ xử lý dữ liệu phân tán (Distributed Processing) tiêu chuẩn, hỗ trợ các connector để đọc dữ liệu từ nhiều nguồn khác nhau (S3, JDBC cho MySQL) và thực hiện các phép tính toán JOIN, GROUP BY quy mô lớn để "aggregate" (tổng hợp) dữ liệu thành một tập training set sạch. Tại sao không chọn B (Amazon Kinesis Data Streams): Kinesis là dịch vụ dành cho việc thu thập và xử lý dữ liệu Streaming (thời gian thực). Trong khi đó, dữ liệu trong đề bài (transaction logs, tables, profiles) là dữ liệu tĩnh/lịch sử (batch data), nên Kinesis không phù hợp. Tại sao không chọn C (Amazon DynamoDB): DynamoDB là cơ sở dữ liệu NoSQL (Key-Value) được tối ưu cho các truy vấn nhanh (low latency) của ứng dụng, không phải là một công cụ Analytics hay ETL để thực hiện việc tổng hợp dữ liệu (aggregation) từ nhiều nguồn khác nhau. Tại sao không chọn D (AWS Lake Formation): Lake Formation là dịch vụ giúp thiết lập, bảo mật và quản trị (Governance) Data Lake. Mặc dù nó có thể giúp "gom" dữ liệu về S3 (thông qua Glue Blueprints), nhưng bản thân nó là một lớp quản lý quyền truy cập và catalog, không phải là compute engine để xử lý logic Feature Engineering phức tạp (như xử lý class imbalance hay interdependencies) mà đề bài yêu cầu.

---

## Question 11

Case study - An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3. The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data. After the data is aggregated, the ML engineer must implement a solution to automatically detect anomalies in the data and to visualize the result. Which solution will meet these requirements?

- **A.** Use Amazon Athena to automatically detect the anomalies and to visualize the result.
- **B.** Use Amazon Redshift Spectrum to automatically detect the anomalies. Use Amazon QuickSight to visualize the result.
- **C.** Use Amazon SageMaker Data Wrangler to automatically detect the anomalies and to visualize the result.
- **D.** Use AWS Batch to automatically detect the anomalies. Use Amazon QuickSight to visualize the result.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Data Wrangler): Trong quy trình Machine Learning, SageMaker Data Wrangler là dịch vụ chuyên biệt giúp các kỹ sư ML chuẩn bị dữ liệu.2 Nó cung cấp tính năng Data Quality and Insights Report (Báo cáo chất lượng và thông tin dữ liệu) và Analyses tích hợp sẵn.3 Tính năng này có thể tự động phát hiện các bất thường (anomalies), trùng lặp, target leakage (rò rỉ dữ liệu mục tiêu) và mất cân bằng lớp (class imbalance) ngay khi nhập dữ liệu. Ngoài ra, Data Wrangler còn tích hợp sẵn khả năng trực quan hóa (visualization) như histogram, scatter plots mà không cần viết mã hay tích hợp thêm công cụ bên ngoài như QuickSight.4 Đây là giải pháp "ít thao tác nhất" (low-code) đáp ứng trọn vẹn yêu cầu của đề bài. Tại sao không chọn A (Amazon Athena): Athena là dịch vụ truy vấn tương tác (Interactive Query Service) sử dụng SQL để truy vấn dữ liệu trên S3.5 Mặc dù bạn có thể viết câu lệnh SQL để tìm các giá trị ngoại lai, nhưng nó không có tính năng "tự động phát hiện bất thường" dành cho ML (như Isolation Forest hay thống kê phân phối tự động). Hơn nữa, Athena không có khả năng trực quan hóa dữ liệu (visualization) tích hợp sẵn mà bắt buộc phải kết nối với Amazon QuickSight, làm tăng độ phức tạp so với yêu cầu. Tại sao không chọn B (Amazon Redshift Spectrum): Redshift Spectrum cho phép truy vấn dữ liệu trên S3 thông qua Redshift, nhưng bản chất đây là giải pháp Kho dữ liệu (Data Warehousing). Việc thiết lập một cụm Redshift chỉ để phát hiện bất thường và trực quan hóa trong giai đoạn chuẩn bị dữ liệu ML là quá cồng kềnh (overkill) và tốn kém. Tương tự Athena, Redshift cần QuickSight để trực quan hóa chứ không có sẵn công cụ visual mạnh mẽ trong console cho quy trình ML prep. Tại sao không chọn D (AWS Batch): AWS Batch là dịch vụ điều phối và chạy các tác vụ tính toán hàng loạt (batch computing) bằng container.6 Nó hoàn toàn không phải là công cụ phân tích dữ liệu hay trực quan hóa. Để dùng Batch, bạn phải tự viết code phát hiện bất thường, đóng gói vào Docker ...

---

## Question 12

Case study - An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3. The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data. The training dataset includes categorical data and numerical data. The ML engineer must prepare the training dataset to maximize the accuracy of the model. Which action will meet this requirement with the LEAST operational overhead?

- **A.** Use AWS Glue to transform the categorical data into numerical data.
- **B.** Use AWS Glue to transform the numerical data into categorical data.
- **C.** Use Amazon SageMaker Data Wrangler to transform the categorical data into numerical data.
- **D.** Use Amazon SageMaker Data Wrangler to transform the numerical data into categorical data.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Data Wrangler + Categorical to Numerical): o Nguyên lý ML: Hầu hết các thuật toán Machine Learning (như trong bài toán phát hiện gian lận) hoạt động dựa trên toán học (ma trận, khoảng cách vectơ), do đó bắt buộc phải chuyển đổi dữ liệu phân loại (categorical data - ví dụ: "High", "Medium", "Low") thành dữ liệu số (numerical data - ví dụ: 2, 1, 0 hoặc One-hot encoding). o Tối ưu vận hành (Least Operational Overhead): SageMaker Data Wrangler cung cấp các tính năng chuyển đổi tích hợp sẵn (built-in transforms) như "Encode Categorical" ngay trên giao diện người dùng (GUI).1 Kỹ sư ML chỉ cần chọn cột và loại encoding mà không cần viết code ETL phức tạp hay quản lý hạ tầng, đáp ứng tốt nhất yêu cầu về giảm thiểu vận hành. Tại sao không chọn A (AWS Glue + Categorical to Numerical): Mặc dù AWS Glue có thể thực hiện việc này, nhưng Glue được thiết kế thiên về các tác vụ ETL kỹ thuật dữ liệu quy mô lớn (Data Engineering). Việc thiết lập Glue Job, viết script (PySpark/Python), và debug thường tốn nhiều công sức vận hành hơn so với trải nghiệm "click-and-config" chuyên biệt cho ML của Data Wrangler. Tại sao không chọn B (AWS Glue + Numerical to Categorical): Đây là hướng xử lý sai về mặt khoa học dữ liệu. Thông thường, chúng ta cần biến dữ liệu chữ thành số để máy học, chứ không phải biến dữ liệu số (đang có giá trị định lượng) thành dữ liệu phân loại (trừ các trường hợp binning rất cụ thể). Việc này sẽ làm mất mát thông tin quan trọng. Tại sao không chọn D (SageMaker Data Wrangler + Numerical to Categorical): Tương tự đáp án B, hướng chuyển đổi này (Numerical -> Categorical) là không hợp lý cho mục tiêu "tối đa hóa độ chính xác mô hình" trong bối cảnh chung. Dù công cụ đúng (Data Wrangler) nhưng phương pháp sai.

---

## Question 13

Case study - An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3. The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data. Before the ML engineer trains the model, the ML engineer must resolve the issue of the imbalanced data. Which solution will meet this requirement with the LEAST operational effort?

- **A.** Use Amazon Athena to identify patterns that contribute to the imbalance. Adjust the dataset accordingly.
- **B.** Use Amazon SageMaker Studio Classic built-in algorithms to process the imbalanced dataset.
- **C.** Use AWS Glue DataBrew built-in features to oversample the minority class.
- **D.** Use the Amazon SageMaker Data Wrangler balance data operation to oversample the minority class.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (SageMaker Data Wrangler): Đề bài yêu cầu giải quyết vấn đề mất cân bằng dữ liệu (class imbalance) với "nỗ lực vận hành ít nhất" (LEAST operational effort). SageMaker Data Wrangler cung cấp sẵn một phép biến đổi (transform) tên là "Balance Data". Tính năng này cho phép người dùng thực hiện Oversample (nhân bản lớp thiểu số), Undersample (giảm lớp đa số) hoặc sử dụng thuật toán SMOTE (Synthetic Minority Over-sampling Technique) chỉ bằng vài cú nhấp chuột trên giao diện đồ họa. Đây là giải pháp chuyên biệt cho ML Prep và không yêu cầu viết code. Tại sao không chọn A (Amazon Athena): Athena dùng để truy vấn và phân tích dữ liệu bằng SQL. Mặc dù bạn có thể dùng SQL để lọc và trích xuất dữ liệu nhằm cân bằng thủ công, nhưng nó không có chức năng "tự động cân bằng" (như SMOTE). Việc phải viết query phức tạp để điều chỉnh dataset đòi hỏi nỗ lực vận hành cao hơn nhiều so với công cụ GUI có sẵn của Data Wrangler. Tại sao không chọn B (Amazon SageMaker Studio Classic built-in algorithms): Các thuật toán tích hợp sẵn (built-in algorithms) của SageMaker (như XGBoost, Linear Learner) thường có tham số để xử lý trọng số lớp (class weights), nhưng đó là cấu hình trong quá trình huấn luyện (training phase). Đề bài đang hỏi về việc xử lý chính bộ dữ liệu trước khi train ("Before the ML engineer trains the model"). Ngoài ra, việc tinh chỉnh hyperparameter không giải quyết triệt để vấn đề ở mức dataset tốt bằng việc oversampling. Tại sao không chọn C (AWS Glue DataBrew): Glue DataBrew cũng là công cụ chuẩn bị dữ liệu trực quan (visual data prep). Tuy nhiên, DataBrew tập trung vào làm sạch và chuẩn hóa dữ liệu chung (ETL/Data Cleaning). DataBrew không cung cấp sẵn các tính năng chuyên sâu để cân bằng dữ liệu cho ML như SMOTE hay các kỹ thuật oversampling phức tạp một cách tự động (built-in recipe step for balancing) mạnh mẽ và trực diện như Data Wrangler.

---

## Question 14

Case study - An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3. The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data. The ML engineer needs to use an Amazon SageMaker built-in algorithm to train the model. Which algorithm should the ML engineer use to meet this requirement?

- **A.** LightGBM
- **B.** Linear learner
- **C.** К-means clustering
- **D.** Neural Topic Model (NTM)

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (LightGBM): . Tính năng Built-in: Hiện tại, LightGBM đã chính thức là một Amazon SageMaker built-in algorithm. (Trước đây nó chỉ có thể dùng qua script mode, nhưng AWS đã cập nhật hỗ trợ native container cho LightGBM). . Giải quyết "Class Imbalance": LightGBM cực kỳ mạnh mẽ trong việc xử lý dữ liệu mất cân bằng (class imbalance) thông qua tham số scale_pos_weight hoặc tính năng weighted loss tự động, điều mà bài toán phát hiện gian lận (fraud detection) luôn gặp phải. . Giải quyết "Interdependencies": Đề bài nhấn mạnh dữ liệu có sự phụ thuộc lẫn nhau giữa các tính năng (feature interdependencies) và thuật toán hiện tại không nắm bắt được các mẫu (patterns). LightGBM là thuật toán dựa trên cây quyết định (Decision Tree-based Gradient Boosting), nó tự động nắm bắt được các mối quan hệ phi tuyến tính (non-linear) và tương tác phức tạp giữa các tính năng tốt hơn nhiều so với các mô hình tuyến tính. Tại sao không chọn B (Linear learner): Mặc dù Linear Learner là một thuật toán built-in và có thể xử lý binary classification, nhưng nó hoạt động dựa trên giả định về mối quan hệ tuyến tính (linear relationship) giữa đầu vào và đầu ra. Đề bài nói rõ rằng thuật toán hiện tại không nắm bắt được các mẫu tiềm ẩn và các tính năng có sự phụ thuộc lẫn nhau (điều thường tạo ra ranh giới quyết định phi tuyến tính). Linear Learner sẽ gặp khó khăn lớn (underfitting) với loại dữ liệu phức tạp này so với các thuật toán Tree-based như LightGBM hay XGBoost. Tại sao không chọn C (K-means clustering): K-means là thuật toán học không giám sát (Unsupervised Learning) dùng để gom nhóm dữ liệu. Trong bài toán này, chúng ta có "class imbalance" (ngụ ý dữ liệu đã được gán nhãn là gian lận hoặc không), do đó đây là bài toán học có giám sát (Supervised Learning). K-means không phù hợp để huấn luyện mô hình phân lớp gian lận chính xác trong ngữ cảnh này. Tại sao không chọn D (Neural Topic Model - NTM): NTM là thuật toán chuyên dùng cho xử lý ngôn ngữ tự nhiên (NLP) để tìm các chủ đề (to...

---

## Question 15

A company has deployed an XGBoost prediction model in production to predict if a customer is likely to cancel a subscription. The company uses Amazon SageMaker Model Monitor to detect deviations in the F1 score. During a baseline analysis of model quality, the company recorded a threshold for the F1 score. After several months of no change, the model's F1 score decreases significantly. What could be the reason for the reduced F1 score?

- **A.** Concept drift occurred in the underlying customer data that was used for predictions.
- **B.** The model was not sufficiently complex to capture all the patterns in the original baseline data.
- **C.** The original baseline data had a data quality issue of missing values.
- **D.** Incorrect ground truth labels were provided to Model Monitor during the calculation of the baseline.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Concept drift): "Concept drift" (Trôi dạt khái niệm) xảy ra khi mối quan hệ thống kê giữa các tính năng đầu vào (features) và biến mục tiêu (target label) thay đổi theo thời gian. Trong bài toán dự đoán hủy đăng ký (churn), hành vi khách hàng thay đổi theo thời gian (ví dụ: do xu hướng thị trường mới, đối thủ cạnh tranh mới) khiến các mẫu (patterns) mà mô hình đã học trước đây không còn đúng nữa. Đặc điểm nhận dạng chính trong đề bài là mô hình hoạt động ổn định trong vài tháng ("after several months of no change") rồi mới bị suy giảm chỉ số F1. Đây là dấu hiệu kinh điển của việc mô hình bị lỗi thời do Concept Drift. Tại sao không chọn B (Model complexity): Nếu mô hình không đủ phức tạp (underfitting), hiệu suất (F1 score) sẽ thấp ngay từ giai đoạn huấn luyện và triển khai ban đầu (Day 1). Nó sẽ không thể duy trì ổn định trong vài tháng rồi mới giảm đột ngột như mô tả. Tại sao không chọn C (Data quality issue in baseline): Các vấn đề về chất lượng dữ liệu trong tập baseline (như thiếu giá trị) sẽ ảnh hưởng đến chất lượng mô hình hoặc chỉ số baseline ngay từ đầu. Nó không giải thích được nguyên nhân tại sao hiệu suất lại suy giảm sau một khoảng thời gian dài vận hành ổn định. Tại sao không chọn D (Incorrect ground truth labels in baseline): Nếu nhãn thực tế (ground truth) bị sai trong quá trình tính toán baseline, thì chỉ số F1 của baseline sẽ bị tính sai ngay từ thời điểm đó. Điều này dẫn đến việc thiết lập ngưỡng (threshold) sai, nhưng nó là một lỗi tĩnh (static error). Nó không giải thích được hiện tượng "suy giảm" (degradation) diễn ra theo thời gian thực của mô hình hiện tại.

---

## Question 16

A company has a team of data scientists who use Amazon SageMaker notebook instances to test ML models. When the data scientists need new permissions, the company attaches the permissions to each individual role that was created during the creation of the SageMaker notebook instance. The company needs to centralize management of the team's permissions. Which solution will meet this requirement?

- **A.** Create a single IAM role that has the necessary permissions. Attach the role to each notebook instance that the team uses.
- **B.** Create a single IAM group. Add the data scientists to the group. Associate the group with each notebook instance that the team uses.
- **C.** Create a single IAM user. Attach the AdministratorAccess AWS managed IAM policy to the user. Configure each notebook instance to use the IAM user.
- **D.** Create a single IAM group. Add the data scientists to the group. Create an IAM role. Attach the AdministratorAccess AWS managed IAM policy to the role. Associate the role with the group. Associate the group with each notebook instance that the team uses.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Single IAM Role): SageMaker Notebook Instance hoạt động dựa trên cơ chế IAM Execution Role để tương tác với các dịch vụ khác (như S3, Glue, Athena). Bằng cách tạo một IAM Role chung chứa tất cả quyền cần thiết và gán Role này cho tất cả các Notebook Instance của nhóm, bạn đạt được mục tiêu "centralize management" (quản lý tập trung). Khi cần thêm hoặc bớt quyền, bạn chỉ cần sửa Policy của Role duy nhất này một lần, thay vì phải sửa từng Role riêng lẻ của từng Notebook. Tại sao không chọn B (IAM Group): IAM Group được thiết kế để quản lý quyền cho IAM Users (con người), KHÔNG phải cho tài nguyên AWS (AWS Resources). Bạn không thể gán một IAM Group trực tiếp cho một SageMaker Notebook Instance. Tài nguyên AWS phải sử dụng IAM Role. Tại sao không chọn C (IAM User & AdministratorAccess): Thứ nhất, về mặt kỹ thuật, Notebook Instance sử dụng IAM Role, không sử dụng IAM User để chạy (service assumption). Thứ hai, việc gán quyền AdministratorAccess (toàn quyền quản trị) vi phạm nghiêm trọng nguyên tắc bảo mật "Least Privilege" (Quyền tối thiểu), gây rủi ro an ninh lớn nếu Notebook bị xâm nhập. Tại sao không chọn D (Complex setup & IAM Group): Tương tự như đáp án B, bạn không thể gán IAM Group cho Notebook Instance. Ngoài ra, giải pháp này quá phức tạp và cũng vi phạm nguyên tắc "Least Privilege" khi sử dụng AdministratorAccess.

---

## Question 17

An ML engineer needs to use an ML model to predict the price of apartments in a specific location. Which metric should the ML engineer use to evaluate the model's performance?

- **A.** Accuracy
- **B.** Area Under the ROC Curve (AUC)
- **C.** F1 score
- **D.** Mean absolute error (MAE)

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Mean absolute error - MAE): Bài toán yêu cầu dự đoán giá căn hộ (price of apartments). Giá tiền là một biến số liên tục (continuous variable), do đó đây là bài toán Hồi quy (Regression). Trong Machine Learning, các chỉ số dùng để đánh giá mô hình Hồi quy bao gồm MAE (Sai số tuyệt đối trung bình), MSE (Sai số bình phương trung bình), và RMSE (Căn bậc hai của MSE). MAE đo lường mức độ sai lệch trung bình giữa giá trị dự đoán và giá trị thực tế, rất phù hợp để đánh giá độ chính xác của dự đoán giá. Tại sao không chọn A (Accuracy): Accuracy (Độ chính xác) là tỷ lệ số lần dự đoán đúng trên tổng số lần dự đoán. Chỉ số này chỉ dùng cho bài toán Phân loại (Classification) (ví dụ: Căn hộ này có bán được không? - Có/Không). Nó không có ý nghĩa đối với dữ liệu liên tục như giá tiền. Tại sao không chọn B (Area Under the ROC Curve - AUC): AUC là diện tích dưới đường cong ROC, được sử dụng để đánh giá hiệu suất của mô hình Phân loại nhị phân (Binary Classification) tại các ngưỡng phân loại khác nhau. Nó hoàn toàn không áp dụng cho bài toán Hồi quy. Tại sao không chọn C (F1 score): F1 score là trung bình điều hòa (harmonic mean) giữa Precision (Độ chính xác) và Recall (Độ nhạy). Đây là chỉ số quan trọng cho các bài toán Phân loại (Classification), đặc biệt là khi dữ liệu bị mất cân bằng (imbalanced data). Nó không dùng để đo lường sai số của một giá trị liên tục.

---

## Question 18

An ML engineer has trained a neural network by using stochastic gradient descent (SGD). The neural network performs poorly on the test set. The values for training loss and validation loss remain high and show an oscillating pattern. The values decrease for a few epochs and then increase for a few epochs before repeating the same cycle. What should the ML engineer do to improve the training process?

- **A.** Introduce early stopping.
- **B.** Increase the size of the test set.
- **C.** Increase the learning rate.
- **D.** Decrease the learning rate.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Decrease the learning rate): Hiện tượng giá trị hàm mất mát (loss function) không giảm dần mà có biểu hiện "oscillating pattern" (dao động lên xuống) và duy trì ở mức cao là dấu hiệu kinh điển của việc Learning Rate (tốc độ học) quá cao. Trong thuật toán Gradient Descent, nếu bước nhảy (learning rate) quá lớn, thuật toán sẽ "nhảy qua" (overshoot) điểm cực tiểu (minima) thay vì trượt xuống đáy của nó. Nó sẽ liên tục nhảy qua lại giữa hai sườn dốc của hàm mất mát, gây ra hiện tượng dao động. Việc giảm Learning Rate sẽ thu nhỏ bước nhảy, giúp thuật toán đi xuống từ từ và hội tụ chính xác vào điểm cực tiểu. Tại sao không chọn A (Introduce early stopping): Early Stopping là kỹ thuật dùng để chống Overfitting (khi Training Loss giảm nhưng Validation Loss bắt đầu tăng).1 Trong trường hợp này, cả hai loss đều cao và dao động (nghĩa là mô hình chưa học được hoặc không hội tụ - underfitting/non-convergence), nên việc dừng sớm sẽ chỉ khiến bạn nhận được một mô hình kém chất lượng, không giải quyết được nguyên nhân gốc rễ là mô hình không thể hội tụ. Tại sao không chọn B (Increase the size of the test set): Tập Test (Test set) chỉ dùng để đánh giá hiệu năng mô hình sau khi huấn luyện xong. Kích thước của tập Test hoàn toàn không tham gia vào quá trình tính toán Gradient hay cập nhật trọng số (weights) trong quá trình huấn luyện, do đó không thể sửa chữa lỗi dao động của hàm loss. Tại sao không chọn C (Increase the learning rate): Nếu Learning Rate hiện tại đã gây ra dao động (do quá cao), việc tăng nó thêm nữa sẽ làm bước nhảy càng lớn hơn. Điều này sẽ khiến dao động mạnh hơn hoặc làm mô hình phân kỳ hoàn toàn (Divergence - Loss tăng vọt lên vô cực), làm tình hình tồi tệ hơn.

---

## Question 19

An ML engineer needs to process thousands of existing CSV objects and new CSV objects that are uploaded. The CSV objects are stored in a central Amazon S3 bucket and have the same number of columns. One of the columns is a transaction date. The ML engineer must query the data based on the transaction date. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use an Amazon Athena CREATE TABLE AS SELECT (CTAS) statement to create a table based on the transaction date from data in the central S3 bucket. Query the objects from the table.
- **B.** Create a new S3 bucket for processed data. Set up S3 replication from the central S3 bucket to the new S3 bucket. Use S3 Object Lambda to query the objects based on transaction date.
- **C.** Create a new S3 bucket for processed data. Use AWS Glue for Apache Spark to create a job to query the CSV objects based on transaction date. Configure the job to store the results in the new S3 bucket. Query the objects from the new S3 bucket.
- **D.** Create a new S3 bucket for processed data. Use Amazon Data Firehose to transfer the data from the central S3 bucket to the new S3 bucket. Configure Firehose to run an AWS Lambda function to query the data based on transaction date.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Amazon Athena CTAS): . Serverless & SQL: Amazon Athena là dịch vụ truy vấn tương tác không máy chủ (Serverless), cho phép dùng chuẩn SQL để truy vấn trực tiếp dữ liệu nằm trên S3 mà không cần thiết lập hạ tầng (Least operational overhead). . Tối ưu hóa với CTAS: Câu lệnh CREATE TABLE AS SELECT (CTAS) trong Athena không chỉ tạo bảng mà còn có thể dùng để chuyển đổi định dạng dữ liệu (ví dụ: từ CSV sang Parquet) và phân vùng (partition) dữ liệu theo cột transaction_date. Việc này giúp các truy vấn sau này chỉ quét đúng phân vùng ngày tháng cần thiết, tăng tốc độ và giảm chi phí đáng kể so với việc quét toàn bộ file CSV thô. Tại sao không chọn B (S3 Object Lambda): S3 Object Lambda được thiết kế để sửa đổi nội dung của một đối tượng riêng lẻ trong khi nó đang được truy xuất (ví dụ: làm mờ dữ liệu nhạy cảm khi người dùng tải file về). Nó không phải là một công cụ truy vấn phân tích (Analytical Query Engine) để lọc và tổng hợp dữ liệu từ hàng ngàn file dựa trên một cột cụ thể. Tại sao không chọn C (AWS Glue for Apache Spark): Mặc dù Glue có thể làm được việc này, nhưng Glue là một dịch vụ ETL (Trích xuất, Chuyển đổi, Tải) yêu cầu viết code (Python/Scala) hoặc thiết lập Job phức tạp hơn. So với việc chỉ viết một câu lệnh SQL trong Athena, Glue có "operational overhead" (gánh nặng vận hành) cao hơn. Tại sao không chọn D (Amazon Data Firehose): Amazon Data Firehose là dịch vụ Ingestion (nạp dữ liệu) dùng để nhận luồng dữ liệu và lưu vào S3/Redshift. Nó không hỗ trợ việc đọc dữ liệu đã tồn tại (existing objects) trong S3 bucket làm nguồn (Source). Do đó, giải pháp này không khả thi về mặt kỹ thuật cho dữ liệu cũ.

---

## Question 20

A company has a large, unstructured dataset. The dataset includes many duplicate records across several key attributes. Which solution on AWS will detect duplicates in the dataset with the LEAST code development?

- **A.** Use Amazon Mechanical Turk jobs to detect duplicates.
- **B.** Use Amazon QuickSight ML Insights to build a custom deduplication model.
- **C.** Use Amazon SageMaker Data Wrangler to pre-process and detect duplicates.
- **D.** Use the AWS Glue FindMatches transform to detect duplicates. Chào bạn, đây là phân tích chi tiết cho câu hỏi về phát hiện dữ liệu trùng lặp (Deduplication/Entity Resolution) trên AWS với nỗ lực lập trình ít nhất.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (AWS Glue FindMatches): . Tính năng chuyên biệt (Purpose-built): FindMatches là một tính năng Machine Learning chuyển đổi (ML Transform) tích hợp sẵn trong AWS Glue. Nó được thiết kế đặc biệt để giải quyết bài toán "Record Linkage" hoặc "Entity Resolution" (liên kết bản ghi), cho phép tìm các bản ghi trùng lặp ngay cả khi chúng không khớp chính xác từng ký tự (fuzzy matching - ví dụ: "Jon Smith" và "John Smith"). . Least code development (Ít code nhất): Bạn không cần viết mã thuật toán ML. Thay vào đó, bạn dạy hệ thống bằng cách gán nhãn thủ công một tập nhỏ các cặp bản ghi là "trùng" hoặc "không trùng". Glue sẽ tự động học và áp dụng logic đó cho toàn bộ tập dữ liệu lớn. Đây là giải pháp "Zero-code" về mặt thuật toán. Tại sao không chọn A (Amazon Mechanical Turk): Mechanical Turk là dịch vụ sử dụng sức người (crowdsourcing) để thực hiện các tác vụ. Mặc dù con người rất giỏi phát hiện trùng lặp trong dữ liệu phi cấu trúc, nhưng giải pháp này không thể mở rộng (scale) cho "large dataset" một cách hiệu quả về thời gian và chi phí. Nó cũng đòi hỏi quy trình quản lý (operational overhead) phức tạp hơn nhiều so với việc chạy một Glue Job tự động. Tại sao không chọn B (Amazon QuickSight ML Insights): QuickSight là công cụ Business Intelligence (BI) dùng để trực quan hóa dữ liệu. Tính năng ML Insights của nó hỗ trợ phát hiện bất thường (Anomaly Detection) hoặc dự báo (Forecasting) trên biểu đồ, KHÔNG có khả năng xây dựng mô hình chống trùng lặp dữ liệu (Deduplication) để làm sạch dữ liệu nguồn. Tại sao không chọn C (Amazon SageMaker Data Wrangler): SageMaker Data Wrangler có tính năng "Drop duplicates", nhưng tính năng này thường hoạt động dựa trên nguyên tắc khớp chính xác (exact match) trên các cột được chọn. Đối với các bài toán yêu cầu phát hiện trùng lặp phức tạp (ví dụ: lỗi chính tả, viết tắt khác nhau trong các thuộc tính chính), Glue FindMatches (với khả năng Fuzzy Matching) là giải pháp mạnh mẽ và chuyên dụng hơn. Hơn nữa, Glue xử lý tốt hơn ở quy m...

---

## Question 21

A company needs to run a batch data-processing job on Amazon EC2 instances. The job will run during the weekend and will take 90 minutes to finish running. The processing can handle interruptions. The company will run the job every weekend for the next 6 months. Which EC2 instance purchasing option will meet these requirements MOST cost- effectively?

- **A.** Spot Instances
- **B.** Reserved Instances
- **C.** On-Demand Instances
- **D.** Dedicated Instances

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Spot Instances): Đây là lựa chọn tối ưu nhất về chi phí (có thể rẻ hơn tới 90% so với giá On-Demand). Chìa khóa của câu hỏi nằm ở cụm từ "The processing can handle interruptions" (Quy trình có thể xử lý việc bị gián đoạn). Spot Instances là phần dung lượng dư thừa của AWS, giá rất rẻ nhưng có thể bị AWS thu hồi (interruption) bất cứ lúc nào với cảnh báo trước 2 phút. Vì ứng dụng chịu được lỗi này, đây là lựa chọn hoàn hảo. Tại sao không chọn B (Reserved Instances): Reserved Instances (RI) yêu cầu cam kết sử dụng lâu dài (1 hoặc 3 năm) và thường dành cho các tác vụ chạy liên tục 24/7 (steady-state usage). Việc mua RI cho một job chỉ chạy 90 phút mỗi tuần là cực kỳ lãng phí vì bạn phải trả tiền cho cả thời gian không sử dụng. Tại sao không chọn C (On-Demand Instances): On-Demand Instances là lựa chọn tiêu chuẩn, trả tiền theo giờ/giây sử dụng và không bị gián đoạn. Tuy nhiên, mức giá của nó cao hơn nhiều so với Spot Instances. Vì đề bài yêu cầu "Most cost-effectively" và job chịu được gián đoạn, nên việc trả giá cao cho sự ổn định của On-Demand là không cần thiết. Tại sao không chọn D (Dedicated Instances): Dedicated Instances chạy trên phần cứng vật lý dành riêng cho một khách hàng (thường dùng cho yêu cầu tuân thủ/compliance). Đây là phương án đắt đỏ nhất, hoàn toàn trái ngược với mục tiêu tiết kiệm chi phí.

---

## Question 22

An ML engineer has an Amazon Comprehend custom model in Account A in the us-east-1 Region. The ML engineer needs to copy the model to Account В in the same Region. Which solution will meet this requirement with the LEAST development effort?

- **A.** Use Amazon S3 to make a copy of the model. Transfer the copy to Account B.
- **B.** Create a resource-based IAM policy. Use the Amazon Comprehend ImportModel API operation to copy the model to Account B.
- **C.** Use AWS DataSync to replicate the model from Account A to Account B.
- **D.** Create an AWS Site-to-Site VPN connection between Account A and Account В to transfer the model.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (ImportModel API): Amazon Comprehend cung cấp tính năng native (nguyên bản) để sao chép hoặc chia sẻ Custom Model giữa các tài khoản AWS thông qua API ImportModel. Quy trình chuẩn bao gồm: . Tại Account A (Source): Cấu hình Resource-based IAM policy trên Model (hoặc KMS key nếu model được mã hóa) để cho phép Account B truy cập. . Tại Account B (Target): Gọi lệnh ImportModel và trỏ tới ARN của model gốc ở Account A. Đây là giải pháp chính thống, ít tốn công sức lập trình nhất vì AWS xử lý toàn bộ quy trình sao chép ở backend. Tại sao không chọn A (Amazon S3 copy): Một Amazon Comprehend Custom Model không chỉ đơn thuần là các file artifacts nằm trên S3. Nó là một tài nguyên được quản lý (managed resource) bao gồm metadata, cấu hình huấn luyện và endpoint. Việc chỉ sao chép file vật lý từ S3 bucket của Account A sang Account B sẽ không tạo ra một đối tượng "Model" hoạt động được trong giao diện điều khiển (Console) hay API của Account B. Bạn vẫn sẽ cần dùng API để đăng ký nó, do đó cách này thủ công và rườm rà hơn. Tại sao không chọn C (AWS DataSync): AWS DataSync là dịch vụ chuyên dùng để di chuyển lượng dữ liệu lớn giữa các hệ thống lưu trữ (như từ On-premises NAS lên S3, hoặc giữa các EFS). Nó hoạt động ở cấp độ file/object storage, không hiểu ngữ nghĩa của một "Machine Learning Model". Nó không thể dùng để đăng ký hay import model vào dịch vụ Comprehend. Tại sao không chọn D (AWS Site-to-Site VPN): Site-to-Site VPN được dùng để kết nối mạng giữa trung tâm dữ liệu tại chỗ (On-premises) và AWS VPC. Việc kết nối giữa hai tài khoản AWS (Account A và Account B) nằm trong cùng một Region hoàn toàn không cần đến VPN; chúng giao tiếp qua mạng backbone của AWS hoặc VPC Peering/Transit Gateway. VPN là giải pháp sai hoàn toàn về mặt hạ tầng mạng cho ngữ cảnh này.

---

## Question 23

An ML engineer is training a simple neural network model. The ML engineer tracks the performance of the model over time on a validation dataset. The model's performance improves substantially at first and then degrades after a specific number of epochs. Which solutions will mitigate this problem? (Choose two.)

- **A.** Enable early stopping on the model.
- **B.** Increase dropout in the layers.
- **C.** Increase the number of layers.
- **D.** Increase the number of neurons.
- **E.** Investigate and reduce the sources of model bias.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Early stopping): Hiện tượng "hiệu suất cải thiện ban đầu rồi sau đó suy giảm trên tập validation" là định nghĩa sách giáo khoa của Overfitting (Quá khớp). Khi model bắt đầu học thuộc lòng các nhiễu (noise) của tập train thay vì học quy luật chung, lỗi trên tập validation sẽ tăng lên. Early Stopping là kỹ thuật giám sát chỉ số trên tập validation và tự động dừng quá trình huấn luyện ngay khi hiệu suất bắt đầu có dấu hiệu suy giảm, ngăn chặn việc model bị Overfitting. Tại sao chọn B (Increase dropout): Dropout là một kỹ thuật điều chuẩn (Regularization) mạnh mẽ cho mạng nơ-ron. Bằng cách ngẫu nhiên "tắt" một số nơ- ron trong quá trình huấn luyện, Dropout buộc mạng phải học các đặc trưng mạnh mẽ hơn (robust features) và không phụ thuộc quá nhiều vào bất kỳ nơ-ron đơn lẻ nào. Việc tăng tỷ lệ Dropout giúp giảm độ phức tạp thực tế của mô hình, từ đó giảm thiểu Overfitting. Tại sao không chọn C (Increase the number of layers): Tăng số lượng lớp (làm model sâu hơn) đồng nghĩa với việc tăng độ phức tạp và khả năng ghi nhớ (capacity) của mô hình. Một mô hình càng phức tạp thì càng dễ bị Overfitting. Hành động này sẽ làm tình trạng tồi tệ hơn. Tại sao không chọn D (Increase the number of neurons): Tương tự như đáp án C, việc tăng số lượng nơ-ron (làm model rộng hơn) cũng làm tăng khả năng ghi nhớ của mô hình, dẫn đến nguy cơ Overfitting cao hơn. Tại sao không chọn E (Reduce model bias): Khái niệm "Bias" cao thường liên quan đến Underfitting (mô hình quá đơn giản, không học được gì). Trong tình huống này, mô hình đã học được (hiệu suất cải thiện ban đầu) nhưng sau đó học quá kỹ dẫn đến sai trên tập mới (High Variance). Do đó, vấn đề là Variance, không phải Bias.

---

## Question 24

A company has a Retrieval Augmented Generation (RAG) application that uses a vector database to store embeddings of documents. The company must migrate the application to AWS and must implement a solution that provides semantic search of text files. The company has already migrated the text repository to an Amazon S3 bucket. Which solution will meet these requirements?

- **A.** Use an AWS Batch job to process the files and generate embeddings. Use AWS Glue to store the embeddings. Use SQL queries to perform the semantic searches.
- **B.** Use a custom Amazon SageMaker notebook to run a custom script to generate embeddings. Use SageMaker Feature Store to store the embeddings. Use SQL queries to perform the semantic searches.
- **C.** Use the Amazon Kendra S3 connector to ingest the documents from the S3 bucket into Amazon Kendra. Query Amazon Kendra to perform the semantic searches.
- **D.** Use an Amazon Textract asynchronous job to ingest the documents from the S3 bucket. Query Amazon Textract to perform the semantic searches.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Amazon Kendra): . Dịch vụ chuyên biệt (Purpose-built): Amazon Kendra là dịch vụ tìm kiếm thông minh (Intelligent Search Service) được quản lý hoàn toàn bởi AWS. Tính năng cốt lõi của nó là Semantic Search (Tìm kiếm theo ngữ nghĩa) sử dụng Machine Learning để hiểu ý định người dùng thay vì chỉ khớp từ khóa (keyword matching). . Tích hợp sẵn RAG: Kendra thường xuyên được sử dụng làm bộ truy xuất (Retriever) trong kiến trúc RAG (Retrieval Augmented Generation) vì khả năng trả về các đoạn văn bản chính xác cao. . Dễ dàng tích hợp S3: Kendra cung cấp sẵn S3 Connector để tự động thu thập (crawl) và đánh chỉ mục (index) các tài liệu văn bản từ S3 mà không cần viết code xử lý phức tạp. Tại sao không chọn A (AWS Glue & SQL): AWS Glue Data Catalog là một kho chứa metadata, và việc chạy truy vấn SQL tiêu chuẩn trên Glue (thông qua Athena) chỉ hỗ trợ khớp chính xác hoặc khớp mẫu (LIKE operator). SQL truyền thống không hỗ trợ Semantic Search (so sánh độ tương đồng giữa các vector embeddings). Để làm được điều này với SQL, bạn cần các cơ sở dữ liệu hỗ trợ vector extension (như PostgreSQL với pgvector), điều mà Glue không cung cấp. Tại sao không chọn B (SageMaker Feature Store & SQL): SageMaker Feature Store được thiết kế để lưu trữ và phục vụ các tính năng (features) cho mô hình ML với độ trễ thấp (cho inference) hoặc dùng lại cho training. Mặc dù nó có hỗ trợ lưu vector, nhưng nó không phải là một công cụ tìm kiếm (Search Engine). Bạn không thể thực hiện truy vấn tìm kiếm ngữ nghĩa linh hoạt trên Feature Store bằng các câu lệnh SQL đơn thuần. Tại sao không chọn D (Amazon Textract): Amazon Textract là dịch vụ OCR (Optical Character Recognition) dùng để trích xuất văn bản từ hình ảnh hoặc file PDF scan. Nó là công cụ "tiền xử lý" (preprocessing). Textract không có khả năng lưu trữ chỉ mục hay cung cấp API để thực hiện tìm kiếm ngữ nghĩa trên tập dữ liệu đã trích xuất.

---

## Question 25

A company uses Amazon Athena to query a dataset in Amazon S3. The dataset has a target variable that the company wants to predict. The company needs to use the dataset in a solution to determine if a model can predict the target variable. Which solution will provide this information with the LEAST development effort?

- **A.** Create a new model by using Amazon SageMaker Autopilot. Report the model's achieved performance.
- **B.** Implement custom scripts to perform data pre-processing, multiple linear regression, and performance evaluation. Run the scripts on Amazon EC2 instances.
- **C.** Configure Amazon Macie to analyze the dataset and to create a model. Report the model's achieved performance.
- **D.** Select a model from Amazon Bedrock. Tune the model with the data. Report the model's achieved performance.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Amazon SageMaker Autopilot): SageMaker Autopilot là giải pháp AutoML (Tự động hóa Machine Learning) của AWS. Nó tự động thực hiện mọi bước từ khám phá dữ liệu (Data Exploration), tiền xử lý (Preprocessing), chọn thuật toán, đến tinh chỉnh siêu tham số (Hyperparameter Tuning). Để trả lời câu hỏi "Liệu mô hình có thể dự đoán biến mục tiêu không?", bạn chỉ cần trỏ Autopilot vào dữ liệu S3 và chọn cột mục tiêu. Autopilot sẽ chạy hàng loạt thử nghiệm và trả về bảng xếp hạng (Leaderboard) kèm các chỉ số hiệu suất (Accuracy, MSE, F1...). Đây là cách nhanh nhất, tốn ít công sức nhất (Low-code/No-code) để đánh giá tính khả thi. Tại sao không chọn B (Custom scripts on EC2): Việc tự viết script (code tay) để tiền xử lý, chạy hồi quy và đánh giá, cộng với việc phải quản lý hạ tầng máy chủ EC2, đòi hỏi nỗ lực phát triển rất lớn (High development effort). Đây là cách làm thủ công trái ngược với yêu cầu "LEAST development effort". Tại sao không chọn C (Amazon Macie): Amazon Macie là dịch vụ bảo mật dùng để phát hiện dữ liệu nhạy cảm (PII) và phân loại dữ liệu trong S3. Nó hoàn toàn không có chức năng xây dựng mô hình Machine Learning để dự đoán biến mục tiêu (Classification/Regression). Tại sao không chọn D (Amazon Bedrock): Amazon Bedrock cung cấp các mô hình nền tảng (Foundation Models) cho Generative AI (AI tạo sinh). Mặc dù có thể dùng LLM cho một số tác vụ phân loại, nhưng việc "Tune" (tinh chỉnh) một mô hình ngôn ngữ lớn cho một bài toán dữ liệu dạng bảng (tabular data) đơn giản là "dùng dao mổ trâu giết gà", tốn kém và phức tạp hơn nhiều so với việc dùng AutoML chuyên dụng như Autopilot.

---

## Question 26

A company uses Amazon Athena to query a dataset in Amazon S3. The dataset has a target variable that the company wants to predict. The company needs to use the dataset in a solution to determine if a model can predict the target variable. Which solution will provide this information with the LEAST development effort?

- **A.** Create a new model by using Amazon SageMaker Autopilot. Report the model's achieved performance.
- **B.** Implement custom scripts to perform data pre-processing, multiple linear regression, and performance evaluation. Run the scripts on Amazon EC2 instances.
- **C.** Configure Amazon Macie to analyze the dataset and to create a model. Report the model's achieved performance.
- **D.** Select a model from Amazon Bedrock. Tune the model with the data. Report the model's achieved performance.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Amazon SageMaker Autopilot): SageMaker Autopilot là giải pháp AutoML (Tự động hóa Machine Learning) của AWS. Nó tự động thực hiện mọi bước từ khám phá dữ liệu (Data Exploration), tiền xử lý (Preprocessing), chọn thuật toán, đến tinh chỉnh siêu tham số (Hyperparameter Tuning). Để trả lời câu hỏi "Liệu mô hình có thể dự đoán biến mục tiêu không?", bạn chỉ cần trỏ Autopilot vào dữ liệu S3 và chọn cột mục tiêu. Autopilot sẽ chạy hàng loạt thử nghiệm và trả về bảng xếp hạng (Leaderboard) kèm các chỉ số hiệu suất (Accuracy, MSE, F1...). Đây là cách nhanh nhất, tốn ít công sức nhất (Low-code/No-code) để đánh giá tính khả thi. Tại sao không chọn B (Custom scripts on EC2): Việc tự viết script (code tay) để tiền xử lý, chạy hồi quy và đánh giá, cộng với việc phải quản lý hạ tầng máy chủ EC2, đòi hỏi nỗ lực phát triển rất lớn (High development effort). Đây là cách làm thủ công trái ngược với yêu cầu "LEAST development effort". Tại sao không chọn C (Amazon Macie): Amazon Macie là dịch vụ bảo mật dùng để phát hiện dữ liệu nhạy cảm (PII) và phân loại dữ liệu trong S3. Nó hoàn toàn không có chức năng xây dựng mô hình Machine Learning để dự đoán biến mục tiêu (Classification/Regression). Tại sao không chọn D (Amazon Bedrock): Amazon Bedrock cung cấp các mô hình nền tảng (Foundation Models) cho Generative AI (AI tạo sinh). Mặc dù có thể dùng LLM cho một số tác vụ phân loại, nhưng việc "Tune" (tinh chỉnh) một mô hình ngôn ngữ lớn cho một bài toán dữ liệu dạng bảng (tabular data) đơn giản là "dùng dao mổ trâu giết gà", tốn kém và phức tạp hơn nhiều so với việc dùng AutoML chuyên dụng như Autopilot.

---

## Question 27

A company wants to predict the success of advertising campaigns by considering the color scheme of each advertisement. An ML engineer is preparing data for a neural network model. The dataset includes color information as categorical data. Which technique for feature engineering should the ML engineer use for the model?

- **A.** Apply label encoding to the color categories. Automatically assign each color a unique integer.
- **B.** Implement padding to ensure that all color feature vectors have the same length.
- **C.** Perform dimensionality reduction on the color categories.
- **D.** One-hot encode the color categories to transform the color scheme feature into a binary matrix.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (One-hot encode): "Color scheme" (bảng màu) là dữ liệu danh mục định danh (Nominal Categorical Data), nghĩa là các màu sắc như Đỏ, Xanh, Vàng ngang hàng nhau, không có thứ tự hơn kém (Đỏ không "lớn hơn" hay "nhỏ hơn" Xanh). One-hot encoding biến mỗi giá trị màu thành một vector nhị phân riêng biệt (ví dụ: Đỏ = [1, 0, 0], Xanh = [0, 1, 0]). Điều này giúp Mạng Nơ-ron (Neural Network) xử lý từng màu sắc như một tín hiệu độc lập mà không vô tình học sai các mối quan hệ số học (như 1 < 2 < 3) không tồn tại. Tại sao không chọn A (Label encoding): Label encoding gán mỗi màu một số nguyên (ví dụ: Đỏ=1, Xanh=2, Vàng=3). Mạng Nơ-ron sẽ hiểu nhầm rằng Vàng (3) có giá trị "lớn hơn" Đỏ (1) hoặc trung bình cộng của Đỏ và Vàng là Xanh. Điều này sai hoàn toàn về mặt bản chất dữ liệu màu sắc và sẽ làm mô hình học sai lệch. Label encoding chỉ nên dùng cho dữ liệu danh mục có thứ tự (Ordinal Data - ví dụ: Kém, Trung bình, Giỏi). Tại sao không chọn B (Implement padding): Padding là kỹ thuật thêm giá trị (thường là 0) để làm đồng đều độ dài của các chuỗi dữ liệu (sequence length), thường dùng trong xử lý ngôn ngữ tự nhiên (NLP) hoặc chuỗi thời gian. Nó không dùng để mã hóa một biến danh mục đơn lẻ như màu sắc. Tại sao không chọn C (Dimensionality reduction): Dimensionality reduction (như PCA) dùng để giảm số lượng chiều dữ liệu khi chúng quá lớn hoặc bị dư thừa. Trong khi đó, biến màu sắc đang ở dạng thô (text/category), cần được mã hóa thành số trước khi có thể áp dụng bất kỳ thuật toán toán học nào. Hơn nữa, One- hot encoding thực tế làm tăng số chiều dữ liệu, ngược lại với giảm chiều.

---

## Question 28

A company uses a hybrid cloud environment. A model that is deployed on premises uses data in Amazon 53 to provide customers with a live conversational engine. The model is using sensitive data. An ML engineer needs to implement a solution to identify and remove the sensitive data. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Deploy the model on Amazon SageMaker. Create a set of AWS Lambda functions to identify and remove the sensitive data.
- **B.** Deploy the model on an Amazon Elastic Container Service (Amazon ECS) cluster that uses AWS Fargate. Create an AWS Batch job to identify and remove the sensitive data.
- **C.** Use Amazon Macie to identify the sensitive data. Create a set of AWS Lambda functions to remove the sensitive data.
- **D.** Use Amazon Comprehend to identify the sensitive data. Launch Amazon EC2 instances to remove the sensitive data.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Amazon Macie + AWS Lambda): o Phù hợp với mục đích (Purpose-built): Amazon Macie là dịch vụ bảo mật được quản lý hoàn toàn (fully managed), sử dụng Machine Learning và pattern matching chuyên biệt để khám phá và bảo vệ dữ liệu nhạy cảm (PII) lưu trữ trong Amazon S3. Đề bài nêu rõ dữ liệu nằm trong S3, đây là trường hợp sử dụng chính (primary use case) của Macie. o Tối ưu vận hành (Least Operational Overhead): Macie tự động hóa việc quét (scan) mà không cần người dùng xây dựng mô hình hay logic phát hiện. Kết hợp với AWS Lambda (serverless) để thực thi hành động "remove" (xóa hoặc che/redact) dựa trên các phát hiện (findings) của Macie giúp loại bỏ gánh nặng quản lý máy chủ. Đây là kiến trúc Event-driven (Macie $\rightarrow$ EventBridge $\rightarrow$ Lambda) chuẩn mực và ít tốn công sức quản trị nhất. Tại sao không chọn A (Custom identification in Lambda): o Gánh nặng phát triển (High Development Overhead): Phương án này yêu cầu kỹ sư phải tự viết code trong Lambda để "identify" (nhận diện) dữ liệu nhạy cảm. Việc tự xây dựng logic phát hiện PII (bằng Regex hoặc custom ML) cực kỳ phức tạp, dễ sai sót và tốn công bảo trì so với việc dùng dịch vụ có sẵn như Macie. Tại sao không chọn B (ECS/Fargate + AWS Batch): o Sai mục đích và chi phí quản lý cao: Tương tự như đáp án A, việc dùng AWS Batch yêu cầu tự viết logic phát hiện PII. Ngoài ra, AWS Batch thường dùng cho các tác vụ xử lý hàng loạt quy mô lớn (heavy computing), việc thiết lập môi trường Docker, định nghĩa Job definition và quản lý container orchestration cho một tác vụ quản trị dữ liệu này là phức tạp hơn nhiều so với mô hình Serverless của đáp án C. Tại sao không chọn D (Comprehend + EC2): o Gánh nặng vận hành hạ tầng (High Operational Overhead): Mặc dù Amazon Comprehend có khả năng phát hiện PII rất tốt (đặc biệt cho văn bản/NLP), nhưng điểm chết người của phương án này là việc sử dụng EC2. EC2 yêu cầu bạn phải quản lý hệ điều hành (OS patching), cấu hình mạng, auto-scaling và bảo mật server. Đ...

---

## Question 29

An ML engineer needs to create data ingestion pipelines and ML model deployment pipelines on AWS. All the raw data is stored in Amazon S3 buckets. Which solution will meet these requirements?

- **A.** Use Amazon Data Firehose to create the data ingestion pipelines. Use Amazon SageMaker Studio Classic to create the model deployment pipelines.
- **B.** Use AWS Glue to create the data ingestion pipelines. Use Amazon SageMaker Studio Classic to create the model deployment pipelines.
- **C.** Use Amazon Redshift ML to create the data ingestion pipelines. Use Amazon SageMaker Studio Classic to create the model deployment pipelines.
- **D.** Use Amazon Athena to create the data ingestion pipelines. Use an Amazon SageMaker notebook to create the model deployment pipelines.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (AWS Glue + SageMaker Studio Classic): o AWS Glue cho Data Ingestion: Đề bài cho biết dữ liệu thô (raw data) đang nằm trong Amazon S3. AWS Glue là dịch vụ ETL (Extract, Transform, Load) serverless được thiết kế chuyên biệt để xây dựng các pipeline xử lý, làm sạch và tổ chức dữ liệu (ingestion pipelines) từ S3 để chuẩn bị cho Machine Learning. o SageMaker Studio Classic cho Deployment: SageMaker Studio cung cấp giao diện tích hợp để tạo và quản lý SageMaker Pipelines (cho CI/CD của ML). Nó hỗ trợ trực quan hóa, tạo các "Model deployment pipelines" thông qua SageMaker Projects và MLOps template, đáp ứng chính xác yêu cầu thứ hai. Tại sao không chọn A (Amazon Data Firehose): o Sai trường hợp sử dụng (Use Case Mismatch): Amazon Data Firehose là dịch vụ để nạp dữ liệu streaming (thời gian thực) vào các đích đến (như S3, Redshift). Trong bài toán này, dữ liệu đã nằm sẵn ở dạng tĩnh trong S3 (batch data), việc dùng Firehose để xử lý dữ liệu đã lưu trữ là không phù hợp. Firehose thường là bước trước khi dữ liệu vào S3. Tại sao không chọn C (Amazon Redshift ML): o Giới hạn phạm vi (Scope Limitation): Amazon Redshift ML cho phép chạy ML bằng SQL trực tiếp trong kho dữ liệu (Data Warehouse). Tuy nhiên, nó không phải là công cụ đa năng để xây dựng "data ingestion pipelines" tổng quát từ S3. Nó buộc dữ liệu phải được load vào Redshift trước, làm giảm tính linh hoạt so với Glue (có thể xử lý dữ liệu ngay tại S3 - Data Lake). Tại sao không chọn D (Amazon Athena): o Sai chức năng: Amazon Athena là dịch vụ truy vấn tương tác (Interactive Query Service) dùng để phân tích dữ liệu trong S3 bằng SQL, không phải là công cụ để xây dựng và điều phối các "pipeline nạp dữ liệu" tự động và phức tạp (orchestration). Athena thường là công cụ tiêu thụ dữ liệu sau khi Glue đã xử lý.

---

## Question 30

A company that has hundreds of data scientists is using Amazon SageMaker to create ML models. The models are in model groups in the SageMaker Model Registry. The data scientists are grouped into three categories: computer vision, natural language processing (NLP), and speech recognition. An ML engineer needs to implement a solution to organize the existing models into these groups to improve model discoverability at scale. The solution must not affect the integrity of the model artifacts and their existing groupings. Which solution will meet these requirements?

- **A.** Create a custom tag for each of the three categories. Add the tags to the model packages in the SageMaker Model Registry.
- **B.** Create a model group for each category. Move the existing models into these category model groups.
- **C.** Use SageMaker ML Lineage Tracking to automatically identify and tag which model groups should contain the models.
- **D.** Create a Model Registry collection for each of the three categories. Move the existing model groups into the collections.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Model Registry Collections): o Đúng tính năng (Feature Fit): SageMaker Model Registry Collections là tính năng được thiết kế đặc biệt để nhóm các "Model Groups" có liên quan lại với nhau (theo phân cấp). Điều này giải quyết bài toán tổ chức hàng trăm models thành các danh mục lớn (CV, NLP, Speech) để dễ dàng tìm kiếm (discoverability). o Tuân thủ ràng buộc (Constraints Compliance): Đề bài yêu cầu "không làm ảnh hưởng đến tính toàn vẹn và cách nhóm hiện tại" (not affect the integrity... and their existing groupings). Khi bạn thêm một Model Group vào một Collection, bản thân Model Group đó không bị thay đổi, không bị di chuyển vật lý, và các artifact trong S3/ECR vẫn giữ nguyên. Nó chỉ tạo ra một lớp tham chiếu logic bên trên. Tại sao không chọn A (Custom Tags): o Khả năng mở rộng kém hơn (Scalability & Hierarchy): Mặc dù Tags có thể dùng để lọc (filter), nhưng chúng chỉ là metadata phẳng (flat metadata). Khi đề bài nhắc đến việc "organize... into groups" cho hàng trăm data scientists với các danh mục rõ ràng, việc sử dụng cấu trúc phân cấp (Hierarchy) của Collections sẽ quản lý tốt hơn và chuyên nghiệp hơn so với việc chỉ dựa vào tag tìm kiếm. Tag không tạo ra một "view" tổ chức rõ ràng như Collection. Tại sao không chọn B (Create new groups and move): o Vi phạm ràng buộc (Violates Constraints): Đề bài yêu cầu "not affect... their existing groupings". Phương án này đề xuất di chuyển (move) các model từ nhóm cũ sang nhóm mới. Hành động này sẽ phá vỡ cấu trúc tổ chức hiện có, làm thay đổi ARN và lịch sử phiên bản gắn liền với Model Group cũ. Tại sao không chọn C (ML Lineage Tracking): o Sai mục đích (Wrong Purpose): SageMaker ML Lineage Tracking dùng để truy vết nguồn gốc (dữ liệu nào tạo ra model nào, pipeline nào đã chạy). Nó là công cụ để kiểm toán (audit) và tái lập quy trình, không phải là công cụ để tổ chức hay sắp xếp thư mục cho các Model Groups.

---

## Question 31

A company runs an Amazon SageMaker domain in a public subnet of a newly created VPC. The network is configured properly, and ML engineers can access the SageMaker domain. Recently, the company discovered suspicious traffic to the domain from a specific IP address. The company needs to block traffic from the specific IP address. Which update to the network configuration will meet this requirement?

- **A.** Create a security group inbound rule to deny traffic from the specific IP address. Assign the security group to the domain.
- **B.** Create a network ACL inbound rule to deny traffic from the specific IP address. Assign the rule to the default network Ad for the subnet where the domain is located.
- **C.** Create a shadow variant for the domain. Configure SageMaker Inference Recommender to send traffic from the specific IP address to the shadow endpoint.
- **D.** Create a VPC route table to deny inbound traffic from the specific IP address. Assign the route table to the domain.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Network ACL): o Tính năng DENY: Network Access Control List (Network ACL) là lớp bảo mật hoạt động ở cấp độ Subnet và là tường lửa "stateless". Điểm quan trọng nhất là NACL hỗ trợ cả quy tắc cho phép (ALLOW) và từ chối (DENY). Để chặn một IP cụ thể, bạn chỉ cần tạo một rule DENY cho IP đó và đặt số thứ tự ưu tiên (Rule Number) thấp hơn rule ALLOW mặc định. Đây là cơ chế chuẩn để "blacklist" các IP độc hại. Tại sao không chọn A (Security Group): o Chỉ có ALLOW (Allow-only): Security Groups hoạt động ở cấp độ Instance/Interface và là "stateful". Tuy nhiên, Security Group chỉ hỗ trợ các quy tắc cho phép (ALLOW rules). Bạn không thể tạo quy tắc DENY trong Security Group. Mặc định nó chặn tất cả (deny all), nhưng bạn không thể thêm một rule để chặn cụ thể một IP trong khi vẫn cho phép các IP khác. Tại sao không chọn C (Shadow Variant): o Sai miền kiến thức (Wrong Domain): Shadow Variant là một tính năng của SageMaker Inference dùng để thử nghiệm mô hình mới (shadow testing) bằng cách gửi bản sao lưu lượng thực tế đến mô hình mới để đánh giá hiệu năng mà không ảnh hưởng đến phản hồi trả về cho người dùng. Nó hoàn toàn không liên quan đến bảo mật mạng hay chặn IP. Tại sao không chọn D (VPC Route Table): o Sai chức năng: Route Table dùng để định tuyến (routing) lưu lượng mạng (ví dụ: đi ra Internet Gateway hay đi qua NAT Gateway). Nó không có chức năng lọc gói tin (filtering) hay chặn traffic dựa trên IP nguồn.

---

## Question 32

A company is gathering audio, video, and text data in various languages. The company needs to use a large language model (LLM) to summarize the gathered data that is in Spanish. Which solution will meet these requirements in the LEAST amount of time?

- **A.** Train and deploy a model in Amazon SageMaker to convert the data into English text. Train and deploy an LLM in SageMaker to summarize the text.
- **B.** Use Amazon Transcribe and Amazon Translate to convert the data into English text. Use Amazon Bedrock with the Jurassic model to summarize the text.
- **C.** Use Amazon Rekognition and Amazon Translate to convert the data into English text. Use Amazon Bedrock with the Anthropic Claude model to summarize the text.
- **D.** Use Amazon Comprehend and Amazon Translate to convert the data into English text. Use Amazon Bedrock with the Stable Diffusion model to summarize the text.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Transcribe + Translate + Bedrock/Jurassic): o Xử lý Audio/Video (Speech-to-Text): Amazon Transcribe là dịch vụ chuyên dụng để chuyển đổi giọng nói thành văn bản từ cả tệp âm thanh (Audio) và video (lấy track âm thanh). Đây là bước bắt buộc để số hóa dữ liệu phi cấu trúc này. o Tóm tắt văn bản (Summarization): Amazon Bedrock cung cấp quyền truy cập vào các mô hình nền tảng (FM). Mô hình Jurassic (của AI21 Labs) nổi tiếng với khả năng xử lý ngôn ngữ tự nhiên (NLP) mạnh mẽ, đặc biệt là nhiệm vụ đọc hiểu và tóm tắt văn bản phức tạp. o Tối ưu thời gian (Least Time): Việc sử dụng các dịch vụ AI "serverless" có sẵn (Managed AI Services) như Transcribe, Translate và Bedrock giúp loại bỏ hoàn toàn thời gian train mô hình, chỉ cần gọi API để tích hợp. Tại sao không chọn A (Train custom models in SageMaker): o Tốn thời gian và công sức (High Operational Overhead): Đề bài yêu cầu giải pháp tốn ít thời gian nhất. Việc tự thu thập dữ liệu, gán nhãn, huấn luyện (train), tinh chỉnh (fine-tune) và triển khai (deploy) các mô hình riêng biệt cho speech-to-text và summarization trên SageMaker sẽ tốn hàng tuần hoặc hàng tháng so với việc dùng API có sẵn ở đáp án B. Tại sao không chọn C (Rekognition + Translate + Claude): o Sai công cụ xử lý đầu vào: Amazon Rekognition là dịch vụ phân tích hình ảnh/video (Computer Vision) để nhận diện khuôn mặt, vật thể, hoặc văn bản trong khung hình (OCR). Nó không có chức năng chuyển đổi giọng nói (speech) trong video/audio thành văn bản. Do đó, phần nội dung lời nói sẽ bị mất. Tại sao không chọn D (Comprehend + Stable Diffusion): o Sai hoàn toàn về mô hình GenAI: Stable Diffusion là mô hình dùng để tạo sinh hình ảnh (Text-to-Image), không phải là mô hình ngôn ngữ (LLM) để tóm tắt văn bản. o Sai công cụ đầu vào: Amazon Comprehend dùng để phân tích văn bản (sentiment, entities...), không thể dùng để chuyển đổi file Audio/Video sang Text.

---

## Question 33

A financial company receives a high volume of real-time market data streams from an external provider. The streams consist of thousands of JSON records every second. The company needs to implement a scalable solution on AWS to identify anomalous data points. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Ingest real-time data into Amazon Kinesis data streams. Use the built-in RANDOM_CUT_FOREST function in Amazon Managed Service for Apache Flink to process the data streams and to detect data anomalies.
- **B.** Ingest real-time data into Amazon Kinesis data streams. Deploy an Amazon SageMaker endpoint for real-time outlier detection. Create an AWS Lambda function to detect anomalies. Use the data streams to invoke the Lambda function.
- **C.** Ingest real-time data into Apache Kafka on Amazon EC2 instances. Deploy an Amazon SageMaker endpoint for real-time outlier detection. Create an AWS Lambda function to detect anomalies. Use the data streams to invoke the Lambda function.
- **D.** Send real-time data to an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Create an AWS Lambda function to consume the queue messages. Program the Lambda function to start an AWS Glue extract, transform, and load (ETL) job for batch processing and anomaly detection.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Kinesis Data Streams + Managed Service for Apache Flink): o Xử lý luồng tốc độ cao (High Volume Ingestion): Amazon Kinesis Data Streams là dịch vụ serverless tiêu chuẩn để nhận hàng nghìn bản ghi/giây với độ trễ thấp. o Thuật toán chuyên dụng (Built-in Algorithm): RANDOM_CUT_FOREST (RCF) là thuật toán SQL tích hợp sẵn trong dịch vụ phân tích luồng của AWS (trước đây là Kinesis Data Analytics for SQL, nay được hợp nhất vào Managed Service for Apache Flink/SQL). Nó được thiết kế đặc biệt để phát hiện điểm bất thường (anomalies) trong dòng dữ liệu mà không cần huấn luyện mô hình trước (unsupervised). o Tối ưu vận hành (Least Operational Overhead): Đây là giải pháp hoàn toàn được quản lý (Fully Managed). Bạn không cần quản lý hạ tầng máy chủ, không cần quy trình train/deploy model phức tạp như SageMaker. Chỉ cần viết truy vấn SQL/Flink để gọi hàm RCF. Tại sao không chọn B (SageMaker Endpoint + Lambda): o Gánh nặng tích hợp (High Integration Overhead): Việc sử dụng Lambda để gọi SageMaker Endpoint cho hàng nghìn bản ghi mỗi giây là không hiệu quả về mặt kiến trúc. Nó tạo ra độ trễ (latency) mạng không cần thiết và chi phí cao do số lượng invocations quá lớn. Ngoài ra, bạn phải quản lý vòng đời của model trong SageMaker (train, deploy, monitor). Tại sao không chọn C (Kafka on EC2): o Gánh nặng quản trị hạ tầng (Extreme Operational Overhead): Cụm từ "Apache Kafka on Amazon EC2" là dấu hiệu nhận biết của gánh nặng vận hành lớn nhất. Bạn phải tự cài đặt, cấu hình, vá lỗi, và mở rộng cụm Kafka (Brokers, Zookeeper) thay vì dùng dịch vụ serverless như Kinesis. Tại sao không chọn D (SQS + Glue): o Sai mô hình xử lý (Batch vs Streaming): AWS Glue là dịch vụ ETL hướng tới xử lý theo lô (Batch processing) với thời gian khởi động (cold start) tính bằng phút. Nó không thể đáp ứng yêu cầu xử lý dữ liệu thị trường theo thời gian thực (real-time) từng giây.

---

## Question 34

A company has a large collection of chat recordings from customer interactions after a product release. An ML engineer needs to create an ML model to analyze the chat data. The ML engineer needs to determine the success of the product by reviewing customer sentiments about the product. Which action should the ML engineer take to complete the evaluation in the LEAST amount of time?

- **A.** Use Amazon Rekognition to analyze sentiments of the chat conversations.
- **B.** Train a Naive Bayes classifier to analyze sentiments of the chat conversations.
- **C.** Use Amazon Comprehend to analyze sentiments of the chat conversations.
- **D.** Use random forests to classify sentiments of the chat conversations.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Amazon Comprehend): o Dịch vụ có sẵn (Managed Service): Amazon Comprehend là dịch vụ NLP (Natural Language Processing) được AWS quản lý hoàn toàn và đã được huấn luyện trước (pre-trained). Tính năng cốt lõi của nó là Sentiment Analysis (phân tích cảm xúc: Tích cực, Tiêu cực, Trung tính, Hỗn hợp). o Tối ưu thời gian (Least amount of time): Vì mô hình đã được AWS xây dựng sẵn, kỹ sư ML chỉ cần gọi API để nhận kết quả ngay lập tức mà không cần tốn thời gian thu thập dữ liệu, gán nhãn, huấn luyện hay tinh chỉnh mô hình. Đây là giải pháp nhanh nhất (Turn-key solution). Tại sao không chọn A (Amazon Rekognition): o Sai miền dữ liệu (Wrong Domain): Amazon Rekognition là dịch vụ thị giác máy tính (Computer Vision) dùng để phân tích hình ảnh và video (nhận diện khuôn mặt, vật thể). Nó không có khả năng đọc hiểu hay phân tích cảm xúc từ văn bản (chat logs). Tại sao không chọn B (Naive Bayes classifier): o Tốn thời gian phát triển (High Development Time): Naive Bayes là một thuật toán ML cổ điển. Để sử dụng, bạn phải tự chuẩn bị dataset, làm sạch dữ liệu (cleaning), vector hóa (tokenization/vectorization), huấn luyện (training) và đánh giá mô hình. Quy trình này tốn nhiều thời gian hơn rất nhiều so với việc gọi một API có sẵn như Comprehend. Tại sao không chọn D (Random forests): o Tốn thời gian phát triển: Tương tự như đáp án B, Random Forest là một thuật toán học máy cần được huấn luyện thủ công (Custom Model). Việc xây dựng pipeline huấn luyện từ đầu vi phạm yêu cầu "LEAST amount of time" của đề bài.

---

## Question 35

A company has a conversational AI assistant that sends requests through Amazon Bedrock to an Anthropic Claude large language model (LLM). Users report that when they ask similar questions multiple times, they sometimes receive different answers. An ML engineer needs to improve the responses to be more consistent and less random. Which solution will meet these requirements?

- **A.** Increase the temperature parameter and the top_k parameter.
- **B.** Increase the temperature parameter. Decrease the top_k parameter.
- **C.** Decrease the temperature parameter. Increase the top_k parameter.
- **D.** Decrease the temperature parameter and the top_k parameter. Đây là phân tích chi tiết cho câu hỏi về cách tinh chỉnh tham số suy luận (Inference Parameters) của mô hình ngôn ngữ lớn (LLM) trên Amazon Bedrock.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Giảm Temperature và Giảm Top_k): o Giảm Temperature (Temperature $\to$ 0): Tham số Temperature kiểm soát độ "sáng tạo" hay tính ngẫu nhiên của mô hình. Giá trị càng thấp (gần 0), mô hình càng tự tin chọn từ có xác suất cao nhất tiếp theo. Điều này làm cho câu trả lời trở nên định hướng (deterministic), nhất quán và ít ngẫu nhiên hơn. o Giảm Top_k: Tham số Top_k giới hạn số lượng các token tiềm năng được xem xét cho bước tiếp theo. Khi giảm Top_k xuống thấp (ví dụ: k=1), mô hình bị ép buộc chỉ chọn trong số rất ít các từ có khả năng cao nhất, loại bỏ các lựa chọn lạ hoặc ít gặp. o Kết hợp: Việc giảm cả hai tham số này là cách mạnh nhất để ép mô hình hoạt động như một cỗ máy chính xác, luôn trả về cùng một kết quả cho cùng một đầu vào (Consistent & Less Random). Tại sao không chọn A (Increase both): o Tăng tính ngẫu nhiên: Tăng Temperature làm phẳng phân phối xác suất (làm các từ ít khả năng cũng có cơ hội được chọn). Tăng Top_k mở rộng tập hợp các từ được chọn. Kết hợp lại sẽ tạo ra kết quả cực kỳ đa dạng, sáng tạo nhưng rất ngẫu nhiên và thiếu nhất quán, hoàn toàn trái ngược với yêu cầu đề bài. Tại sao không chọn B (Increase Temp, Decrease Top_k): o Xung đột mục tiêu: Mặc dù giảm Top_k giúp hạn chế phạm vi, nhưng việc tăng Temperature lại khuyến khích sự hỗn loạn trong phân phối xác suất. Nhiệt độ cao vẫn sẽ khiến mô hình đưa ra các câu trả lời khác nhau và ảo giác (hallucination) nhiều hơn là sự ổn định. Tại sao không chọn C (Decrease Temp, Increase Top_k): o Chưa tối ưu: Giảm Temperature là đúng hướng để tăng sự ổn định. Tuy nhiên, việc giữ Top_k ở mức cao (Increase Top_k) vẫn mở ra một cửa sổ lựa chọn lớn cho mô hình. So với đáp án D (nơi cả hai đều bị siết chặt), đáp án C vẫn có khả năng sinh ra sự biến thiên (variation) cao hơn.

---

## Question 36

A company is using ML to predict the presence of a specific weed in a farmer's field. The company is using the Amazon SageMaker linear learner built-in algorithm with a value of multiclass_dassifier for the predictorjype hyperparameter. What should the company do to MINIMIZE false positives?

- **A.** Set the value of the weight decay hyperparameter to zero.
- **B.** Increase the number of training epochs.
- **C.** Increase the value of the target_precision hyperparameter.
- **D.** Change the value of the predictorjype hyperparameter to regressor.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Increase target_precision): o Nguyên lý Precision - False Positive: Trong bài toán phân loại, Precision (Độ chính xác) được tính bằng công thức: $Precision = \frac{TP}{TP + FP}$. Để giảm thiểu False Positives (FP - báo động giả, tức là báo có cỏ dại nhưng thực tế không có), ta buộc phải tăng Precision. o Hyperparameter của Linear Learner: Thuật toán SageMaker Linear Learner hỗ trợ hyperparameter target_precision (khi kết hợp với tiêu chí lựa chọn mô hình). Bằng cách tăng giá trị này, bạn đang ra lệnh cho thuật toán tìm kiếm ngưỡng phân loại (threshold) sao cho xác suất dự đoán đúng là cao nhất, chấp nhận việc có thể bỏ sót một số cỏ dại (giảm Recall) miễn là không báo sai. Đây là cách trực tiếp nhất để giải quyết yêu cầu "MINIMIZE false positives". Tại sao không chọn A (Weight decay to zero): o Sai chức năng: weight_decay (suy giảm trọng số) là kỹ thuật Regularization (chống quá khớp/overfitting) bằng cách cộng thêm hình phạt vào hàm mất mát để giữ cho trọng số nhỏ. Việc đặt nó về 0 chỉ làm tắt tính năng này, có thể khiến mô hình bị overfit, nhưng không có cơ chế trực tiếp nào để ưu tiên giảm False Positives so với False Negatives. Tại sao không chọn B (Increase training epochs): o Không giải quyết vấn đề ngưỡng: Tăng số lượng epochs chỉ giúp mô hình học lâu hơn để hội tụ về điểm cực trị của hàm mất mát (Loss function). Nó không thay đổi mục tiêu tối ưu hóa (optimization objective) từ cân bằng sang ưu tiên Precision. Mô hình có thể học tốt hơn nhưng vẫn giữ tỷ lệ FP/FN mặc định. Tại sao không chọn D (Change to regressor): o Sai loại bài toán: predictor_type='regressor' dùng cho bài toán Hồi quy (dự đoán giá trị số liên tục, ví dụ: dự đoán giá nhà, nhiệt độ). Bài toán ở đây là dự đoán sự hiện diện của cỏ dại (Có/Không hoặc Loại A/B/C), tức là bài toán Phân loại (Classification). Chuyển sang Regressor là sai hoàn toàn về mặt kỹ thuật.

---

## Question 37

A company has implemented a data ingestion pipeline for sales transactions from its ecommerce website. The company uses Amazon Data Firehose to ingest data into Amazon OpenSearch Service. The buffer interval of the Firehose stream is set for 60 seconds. An OpenSearch linear model generates real-time sales forecasts based on the data and presents the data in an OpenSearch dashboard. The company needs to optimize the data ingestion pipeline to support sub-second latency for the real-time dashboard. Which change to the architecture will meet these requirements?

- **A.** Use zero buffering in the Firehose stream. Tune the batch size that is used in the PutRecordBatch operation.
- **B.** Replace the Firehose stream with an AWS DataSync task. Configure the task with enhanced fan-out consumers.
- **C.** Increase the buffer interval of the Firehose stream from 60 seconds to 120 seconds.
- **D.** Replace the Firehose stream with an Amazon Simple Queue Service (Amazon SQS) queue.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Zero Buffering): o Giảm độ trễ tối đa: Theo mặc định, Amazon Data Firehose sẽ gom dữ liệu (buffer) trong một khoảng thời gian (ví dụ: 60 giây) hoặc dung lượng nhất định trước khi gửi đến đích để tối ưu hiệu suất I/O. Tuy nhiên, điều này tạo ra độ trễ. Tính năng Zero Buffering (đặt khoảng thời gian buffer về 0) cho phép Firehose gửi dữ liệu đi ngay lập tức sau khi nhận được, giúp giảm độ trễ xuống mức thấp nhất có thể (gần thời gian thực), đáp ứng yêu cầu của dashboard. o Tối ưu Throughput: Việc tinh chỉnh Batch size trong PutRecordBatch giúp đảm bảo rằng dù gửi nhanh nhưng pipeline vẫn xử lý hiệu quả lượng dữ liệu đầu vào lớn mà không bị nghẽn. Tại sao không chọn B (AWS DataSync): o Sai dịch vụ: AWS DataSync là dịch vụ dùng để di chuyển dữ liệu lưu trữ khối lượng lớn (bulk data transfer) giữa các hệ thống lưu trữ (như on-premise NAS, EFS sang S3). Nó không phải là dịch vụ xử lý luồng dữ liệu (streaming ingestion) cho các giao dịch bán hàng thời gian thực từng bản ghi một. Tại sao không chọn C (Increase buffer interval): o Đi ngược mục tiêu: Tăng buffer interval từ 60s lên 120s đồng nghĩa với việc giữ dữ liệu lại lâu hơn trong ống dẫn trước khi gửi đi. Điều này làm tăng độ trễ gấp đôi, hoàn toàn trái ngược với yêu cầu "sub-second latency". Tại sao không chọn D (Amazon SQS): o Mất tính năng tích hợp sẵn: Amazon SQS là hàng đợi thông điệp, nó không có khả năng tự động "ingest" (nạp) dữ liệu vào OpenSearch. Nếu dùng SQS, bạn phải tự xây dựng thêm một lớp compute (ví dụ: Lambda hoặc EC2 worker) để đọc từ SQS và ghi vào OpenSearch. Điều này làm phức tạp hóa kiến trúc và tăng gánh nặng vận hành so với việc chỉ cần chỉnh cấu hình Firehose.

---

## Question 38

A company has trained an ML model in Amazon SageMaker. The company needs to host the model to provide inferences in a production environment. The model must be highly available and must respond with minimum latency. The size of each request will be between 1 KB and 3 MB. The model will receive unpredictable bursts of requests during the day. The inferences must adapt proportionally to the changes in demand. How should the company deploy the model into production to meet these requirements?

- **A.** Create a SageMaker real-time inference endpoint. Configure auto scaling. Configure the endpoint to present the existing model.
- **B.** Deploy the model on an Amazon Elastic Container Service (Amazon ECS) cluster. Use ECS scheduled scaling that is based on the CPU of the ECS cluster.
- **C.** Install SageMaker Operator on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. Deploy the model in Amazon EKS. Set horizontal pod auto scaling to scale replicas based on the memory metric.
- **D.** Use Spot Instances with a Spot Fleet behind an Application Load Balancer (ALB) for inferences. Use the ALBRequestCountPerTarget metric as the metric for auto scaling.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Real-time inference endpoint + Auto scaling): o Minimum Latency (Độ trễ tối thiểu): SageMaker Real-time inference endpoints được thiết kế chuyên biệt cho các ứng dụng yêu cầu phản hồi tức thì với độ trễ thấp (low latency), phù hợp trực tiếp với yêu cầu "respond with minimum latency". o Unpredictable bursts & Adapt proportionally (Xử lý đột biến & Thích ứng): Tính năng Auto Scaling của SageMaker cho phép endpoint tự động tăng giảm số lượng instance (instances count) dựa trên các metric (như InvocationsPerInstance), giúp hệ thống thích ứng linh hoạt với các đợt request tăng đột biến không thể dự đoán trước ("unpredictable bursts"). o Request Size: Kích thước payload từ 1 KB đến 3 MB nằm trong giới hạn hỗ trợ tốt của Real-time endpoints (hỗ trợ payload lên tới 6MB cho synchronous requests). Tại sao không chọn B (Amazon ECS + Scheduled scaling): o Scheduled scaling (Scaling theo lịch trình): Giải pháp này chỉ hoạt động hiệu quả khi bạn biết trước mô hình lưu lượng truy cập (ví dụ: traffic tăng vào 8 giờ sáng). Đề bài nhấn mạnh "unpredictable bursts" (đột biến không dự báo trước), do đó Scheduled scaling sẽ thất bại trong việc đáp ứng nhu cầu tức thời, gây ra độ trễ hoặc lỗi. Tại sao không chọn C (Amazon EKS + SageMaker Operator): o Overhead vận hành: Mặc dù EKS có thể chạy inference, nhưng việc thiết lập và quản lý một cluster Kubernetes chỉ để host model làm tăng độ phức tạp không cần thiết so với dịch vụ native SageMaker. o Scaling Metric (Memory): Scaling dựa trên Memory (bộ nhớ) thường không nhạy bén cho inference bằng scaling dựa trên số lượng request hoặc GPU utilization. Quan trọng hơn, giải pháp này không tối ưu hóa "out-of-the-box" cho latency tốt bằng SageMaker Real-time endpoint. Tại sao không chọn D (Spot Instances + Spot Fleet): o Vi phạm tính sẵn sàng (Availability): Spot Instances có thể bị AWS thu hồi bất cứ lúc nào (với cảnh báo 2 phút). Việc này vi phạm yêu cầu "highly available" của hệ thống Production. Nếu instance bị thu hồi trong lú...

---

## Question 39

An ML engineer needs to use an Amazon EMR cluster to process large volumes of data in batches. Any data loss is unacceptable. Which instance purchasing option will meet these requirements MOST cost-effectively?

- **A.** Run the primary node, core nodes, and task nodes on On-Demand Instances.
- **B.** Run the primary node, core nodes, and task nodes on Spot Instances.
- **C.** Run the primary node on an On-Demand Instance. Run the core nodes and task nodes on Spot Instances.
- **D.** Run the primary node and core nodes on On-Demand Instances. Run the task nodes on Spot Instances.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Primary/Core On-Demand + Task Spot): o Bảo vệ dữ liệu (Data Integrity): Trong kiến trúc EMR, Core nodes chịu trách nhiệm lưu trữ dữ liệu trên HDFS (Hadoop Distributed File System). Nếu chạy Core nodes bằng Spot Instances và bị AWS thu hồi, bạn có nguy cơ mất dữ liệu được lưu trên đó (vi phạm yêu cầu "Any data loss is unacceptable"). Do đó, Core nodes bắt buộc phải dùng On-Demand (hoặc Reserved) để đảm bảo độ bền dữ liệu. o Tối ưu chi phí (Cost-effective): Task nodes chỉ thực hiện tính toán (compute) và không lưu trữ dữ liệu HDFS. Nếu một Task node bị thu hồi, tác vụ đó chỉ đơn giản là được gửi lại cho node khác xử lý mà không gây mất mát dữ liệu. Vì vậy, sử dụng Spot Instances cho Task nodes là cách an toàn nhất để giảm chi phí mà không hy sinh tính toàn vẹn dữ liệu. o Primary Node: Luôn cần ổn định để quản lý cluster, nên dùng On-Demand. Tại sao không chọn A (All On-Demand): o Không tối ưu chi phí: Chạy Task nodes bằng On-Demand là lãng phí tiền bạc vì Task nodes hoàn toàn có thể chịu lỗi (fault-tolerant) và tận dụng được giá rẻ của Spot Instances. Tại sao không chọn B (All Spot): o Rủi ro cao nhất: Nếu Primary node (Spot) bị thu hồi, toàn bộ cluster sẽ dừng hoạt động (terminate). Nếu Core nodes (Spot) bị thu hồi, dữ liệu HDFS có thể bị mất vĩnh viễn. Tại sao không chọn C (Core nodes on Spot): o Rủi ro mất dữ liệu: Như đã phân tích, Core nodes lưu trữ data. Dù HDFS có cơ chế replication, việc mất Core nodes đột ngột do Spot interruption vẫn gây rủi ro cao cho dữ liệu và tính ổn định của HDFS, vi phạm yêu cầu "không chấp nhận mất dữ liệu".

---

## Question 40

A company wants to improve the sustainability of its ML operations. Which actions will reduce the energy usage and computational resources that are associated with the company's training jobs? (Choose two.)

- **A.** Use Amazon SageMaker Debugger to stop training jobs when non-converging conditions are detected.
- **B.** Use Amazon SageMaker Ground Truth for data labeling.
- **C.** Deploy models by using AWS Lambda functions.
- **D.** Use AWS Trainium instances for training.
- **E.** Use PyTorch or TensorFlow with the distributed training option.
- **A.** Use Amazon SageMaker Debugger to stop training jobs when non-converging conditions are detected.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (SageMaker Debugger): o Loại bỏ lãng phí tài nguyên (Waste Reduction): SageMaker Debugger có khả năng giám sát quá trình training theo thời gian thực (real-time monitoring). Nếu nó phát hiện loss function không giảm (non-converging) hoặc các lỗi kỹ thuật (vanishing gradients), nó có thể tự động dừng job. Việc này ngăn chặn việc chạy máy trong nhiều giờ hoặc nhiều ngày vô ích, giúp tiết kiệm điện năng và tài nguyên tính toán đáng kể. Tại sao chọn D (AWS Trainium): o Tối ưu hóa phần cứng (Hardware Efficiency): AWS Trainium là dòng chip được AWS thiết kế chuyên biệt (custom silicon) cho mục đích Deep Learning training. Theo công bố của AWS, Trainium cung cấp hiệu năng trên mỗi watt (performance per watt) tốt hơn nhiều so với các instance GPU tiêu chuẩn, trực tiếp giúp giảm lượng tiêu thụ năng lượng cho cùng một khối lượng công việc training. Tại sao không chọn B (SageMaker Ground Truth): o Sai giai đoạn (Wrong Phase): Ground Truth là dịch vụ hỗ trợ gán nhãn dữ liệu (data labeling), thuộc giai đoạn chuẩn bị dữ liệu (Data Prep). Việc gán nhãn hiệu quả không tác động trực tiếp đến mức tiêu thụ điện năng của hạ tầng tính toán (compute infrastructure) khi chạy training job. Tại sao không chọn C (AWS Lambda): o Sai mục đích (Inference vs Training): AWS Lambda thường được dùng để triển khai mô hình (Inference) cho các workload nhẹ hoặc không thường xuyên. Lambda không được thiết kế và không phù hợp để chạy các training job nặng nề, kéo dài (long-running) và đòi hỏi tài nguyên GPU lớn. Tại sao không chọn E (Distributed Training): o Không đảm bảo tiết kiệm tổng năng lượng: Distributed training giúp giảm thời gian chạy thực tế (wall-clock time) nhưng thường làm tăng tổng tài nguyên tiêu thụ do chi phí giao tiếp mạng (communication overhead) và đồng bộ hóa giữa các node. Ví dụ: Chạy 1 GPU trong 10 giờ (10 GPU-hours) thường tốn ít năng lượng hơn chạy 10 GPU trong 1.2 giờ (12 GPU-hours) do hiệu suất scaling không bao giờ đạt 100%.

---

## Question 41

A company is planning to create several ML prediction models. The training data is stored in Amazon S3. The entire dataset is more than 5 ТВ in size and consists of CSV, JSON, Apache Parquet, and simple text files. The data must be processed in several consecutive steps. The steps include complex manipulations that can take hours to finish running. Some of the processing involves natural language processing (NLP) transformations. The entire process must be automated. Which solution will meet these requirements?

- **A.** Process data at each step by using Amazon SageMaker Data Wrangler. Automate the process by using Data Wrangler jobs.
- **B.** Use Amazon SageMaker notebooks for each data processing step. Automate the process by using Amazon EventBridge.
- **C.** Process data at each step by using AWS Lambda functions. Automate the process by using AWS Step Functions and Amazon EventBridge.
- **D.** Use Amazon SageMaker Pipelines to create a pipeline of data processing steps. Automate the pipeline by using Amazon EventBridge.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (SageMaker Pipelines + EventBridge): o Xử lý tác vụ dài (Long-running tasks): Đề bài ghi rõ các bước xử lý "take hours to finish" (mất hàng giờ). SageMaker Pipelines sử dụng SageMaker Processing Jobs ở bên dưới, chạy trên các EC2 instances chuyên dụng, cho phép xử lý khối lượng công việc lớn (5 TB) trong thời gian dài mà không bị giới hạn thời gian (timeout) ngắn hạn. o Orchestration (Điều phối quy trình): SageMaker Pipelines là dịch vụ native CI/CD cho ML, được thiết kế chuyên biệt để quản lý các "consecutive steps" (các bước liên tiếp), quản lý sự phụ thuộc (dependencies), và lưu vết (lineage) của dữ liệu/model. o Automation: EventBridge tích hợp hoàn hảo để kích hoạt (trigger) Pipeline chạy tự động dựa trên sự kiện (ví dụ: khi có file mới upload lên S3). Tại sao không chọn C (AWS Lambda + Step Functions): o Giới hạn thời gian (Timeout): Đây là lỗi kỹ thuật chí mạng (Hard Fail). AWS Lambda có giới hạn thời gian chạy tối đa là 15 phút. Với yêu cầu xử lý mất "hàng giờ" (hours), Lambda chắc chắn sẽ bị timeout và thất bại giữa chừng. Tại sao không chọn B (SageMaker Notebooks): o Không phải môi trường Production: Notebooks được thiết kế cho việc phát triển (development) và tương tác (interactive), không phải để chạy các quy trình tự động hóa quy mô lớn (production pipelines). Việc dùng EventBridge kích hoạt Notebook là một giải pháp chắp vá, khó quản lý lỗi (error handling) và khó mở rộng. Tại sao không chọn A (SageMaker Data Wrangler): o Hạn chế về tính tùy biến (Custom Logic): Mặc dù Data Wrangler tốt cho việc làm sạch dữ liệu (cleaning), nhưng với các tác vụ "complex NLP manipulations" (xử lý ngôn ngữ tự nhiên phức tạp) thường đòi hỏi code tùy chỉnh sâu (custom scripts/containers) hoặc thư viện chuyên biệt. SageMaker Processing Jobs (thành phần của Pipelines) linh hoạt và mạnh mẽ hơn nhiều cho các tác vụ xử lý hạng nặng (heavy lifting) so với giao diện low-code của Data Wrangler.

---

## Question 42

An ML engineer needs to use AWS CloudFormation to create an ML model that an Amazon SageMaker endpoint will host. Which resource should the ML engineer declare in the CloudFormation template to meet this requirement?

- **A.** AWS::SageMaker::Model
- **B.** AWS::SageMaker::Endpoint
- **C.** AWS::SageMaker::NotebookInstance
- **D.** AWS::SageMaker::Pipeline

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (AWS::SageMaker::Model): Trong kiến trúc triển khai của Amazon SageMaker, resource AWS::SageMaker::Model chính là thành phần chịu trách nhiệm "tạo" đối tượng model logic. Nó định nghĩa các thông số cốt lõi gồm: vị trí của model artifacts (trong S3), Docker container image dùng để chạy inference (Inference Image), và IAM Execution Role. Đây là resource bắt buộc phải được khai báo trước khi bạn có thể tạo Endpoint Configuration hay Endpoint. Tại sao không chọn B (AWS::SageMaker::Endpoint): Resource này được dùng ở bước cuối cùng để provision (cấp phát) tài nguyên HTTPS endpoint thực tế phục vụ cho việc gửi request inference. AWS::SageMaker::Endpoint phụ thuộc vào AWS::SageMaker::EndpointConfig, chứ nó không dùng để định nghĩa bản thân model. Tại sao không chọn C (AWS::SageMaker::NotebookInstance): Đây là một EC2 instance được cài đặt sẵn Jupyter/JupyterLab, đóng vai trò là môi trường phát triển (IDE) cho Data Scientist để viết code và train model. Nó không phải là resource đại diện cho model để hosting/deployment. Tại sao không chọn D (AWS::SageMaker::Pipeline): Resource này dùng để định nghĩa workflow tự động hóa (MLOps pipeline) gồm các bước như xử lý dữ liệu, training, đánh giá model. Mặc dù pipeline có thể tạo ra model (thông qua bước CreateModel), nhưng bản thân resource AWS::SageMaker::Pipeline là công cụ quản lý quy trình, không phải là đối tượng model được host.

---

## Question 43

An advertising company uses AWS Lake Formation to manage a data lake. The data lake contains structured data and unstructured data. The company's ML engineers are assigned to specific advertisement campaigns. The ML engineers must interact with the data through Amazon Athena and by browsing the data directly in an Amazon S3 bucket. The ML engineers must have access to only the resources that are specific to their assigned advertisement campaigns. Which solution will meet these requirements in the MOST operationally efficient way?

- **A.** Configure IAM policies on an AWS Glue Data Catalog to restrict access to Athena based on the ML engineers' campaigns.
- **B.** Store users and campaign information in an Amazon DynamoDB table. Configure DynamoDB Streams to invoke an AWS Lambda function to update S3 bucket policies.
- **C.** Use Lake Formation to authorize AWS Glue to access the S3 bucket. Configure Lake Formation tags to map ML engineers to their campaigns.
- **D.** Configure S3 bucket policies to restrict access to the S3 bucket based on the ML engineers' campaigns.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Lake Formation tags): Đây là giải pháp hiệu quả nhất về mặt vận hành (Operationally Efficient) để quản lý quyền truy cập chi tiết (fine-grained access control) trong Data Lake. o Lake Formation sử dụng mô hình Tag-based Access Control (LF-Tags). Bạn có thể gán tag (ví dụ: Campaign=A) cho database, table, hoặc column, sau đó cấp quyền cho người dùng dựa trên tag này. o Khi có engineer mới hoặc campaign mới, chỉ cần update tag hoặc policy trong Lake Formation một lần duy nhất, thay vì sửa từng IAM Policy hay Bucket Policy phức tạp. o Lake Formation tự động quản lý credential tạm thời để truy cập S3 khi user query qua Athena, đảm bảo user chỉ thấy dữ liệu họ được phép thấy. Tại sao không chọn A (IAM policies on Glue Catalog): o IAM Policy quản lý quyền truy cập vào metadata trong Glue Data Catalog, nhưng nó không thể kiểm soát chi tiết quyền truy cập vào dữ liệu gốc (underlying data) nằm trong S3 một cách linh hoạt và bảo mật granular như Lake Formation (ví dụ: column-level security). o Việc viết IAM condition phức tạp cho từng campaign sẽ rất khó quản lý và bảo trì (Operational burden cao). Tại sao không chọn B (DynamoDB + Lambda + S3 Bucket Policy): o Đây là một giải pháp "tự chế" (custom solution) cực kỳ phức tạp và rủi ro. Bạn phải viết code Lambda, quản lý DynamoDB, và quan trọng nhất là S3 Bucket Policy có giới hạn về kích thước ký tự (policy size limit). o Khi số lượng user và campaign tăng, bucket policy sẽ nhanh chóng chạm trần giới hạn kích thước, khiến giải pháp này không thể mở rộng (not scalable). Tại sao không chọn D (S3 Bucket Policies): o Tương tự như B, S3 Bucket Policy không được thiết kế để quản lý hàng trăm user mapping với hàng trăm campaign riêng biệt. o Việc hard-code quyền truy cập vào bucket policy cho từng engineer/campaign là ác mộng vận hành (operational nightmare), dễ gây lỗi và khó audit.

---

## Question 44

An ML engineer needs to use data with Amazon SageMaker Canvas to train an ML model. The data is stored in Amazon S3 and is complex in structure. The ML engineer must use a file format that minimizes processing time for the data. Which file format will meet these requirements?

- **A.** CSV files compressed with Snappy
- **B.** JSON objects in JSONL format
- **C.** JSON files compressed with gzip
- **D.** Apache Parquet files

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Apache Parquet files): o Hiệu suất tối ưu (Minimize processing time): Apache Parquet là định dạng lưu trữ dạng cột (columnar storage format). Nó cho phép hệ thống (như SageMaker Canvas) chỉ đọc những cột dữ liệu cần thiết thay vì quét toàn bộ dòng, giúp giảm đáng kể lượng I/O và tăng tốc độ xử lý. o Hỗ trợ cấu trúc phức tạp (Complex structure): Đề bài nhắc đến dữ liệu có "complex in structure". Parquet hỗ trợ rất tốt các kiểu dữ liệu lồng nhau (nested data structures) một cách hiệu quả mà vẫn giữ được schema chặt chẽ. o Nén hiệu quả: Parquet thường đi kèm với thuật toán nén (như Snappy) ngay trong định dạng, giúp giảm dung lượng lưu trữ và băng thông mạng tốt hơn so với các định dạng văn bản thuần túy. Tại sao không chọn A (CSV files compressed with Snappy): o CSV là định dạng dựa trên hàng (row-based). Để truy xuất dữ liệu, hệ thống phải phân tích cú pháp (parse) từng dòng văn bản, điều này tốn nhiều CPU hơn và chậm hơn so với format binary như Parquet. o CSV xử lý các cấu trúc dữ liệu phức tạp (như mảng hoặc object lồng nhau) rất kém và thường dễ gây lỗi định dạng. Tại sao không chọn B (JSON objects in JSONL format): o Mặc dù JSONL (JSON Lines) hỗ trợ cấu trúc phức tạp tốt, nhưng nó vẫn là định dạng văn bản (text-based). Việc parse JSON tốn kém tài nguyên CPU và dung lượng file thường lớn hơn nhiều so với Parquet (do lặp lại tên trường ở mỗi bản ghi). Tại sao không chọn C (JSON files compressed with gzip): o Gzip giúp giảm dung lượng file khi truyền tải, nhưng nó là định dạng nén không thể chia nhỏ (non-splittable) một cách hiệu quả trong xử lý song song (parallel processing) như Snappy hay cấu trúc block của Parquet. o Khi cần đọc một phần dữ liệu, hệ thống vẫn phải giải nén (decompress) toàn bộ block hoặc file, gây chậm trễ trong xử lý (processing time).

---

## Question 45

A company has trained and deployed an ML model by using Amazon SageMaker. The company needs to implement a solution to record and monitor all the API call events for the SageMaker endpoint. The solution also must provide a notification when the number of API call events breaches a threshold. Which solution will meet these requirements?

- **A.** Use SageMaker Debugger to track the inferences and to report metrics. Create a custom rule to provide a notification when the threshold is breached.
- **B.** Use SageMaker Debugger to track the inferences and to report metrics. Use the tensor_variance built-in rule to provide a notification when the threshold is breached.
- **C.** Log all the endpoint invocation API events by using AWS CloudTrail. Use an Amazon CloudWatch dashboard for monitoring. Set up a CloudWatch alarm to provide notification when the threshold is breached.
- **D.** Add the Invocations metric to an Amazon CloudWatch dashboard for monitoring. Set up a CloudWatch alarm to provide notification when the threshold is breached.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (CloudTrail + CloudWatch): o Record API call events: Đề bài yêu cầu "record... all the API call events" (ghi lại chi tiết toàn bộ sự kiện gọi API). AWS CloudTrail là dịch vụ duy nhất được thiết kế chuyên biệt để ghi nhật ký (logging/auditing) mọi hành động gọi API trong tài khoản AWS, bao gồm cả thông tin ai gọi, từ IP nào, và thời gian gọi. Đối với SageMaker Endpoint, hành động InvokeEndpoint được coi là "Data Event" và CloudTrail có thể ghi lại nó. o Monitor & Notify: CloudWatch Dashboard dùng để trực quan hóa dữ liệu log/metric này và CloudWatch Alarm dùng để gửi thông báo khi số lượng sự kiện vượt ngưỡng. Sự kết hợp này giải quyết trọn vẹn cả hai vế "Record" và "Monitor/Notify". Tại sao không chọn D (Invocations metric only): o Mặc dù CloudWatch Metric Invocations có thể đếm số lượng request và kích hoạt Alarm (đáp ứng vế Monitor/Notify), nhưng nó không đáp ứng được yêu cầu "Record all the API call events". Metric chỉ lưu trữ con số thống kê (ví dụ: có 100 calls), chứ không lưu trữ bản ghi chi tiết của từng event (log entry) để phục vụ việc kiểm tra hay audit sau này. Tại sao không chọn A (SageMaker Debugger - Custom rule): o SageMaker Debugger được thiết kế để theo dõi trạng thái nội tại của model (internal model state) trong quá trình training (như giá trị weights, gradients, loss) để tìm lỗi thuật toán. Nó không dùng để ghi nhận các sự kiện gọi API ở tầng hạ tầng (Infrastructure/API level). Tại sao không chọn B (SageMaker Debugger - tensor_variance): o Tương tự như A, rule tensor_variance dùng để phát hiện sự bất thường trong tính toán tensor của model (ví dụ: gradient vanishing/exploding), hoàn toàn không liên quan đến việc đếm hay ghi log số lần gọi API của endpoint.

---

## Question 46

A company has AWS Glue data processing jobs that are orchestrated by an AWS Glue workflow. The AWS Glue jobs can run on a schedule or can be launched manually. The company is developing pipelines in Amazon SageMaker Pipelines for ML model development. The pipelines will use the output of the AWS Glue jobs during the data processing phase of model development. An ML engineer needs to implement a solution that integrates the AWS Glue jobs with the pipelines. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use AWS Step Functions for orchestration of the pipelines and the AWS Glue jobs.
- **B.** Use processing steps in SageMaker Pipelines. Configure inputs that point to the Amazon Resource Names (ARNs) of the AWS Glue jobs.
- **C.** Use Callback steps in SageMaker Pipelines to start the AWS Glue workflow and to stop the pipelines until the AWS Glue jobs finish running.
- **D.** Use Amazon EventBridge to invoke the pipelines and the AWS Glue jobs in the desired order.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Callback steps): o Cơ chế hoạt động: CallbackStep trong Amazon SageMaker Pipelines được thiết kế đặc biệt để tích hợp các quy trình xử lý bên ngoài (external processes) vào pipeline. Khi pipeline chạy đến bước này, nó sẽ gửi một token (thường qua SQS) và chuyển sang trạng thái "Waiting". Một Lambda function có thể nhận token này, kích hoạt AWS Glue Workflow hiện có, và khi Glue Workflow chạy xong, Lambda sẽ gọi ngược lại API SendPipelineCallbackStepSuccess để pipeline tiếp tục. o Least Operational Overhead: Giải pháp này tận dụng lại toàn bộ logic của AWS Glue Workflow đã có sẵn (đúng như đề bài yêu cầu là công ty đã có jobs và workflow). Bạn không cần phải viết lại code xử lý dữ liệu (ETL) hay cấu hình lại hạ tầng chạy job, chỉ cần thêm một lớp keo dán (integration layer) nhỏ là xong. Tại sao không chọn A (AWS Step Functions): o Mặc dù Step Functions là công cụ điều phối (orchestrator) rất mạnh, nhưng việc chuyển đổi cả SageMaker Pipelines và AWS Glue Workflow hiện có sang một State Machine mới trong Step Functions đòi hỏi nỗ lực tái cấu trúc (re- architecting) rất lớn. Điều này vi phạm nguyên tắc "LEAST operational overhead". SageMaker Pipelines đã là một orchestrator chuyên dụng cho ML, không cần chồng thêm một orchestrator khác. Tại sao không chọn B (Processing steps): o ProcessingStep trong SageMaker Pipelines dùng để chạy code (Python/bash) bên trong các container do SageMaker quản lý (Processing Job). Nó không có chức năng nhận đầu vào là ARN của một AWS Glue Job để kích hoạt job đó từ xa. o Để dùng cách này, bạn phải migrate (di chuyển) code từ Glue sang SageMaker Processing, điều này tốn rất nhiều công sức và bỏ phí tài nguyên Glue đã thiết lập. Tại sao không chọn D (Amazon EventBridge): o EventBridge được dùng cho kiến trúc hướng sự kiện (Event-driven) lỏng lẻo (loose coupling). Nó rất khó để thiết lập một quy trình tuần tự chặt chẽ (Sequential workflow) theo kiểu: "Pipeline dừng chờ -> Glue chạy xong -> Pipeline chạy tiếp". Việc quản lý tr...

---

## Question 47

A company is using an Amazon Redshift database as its single data source. Some of the data is sensitive. A data scientist needs to use some of the sensitive data from the database. An ML engineer must give the data scientist access to the data without transforming the source data and without storing anonymized data in the database. Which solution will meet these requirements with the LEAST implementation effort?

- **A.** Configure dynamic data masking policies to control how sensitive data is shared with the data scientist at query time.
- **B.** Create a materialized view with masking logic on top of the database. Grant the necessary read permissions to the data scientist.
- **C.** Unload the Amazon Redshift data to Amazon S3. Use Amazon Athena to create schema-on-read with masking logic. Share the view with the data scientist.
- **D.** Unload the Amazon Redshift data to Amazon S3. Create an AWS Glue job to anonymize the data. Share the dataset with the data scientist.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Dynamic Data Masking): o Mapping với đề bài: Đề bài yêu cầu "access... without transforming the source data" (không sửa đổi dữ liệu gốc) và "without storing anonymized data" (không lưu trữ thêm bản sao dữ liệu đã ẩn danh). o Giải pháp kỹ thuật: Amazon Redshift hỗ trợ tính năng Dynamic Data Masking (DDM). Tính năng này cho phép bạn định nghĩa các chính sách bảo mật (masking policies) để ẩn hoặc thay đổi định dạng dữ liệu nhạy cảm (như số thẻ tín dụng, SSN) ngay tại thời điểm truy vấn (query time) dựa trên vai trò của người dùng (Data Scientist). o Least Implementation Effort: Bạn chỉ cần áp dụng policy lên cột dữ liệu và gắn nó với role của Data Scientist. Không cần tạo bảng mới, view mới hay job ETL phức tạp. Tại sao không chọn B (Materialized view with masking logic): o Vi phạm yêu cầu về lưu trữ: Materialized View về bản chất là một bảng vật lý lưu trữ kết quả của câu query. Điều này vi phạm yêu cầu "without storing anonymized data in the database" của đề bài. o Materialized View cũng tiêu tốn tài nguyên lưu trữ và cần cơ chế refresh để đồng bộ dữ liệu, gây thêm gánh nặng quản trị (overhead) so với DDM. Tại sao không chọn C (Unload to S3 + Athena): o Implementation Effort cao: Bạn phải thực hiện nhiều bước: Unload dữ liệu ra S3 $\rightarrow$ Crawler/Define Schema trong Glue/Athena $\rightarrow$ Viết View trong Athena. Quá trình này phức tạp hơn nhiều so với việc cấu hình policy trực tiếp trên Redshift. o Việc di chuyển dữ liệu ra khỏi Redshift cũng làm tăng rủi ro bảo mật và độ trễ khi truy cập. Tại sao không chọn D (Unload to S3 + Glue Job): o Vi phạm yêu cầu: Đề bài cấm "storing anonymized data". Glue job sẽ xử lý và sinh ra một dataset mới đã ẩn danh và lưu nó xuống S3 (hoặc load lại DB), tức là tạo ra bản sao dữ liệu. o Đây là giải pháp tốn kém nhất về công sức triển khai (viết code ETL) và chi phí vận hành (trả tiền cho Glue DPU).

---

## Question 48

An ML engineer is using a training job to fine-tune a deep learning model in Amazon SageMaker Studio. The ML engineer previously used the same pre-trained model with a similar dataset. The ML engineer expects vanishing gradient, underutilized GPU, and overfitting problems. The ML engineer needs to implement a solution to detect these issues and to react in predefined ways when the issues occur. The solution also must provide comprehensive real-time metrics during the training. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use TensorBoard to monitor the training job. Publish the findings to an Amazon Simple Notification Service (Amazon SNS) topic. Create an AWS Lambda function to consume the findings and to initiate the predefined actions.
- **B.** Use Amazon CloudWatch default metrics to gain insights about the training job. Use the metrics to invoke an AWS Lambda function to initiate the predefined actions.
- **C.** Expand the metrics in Amazon CloudWatch to include the gradients in each training step. Use the metrics to invoke an AWS Lambda function to initiate the predefined actions.
- **D.** Use SageMaker Debugger built-in rules to monitor the training job. Configure the rules to initiate the predefined actions.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (SageMaker Debugger): o Khả năng phát hiện lỗi chuyên sâu: Amazon SageMaker Debugger được thiết kế đặc biệt để nhìn sâu vào "nội tạng" của quá trình training (Internal Model State). Nó cung cấp các Built-in Rules (quy tắc có sẵn) để phát hiện chính xác các vấn đề kỹ thuật mà đề bài nêu:  VanishingGradient: Theo dõi giá trị gradient xem có về 0 hay không.  LowGPUUtilization: Theo dõi hiệu suất phần cứng.  Overfit: So sánh loss giữa training và validation set. o Tự động hóa phản ứng (React): Khi một Rule bị vi phạm (trigger), SageMaker Debugger sẽ gửi sự kiện tới Amazon EventBridge. Từ đó, bạn có thể kích hoạt các hành động định sẵn (như StopTrainingJob hoặc gửi SNS notification) mà không cần viết code giám sát phức tạp. o Least Operational Overhead: Vì sử dụng rules "built-in" (có sẵn), Engineer chỉ cần bật cấu hình trong Estimator SDK mà không cần xây dựng hệ thống thu thập log hay phân tích thủ công. Tại sao không chọn A (TensorBoard + SNS + Lambda): o TensorBoard là công cụ tuyệt vời để con người trực quan hóa (visualize) quá trình training, nhưng nó không được thiết kế để tự động kích hoạt hành động khắc phục lỗi (remediation). o Việc xây dựng một pipeline để trích xuất dữ liệu từ TensorBoard, đẩy qua SNS và kích hoạt Lambda là một giải pháp thủ công tốn nhiều công sức bảo trì (high operational overhead). Tại sao không chọn B (CloudWatch default metrics + Lambda): o Phạm vi giám sát hạn chế: CloudWatch Default Metrics chỉ cung cấp thông số về hạ tầng (CPU, Memory, Disk I/O). Nó hoàn toàn "mù" trước các vấn đề về thuật toán như Vanishing Gradient (đòi hỏi phải xem giá trị tensor) hay Overfitting (đòi hỏi logic so sánh loss function). Tại sao không chọn C (Expand CloudWatch metrics + Lambda): o Không khả thi về hiệu năng: Việc đẩy toàn bộ dữ liệu Gradients (vốn rất lớn và cập nhật liên tục từng step) lên CloudWatch Logs sẽ gây ra độ trễ lớn và chi phí cao. o Việc viết logic Lambda để phân tích dòng dữ liệu gradient thời gian thực nhằm phát hiện va...

---

## Question 49

A credit card company has a fraud detection model in production on an Amazon SageMaker endpoint. The company develops a new version of the model. The company needs to assess the new model's performance by using live data and without affecting production end users. Which solution will meet these requirements?

- **A.** Set up SageMaker Debugger and create a custom rule.
- **B.** Set up blue/green deployments with all-at-once traffic shifting.
- **C.** Set up blue/green deployments with canary traffic shifting.
- **D.** Set up shadow testing with a shadow variant of the new model.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Shadow testing): o Cơ chế hoạt động: Shadow Testing (Thử nghiệm bóng) cho phép bạn triển khai phiên bản model mới (Shadow variant) chạy song song với phiên bản sản phẩm (Production variant). o Live Data: Mọi request gửi đến endpoint sẽ được gửi đến cả hai model. o No User Impact: Chỉ có phản hồi từ Production variant được trả về cho người dùng. Phản hồi từ Shadow variant được ghi lại để phân tích sau (để so sánh độ chính xác) nhưng hoàn toàn bị loại bỏ khỏi luồng phản hồi người dùng. Do đó, nếu model mới bị lỗi hoặc chạy chậm, nó không hề ảnh hưởng đến trải nghiệm của người dùng cuối. Đây chính xác là những gì đề bài yêu cầu. Tại sao không chọn A (SageMaker Debugger): o SageMaker Debugger chủ yếu dùng để giám sát trạng thái nội tại (tensor, weights) trong quá trình Training hoặc phát hiện lỗi kỹ thuật. Nó không phải là phương pháp deployment để so sánh hiệu năng suy luận (inference performance) giữa hai phiên bản model trên production. Tại sao không chọn B (Blue/Green all-at-once): o Phương pháp này chuyển toàn bộ 100% traffic sang model mới ngay lập tức. Nếu model mới có lỗi, toàn bộ người dùng sẽ bị ảnh hưởng ngay lập tức. Điều này vi phạm yêu cầu "without affecting production end users". Tại sao không chọn C (Blue/Green canary): o Canary deployment chuyển một phần nhỏ traffic (ví dụ 10%) sang model mới để thử nghiệm. Mặc dù rủi ro thấp hơn All-at-once, nhưng vẫn có 10% người dùng nhận phản hồi từ model mới. Nếu model mới sai, những người dùng này sẽ bị ảnh hưởng.

---

## Question 50

A company stores time-series data about user clicks in an Amazon S3 bucket. The raw data consists of millions of rows of user activity every day. ML engineers access the data to develop their ML models. The ML engineers need to generate daily reports and analyze click trends over the past 3 days by using Amazon Athena. The company must retain the data for 30 days before archiving the data. Which solution will provide the HIGHEST performance for data retrieval?

- **A.** Keep all the time-series data without partitioning in the S3 bucket. Manually move data that is older than 30 days to separate S3 buckets.
- **B.** Create AWS Lambda functions to copy the time-series data into separate S3 buckets. Apply S3 Lifecycle policies to archive data that is older than 30 days to S3 Glacier Flexible Retrieval.
- **C.** Organize the time-series data into partitions by date prefix in the S3 bucket. Apply S3 Lifecycle policies to archive partitions that are older than 30 days to S3 Glacier Flexible Retrieval.
- **D.** Put each day's time-series data into its own S3 bucket. Use S3 Lifecycle policies to archive S3 buckets that hold data that is older than 30 days to S3 Glacier Flexible Retrieval.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Partitioning by date): o Tối ưu hiệu năng Athena (Highest Performance): Amazon Athena hoạt động theo cơ chế tính phí và hiệu năng dựa trên lượng dữ liệu quét (data scanned). Khi dữ liệu time-series được tổ chức thành các partition theo cấu trúc thư mục (ví dụ: s3://bucket/data/year=2024/month=01/day=11/), Athena có thể sử dụng kỹ thuật Partition Pruning. o Khi Engineer truy vấn dữ liệu "3 ngày qua", Athena chỉ quét đúng 3 thư mục tương ứng và bỏ qua toàn bộ dữ liệu của 27 ngày còn lại. Điều này giúp giảm đáng kể I/O, làm cho truy vấn nhanh hơn rất nhiều so với việc quét toàn bộ (Full scan). o Tự động hóa lưu trữ: S3 Lifecycle Policies hoạt động hiệu quả trên các prefix (thư mục), cho phép tự động chuyển data cũ (>30 ngày) sang Glacier để tiết kiệm chi phí mà không cần can thiệp thủ công. Tại sao không chọn A (No partitioning): o Nếu không phân vùng (partition), Athena buộc phải thực hiện Full Table Scan (quét toàn bộ file trong bucket) cho bất kỳ câu lệnh truy vấn nào, dù chỉ cần data của 1 ngày. Điều này khiến tốc độ truy vấn cực chậm khi dữ liệu lớn dần và chi phí tăng vọt. o Việc di chuyển dữ liệu thủ công (Manually move) là gánh nặng vận hành không cần thiết. Tại sao không chọn B (Lambda to separate buckets): o Việc sao chép dữ liệu (copy) tạo ra sự dư thừa lưu trữ (duplication) và tốn chi phí không đáng có. o Phân tán dữ liệu ra nhiều bucket làm phức tạp hóa việc định nghĩa bảng trong Athena (Athena table thường trỏ về một location gốc duy nhất). Việc join dữ liệu từ nhiều bucket khác nhau sẽ làm giảm hiệu năng truy vấn. Tại sao không chọn D (One bucket per day): o Đây là một thiết kế "anti-pattern" trong Data Lake. Việc tạo hàng ngàn bucket (mỗi ngày 1 cái) sẽ chạm giới hạn số lượng bucket của AWS (mặc định 100). o Athena sẽ gặp rất nhiều khó khăn để truy vấn tổng hợp (aggregate) dữ liệu xuyên suốt nhiều ngày vì không thể định nghĩa một bảng (table) duy nhất bao trùm hàng loạt bucket rời rạc một cách hiệu quả.

---

## Question 51

A company has deployed an ML model that detects fraudulent credit card transactions in real time in a banking application. The model uses Amazon SageMaker Asynchronous Inference. Consumers are reporting delays in receiving the inference results. An ML engineer needs to implement a solution to improve the inference performance. The solution also must provide a notification when a deviation in model quality occurs. Which solution will meet these requirements?

- **A.** Use SageMaker real-time inference for inference. Use SageMaker Model Monitor for notifications about model quality.
- **B.** Use SageMaker batch transform for inference. Use SageMaker Model Monitor for notifications about model quality.
- **C.** Use SageMaker Serverless Inference for inference. Use SageMaker Inference Recommender for notifications about model quality.
- **D.** Keep using SageMaker Asynchronous Inference for inference. Use SageMaker Inference Recommender for notifications about model quality.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Real-time Inference + Model Monitor): o Giải quyết vấn đề độ trễ (Delays): Đề bài mô tả ứng dụng phát hiện gian lận thẻ tín dụng "in real time" (thời gian thực), nhưng người dùng đang gặp sự cố trễ (delays) do sử dụng Asynchronous Inference. Asynchronous Inference được thiết kế cho các payload lớn và thời gian xử lý dài (có thể lên tới 1 giờ), nên nó có độ trễ hàng đợi (queueing delay) cố hữu, không phù hợp cho giao dịch cần phản hồi tức thì. Chuyển sang Real-time Inference là giải pháp chuẩn xác để đảm bảo độ trễ thấp (low latency) ở mức mili-giây. o Giám sát chất lượng (Model Quality): SageMaker Model Monitor là công cụ chuyên dụng để theo dõi drift (sự trôi dạt) về chất lượng model (Model Quality Drift) hoặc dữ liệu (Data Drift) trên production endpoint và gửi thông báo qua CloudWatch/SNS khi phát hiện sai lệch. Tại sao không chọn B (Batch Transform): o Batch Transform dùng để xử lý dữ liệu hàng loạt (offline processing) cho lượng lớn dữ liệu được lưu sẵn trong S3, không phải cho ứng dụng tương tác thời gian thực. Độ trễ của nó là phút hoặc giờ, tệ hơn cả Asynchronous Inference. Tại sao không chọn C (Serverless Inference + Inference Recommender): o Serverless Inference: Mặc dù tiện lợi, nhưng Serverless Inference có thể gặp vấn đề "Cold Start" (khởi động nguội) gây độ trễ ngẫu nhiên, không ổn định bằng Real-time Inference (Provisioned instances) cho các ứng dụng ngân hàng quan trọng. o Sai công cụ: SageMaker Inference Recommender là công cụ dùng để load test và gợi ý chọn loại instance/cấu hình tối ưu trước khi triển khai, chứ không phải là công cụ giám sát chất lượng model (quality deviation) liên tục trong khi vận hành (runtime). Tại sao không chọn D (Keep Asynchronous Inference): o Như đã giải thích ở mục A, bản chất của Asynchronous Inference là nguyên nhân gây ra độ trễ. Giữ nguyên kiến trúc này sẽ không giải quyết được vấn đề cốt lõi của người dùng ("consumers are reporting delays").

---

## Question 52

An ML engineer needs to implement a solution to host a trained ML model. The rate of requests to the model will be inconsistent throughout the day. The ML engineer needs a scalable solution that minimizes costs when the model is not in use. The solution also must maintain the model's capacity to respond to requests during times of peak usage. Which solution will meet these requirements?

- **A.** Create AWS Lambda functions that have fixed concurrency to host the model. Configure the Lambda functions to automatically scale based on the number of requests to the model.
- **B.** Deploy the model on an Amazon Elastic Container Service (Amazon ECS) cluster that uses AWS Fargate. Set a static number of tasks to handle requests during times of peak usage.
- **C.** Deploy the model to an Amazon SageMaker endpoint. Deploy multiple copies of the model to the endpoint. Create an Application Load Balancer to route traffic between the different copies of the model at the endpoint.
- **D.** Deploy the model to an Amazon SageMaker endpoint. Create SageMaker endpoint auto scaling policies that are based on Amazon CloudWatch metrics to adjust the number of instances dynamically.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (SageMaker Endpoint Auto Scaling): o Khả năng mở rộng (Scalable): Amazon SageMaker Endpoints hỗ trợ tính năng Application Auto Scaling tích hợp sẵn. Bạn có thể định nghĩa chính sách (scaling policy) dựa trên các chỉ số CloudWatch (như InvocationsPerInstance hoặc CPUUtilization). o Tối ưu chi phí & Hiệu năng: Hệ thống sẽ tự động thêm instance (Scale Out) khi traffic tăng để đảm bảo năng lực xử lý giờ cao điểm, và quan trọng hơn là tự động tắt bớt instance (Scale In) khi traffic giảm hoặc không có người dùng, giúp giảm thiểu chi phí đúng theo yêu cầu đề bài. Tại sao không chọn A (Lambda with fixed concurrency): o Mâu thuẫn kỹ thuật: Việc thiết lập "fixed concurrency" (đồng thời cố định) đồng nghĩa với việc bạn giới hạn khả năng mở rộng của Lambda, đi ngược lại với yêu cầu "configure... to automatically scale". o Ngoài ra, Lambda có giới hạn về thời gian chạy (timeout) và dung lượng bộ nhớ, thường không phải là lựa chọn tối ưu cho các model ML phức tạp cần stateful hosting. Tại sao không chọn B (ECS Fargate with static tasks): o Lãng phí chi phí: "Static number of tasks" (Số lượng tác vụ tĩnh) có nghĩa là bạn phải luôn duy trì số lượng container đủ để chịu tải cho lúc cao điểm nhất (peak usage). Khi traffic thấp, các resource này vẫn chạy và tính tiền, vi phạm yêu cầu "minimizes costs when the model is not in use". Tại sao không chọn C (SageMaker Endpoint + Manual ALB): o Sai kiến trúc: SageMaker Endpoint bản thân nó đã bao gồm một lớp Load Balancer nội bộ để phân phối traffic tới các instance phía sau. Bạn không cần (và không thể) tạo thủ công một Application Load Balancer (ALB) để điều hướng traffic giữa các model copy bên trong một endpoint. o Thiếu cơ chế Auto Scaling để tối ưu chi phí.

---

## Question 53

A company uses Amazon SageMaker Studio to develop an ML model. The company has a single SageMaker Studio domain. An ML engineer needs to implement a solution that provides an automated alert when SageMaker compute costs reach a specific threshold. Which solution will meet these requirements?

- **A.** Add resource tagging by editing the SageMaker user profile in the SageMaker domain. Configure AWS Cost Explorer to send an alert when the threshold is reached.
- **B.** Add resource tagging by editing the SageMaker user profile in the SageMaker domain. Configure AWS Budgets to send an alert when the threshold is reached.
- **C.** Add resource tagging by editing each user's IAM profile. Configure AWS Cost Explorer to send an alert when the threshold is reached.
- **D.** Add resource tagging by editing each user's IAM profile. Configure AWS Budgets to send an alert when the threshold is reached.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (SageMaker User Profile Tags + AWS Budgets): o Resource Tagging: Trong Amazon SageMaker Studio, để theo dõi chi phí theo từng người dùng hoặc nhóm, bạn cần gắn thẻ (tag) vào SageMaker User Profile. Các thẻ này sẽ tự động được lan truyền (propagate) xuống các tài nguyên tính toán (như Apps, Notebooks, Training Jobs) mà user đó tạo ra. Điều này cho phép phân bổ chi phí (Cost Allocation) chính xác trong hóa đơn. o Alerting: AWS Budgets là dịch vụ chuyên dụng để thiết lập ngân sách và gửi thông báo cảnh báo (email/SNS) khi chi phí thực tế hoặc dự báo vượt quá ngưỡng (threshold) bạn đặt ra. Đây là giải pháp tiêu chuẩn cho yêu cầu "automated alert when costs reach a specific threshold". Tại sao không chọn A (AWS Cost Explorer): o Sai chức năng: AWS Cost Explorer chủ yếu là công cụ để phân tích và báo cáo lịch sử chi phí hoặc dự báo. Mặc dù nó có tính năng Cost Anomaly Detection, nhưng để thiết lập một cảnh báo ngưỡng cố định đơn giản (ví dụ: "Báo cho tôi khi tiêu hết $100"), AWS Budgets là công cụ trực tiếp và phù hợp hơn. Tại sao không chọn C và D (Tagging IAM Profile): o Cơ chế không hiệu quả: Việc gắn tag vào IAM User hoặc IAM Role không tự động gán tag đó cho các tài nguyên (như EC2 instances, SageMaker Jobs) mà IAM identity đó tạo ra. Do đó, trong bảng phân tích chi phí (Cost Allocation Report), các tài nguyên SageMaker sẽ không mang tag của IAM user, khiến việc theo dõi chi phí theo user trở nên bất khả thi theo cách này. o Riêng C còn sai vì dùng Cost Explorer để alert như lý do ở mục A.

---

## Question 54

A company uses Amazon SageMaker for its ML workloads. The company's ML engineer receives a 50 MB Apache Parquet data file to build a fraud detection model. The file includes several correlated columns that are not required. What should the ML engineer do to drop the unnecessary columns in the file with the LEAST effort?

- **A.** Download the file to a local workstation. Perform one-hot encoding by using a custom Python script.
- **B.** Create an Apache Spark job that uses a custom processing script on Amazon EMR.
- **C.** Create a SageMaker processing job by calling the SageMaker Python SDK.
- **D.** Create a data flow in SageMaker Data Wrangler. Configure a transform step.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (SageMaker Data Wrangler): o Least Effort (Nỗ lực ít nhất): SageMaker Data Wrangler là công cụ Low- code/No-code (Giao diện người dùng đồ họa) được tích hợp sẵn trong SageMaker Studio. Nó cho phép bạn import dữ liệu từ S3, xem trước (visualize), và thực hiện các thao tác xử lý dữ liệu như Drop Column chỉ bằng các cú click chuột mà không cần viết một dòng code nào. o Đối với file kích thước nhỏ (50 MB) và yêu cầu đơn giản (bỏ cột), việc sử dụng công cụ UI kéo-thả là nhanh chóng và tiện lợi nhất so với việc phải viết code và setup môi trường. Tại sao không chọn A (Download to local workstation): o Bad Practice: Việc download dữ liệu ra khỏi môi trường Cloud (AWS) về máy local thường bị hạn chế vì lý do bảo mật và quản trị dữ liệu (Data Governance). o Manual process: Đây là quy trình thủ công, khó tự động hóa và không thể scale nếu sau này file lớn hơn hoặc cần xử lý định kỳ. Tại sao không chọn B (Amazon EMR Spark job): o Overkill (Dùng dao mổ trâu giết gà): Amazon EMR (Elastic MapReduce) là dịch vụ dành cho Big Data xử lý hàng TB/PB dữ liệu. Việc khởi tạo và cấu hình cả một cluster EMR chỉ để xử lý một file 50 MB là cực kỳ lãng phí tài nguyên, tiền bạc và công sức quản trị. Tại sao không chọn C (SageMaker Processing Job): o High Effort: Để chạy Processing Job, bạn phải viết script Python, chuẩn bị Docker container, và cấu hình SDK để submit job. Mặc dù đây là cách chuẩn cho quy trình tự động hóa (MLOps), nhưng so với việc click chuột trong Data Wrangler cho một tác vụ ad-hoc đơn giản, thì Processing Job tốn nhiều công sức triển khai hơn (coding overhead).

---

## Question 55

company is creating an application that will recommend products for customers to purchase. The application will make API calls to Amazon Q Business. The company must ensure that responses from Amazon Q Business do not include the name of the company's main competitor. Which solution will meet this requirement?

- **A.** Configure the competitor's name as a blocked phrase in Amazon Q Business.
- **B.** Configure an Amazon Q Business retriever to exclude the competitor's name.
- **C.** Configure an Amazon Kendra retriever for Amazon Q Business to build indexes that exclude the competitor's name.
- **D.** Configure document attribute boosting in Amazon Q Business to deprioritize the competitor's name.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Blocked phrase): o Tính năng trực tiếp: Amazon Q Business cung cấp tính năng Global Controls (Kiểm soát toàn cục), cho phép quản trị viên định nghĩa danh sách Blocked phrases (Các cụm từ bị chặn). o Cơ chế hoạt động: Khi bạn thêm tên đối thủ vào danh sách này, Amazon Q Business sẽ chủ động phát hiện và ngăn chặn cụm từ đó xuất hiện trong câu trả lời được sinh ra (generated response) cho người dùng cuối. Đây là giải pháp "Hard block" (chặn cứng) đảm bảo tuân thủ yêu cầu đề bài một cách chính xác nhất. Tại sao không chọn B (Retriever exclusion): o Việc cấu hình Retriever để loại bỏ tên đối thủ thường tác động vào việc tìm kiếm tài liệu (filtering documents). Nếu một tài liệu sản phẩm hợp lệ của công ty có chứa tên đối thủ (ví dụ: trong bảng so sánh), tài liệu đó có thể bị loại bỏ hoàn toàn, dẫn đến mất thông tin ngữ cảnh cần thiết. Nó lọc ở đầu vào (Input), không phải kiểm soát đầu ra (Output). Tại sao không chọn C (Kendra index exclusion): o Tương tự như B, việc can thiệp vào quá trình Indexing của Amazon Kendra là để quản lý dữ liệu nguồn. Nó không đảm bảo ngăn chặn được việc mô hình ngôn ngữ (LLM) tự sinh ra (hallucinate) tên đối thủ trong quá trình tạo câu trả lời. Tại sao không chọn D (Document attribute boosting): o Deprioritize $\neq$ Block: Việc hạ thấp độ ưu tiên (Deprioritize) chỉ làm cho các tài liệu chứa tên đối thủ xuất hiện ở vị trí thấp hơn trong kết quả tìm kiếm. Tuy nhiên, nếu không có tài liệu nào khác tốt hơn, Amazon Q vẫn có thể sử dụng tài liệu đó và sinh ra câu trả lời chứa tên đối thủ. Đây là biện pháp "Soft" (mềm), không đảm bảo yêu cầu cấm tuyệt đối.

---

## Question 56

An ML engineer needs to use Amazon SageMaker to fine-tune a large language model (LLM) for text summarization. The ML engineer must follow a low-code no-code (LCNC) approach. Which solution will meet these requirements?

- **A.** Use SageMaker Studio to fine-tune an LLM that is deployed on Amazon EC2 instances.
- **B.** Use SageMaker Autopilot to fine-tune an LLM that is deployed by a custom API endpoint.
- **C.** Use SageMaker Autopilot to fine-tune an LLM that is deployed on Amazon EC2 instances.
- **D.** Use SageMaker Autopilot to fine-tune an LLM that is deployed by SageMaker JumpStart.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Autopilot + JumpStart): o Low-code/No-code (LCNC): Amazon SageMaker Autopilot đã hỗ trợ tính năng Fine-tuning LLMs (tinh chỉnh mô hình ngôn ngữ lớn) cho bài toán Generative AI (như Text Summarization). o Integration: Quy trình này tích hợp trực tiếp với SageMaker JumpStart - thư viện chứa các Foundation Models (FM) được huấn luyện sẵn. Bạn chỉ cần chọn model từ JumpStart, cung cấp dataset, và Autopilot sẽ tự động chạy experiment để fine-tune mà không cần viết code training phức tạp. o Deployment: Sau khi fine-tune xong, model có thể được deploy dễ dàng thông qua cơ chế "One-click deployment" của JumpStart (hoặc tạo Endpoint từ Model Package của Autopilot), đảm bảo tính chất Low-code từ đầu đến cuối. Tại sao không chọn A (SageMaker Studio + EC2): o Việc tự fine-tune trên Studio và quản lý triển khai thủ công lên EC2 instances là phương pháp High-code (nhiều code), đòi hỏi kiến thức sâu về quản trị hạ tầng và scripting, vi phạm yêu cầu LCNC. Tại sao không chọn B (Custom API endpoint): o "Custom API endpoint" ám chỉ việc bạn phải tự xây dựng lớp API (ví dụ dùng Flask/FastAPI, Dockerize, setup Server), đây là công việc nặng về kỹ thuật (Engineering heavy), không phải Low-code. Tại sao không chọn C (Deploy on EC2): o Tương tự như A, việc deploy trực tiếp lên EC2 (IaaS) đòi hỏi bạn phải tự quản lý OS, driver GPU, security patching và scaling, không phù hợp với tiêu chí giảm thiểu vận hành của LCNC.

---

## Question 57

A company has an ML model that needs to run one time each night to predict stock values. The model input is 3 MB of data that is collected during the current day. The model produces the predictions for the next day. The prediction process takes less than 1 minute to finish running. How should the company deploy the model on Amazon SageMaker to meet these requirements?

- **A.** Use a multi-model serverless endpoint. Enable caching.
- **B.** Use an asynchronous inference endpoint. Set the InitialInstanceCount parameter to 0.
- **C.** Use a real-time endpoint. Configure an auto scaling policy to scale the model to 0 when the model is not in use.
- **D.** Use a serverless inference endpoint. Set the MaxConcurrency parameter to 1.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Serverless inference endpoint): o Tối ưu chi phí cho traffic ngắt quãng: Mô hình chỉ chạy "một lần mỗi đêm" (intermittent traffic). SageMaker Serverless Inference có khả năng tự động Scale to 0 khi không có request, nghĩa là bạn không tốn bất kỳ chi phí nào cho thời gian chờ (idle time). Bạn chỉ trả tiền cho đúng khoảng thời gian tính toán (< 1 phút) mà mô hình chạy. o Phù hợp với workload: Serverless Inference hỗ trợ payload lên tới 4MB (đề bài 3MB) và thời gian xử lý tối đa 3 phút (đề bài < 1 phút), hoàn toàn phù hợp với yêu cầu kỹ thuật này. o MaxConcurrency = 1: Vì chỉ chạy 1 lần/đêm, không cần xử lý song song, đặt concurrency = 1 để giới hạn tài nguyên là hợp lý. Tại sao không chọn A (Multi-model serverless): o Dư thừa: Multi-model Endpoint (MME) được thiết kế để host hàng trăm/hàng ngàn model khác nhau trên cùng một container chung để tiết kiệm chi phí. Ở đây chỉ có một model duy nhất, nên việc dùng MME là không cần thiết và làm phức tạp cấu hình. Tại sao không chọn B (Asynchronous inference endpoint): o Sai mục đích: Asynchronous Inference thường dùng cho các payload rất lớn (lên tới 1GB) hoặc thời gian xử lý rất dài (lên tới 1 giờ). Với input nhỏ (3 MB) và xử lý nhanh (< 1 phút), Serverless Inference nhanh gọn và đơn giản hơn nhiều so với việc quản lý hàng đợi (queue) của Async. Tại sao không chọn C (Real-time endpoint scale to 0): o Lỗi kỹ thuật: Standard Real-time Endpoint (Provisioned Instances) không thể scale về 0. Số lượng instance tối thiểu luôn là 1. Do đó, bạn sẽ phải trả tiền cho instance đó chạy 24/7 dù chỉ dùng nó 1 phút mỗi đêm. Điều này cực kỳ lãng phí.

---

## Question 58

An ML engineer trained an ML model on Amazon SageMaker to detect automobile accidents from dosed-circuit TV footage. The ML engineer used SageMaker Data Wrangler to create a training dataset of images of accidents and non-accidents. The model performed well during training and validation. However, the model is underperforming in production because of variations in the quality of the images from various cameras. Which solution will improve the model's accuracy in the LEAST amount of time?

- **A.** Collect more images from all the cameras. Use Data Wrangler to prepare a new training dataset.
- **B.** Recreate the training dataset by using the Data Wrangler corrupt image transform. Specify the impulse noise option.
- **C.** Recreate the training dataset by using the Data Wrangler enhance image contrast transform. Specify the Gamma contrast option.
- **D.** Recreate the training dataset by using the Data Wrangler resize image transform. Crop all images to the same size.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Corrupt image transform - Impulse noise): o Tăng cường tính bền vững (Robustness via Data Augmentation): Vấn đề cốt lõi là mô hình đang bị "Overfitting" với dữ liệu sạch trong phòng lab và thất bại khi gặp dữ liệu thực tế "kém chất lượng" (nhiễu, mờ) từ CCTV. o Trong SageMaker Data Wrangler, nhóm tính năng "Corrupt image" (bao gồm thêm nhiễu Impulse noise, Gaussian noise, Blur...) được thiết kế chính xác để giải quyết vấn đề này. Bằng cách chủ động thêm nhiễu vào dữ liệu huấn luyện, bạn ép mô hình học các đặc trưng quan trọng (như hình dáng xe, va chạm) thay vì phụ thuộc vào độ sắc nét hay chất lượng điểm ảnh. o Kỹ thuật này giúp mô hình "miễn nhiễm" tốt hơn với các biến thể chất lượng thấp từ camera thực tế mà không cần thu thập thêm dữ liệu mới. Tại sao không chọn A (Collect more images): o Vi phạm ràng buộc thời gian: Đề bài yêu cầu giải pháp tốn "LEAST amount of time". Việc thu thập thêm hình ảnh từ camera, gán nhãn lại (labeling), và chuẩn bị dữ liệu mới là một quy trình cực kỳ tốn thời gian và công sức so với việc chỉ click chọn biến đổi (transform) trên dữ liệu có sẵn. Tại sao không chọn C (Enhance image contrast): o Sai mục tiêu: "Enhance image contrast" (Tăng độ tương phản) thường dùng để xử lý vấn đề về ánh sáng (quá tối/quá sáng). Tuy nhiên, "variations in quality" từ CCTV thường ám chỉ nhiễu hạt (grain), mờ (blur) hoặc nén ảnh (compression artifacts). o Việc tăng tương phản cho ảnh nhiễu đôi khi còn làm tệ hơn (khuếch đại nhiễu). Quan trọng hơn, để mô hình chịu được ảnh xấu, ta cần train nó trên ảnh xấu (Option B), chứ không phải train trên ảnh đã được làm đẹp (Option C) trừ khi ta cũng áp dụng bước làm đẹp đó cho production pipeline (điều này làm tăng độ trễ). Tại sao không chọn D (Resize/Crop): o Không liên quan: Resize và Crop chỉ giải quyết vấn đề về kích thước hoặc tỷ lệ khung hình (dimension/aspect ratio), hoàn toàn không giúp cải thiện khả năng nhận diện của mô hình đối với các vấn đề về chất lượng hình ảnh (nhiễu/mờ).

---

## Question 59

A company has an application that uses different APIs to generate embeddings for input text. The company needs to implement a solution to automatically rotate the API tokens every 3 months. Which solution will meet this requirement?

- **A.** Store the tokens in AWS Secrets Manager. Create an AWS Lambda function to perform the rotation.
- **B.** Store the tokens in AWS Systems Manager Parameter Store. Create an AWS Lambda function to perform the rotation.
- **C.** Store the tokens in AWS Key Management Service (AWS KMS). Use an AWS managed key to perform the rotation.
- **D.** Store the tokens in AWS Key Management Service (AWS KMS). Use an AWS owned key to perform the rotation.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Secrets Manager + Lambda): o Tính năng chuyên dụng: AWS Secrets Manager là dịch vụ được thiết kế đặc biệt để lưu trữ và quản lý vòng đời của các bí mật (secrets) như API tokens, database credentials. o Automatic Rotation: Nó có tính năng tích hợp sẵn để tự động xoay vòng bí mật theo lịch trình (ví dụ: mỗi 3 tháng). o Custom Rotation Logic: Vì đây là API token của dịch vụ bên ngoài (generic API), Secrets Manager không thể tự biết cách "đổi mật khẩu". Do đó, bạn cần viết một AWS Lambda function (chứa logic gọi API để xin token mới) và gắn nó vào Secrets Manager. Secrets Manager sẽ chịu trách nhiệm kích hoạt Lambda này đúng lịch để thực hiện xoay vòng. Tại sao không chọn B (Systems Manager Parameter Store): o Mặc dù Parameter Store (SecureString) có thể lưu trữ bí mật, nhưng nó không có tính năng tự động xoay vòng tích hợp sẵn (native rotation scheduler). o Để thực hiện xoay vòng với Parameter Store, bạn phải tự xây dựng hệ thống kích hoạt (ví dụ: dùng EventBridge để trigger Lambda thủ công). Điều này tốn công sức quản trị hơn so với giải pháp trọn gói của Secrets Manager. Tại sao không chọn C (AWS KMS - Managed key): o Sai đối tượng: AWS KMS quản lý khóa mã hóa (encryption keys) dùng để mã hóa dữ liệu, chứ không phải là nơi lưu trữ nội dung bí mật (secret value) như API Token để ứng dụng truy xuất. o Việc xoay vòng key trong KMS (Key Rotation) chỉ là thay đổi vật liệu khóa mã hóa bên dưới (backing key material), nó không hề thay đổi chuỗi ký tự API Token mà ứng dụng đang sử dụng. Tại sao không chọn D (AWS KMS - Owned key): o Tương tự như C, KMS xoay vòng khóa mã hóa, không xoay vòng giá trị của API Token. Ngoài ra, bạn không thể quản lý việc xoay vòng của AWS Owned Key (khóa do AWS sở hữu hoàn toàn).

---

## Question 60

An ML engineer receives datasets that contain missing values, duplicates, and extreme outliers. The ML engineer must consolidate these datasets into a single data frame and must prepare the data for ML. Which solution will meet these requirements?

- **A.** Use Amazon SageMaker Data Wrangler to import the datasets and to consolidate them into a single data frame. Use the cleansing and enrichment functionalities to prepare the data.
- **B.** Use Amazon SageMaker Ground Truth to import the datasets and to consolidate them into a single data frame. Use the human-in-the-loop capability to prepare the data.
- **C.** Manually import and merge the datasets. Consolidate the datasets into a single data frame. Use Amazon Q Developer to generate code snippets that will prepare the data.
- **D.** Manually import and merge the datasets. Consolidate the datasets into a single data frame. Use Amazon SageMaker data labeling to prepare the data.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (SageMaker Data Wrangler): o Consolidate Data: SageMaker Data Wrangler cho phép import dữ liệu từ nhiều nguồn khác nhau (S3, Athena, Redshift...) và hỗ trợ các thao tác Join hoặc Concatenate trực quan ngay trên giao diện để gộp nhiều dataset thành một data frame duy nhất. o Data Preparation: Đây là công cụ chuyên dụng cho việc làm sạch dữ liệu (Data Cleaning) mà không cần viết code. Nó có sẵn các built-in transforms để tự động xử lý các vấn đề đề bài nêu:  Missing values: Fill giá trị thiếu (Impute) hoặc drop dòng.  Duplicates: Drop các dòng trùng lặp.  Outliers: Phát hiện và xử lý các giá trị ngoại lai (Standard deviation, Quantile ranges...). Tại sao không chọn B (SageMaker Ground Truth): o Sai mục đích: Ground Truth là dịch vụ dùng để gán nhãn dữ liệu (Data Labeling) thủ công (ví dụ: vẽ khung bao quanh vật thể trong ảnh, phân loại văn bản) để tạo ra Ground Truth dataset. Nó không có chức năng làm sạch dữ liệu dạng bảng (tabular cleaning) như xử lý missing value hay outliers. Tại sao không chọn C (Manual + Amazon Q Developer): o Tốn công sức (High Effort): Việc import và merge thủ công đòi hỏi bạn phải viết code và xử lý môi trường. Dù Amazon Q có thể gợi ý code, nhưng so với giải pháp trọn gói (out-of-the-box) như Data Wrangler, cách này tốn nhiều thời gian và công sức quản trị hơn cho các tác vụ chuẩn hóa dữ liệu cơ bản. Tại sao không chọn D (SageMaker data labeling): o Tương tự như B, Data Labeling chỉ giải quyết vấn đề thiếu nhãn (target variable), không giải quyết vấn đề dữ liệu bẩn (dirty data) như duplicates hay outliers.

---

## Question 61

A company has historical data that shows whether customers needed long-term support from company staff. The company needs to develop an ML model to predict whether new customers will require long-term support. Which modeling approach should the company use to meet this requirement?

- **A.** Anomaly detection
- **B.** Linear regression
- **C.** Logistic regression
- **D.** Semantic segmentation

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Logistic regression): o Loại bài toán: Câu hỏi yêu cầu dự đoán "whether... will require" (Liệu khách hàng có cần hỗ trợ hay không). Đây là bài toán Phân loại nhị phân (Binary Classification) với đầu ra là 0 (Không) hoặc 1 (Có). o Cơ chế kỹ thuật: Logistic Regression là thuật toán cơ bản và hiệu quả nhất cho bài toán phân loại nhị phân. Nó sử dụng hàm Sigmoid để chuyển đổi đầu ra thành xác suất (từ 0 đến 1) cho việc ra quyết định Yes/No. Tại sao không chọn A (Anomaly detection): o Anomaly detection (Phát hiện bất thường) được dùng để tìm ra các điểm dữ liệu hiếm gặp hoặc khác biệt so với phần còn lại (ví dụ: phát hiện gian lận thẻ tín dụng). Nó không dùng để phân loại hai nhóm khách hàng có tính chất rõ ràng như nhau. Tại sao không chọn B (Linear regression): o Linear Regression (Hồi quy tuyến tính) dùng để dự đoán giá trị liên tục (Continuous values) như giá nhà, nhiệt độ, doanh thu. Đầu ra của nó là một con số vô hạn ($-\infty$ đến $+\infty$), không phù hợp để trả lời câu hỏi dạng Yes/No. Tại sao không chọn D (Semantic segmentation): o Semantic Segmentation là một kỹ thuật trong Computer Vision (Thị giác máy tính) dùng để phân loại từng pixel trong một bức ảnh (ví dụ: đâu là đường, đâu là xe). Nó hoàn toàn không liên quan đến dữ liệu dạng bảng (tabular data) về khách hàng.

---

## Question 62

An ML engineer has developed a binary classification model outside of Amazon SageMaker. The ML engineer needs to make the model accessible to a SageMaker Canvas user for additional tuning. The model artifacts are stored in an Amazon S3 bucket. The ML engineer and the Canvas user are part of the same SageMaker domain. Which combination of requirements must be met so that the ML engineer can share the model with the Canvas user? (Choose two.)

- **A.** The ML engineer and the Canvas user must be in separate SageMaker domains.
- **B.** The Canvas user must have permissions to access the S3 bucket where the model artifacts are stored.
- **C.** The model must be registered in the SageMaker Model Registry.
- **D.** The ML engineer must host the model on AWS Marketplace.
- **E.** The ML engineer must deploy the model to a SageMaker endpoint.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (S3 Permissions): o Quyền truy cập vật lý: Model artifacts (file model.tar.gz, weights, code) đang nằm trong Amazon S3. Để SageMaker Canvas (và người dùng Canvas) có thể load được model này lên để tiếp tục fine-tune, role IAM của người dùng Canvas bắt buộc phải có quyền s3:GetObject đối với bucket chứa artifacts. Nếu không có quyền này, quá trình import sẽ thất bại ngay lập tức do "Access Denied". Tại sao chọn C (SageMaker Model Registry): o Cơ chế tích hợp (The Bridge): SageMaker Canvas được thiết kế để tích hợp chặt chẽ với SageMaker Model Registry. Để mang một model được train bên ngoài (outside SageMaker) vào trong Canvas, quy trình chuẩn là bạn phải đóng gói và đăng ký model đó vào Model Registry (tạo Model Package Group). o Sau khi đăng ký, người dùng Canvas có thể dễ dàng nhìn thấy model trong giao diện Canvas và chọn "Import" để tinh chỉnh tiếp. Đây là cầu nối quản lý phiên bản và metadata cần thiết. Tại sao không chọn A (Separate SageMaker domains): o Đây không phải là yêu cầu kỹ thuật. Thực tế, việc hai người dùng nằm trong cùng một Domain (như đề bài đã nêu) càng thuận lợi cho việc chia sẻ tài nguyên và profile. Việc tách ra separate domains sẽ làm phức tạp hóa vấn đề permission (cross-account/cross-domain access) chứ không giúp ích gì cho việc share model. Tại sao không chọn D (AWS Marketplace): o AWS Marketplace dùng để bán hoặc chia sẻ model công khai cho cộng đồng/khách hàng bên ngoài. Việc chia sẻ nội bộ giữa Engineer và Canvas user trong cùng công ty không cần thông qua Marketplace. Tại sao không chọn E (Deploy to endpoint): o Sai mục đích: Endpoint dùng để phục vụ suy luận (Inference/Prediction). Người dùng Canvas cần thực hiện "additional tuning" (tức là huấn luyện lại/fine-tuning). Để tune model, Canvas cần truy cập vào model artifacts (file gốc) chứ không phải gọi API vào một endpoint đang chạy.

---

## Question 63

A company is building a deep learning model on Amazon SageMaker. The company uses a large amount of data as the training dataset. The company needs to optimize the model's hyperparameters to minimize the loss function on the validation dataset. Which hyperparameter tuning strategy will accomplish this goal with the LEAST computation time?

- **A.** Hyperband
- **B.** Grid search
- **C.** Bayesian optimization
- **D.** Random search

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Hyperband): o Cơ chế Early Stopping (Dừng sớm): Hyperband là một chiến lược tối ưu hóa siêu tham số (Hyperparameter Optimization - HPO) tiên tiến, được thiết kế đặc biệt để giảm thiểu thời gian tính toán. o Tư duy kỹ thuật: Thay vì chạy tất cả các thử nghiệm (training jobs) đến khi hoàn thành (full epochs) như các phương pháp truyền thống, Hyperband bắt đầu với nhiều tổ hợp tham số ngẫu nhiên nhưng chỉ train chúng trong một vài epoch ngắn (budget nhỏ). Sau đó, nó đánh giá hiệu năng, loại bỏ ngay lập tức một nửa số model kém hiệu quả (pruning) và chỉ cấp thêm tài nguyên (epochs) cho các model tốt nhất để chạy tiếp. o Kết quả: Nhờ việc không lãng phí tài nguyên tính toán vào các model "vô vọng", Hyperband có thể tìm ra model tối ưu nhanh hơn gấp nhiều lần (trên AWS SageMaker nhanh hơn tới 3 lần) so với Bayesian Optimization trên các tập dữ liệu lớn. Tại sao không chọn B (Grid search): o Duyệt toàn bộ (Exhaustive): Grid search thử nghiệm tất cả các tổ hợp có thể. Với Deep Learning, không gian tham số rất lớn, Grid Search sẽ gây ra bùng nổ tổ hợp (combinatorial explosion), dẫn đến thời gian tính toán cực kỳ lớn, không thể chấp nhận được. Tại sao không chọn C (Bayesian optimization): o Chạy tuần tự: Mặc dù Bayesian Optimization "thông minh" hơn Random Search vì nó học từ các kết quả trước đó để đoán tham số tiếp theo, nhưng theo mặc định, nó thường chạy các training job đến khi hoàn thành (to completion) để lấy kết quả chính xác. Điều này khiến nó chậm hơn Hyperband trong bối cảnh Deep Learning tốn kém, nơi việc phát hiện sớm và loại bỏ model xấu quan trọng hơn là train kỹ từng model. Tại sao không chọn D (Random search): o May rủi: Random search chọn ngẫu nhiên và cũng thường chạy hết thời gian training cho mỗi job. Nó không có cơ chế quản lý tài nguyên thông minh để dừng sớm các job kém như Hyperband.

---

## Question 64

A company is planning to use Amazon Redshift ML in its primary AWS account. The source data is in an Amazon S3 bucket in a secondary account. An ML engineer needs to set up an ML pipeline in the primary account to access the S3 bucket in the secondary account. The solution must not require public IPv4 addresses. Which solution will meet these requirements?

- **A.** Provision a Redshift cluster and Amazon SageMaker Studio in a VPC with no public access enabled in the primary account. Create a VPC peering connection between the accounts. Update the VPC route tables to remove the route to 0.0.0.0/0.
- **B.** Provision a Redshift cluster and Amazon SageMaker Studio in a VPC with no public access enabled in the primary account. Create an AWS Direct Connect connection and a transit gateway. Associate the VPCs from both accounts with the transit gateway. Update the VPC route tables to remove the route to 0.0.0.0/0.
- **C.** Provision a Redshift cluster and Amazon SageMaker Studio in a VPC in the primary account. Create an AWS Site-to-Site VPN connection with two encrypted IPsec tunnels between the accounts. Set up interface VPC endpoints for Amazon S3.
- **D.** Provision a Redshift cluster and Amazon SageMaker Studio in a VPC in the primary account. Create an S3 gateway endpoint. Update the S3 bucket policy to allow IAM principals from the primary account. Set up interface VPC endpoints for SageMaker and Amazon Redshift.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (S3 Gateway Endpoint + Cross-account Policy): o Kết nối riêng tư tới S3 (Private Connectivity): Để truy cập Amazon S3 từ một VPC mà không đi qua Internet công cộng (Public IPv4), giải pháp chuẩn là sử dụng VPC Gateway Endpoint cho S3. Gateway Endpoint sẽ thêm một route vào bảng định tuyến (Route Table) của VPC, hướng toàn bộ lưu lượng S3 đi qua mạng nội bộ của AWS. o Truy cập chéo tài khoản (Cross-account Access): Vì dữ liệu nằm ở tài khoản phụ (Secondary account), bạn cần cập nhật S3 Bucket Policy ở tài khoản phụ để cấp quyền (Allow) cho IAM Principal (Role mà Redshift/SageMaker sử dụng) ở tài khoản chính (Primary account). o Interface Endpoints: Cần thiết lập Interface VPC Endpoints cho SageMaker API và Redshift API để các dịch vụ này có thể giao tiếp với Control Plane của AWS một cách riêng tư mà không cần NAT Gateway hay Internet Gateway. Tại sao không chọn A (VPC Peering): o VPC Peering dùng để kết nối 2 VPC với nhau. Tuy nhiên, S3 là dịch vụ nằm ngoài VPC (Regional Service). Việc peering 2 VPC không giải quyết trực tiếp vấn đề truy cập S3 một cách hiệu quả. S3 Gateway Endpoint tại VPC nguồn là cách trực tiếp nhất. Ngoài ra, VPC Peering không thay thế được nhu cầu về S3 Bucket Policy để cấp quyền truy cập dữ liệu. Tại sao không chọn B (Direct Connect + Transit Gateway): o Overkill và sai mục đích: AWS Direct Connect dùng để kết nối trung tâm dữ liệu on-premise với AWS. Transit Gateway dùng để kết nối nhiều VPC. Cả hai đều là giải pháp hạ tầng mạng phức tạp và tốn kém, không cần thiết cho việc truy cập S3 (vốn chỉ cần Gateway Endpoint). Tại sao không chọn C (Site-to-Site VPN): o Site-to-Site VPN dùng để tạo kết nối bảo mật giữa mạng on-premise và AWS VPC qua internet. Nó không dùng để kết nối hai tài khoản AWS với nhau để truy cập S3. Việc định tuyến traffic S3 qua VPN tunnel là không khả thi và hiệu năng rất thấp so với Gateway Endpoint.

---

## Question 65

A company is using an AWS Lambda function to monitor the metrics from an ML model. An ML engineer needs to implement a solution to send an email message when the metrics breach a threshold. Which solution will meet this requirement?

- **A.** Log the metrics from the Lambda function to AWS CloudTrail. Configure a CloudTrail trail to send the email message.
- **B.** Log the metrics from the Lambda function to Amazon CloudFront. Configure an Amazon CloudWatch alarm to send the email message.
- **C.** Log the metrics from the Lambda function to Amazon CloudWatch. Configure a CloudWatch alarm to send the email message.
- **D.** Log the metrics from the Lambda function to Amazon CloudWatch. Configure an Amazon CloudFront rule to send the email message.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (CloudWatch + Alarm): o Kiến trúc tiêu chuẩn: Đây là mô hình giám sát và cảnh báo (Monitoring & Alerting) kinh điển trên AWS. o Quy trình: . Lambda function gửi metrics (ví dụ: model accuracy, latency) lên Amazon CloudWatch Metrics (thông qua API PutMetricData hoặc CloudWatch Logs). . CloudWatch Alarm sẽ liên tục theo dõi metric này. . Khi giá trị metric vượt quá ngưỡng (threshold), Alarm sẽ chuyển sang trạng thái "ALARM" và kích hoạt hành động gửi thông báo (thường là qua Amazon SNS topic, từ đó gửi email đến người dùng). Tại sao không chọn A (CloudTrail): o Sai chức năng: AWS CloudTrail được dùng để ghi lại lịch sử gọi API (Audit logs) nhằm mục đích bảo mật và tuân thủ (compliance). Nó không được thiết kế để lưu trữ và vẽ biểu đồ cho các chỉ số hiệu năng (performance metrics) dạng số học. Tại sao không chọn B (CloudFront): o Sai dịch vụ: Amazon CloudFront là dịch vụ CDN (Content Delivery Network) dùng để phân phối nội dung tĩnh/động tới người dùng cuối với độ trễ thấp. Nó hoàn toàn không có chức năng nhận log metrics từ Lambda hay gửi email cảnh báo. Tại sao không chọn D (CloudFront rule): o Tương tự B, CloudFront không liên quan đến quy trình monitoring backend.

---

