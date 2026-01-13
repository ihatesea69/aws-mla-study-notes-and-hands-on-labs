# Practice Exam 03

!!! info "Exam Details"
    - **Total Questions**: 65
    - **Estimated Time**: ~130 minutes
    - **Passing Score**: 72%

## Question 1

A company has used Amazon SageMaker to deploy a predictive ML model in production. The company is using SageMaker Model Monitor on the model. After a model update, an ML engineer notices data quality issues in the Model Monitor checks. What should the ML engineer do to mitigate the data quality issues that Model Monitor has identified?

- **A.** Adjust the model's parameters and hyperparameters.
- **B.** Initiate a manual Model Monitor job that uses the most recent production data.
- **C.** Create a new baseline from the latest dataset. Update Model Monitor to use the new baseline for evaluations.
- **D.** Include additional data in the existing training set for the model. Retrain and redeploy the model.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Create a new baseline): Trong Amazon SageMaker Model Monitor, chức năng Data Quality Monitor hoạt động bằng cách so sánh dữ liệu thực tế (live inference data) với một tập dữ liệu tham chiếu, được gọi là Baseline (thường được tạo ra từ tập dữ liệu huấn luyện - training dataset). Đề bài nêu rõ vấn đề xuất hiện "After a model update" (Sau khi cập nhật model). Khi một model mới được deploy, nó thường được huấn luyện trên dữ liệu mới hoặc có sự thay đổi về phân phối dữ liệu (data distribution). Nếu bạn không cập nhật Baseline, Model Monitor sẽ tiếp tục so sánh dữ liệu mới với Baseline cũ (của phiên bản model trước đó). Sự sai lệch này sẽ dẫn đến việc Model Monitor báo cáo sai các vấn đề về chất lượng dữ liệu (False Positives). Do đó, hành động chính xác là phải tạo một baseline mới từ tập dữ liệu mới nhất (được dùng để train model hiện tại) và cập nhật cấu hình Model Monitor để phản ánh đúng thực tế "bình thường mới". Tại sao không chọn A (Adjust parameters/hyperparameters): Việc điều chỉnh tham số (parameters) hoặc siêu tham số (hyperparameters) chỉ ảnh hưởng đến hiệu suất và hành vi dự đoán của model (model performance). Nó không thay đổi các quy tắc (rules) hoặc ngưỡng thống kê (statistics) mà Model Monitor sử dụng để xác định "chất lượng dữ liệu". Nếu Baseline không đổi, lỗi vẫn sẽ được báo cáo bất kể model hoạt động thế nào. Tại sao không chọn B (Initiate a manual job): Chạy lại job kiểm tra (Model Monitor job) một cách thủ công mà không thay đổi cấu hình cơ bản (Baseline) sẽ chỉ cho ra kết quả y hệt như cũ. Công cụ vẫn sẽ dùng bộ quy tắc cũ để so sánh với dữ liệu mới và lại tiếp tục báo lỗi. Đây là hành động lãng phí tài nguyên tính toán mà không giải quyết được nguyên nhân gốc rễ. Tại sao không chọn D (Include additional data ... Retrain): Đề bài cho biết model vừa mới được cập nhật ("After a model update"). Việc ngay lập tức thu thập thêm dữ liệu và retrain lại model là không cần thiết và đi ngược lại quy trình logic, trừ khi model đó thực sự bị l...

---

## Question 2

Topic #: 1 [All AWS Certified Machine Learning Engineer - Associate MLA-C01 Questions] A company has an ML model that generates text descriptions based on images that customers upload to the company's website. The images can be up to 50 MB in total size. An ML engineer decides to store the images in an Amazon S3 bucket. The ML engineer must implement a processing solution that can scale to accommodate changes in demand. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Create an Amazon SageMaker batch transform job to process all the images in the S3 bucket.
- **B.** Create an Amazon SageMaker Asynchronous Inference endpoint and a scaling policy. Run a script to make an inference request for each image.
- **C.** Create an Amazon Elastic Kubernetes Service (Amazon EKS) cluster that uses Karpenter for auto scaling. Host the model on the EKS cluster. Run a script to make an inference request for each image.
- **D.** Create an AWS Batch job that uses an Amazon Elastic Container Service (Amazon ECS) cluster. Specify a list of images to process for each AWS Batch job.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (SageMaker Asynchronous Inference): Đề bài đặt ra hai thách thức chính: kích thước payload lớn (ảnh lên đến 50 MB) và yêu cầu giảm thiểu gánh nặng vận hành (Least operational overhead) cho một giải pháp có khả năng mở rộng (scale). SageMaker Asynchronous Inference là dịch vụ hoàn hảo cho trường hợp này vì: . Hỗ trợ Large Payload: Không giống như Real-time Inference (giới hạn payload nhỏ, thường < 6MB), Asynchronous Inference cho phép xử lý payload lên tới 1 GB bằng cách lưu trữ input/output trên Amazon S3, giải quyết trực tiếp vấn đề ảnh 50 MB. . Managed Auto-scaling (Scale to Zero): Dịch vụ này có hàng đợi (queue) tích hợp sẵn và khả năng tự động scale số lượng instance dựa trên lượng request trong hàng đợi, thậm chí scale xuống 0 khi không có request để tiết kiệm chi phí. Điều này giúp loại bỏ gánh nặng quản lý hạ tầng thủ công. Tại sao không chọn A (SageMaker Batch Transform): Batch Transform phù hợp cho việc xử lý offline hàng loạt dữ liệu lớn đã có sẵn (ví dụ: chạy job mỗi đêm), không phù hợp cho mô hình tương tác trên website nơi khách hàng upload và cần kết quả trong thời gian hợp lý (near real-time). Batch Transform không phải là một endpoint luôn sẵn sàng phục vụ request đơn lẻ ngay lập tức. Tại sao không chọn C (Amazon EKS + Karpenter): Phương án này vi phạm nghiêm trọng tiêu chí "Least operational overhead". Việc dựng và quản lý một cụm Kubernetes (EKS), cài đặt và cấu hình Karpenter để autoscaling, cũng như quản lý container pods đòi hỏi nỗ lực kỹ thuật và bảo trì cực lớn so với việc sử dụng dịch vụ managed có sẵn như SageMaker. Tại sao không chọn D (AWS Batch on ECS): Tương tự như phương án A, AWS Batch được thiết kế cho các tác vụ tính toán hàng loạt (batch computing) thay vì phục vụ suy luận mô hình theo hướng sự kiện (event-driven inference). Việc cấu hình Job Queues, Compute Environments và Job Definitions trên ECS phức tạp hơn nhiều so với việc chỉ cần deploy một endpoint Asynchronous trên SageMaker.

---

## Question 3

An ML engineer needs to use AWS services to identify and extract meaningful unique keywords from documents. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use the Natural Language Toolkit (NLTK) library on Amazon EC2 instances for text pre-processing. Use the Latent Dirichlet Allocation (LDA) algorithm to identify and extract relevant keywords.
- **B.** Use Amazon SageMaker and the BlazingText algorithm. Apply custom pre- processing steps for stemming and removal of stop words. Calculate term frequency-inverse document frequency (TF-IDF) scores to identify and extract relevant keywords.
- **C.** Store the documents in an Amazon S3 bucket. Create AWS Lambda functions to process the documents and to run Python scripts for stemming and removal of stop words. Use bigram and trigram techniques to identify and extract relevant keywords.
- **D.** Use Amazon Comprehend custom entity recognition and key phrase extraction to identify and extract relevant keywords.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Amazon Comprehend): Câu hỏi yêu cầu giải pháp có "chi phí vận hành thấp nhất" (LEAST operational overhead) để trích xuất từ khóa (keywords). Amazon Comprehend là một dịch vụ AI cao cấp (AI Service) về Xử lý Ngôn ngữ Tự nhiên (NLP) được quản lý hoàn toàn (Serverless/Fully Managed). Nó cung cấp sẵn các API (Pre-trained models) cho tính năng Key Phrase Extraction (Trích xuất cụm từ khóa) và Entity Recognition (Nhận diện thực thể) ngay lập tức mà không cần người dùng phải quản lý hạ tầng, viết code xử lý dữ liệu phức tạp hay huấn luyện mô hình. Đây là lựa chọn "mì ăn liền" tối ưu nhất. Tại sao không chọn A (EC2 + NLTK + LDA): Đây là phương án tự quản lý (Self- managed). Bạn phải chịu trách nhiệm hoàn toàn về việc quản lý máy chủ (EC2), cài đặt môi trường, thư viện (NLTK) và tự viết thuật toán (LDA). Điều này vi phạm tiêu chí "Least operational overhead". Tại sao không chọn B (SageMaker + BlazingText): Mặc dù SageMaker giúp quản lý việc huấn luyện, nhưng bạn vẫn phải thực hiện các bước: Tiền xử lý dữ liệu (Pre- processing), Huấn luyện (Training), và Triển khai (Deploying). Quy trình này tốn nhiều công sức và thời gian hơn rất nhiều so với việc gọi API của Comprehend. Tại sao không chọn C (Lambda + Custom Scripts): Tương tự như phương án A, bạn phải tự viết code thủ công (hard-code) các kỹ thuật xử lý ngôn ngữ (stemming, bigram/trigram) bên trong Lambda. Bạn không tận dụng được các mô hình Deep Learning mạnh mẽ đã được AWS tối ưu sẵn.

---

## Question 4

A company needs to give its ML engineers appropriate access to training data. The ML engineers must access training data from only their own business group. The ML engineers must not be allowed to access training data from other business groups. The company uses a single AWS account and stores all the training data in Amazon S3 buckets. All ML model training occurs in Amazon SageMaker. Which solution will provide the ML engineers with the appropriate access?

- **A.** Enable S3 bucket versioning.
- **B.** Configure S3 Object Lock settings for each user.
- **C.** Add cross-origin resource sharing (CORS) policies to the S3 buckets.
- **D.** Create IAM policies. Attach the policies to IAM users or IAM roles.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (IAM policies): Bài toán yêu cầu kiểm soát quyền truy cập (Access Control) một cách chi tiết: Kỹ sư của nhóm nào chỉ được truy cập dữ liệu (S3) của nhóm đó. Trong AWS, IAM Policies (Chính sách quản lý truy cập) là cơ chế cốt lõi để định nghĩa ai (Principal) được làm gì (Action) trên tài nguyên nào (Resource). Bạn có thể tạo các chính sách riêng biệt (ví dụ: Policy_GroupA chỉ cho phép s3:GetObject trên bucket/group-a/) và gắn chúng vào các IAM Users hoặc Roles tương ứng của từng nhóm kỹ sư. Đây là giải pháp tiêu chuẩn và chính xác nhất để phân quyền. Tại sao không chọn A (S3 bucket versioning): Versioning (Đánh phiên bản) là tính năng giúp lưu giữ nhiều phiên bản của một object, mục đích chính là để phục hồi dữ liệu khi bị xóa nhầm hoặc ghi đè (Data Protection/Recovery). Nó không có chức năng ngăn chặn người dùng truy cập vào dữ liệu. Tại sao không chọn B (S3 Object Lock): Object Lock được sử dụng cho mô hình WORM (Write Once, Read Many), ngăn chặn việc xóa hoặc sửa đổi object trong một khoảng thời gian nhất định (thường dùng cho tuân thủ pháp lý - Compliance). Nó không dùng để phân chia quyền xem dữ liệu giữa các nhóm. Tại sao không chọn C (CORS policies): Cross-Origin Resource Sharing (CORS) là cơ chế bảo mật cho trình duyệt web, cho phép một ứng dụng web ở domain này truy cập tài nguyên ở domain khác. Nó không liên quan đến việc cấp quyền cho backend service (SageMaker) hay người dùng (ML Engineers) truy cập vào dữ liệu trong S3.

---

## Question 5

A company needs to host a custom ML model to perform forecast analysis. The forecast analysis will occur with predictable and sustained load during the same 2-hour period every day. Multiple invocations during the analysis period will require quick responses. The company needs AWS to manage the underlying infrastructure and any auto scaling activities. Which solution will meet these requirements?

- **A.** Schedule an Amazon SageMaker batch transform job by using AWS Lambda.
- **B.** Configure an Auto Scaling group of Amazon EC2 instances to use scheduled scaling.
- **C.** Use Amazon SageMaker Serverless Inference with provisioned concurrency.
- **D.** Run the model on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster on Amazon EC2 with pod auto scaling.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Serverless Inference): Bài toán đặt ra một mô hình tải (traffic pattern) rất đặc thù: chỉ hoạt động trong 2 giờ mỗi ngày và không hoạt động trong 22 giờ còn lại. . Cost & Ops Efficiency: Nếu sử dụng Real-time Endpoint thông thường, bạn sẽ phải trả tiền cho 24/24 giờ (hoặc phải viết script phức tạp để tạo/xóa endpoint mỗi ngày). SageMaker Serverless Inference là giải pháp tối ưu nhất vì nó có khả năng Scale to Zero (tự động tắt hoàn toàn khi không có request), giúp tiết kiệm chi phí tuyệt đối trong thời gian nhàn rỗi mà không cần quản lý hạ tầng thủ công. . Handling Load: Với yêu cầu "quick responses" (phản hồi nhanh) cho "multiple invocations" (nhiều lượt gọi), đây là đặc điểm của mô hình API Endpoint chứ không phải xử lý Batch. Mặc dù thuật ngữ "Provisioned Concurrency" thường gắn liền với Lambda hoặc SageMaker Real-time, trong ngữ cảnh câu hỏi này, nó ám chỉ việc cấu hình khả năng xử lý đồng thời (concurrency) để đảm bảo endpoint chịu được tải "sustained" (liên tục) trong 2 giờ cao điểm mà không bị nghẽn. Tại sao không chọn A (SageMaker batch transform): Batch Transform được thiết kế để xử lý offline các tập dữ liệu lớn (bulk processing). Người dùng upload file dữ liệu lên S3, chờ xử lý xong và nhận kết quả trả về S3. Nó hoạt động theo cơ chế bất đồng bộ (asynchronous) và không cung cấp "quick responses" (phản hồi tức thì) cho từng invocation riêng lẻ theo thời gian thực như yêu cầu đề bài. Tại sao không chọn B (EC2 Auto Scaling): Sử dụng EC2 yêu cầu bạn phải tự quản lý hệ điều hành (OS), cài đặt môi trường (Docker/Python), cấu hình Load Balancer và Auto Scaling Group. Điều này vi phạm yêu cầu quan trọng của đề bài là "AWS to manage the underlying infrastructure" (AWS quản lý hạ tầng cơ sở). Đây là giải pháp có chi phí vận hành (Operational Overhead) cao nhất. Tại sao không chọn D (EKS Cluster): Tương tự như EC2, việc vận hành một cụm Kubernetes (EKS) đòi hỏi kiến thức chuyên sâu về container orchestration và nỗ lực quản trị rất lớn (quản...

---

## Question 6

A company's ML engineer has deployed an ML model for sentiment analysis to an Amazon SageMaker endpoint. The ML engineer needs to explain to company stakeholders how the model makes predictions. Which solution will provide an explanation for the model's predictions?

- **A.** Use SageMaker Model Monitor on the deployed model.
- **B.** Use SageMaker Clarify on the deployed model.
- **C.** Show the distribution of inferences from A/В testing in Amazon CloudWatch.
- **D.** Add a shadow endpoint. Analyze prediction differences on samples.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (SageMaker Clarify): Amazon SageMaker Clarify là dịch vụ chuyên biệt được thiết kế để cung cấp khả năng giải thích mô hình (Model Explainability) và phát hiện thiên kiến (Bias Detection). Nó sử dụng phương pháp SHAP (SHapley Additive exPlanations) để phân tích và định lượng mức độ đóng góp của từng đặc trưng (feature) vào kết quả dự đoán cuối cùng. Đối với bài toán phân tích cảm xúc (Sentiment Analysis), Clarify sẽ chỉ ra những từ ngữ hoặc cụm từ nào (feature importance) đã khiến model đưa ra kết quả là "Tích cực" hay "Tiêu cực", giúp các bên liên quan (stakeholders) hiểu rõ cơ chế ra quyết định của model. Tại sao không chọn A (SageMaker Model Monitor): SageMaker Model Monitor có nhiệm vụ chính là giám sát liên tục chất lượng của model và dữ liệu theo thời gian thực (ví dụ: phát hiện Data Drift, Model Quality Drift). Mặc dù nó có thể theo dõi sự thay đổi về Feature Attribution (sử dụng công nghệ của Clarify bên dưới), nhưng khi nhắc đến nhu cầu cốt lõi là "giải thích model hoạt động thế nào" cho con người hiểu, SageMaker Clarify là công cụ trực tiếp và chính xác nhất. Tại sao không chọn C (A/B testing in CloudWatch): A/B Testing được sử dụng để so sánh hiệu năng (performance) giữa hai phiên bản model khác nhau (ví dụ: Model A chính xác hơn Model B bao nhiêu %). Nó chỉ cho biết model nào tốt hơn, chứ không giải thích được tại sao model lại đưa ra một dự đoán cụ thể. Tại sao không chọn D (Shadow endpoint): Shadow testing (thử nghiệm bóng) là kỹ thuật triển khai model mới để nhận traffic thực tế nhưng không trả kết quả cho người dùng (chỉ để log lại và so sánh). Mục đích của nó là kiểm tra độ ổn định và lỗi của model mới trước khi promote lên production, không liên quan đến việc giải thích logic bên trong model.

---

## Question 7

An ML engineer is using Amazon SageMaker to train a deep learning model that requires distributed training. After some training attempts, the ML engineer observes that the instances are not performing as expected. The ML engineer identifies communication overhead between the training instances. What should the ML engineer do to MINIMIZE the communication overhead between the instances?

- **A.** Place the instances in the same VPC subnet. Store the data in a different AWS Region from where the instances are deployed.
- **B.** Place the instances in the same VPC subnet but in different Availability Zones. Store the data in a different AWS Region from where the instances are deployed.
- **C.** Place the instances in the same VPC subnet. Store the data in the same AWS Region and Availability Zone where the instances are deployed.
- **D.** Place the instances in the same VPC subnet. Store the data in the same AWS Region but in a different Availability Zone from where the instances are deployed.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Same Region & Availability Zone): Trong huấn luyện phân tán (Distributed Training), các instance (nút tính toán) phải thường xuyên trao đổi thông tin (như gradients trong Data Parallelism) với nhau. "Communication overhead" (độ trễ mạng) là kẻ thù lớn nhất làm chậm quá trình này. Để giảm thiểu độ trễ xuống mức thấp nhất, giải pháp tối ưu là đặt tất cả tài nguyên (Compute Instances và Data Storage) gần nhau nhất có thể về mặt vật lý. . Network Latency: Một Subnet trong AWS luôn nằm trọn trong một Availability Zone (AZ). Việc đặt các instance trong cùng một subnet đảm bảo chúng nằm trong cùng một AZ (thậm chí cùng data center), giúp lưu lượng mạng đi qua đường truyền tốc độ cao nội bộ (intra-AZ), thay vì phải đi vòng qua các đường truyền liên kết giữa các AZ (inter-AZ) hoặc giữa các Region. . Data Proximity: Đặt dữ liệu (S3/EFS/FSx) cùng Region và AZ với instance giúp giảm thời gian tải dữ liệu (I/O latency), tránh nghẽn cổ chai khi model đọc dữ liệu huấn luyện. Tại sao không chọn A (Data in different AWS Region): Việc lưu trữ dữ liệu ở một Region khác với nơi đặt instance sẽ tạo ra độ trễ mạng cực lớn (hàng chục đến hàng trăm ms) khi tải dữ liệu. Điều này sẽ khiến GPU/CPU phải chờ đợi (idle) trong khi dữ liệu được truyền qua internet, làm giảm hiệu suất nghiêm trọng. Tại sao không chọn B (Different Availability Zones): Về mặt kỹ thuật AWS, một Subnet không thể kéo dài qua nhiều AZ (1 Subnet = 1 AZ). Do đó, mệnh đề "same VPC subnet but in different Availability Zones" là không khả thi. Hơn nữa, giao tiếp giữa các AZ (Cross-AZ traffic) luôn có độ trễ cao hơn so với giao tiếp trong cùng một AZ. Tại sao không chọn D (Data in different Availability Zone): Mặc dù tốt hơn việc khác Region, nhưng việc truy cập dữ liệu từ một AZ khác vẫn phải chịu phí truyền tải dữ liệu (Cross-AZ data transfer cost) và độ trễ cao hơn so với việc dữ liệu nằm ngay tại local AZ.

---

## Question 8

A company is running ML models on premises by using custom Python scripts and proprietary datasets. The company is using PyTorch. The model building requires unique domain knowledge. The company needs to move the models to AWS. Which solution will meet these requirements with the LEAST effort?

- **A.** Use SageMaker built-in algorithms to train the proprietary datasets.
- **B.** Use SageMaker script mode and premade images for ML frameworks.
- **C.** Build a container on AWS that includes custom packages and a choice of ML frameworks.
- **D.** Purchase similar production models through AWS Marketplace.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (SageMaker Script Mode): Đây là giải pháp tốn ít công sức nhất (LEAST effort) để di chuyển các đoạn mã (code) huấn luyện mô hình từ on- premises lên AWS mà vẫn giữ nguyên được logic tùy chỉnh. SageMaker Script Mode cho phép bạn tái sử dụng trực tiếp các file train.py (custom Python scripts) hiện có. Bạn không cần phải đóng gói Docker container từ đầu. Thay vào đó, bạn chỉ cần chỉ định framework (ở đây là PyTorch) và AWS sẽ tự động cung cấp một Premade Image (Container đã cài sẵn PyTorch và các thư viện cần thiết). Bạn chỉ việc "mang code đến" và chạy, giúp giảm thiểu tối đa việc thay đổi mã nguồn hay cấu hình hạ tầng. Tại sao không chọn A (SageMaker built-in algorithms): Các thuật toán tích hợp sẵn (Built-in algorithms) của SageMaker (như XGBoost, Image Classification...) là các hộp đen (black-box) được tối ưu hóa cho các tác vụ cụ thể. Vì đề bài nói mô hình yêu cầu "unique domain knowledge" và được viết bằng custom scripts, việc ép logic phức tạp này vào các thuật toán có sẵn thường không khả thi hoặc đòi hỏi phải viết lại toàn bộ logic xử lý dữ liệu và huấn luyện, tốn rất nhiều công sức. Tại sao không chọn C (Build a container - BYOC): Phương pháp "Bring Your Own Container" (BYOC) yêu cầu bạn phải tự viết Dockerfile, cài đặt môi trường, tuân thủ cấu trúc thư mục của SageMaker (/opt/ml/...), build image và push lên Amazon ECR. Đây là quy trình phức tạp và tốn công sức vận hành hơn rất nhiều so với việc sử dụng Script Mode (nơi AWS đã lo phần Container cho bạn). Tại sao không chọn D (AWS Marketplace): Mô hình của công ty chứa "unique domain knowledge" (kiến thức nghiệp vụ độc quyền/đặc thù). Các mô hình bán sẵn trên Marketplace là các giải pháp tổng quát, không thể chứa tri thức riêng biệt của công ty bạn được. Do đó, phương án này không đáp ứng được yêu cầu nghiệp vụ.

---

## Question 9

A company is using Amazon SageMaker and millions of files to train an ML model. Each file is several megabytes in size. The files are stored in an Amazon S3 bucket. The company needs to improve training performance. Which solution will meet these requirements in the LEAST amount of time?

- **A.** Transfer the data to a new S3 bucket that provides S3 Express One Zone storage. Adjust the training job to use the new S3 bucket.
- **B.** Create an Amazon FSx for Lustre file system. Link the file system to the existing S3 bucket. Adjust the training job to read from the file system.
- **C.** Create an Amazon Elastic File System (Amazon EFS) file system. Transfer the existing data to the file system. Adjust the training job to read from the file system.
- **D.** Create an Amazon ElastiCache (Redis OSS) cluster. Link the Redis OSS cluster to the existing S3 bucket. Stream the data from the Redis OSS cluster directly to the

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (FSx for Lustre): Bài toán yêu cầu cải thiện hiệu suất huấn luyện (improve training performance) cho hàng triệu file có kích thước vài MB (đây là workload yêu cầu thông lượng/throughput cực cao và độ trễ/latency thấp để nạp dữ liệu vào GPU/CPU). Amazon FSx for Lustre là hệ thống file hiệu năng cao được thiết kế đặc biệt cho các ứng dụng tính toán chuyên sâu (HPC) và Machine Learning. Tính năng "Data Repository Association" cho phép FSx for Lustre liên kết trực tiếp với S3 bucket hiện có. Khi training job chạy, dữ liệu sẽ được "lazy load" (tải khi cần) hoặc "preload" (tải trước) vào hệ thống file tốc độ cao này, giúp tăng tốc độ đọc dữ liệu lên gấp nhiều lần so với đọc trực tiếp từ S3 (đặc biệt là với File Mode). Đây là giải pháp chuẩn công nghiệp để tăng tốc training. Tại sao không chọn A (S3 Express One Zone): Mặc dù S3 Express One Zone có độ trễ thấp hơn S3 Standard, nhưng đối với các tác vụ ML training quy mô lớn cần throughput cực đại, FSx for Lustre vẫn vượt trội hơn nhờ khả năng caching và kiến trúc file system song song (parallel file system). Hơn nữa, việc copy toàn bộ dữ liệu sang bucket mới (vùng One Zone) sẽ tốn thời gian và công sức quản lý hơn so với việc chỉ cần "link" FSx vào bucket hiện tại. Tại sao không chọn C (Amazon EFS): Amazon EFS là hệ thống file dùng chung (General Purpose) cho Linux, phù hợp với các ứng dụng web hoặc chia sẻ dữ liệu thông thường. Mặc dù EFS có thể dùng cho SageMaker, nhưng throughput và IOPS của nó thấp hơn đáng kể so với FSx for Lustre trong các tác vụ huấn luyện Deep Learning yêu cầu băng thông dữ liệu lớn. Tại sao không chọn D (ElastiCache Redis): Redis là in-memory key-value store, không phải là File System. SageMaker Training Job thường mong đợi dữ liệu đầu vào dưới dạng File System (Local, EFS, FSx) hoặc S3 Object, chứ không hỗ trợ đọc trực tiếp stream dữ liệu từ Redis một cách tự nhiên (native integration) cho việc huấn luyện quy mô lớn. Việc thiết lập cơ chế này sẽ cực kỳ phức tạp (cần custom data load...

---

## Question 10

A company wants to develop an ML model by using tabular data from its customers. The data contains meaningful ordered features with sensitive information that should not be discarded. An ML engineer must ensure that the sensitive data is masked before another team starts to build the model. Which solution will meet these requirements?

- **A.** Use Amazon Made to categorize the sensitive data.
- **B.** Prepare the data by using AWS Glue DataBrew.
- **C.** Run an AWS Batch job to change the sensitive data to random values.
- **D.** Run an Amazon EMR job to change the sensitive data to random values.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (AWS Glue DataBrew): Bài toán yêu cầu chuẩn bị dữ liệu dạng bảng (tabular data), cụ thể là làm sạch (masking) thông tin nhạy cảm trước khi đưa cho đội ngũ khác huấn luyện model. AWS Glue DataBrew là công cụ chuẩn bị dữ liệu trực quan (visual data preparation tool) không cần viết code (no-code). Nó cung cấp sẵn các tính năng chuyển đổi (transformations) chuyên biệt để xử lý thông tin cá nhân (PII), bao gồm các kỹ thuật như Masking (che dấu), Hashing (băm), hoặc Shuffling (tráo đổi). Điều này giúp bảo vệ dữ liệu nhạy cảm nhưng vẫn giữ lại cấu trúc hoặc định dạng cần thiết cho việc huấn luyện Machine Learning, đáp ứng chính xác yêu cầu đề bài. Tại sao không chọn A (Amazon Macie): Amazon Macie là dịch vụ bảo mật dùng để khám phá (discover) và phân loại (classify) dữ liệu nhạy cảm trong S3. Macie chỉ báo cáo cho bạn biết "Dữ liệu nhạy cảm nằm ở đâu", chứ không có chức năng thực hiện hành động biến đổi (transform) hoặc che giấu dữ liệu đó để tạo ra tập dữ liệu mới sạch hơn. Tại sao không chọn C (AWS Batch): Việc sử dụng AWS Batch yêu cầu bạn phải tự viết code (Python/Shell) để xử lý dữ liệu. Hơn nữa, phương án đề xuất thay thế dữ liệu nhạy cảm bằng "random values" (giá trị ngẫu nhiên) là một kỹ thuật tồi trong ML vì nó phá vỡ mối tương quan và tính quy luật ("meaningful ordered features") của dữ liệu, khiến model không thể học được gì từ các đặc trưng đó (noise). Tại sao không chọn D (Amazon EMR): Tương tự như AWS Batch, EMR đòi hỏi chi phí vận hành cao (quản lý cluster) và kỹ năng viết code Spark/Hadoop. Việc thay thế bằng giá trị ngẫu nhiên cũng mắc phải lỗi logic tương tự như phương án C, làm giảm giá trị sử dụng của dữ liệu đối với model.

---

## Question 11

An ML engineer needs to deploy ML models to get inferences from large datasets in an asynchronous manner. The ML engineer also needs to implement scheduled monitoring of the data quality of the models. The ML engineer must receive alerts when changes in data quality occur. Which solution will meet these requirements?

- **A.** Deploy the models by using scheduled AWS Glue jobs. Use Amazon CloudWatch alarms to monitor the data quality and to send alerts.
- **B.** Deploy the models by using scheduled AWS Batch jobs. Use AWS CloudTrail to monitor the data quality and to send alerts.
- **C.** Deploy the models by using Amazon Elastic Container Service (Amazon ECS) on AWS Fargate. Use Amazon EventBridge to monitor the data quality and to send alerts.
- **D.** Deploy the models by using Amazon SageMaker batch transform. Use SageMaker Model Monitor to monitor the data quality and to send alerts.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (SageMaker Batch Transform + Model Monitor): Câu hỏi có hai yêu cầu chính: xử lý suy luận (inference) cho tập dữ liệu lớn theo phương thức bất đồng bộ (asynchronous) và giám sát chất lượng dữ liệu. . Asynchronous Inference: SageMaker Batch Transform là tính năng chuyên dụng để xử lý suy luận offline cho hàng loạt dữ liệu lớn (Bulk data) được lưu trữ trên S3. Nó hoạt động bất đồng bộ, tự động quản lý tài nguyên tính toán và tắt đi khi hoàn thành, rất phù hợp cho "large datasets". . Data Quality Monitoring: SageMaker Model Monitor là dịch vụ chuẩn để phát hiện các vấn đề về chất lượng dữ liệu (Data Quality Drift) so với Baseline. Model Monitor hỗ trợ giám sát các Batch Transform jobs bằng cách phân tích dữ liệu đầu vào/đầu ra được lưu trên S3 theo lịch trình định kỳ và tự động đẩy các metrics vi phạm (violations) lên CloudWatch để gửi cảnh báo. Tại sao không chọn A (AWS Glue + CloudWatch): Mặc dù AWS Glue có thể chạy code Python để thực hiện suy luận, nhưng nó là công cụ ETL (Trích xuất, Chuyển đổi, Tải), không được tối ưu hóa cho quản lý vòng đời ML (MLOps). Quan trọng hơn, CloudWatch là nơi nhận metrics chứ không phải công cụ phân tích dữ liệu để phát hiện lỗi chất lượng (như distribution drift). Bạn sẽ phải tự viết code phức tạp để tính toán thống kê dữ liệu. Tại sao không chọn B (AWS Batch + CloudTrail): Đây là sai lầm nghiêm trọng về kiến thức dịch vụ. AWS CloudTrail là dịch vụ để ghi lại lịch sử gọi API (Audit logs - Ai làm gì, lúc nào) nhằm mục đích bảo mật và tuân thủ. Nó hoàn toàn không có khả năng đọc nội dung dữ liệu (payload) để phân tích chất lượng hay độ chính xác của model. Tại sao không chọn C (ECS + EventBridge): Amazon EventBridge là một Serverless Event Bus dùng để định tuyến sự kiện giữa các ứng dụng. Nó không có khả năng phân tích dữ liệu thống kê (statistical analysis) để biết dữ liệu có tốt hay xấu. Việc dùng ECS đòi hỏi bạn phải tự xây dựng toàn bộ hệ thống giám sát dữ liệu từ con số 0 (Self-managed), tốn kém thời gian hơn nhiều ...

---

## Question 12

Topic #: 1 [All AWS Certified Machine Learning Engineer - Associate MLA-C01 Questions] An ML engineer normalized training data by using min-max normalization in AWS Glue DataBrew. The ML engineer must normalize the production inference data in the same way as the training data before passing the production inference data to the model for predictions. Which solution will meet this requirement?

- **A.** Apply statistics from a well-known dataset to normalize the production samples.
- **B.** Keep the min-max normalization statistics from the training set. Use these values to normalize the production samples.
- **C.** Calculate a new set of min-max normalization statistics from a batch of production samples. Use these values to normalize all the production samples.
- **D.** Calculate a new set of min-max normalization statistics from each production sample. Use these values to normalize all the production samples.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Keep training statistics): Đây là nguyên tắc bất di bất dịch trong Machine Learning: Dữ liệu Inference phải được xử lý giống hệt dữ liệu Training. Khi huấn luyện model, trọng số (weights) được điều chỉnh dựa trên phân phối và thang đo (scale) cụ thể của dữ liệu training (ví dụ: giá trị Min là 0, Max là 100). Khi đưa model ra thực tế (Inference), bạn phải áp dụng lại chính xác các tham số thống kê (Min, Max, Mean, Variance) đã tính được từ tập Training lên dữ liệu mới. Nếu bạn tính toán lại Min/Max dựa trên dữ liệu mới, bạn sẽ làm thay đổi thang đo, dẫn đến hiện tượng Training-Serving Skew (Lệch pha giữa huấn luyện và phục vụ), khiến model đưa ra dự đoán sai lệch hoàn toàn. Tại sao không chọn A (Well-known dataset): Thống kê từ một tập dữ liệu công khai (well-known dataset) không liên quan gì đến dữ liệu riêng của công ty bạn. Áp dụng thống kê ngoại lai này sẽ làm sai lệch bản chất của dữ liệu đầu vào. Tại sao không chọn C (New stats from batch): Nếu mỗi batch inference lại có một bộ Min/Max riêng, thì cùng một giá trị input (ví dụ: x = 50) sẽ bị biến đổi thành các giá trị khác nhau tùy thuộc vào việc nó nằm trong batch nào. Điều này làm mất tính nhất quán (inconsistency) và khiến model không thể dự đoán chính xác. Tại sao không chọn D (New stats from sample): Tính toán Min/Max trên một mẫu đơn lẻ (single sample) là vô nghĩa. Ví dụ: nếu mẫu chỉ có giá trị là 10, thì Min=10, Max=10. Khi áp dụng công thức (x - Min) / (Max - Min), bạn sẽ gặp lỗi chia cho 0 hoặc biến mọi giá trị thành 0. Nó triệt tiêu hoàn toàn thông tin của dữ liệu.

---

## Question 13

A company is planning to use Amazon SageMaker to make classification ratings that are based on images. The company has 6 ТВ of training data that is stored on an Amazon FSx for NetApp ONTAP system virtual machine (SVM). The SVM is in the same VPC as SageMaker. An ML engineer must make the training data accessible for ML models that are in the SageMaker environment. Which solution will meet these requirements?

- **A.** Mount the FSx for ONTAP file system as a volume to the SageMaker Instance.
- **B.** Create an Amazon S3 bucket. Use Mountpoint for Amazon S3 to link the S3 bucket to the FSx for ONTAP file system.
- **C.** Create a catalog connection from SageMaker Data Wrangler to the FSx for ONTAP file system.
- **D.** Create a direct connection from SageMaker Data Wrangler to the FSx for ONTAP file system.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Mount FSx volume): Đây là giải pháp trực tiếp và hiệu quả nhất. Amazon FSx for NetApp ONTAP hỗ trợ giao thức NFS (Network File System). Các instance của Amazon SageMaker (về cơ bản là máy chủ Linux) có khả năng mount các volume NFS một cách tự nhiên. Vì cả hai dịch vụ đều nằm trong cùng một VPC, bạn có thể cấu hình SageMaker Training Job để mount volume FSx này trực tiếp vào môi trường huấn luyện. Điều này cho phép code huấn luyện truy cập 6 TB dữ liệu như thể chúng là các file cục bộ (local path) mà không cần phải di chuyển hay copy dữ liệu đi đâu cả, đảm bảo hiệu suất cao và độ trễ thấp. Tại sao không chọn B (Mountpoint for Amazon S3): Mountpoint for Amazon S3 là công cụ để mount S3 Bucket thành file system cục bộ, chứ không phải dùng để link S3 vào FSx. Hơn nữa, dữ liệu đã nằm sẵn trên FSx, việc đưa S3 vào giữa là dư thừa và làm phức tạp hóa kiến trúc không cần thiết. Tại sao không chọn C và D (SageMaker Data Wrangler): SageMaker Data Wrangler là công cụ low-code dùng để chuẩn bị, làm sạch và feature engineering dữ liệu (thường là dạng bảng/tabular hoặc time-series). Nó không phải là cơ chế để "mount" một hệ thống file 6 TB chứa ảnh (image data) cho một Training Job. Việc import 6 TB ảnh vào Data Wrangler để xử lý sẽ cực kỳ chậm chạp và không đúng mục đích sử dụng (purpose-built) của công cụ này so với việc mount file system trực tiếp.

---

## Question 14

A company regularly receives new training data from the vendor of an ML model. The vendor delivers cleaned and prepared data to the company's Amazon S3 bucket every 3-4 days. The company has an Amazon SageMaker pipeline to retrain the model. An ML engineer needs to implement a solution to run the pipeline when new data is uploaded to the S3 bucket. Which solution will meet these requirements with the LEAST operational effort?

- **A.** Create an S3 Lifecycle rule to transfer the data to the SageMaker training instance and to initiate training.
- **B.** Create an AWS Lambda function that scans the S3 bucket. Program the Lambda function to initiate the pipeline when new data is uploaded.
- **C.** Create an Amazon EventBridge rule that has an event pattern that matches the S3 upload. Configure the pipeline as the target of the rule.
- **D.** Use Amazon Managed Workflows for Apache Airflow (Amazon MWAA) to orchestrate the pipeline when new data is uploaded.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (EventBridge): Đây là mô hình kiến trúc hướng sự kiện (Event- Driven Architecture) điển hình và tối ưu nhất về công sức vận hành (LEAST operational effort). Amazon S3 tích hợp trực tiếp với Amazon EventBridge để gửi thông báo khi có file mới được tải lên (ví dụ: sự kiện Object Created). Bạn chỉ cần tạo một Rule trên EventBridge để bắt sự kiện này và đặt Target là SageMaker Pipeline. Hệ thống sẽ tự động kích hoạt quy trình huấn luyện lại (Retrain) ngay lập tức mà không cần viết bất kỳ dòng code nào hay quản lý hạ tầng máy chủ. Tại sao không chọn A (S3 Lifecycle rule): S3 Lifecycle Rules chỉ dùng để quản lý vòng đời lưu trữ (ví dụ: chuyển dữ liệu sang lớp lưu trữ rẻ hơn như Glacier hoặc xóa tự động sau một thời gian). Nó không có chức năng kích hoạt các tác vụ tính toán hay khởi chạy quy trình ML bên ngoài. Tại sao không chọn B (Lambda polling/scanning): Phương án này yêu cầu bạn phải viết code cho hàm Lambda để quét S3 (polling) hoặc xử lý sự kiện, sau đó lại phải viết thêm logic để gọi API kích hoạt Pipeline. Việc viết, test và bảo trì code sẽ tốn công sức vận hành hơn nhiều so với giải pháp không cần code (no-code) của EventBridge. Tại sao không chọn D (Amazon MWAA): Amazon MWAA (Managed Airflow) là một dịch vụ điều phối workflow mạnh mẽ nhưng phức tạp và tốn kém (cần khởi tạo môi trường, quản lý DAGs). Sử dụng MWAA chỉ để bắt một sự kiện đơn giản như S3 upload là "dùng dao mổ trâu để giết gà" (over-engineering), không thỏa mãn tiêu chí "Least operational effort".

---

## Question 15

An ML engineer is developing a fraud detection model by using the Amazon SageMaker XGBoost algorithm. The model classifies transactions as either fraudulent or legitimate. During testing, the model excels at identifying fraud in the training dataset. However, the model is inefficient at identifying fraud in new and unseen transactions. What should the ML engineer do to improve the fraud detection for new transactions?

- **A.** Increase the learning rate.
- **B.** Remove some irrelevant features from the training dataset.
- **C.** Increase the value of the max_depth hyperparameter.
- **D.** Decrease the value of the max_depth hyperparameter.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Decrease max_depth): Hiện tượng mô hình hoạt động cực tốt trên tập dữ liệu huấn luyện (Training data) nhưng lại kém trên dữ liệu mới/chưa thấy (Unseen data) chính là định nghĩa kinh điển của Overfitting (Quá khớp). Điều này có nghĩa là mô hình quá phức tạp, nó đang "học thuộc lòng" các nhiễu (noise) của dữ liệu train thay vì học các quy luật tổng quát. Trong thuật toán XGBoost, siêu tham số max_depth kiểm soát độ sâu tối đa của cây quyết định. Cây càng sâu thì càng nắm bắt được nhiều chi tiết cụ thể của dữ liệu train (bao gồm cả nhiễu). Để khắc phục Overfitting, ta cần giảm độ phức tạp của mô hình bằng cách giảm max_depth. Cây nông hơn (shallower trees) sẽ buộc mô hình phải học các mẫu tổng quát hơn, từ đó cải thiện khả năng dự đoán trên dữ liệu mới. Tại sao không chọn A (Increase learning rate): Tăng tốc độ học (eta hoặc learning_rate) thường làm cho mô hình cập nhật trọng số nhanh hơn và mạnh hơn sau mỗi vòng lặp. Nếu không được kiểm soát kỹ, điều này thường dẫn đến việc mô hình hội tụ quá nhanh vào các điểm cực tiểu cục bộ hoặc làm tăng khả năng Overfitting, khiến tình trạng tồi tệ hơn. Tại sao không chọn B (Remove irrelevant features): Mặc dù loại bỏ các đặc trưng không liên quan (Feature Selection) là một phương pháp tốt để giảm nhiễu, nhưng trong bối cảnh tinh chỉnh siêu tham số (Hyperparameter Tuning) để xử lý Overfitting trực tiếp trên mô hình cây, việc điều chỉnh max_depth là biện pháp kỹ thuật trực diện và phổ biến nhất. Hơn nữa, đề bài không cung cấp thông tin khẳng định có "irrelevant features" hay không, trong khi triệu chứng Overfitting do model complexity là rất rõ ràng. Tại sao không chọn C (Increase max_depth): Tăng max_depth sẽ làm cho cây trở nên sâu hơn và phức tạp hơn. Điều này sẽ làm tăng khả năng "học thuộc lòng" dữ liệu train, khiến vấn đề Overfitting trở nên nghiêm trọng hơn thay vì giải quyết nó.

---

## Question 16

A company is using Amazon SageMaker to create ML models. The company's data scientists need fine-grained control of the ML workflows that they orchestrate. The data scientists also need the ability to visualize SageMaker jobs and workflows as a directed acyclic graph (DAG). The data scientists must keep a running history of model discovery experiments and must establish model governance for auditing and compliance verifications. Which solution will meet these requirements?

- **A.** Use AWS CodePipeline and its integration with SageMaker Studio to manage the entire ML workflows. Use SageMaker ML Lineage Tracking for the running history of experiments and for auditing and compliance verifications.
- **B.** Use AWS CodePipeline and its integration with SageMaker Experiments to manage the entire ML workflows. Use SageMaker Experiments for the running history of experiments and for auditing and compliance verifications.
- **C.** Use SageMaker Pipelines and its integration with SageMaker Studio to manage the entire ML workflows. Use SageMaker ML Lineage Tracking for the running history of experiments and for auditing and compliance verifications.
- **D.** Use SageMaker Pipelines and its integration with SageMaker Experiments to manage the entire ML workflows. Use SageMaker Experiments for the running history of experiments and for auditing and compliance verifications.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Pipelines + Lineage Tracking): Câu hỏi có hai nhóm yêu cầu chính: . Workflow Orchestration & Visualization: Cần kiểm soát chi tiết quy trình (fine-grained control) và trực quan hóa dưới dạng biểu đồ (DAG). SageMaker Pipelines là dịch vụ CI/CD chuyên dụng cho ML đầu tiên, cho phép định nghĩa quy trình bằng code (SDK) và tự động hiển thị biểu đồ trực quan (DAG Visualizer) ngay trong SageMaker Studio. . Audit & Compliance: Cần lưu lịch sử thí nghiệm và thiết lập quản trị (governance) cho mục đích kiểm toán. SageMaker ML Lineage Tracking là tính năng cốt lõi được thiết kế chính xác để truy vết nguồn gốc (lineage) của model (từ dữ liệu thô, code xử lý, đến artifact model cuối cùng). Nó lưu trữ siêu dữ liệu (metadata) của mọi bước, cho phép bạn trả lời câu hỏi "Model này được tạo ra từ dữ liệu nào, bởi ai, và tham số gì?" - đây chính là yêu cầu về auditing và compliance. Tại sao không chọn A & B (AWS CodePipeline): AWS CodePipeline là công cụ CI/CD đa năng cho DevOps (phát triển phần mềm), không được thiết kế chuyên biệt cho các đặc thù của ML (như visualize DAG của các bước training/processing step, caching các bước ML). Mặc dù có thể dùng, nhưng nó thiếu tính năng "fine-grained control" và tích hợp sâu (native integration) với hệ sinh thái SageMaker Studio để visualize DAG cho Data Scientist như SageMaker Pipelines. Tại sao không chọn D (SageMaker Experiments cho governance): Mặc dù SageMaker Experiments giúp tổ chức và theo dõi các lần chạy huấn luyện (runs/trials), nhưng mục đích chính của nó là so sánh hiệu năng (metrics comparison). Để đáp ứng yêu cầu khắt khe về Auditing và Compliance Verifications (như truy vết nguồn gốc artifact), SageMaker ML Lineage Tracking là công cụ chuyên sâu và chính xác hơn (nó tạo ra các mối quan hệ liên kết ContributedTo, Produced, DerivedFrom giữa các thực thể). Câu trả lời C chính xác hơn về mặt thuật ngữ kỹ thuật cho "governance".

---

## Question 17

A company wants to reduce the cost of its containerized ML applications. The applications use ML models that run on Amazon EC2 instances, AWS Lambda functions, and an Amazon Elastic Container Service (Amazon ECS) cluster. The EC2 workloads and ECS workloads use Amazon Elastic Block Store (Amazon EBS) volumes to save predictions and artifacts. An ML engineer must identify resources that are being used inefficiently. The ML engineer also must generate recommendations to reduce the cost of these resources. Which solution will meet these requirements with the LEAST development effort?

- **A.** Create code to evaluate each instance's memory and compute usage.
- **B.** Add cost allocation tags to the resources. Activate the tags in AWS Billing and Cost Management.
- **C.** Check AWS CloudTrail event history for the creation of the resources.
- **D.** Run AWS Compute Optimizer.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (AWS Compute Optimizer): Bài toán yêu cầu "xác định tài nguyên sử dụng không hiệu quả" (inefficient resources) và "đưa ra khuyến nghị giảm chi phí" (generate recommendations) cho cả EC2, Lambda, ECS, và EBS với "nỗ lực phát triển ít nhất" (LEAST development effort). AWS Compute Optimizer là dịch vụ hoàn toàn tự động, sử dụng Machine Learning để phân tích lịch sử sử dụng (CloudWatch Metrics) của các tài nguyên tính toán (Compute resources). Nó tự động phát hiện các instance bị dư thừa (over-provisioned) hoặc thiếu hụt (under-provisioned) và đưa ra các khuyến nghị cụ thể (ví dụ: "Đổi từ m5.xlarge xuống m5.large để tiết kiệm $X/tháng"). Nó hỗ trợ chính xác các tài nguyên được nêu trong đề bài: EC2, Lambda, ECS services (trên Fargate), và EBS volumes. Bạn chỉ cần bật (opt-in) dịch vụ này mà không cần viết bất kỳ dòng code nào. Tại sao không chọn A (Create code to evaluate): Việc tự viết code để thu thập metrics (CPU, RAM) từ CloudWatch, phân tích và đưa ra quyết định là việc làm thủ công, tốn nhiều thời gian và công sức phát triển (High development effort), vi phạm yêu cầu "Least development effort". Tại sao không chọn B (Cost allocation tags): Cost allocation tags giúp bạn phân loại hóa đơn (ví dụ: Chi phí này thuộc về Project A hay Project B) để báo cáo tài chính. Nó chỉ cho biết bạn đã tiêu bao nhiêu tiền, chứ không có khả năng phân tích hiệu năng kỹ thuật để nói rằng "Tài nguyên này đang bị lãng phí, hãy giảm size đi". Tại sao không chọn C (AWS CloudTrail): CloudTrail là dịch vụ ghi log hoạt động (Audit log) để biết "Ai đã tạo ra instance này vào lúc nào". Nó không chứa thông tin về mức độ sử dụng tài nguyên (CPU % utilization, Memory usage) nên không thể dùng để tối ưu hóa chi phí hay hiệu năng.

---

## Question 18

A company needs to create a central catalog for all the company's ML models. The models are in AWS accounts where the company developed the models initially. The models are hosted in Amazon Elastic Container Registry (Amazon ECR) repositories. Which solution will meet these requirements?

- **A.** Configure ECR cross-account replication for each existing ECR repository. Ensure that each model is visible in each AWS account.
- **B.** Create a new AWS account with a new ECR repository as the central catalog. Configure ECR cross-account replication between the initial ECR repositories and the central catalog.
- **C.** Use the Amazon SageMaker Model Registry to create a model group for models hosted in Amazon ECR. Create a new AWS account. In the new account, use the SageMaker Model Registry as the central catalog. Attach a cross-account resource policy to each model group in the initial AWS accounts.
- **D.** Use an AWS Glue Data Catalog to store the models. Run an AWS Glue crawler to migrate the models from the ECR repositories to the Data Catalog. Configure cross- account access to the Data Catalog.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Model Registry): Đề bài yêu cầu tạo một "central catalog" (danh mục tập trung) cho các ML models. Khái niệm "Catalog" trong ML không chỉ đơn thuần là nơi chứa file (docker image), mà nó cần quản lý siêu dữ liệu (metadata), phiên bản (versioning), trạng thái phê duyệt (approval status - Pending/Approved/Rejected), và lineage. Amazon SageMaker Model Registry là dịch vụ chuyên biệt được thiết kế đúng cho mục đích này. Nó cho phép bạn đăng ký các model (bao gồm cả image nằm trong ECR) vào các "Model Groups". Tính năng quan trọng nhất ở đây là Cross-account support: Bạn có thể cấu hình Resource Policy trên các Model Group để cho phép một tài khoản trung tâm (Central Account) truy cập và quản lý metadata của các model nằm rải rác ở các tài khoản khác. Đây là cách chuẩn mực để xây dựng kho quản lý model tập trung (Model Governance) cấp doanh nghiệp. Tại sao không chọn A (ECR Replication): ECR Cross-account replication chỉ đơn giản là copy các Docker images từ tài khoản này sang tài khoản khác. Nó không cung cấp tính năng "Catalog" (quản lý phiên bản model, trạng thái phê duyệt, metadata). Việc có hàng đống image nằm ở khắp nơi không giải quyết được bài toán quản trị tập trung. Tại sao không chọn B (New ECR account): Tương tự như A, việc dồn tất cả Docker images về một tài khoản ECR mới chỉ giải quyết vấn đề lưu trữ (Storage), không giải quyết vấn đề quản lý vòng đời model (Model Lifecycle Management). ECR là container registry, không phải là Model Registry. Tại sao không chọn D (AWS Glue Data Catalog): AWS Glue Data Catalog là kho chứa metadata cho dữ liệu (bảng, database, schema) dùng cho ETL và Analytics (Athena, Redshift). Nó không được thiết kế để quản lý các thực thể ML Model (như hyperparameters, metrics, inference images). Sử dụng Glue Crawler để quét Docker images là không khả thi về mặt kỹ thuật.

---

## Question 19

A company has developed a new ML model. The company requires online model validation on 10% of the traffic before the company fully releases the model in production. The company uses an Amazon SageMaker endpoint behind an Application Load Balancer (ALB) to serve the model. Which solution will set up the required online validation with the LEAST operational overhead?

- **A.** Use production variants to add the new model to the existing SageMaker endpoint. Set the variant weight to 0.1 for the new model. Monitor the number of invocations by using Amazon CloudWatch.
- **B.** Use production variants to add the new model to the existing SageMaker endpoint. Set the variant weight to 1 for the new model. Monitor the number of invocations by using Amazon CloudWatch.
- **C.** Create a new SageMaker endpoint. Use production variants to add the new model to the new endpoint. Monitor the number of invocations by using Amazon CloudWatch.
- **D.** Configure the ALB to route 10% of the traffic to the new model at the existing SageMaker endpoint. Monitor the number of invocations by using AWS CloudTrail.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Production Variants with weight 0.1): Câu hỏi yêu cầu thực hiện xác thực mô hình mới trên 10% lưu lượng truy cập (tương tự Canary Deployment hoặc A/B Testing) với "chi phí vận hành thấp nhất". SageMaker Production Variants là tính năng được tích hợp sẵn (native feature), cho phép bạn triển khai nhiều model (variants) đằng sau cùng một Endpoint duy nhất. Bạn kiểm soát lưu lượng truy cập bằng cách gán trọng số (weights) cho từng variant. Để định tuyến 10% traffic vào model mới, bạn chỉ cần cấu hình trọng số (hoặc tỷ lệ) tương ứng (ví dụ: Model cũ = 0.9, Model mới = 0.1). SageMaker sẽ tự động phân phối traffic ngẫu nhiên theo tỷ lệ này mà không cần cấu hình thêm bất kỳ load balancer hay proxy nào bên ngoài. Đây là cách đơn giản và chuẩn mực nhất. Tại sao không chọn B (Weight 1): Nếu đặt trọng số là 1 (trong khi model cũ cũng có trọng số >= 0), traffic sẽ được chia theo tỷ lệ tương ứng của tổng trọng số, nhưng con số "1" không đảm bảo chính xác 10% nếu không biết trọng số của model kia. Hơn nữa, nếu tổng trọng số chỉ có model này là 1, nó sẽ nhận 100% traffic, vi phạm yêu cầu đề bài. Tại sao không chọn C (New Endpoint): Tạo một Endpoint hoàn toàn mới đồng nghĩa với việc bạn có hai URL endpoint khác nhau. Để chia traffic (split traffic) giữa hai URL này, bạn sẽ phải cấu hình thêm logic định tuyến phức tạp ở tầng ứng dụng (Application Layer) hoặc Load Balancer, làm tăng chi phí vận hành so với việc dùng tính năng có sẵn của SageMaker. Tại sao không chọn D (ALB routing + CloudTrail): ALB thường định tuyến dựa trên Path hoặc Header. Mặc dù ALB có hỗ trợ weighted target groups, nhưng việc cấu hình nó để trỏ vào SageMaker Endpoint (thường được truy cập qua API invoke của AWS chứ không phải HTTP target thông thường trong VPC theo cách truyền thống) phức tạp hơn. Quan trọng hơn, CloudTrail dùng để audit API calls (quản lý), không phải để monitor số lượng invocations (metrics) thời gian thực hiệu quả như CloudWatch.

---

## Question 20

A company needs to develop an ML model. The model must identify an item in an image and must provide the location of the item. Which Amazon SageMaker algorithm will meet these requirements?

- **A.** Image classification
- **B.** XGBoost
- **C.** Object detection
- **D.** K-nearest neighbors (k-NN)

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Object detection): Đề bài yêu cầu hai nhiệm vụ đồng thời: xác định vật thể là gì ("identify an item") và xác định vị trí của nó ("provide the location"). Đây chính xác là định nghĩa của bài toán Object Detection (Phát hiện vật thể). Thuật toán Object Detection (như SSD hoặc Faster R-CNN trong SageMaker) sẽ đầu ra một danh sách các vật thể được phát hiện cùng với Bounding Box (hộp bao quanh) để chỉ ra tọa độ vị trí của vật thể đó trong ảnh. Tại sao không chọn A (Image classification): Image Classification (Phân loại ảnh) chỉ trả lời câu hỏi "Trong ảnh này có cái gì?" (ví dụ: "Con chó"), nhưng nó gán nhãn cho toàn bộ bức ảnh và không cung cấp thông tin về vị trí (tọa độ pixel) của vật thể đó nằm ở đâu. Tại sao không chọn B (XGBoost): XGBoost là thuật toán tăng cường độ dốc (gradient boosting) chuyên dùng cho dữ liệu dạng bảng (tabular/structured data). Nó không được thiết kế để xử lý dữ liệu hình ảnh (unstructured data) cho các tác vụ thị giác máy tính. Tại sao không chọn D (K-nearest neighbors - k-NN): k-NN là thuật toán dựa trên khoảng cách, thường dùng để tìm các điểm dữ liệu tương đồng (ví dụ: tìm các ảnh giống nhau hoặc phân loại dựa trên đặc trưng). Nó không có khả năng tự nhiên để vẽ bounding box quanh một vật thể cụ thể trong ảnh.

---

## Question 21

A company has an Amazon S3 bucket that contains 1 ТВ of files from different sources. The S3 bucket contains the following file types in the same S3 folder: CSV, JSON, XLSX, and Apache Parquet. An ML engineer must implement a solution that uses AWS Glue DataBrew to process the data. The ML engineer also must store the final output in Amazon S3 so that AWS Glue can consume the output in the future. Which solution will meet these requirements?

- **A.** Use DataBrew to process the existing S3 folder. Store the output in Apache Parquet format.
- **B.** Use DataBrew to process the existing S3 folder. Store the output in AWS Glue Parquet format.
- **C.** Separate the data into a different folder for each file type. Use DataBrew to process each folder individually. Store the output in Apache Parquet format.
- **D.** Separate the data into a different folder for each file type. Use DataBrew to process each folder individually. Store the output in AWS Glue Parquet format.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Separate data + Process individually + Apache Parquet): Đây là giải pháp duy nhất khả thi về mặt kỹ thuật. . Hạn chế của DataBrew: Một Dataset trong AWS Glue DataBrew được định nghĩa từ một nguồn dữ liệu (S3 path). DataBrew yêu cầu tất cả các file trong nguồn đó phải có cùng định dạng (format) và cấu trúc (schema) tương thích để nó có thể đọc và suy luận (infer) chính xác. Nếu bạn trỏ DataBrew vào một folder chứa hỗn hợp CSV, JSON, và Parquet, DataBrew sẽ không thể xử lý đồng thời vì mỗi loại file cần một parser khác nhau. Do đó, bắt buộc phải tách dữ liệu ra các folder riêng biệt theo định dạng. . Output Format: Apache Parquet là định dạng cột (columnar storage) tiêu chuẩn mở, tối ưu hóa cực tốt cho hiệu suất truy vấn và tiết kiệm chi phí lưu trữ. Đây là định dạng lý tưởng ("gold standard") để AWS Glue và các dịch vụ phân tích khác tiêu thụ sau này. Tại sao không chọn A (Process mixed folder): DataBrew không có khả năng tự động xử lý một folder chứa "thập cẩm" các định dạng file khác nhau (mixed file types) trong cùng một Dataset. Nó sẽ cố gắng áp dụng một bộ quy tắc đọc (ví dụ: CSV parser) cho tất cả các file, dẫn đến lỗi khi gặp file JSON hoặc Parquet. Tại sao không chọn B và D (AWS Glue Parquet format): Đây là một thuật ngữ "bẫy" (distractor). Trong thế giới dữ liệu lớn, chỉ có định dạng chuẩn là Apache Parquet. Không có định dạng nào tên là "AWS Glue Parquet". Sự xuất hiện của thuật ngữ sai lệch này làm cho các đáp án B và D trở nên vô giá trị.

---

## Question 22

A manufacturing company uses an ML model to determine whether products meet a standard for quality. The model produces an output of "Passed" or "Failed." Robots separate the products into the two categories by using the model to analyze photos on the assembly line. Which metrics should the company use to evaluate the model's performance? (Choose two.)

- **A.** Precision and recall
- **B.** Root mean square error (RMSE) and mean absolute percentage error (MAPE)
- **C.** Accuracy and F1 score
- **D.** Bilingual Evaluation Understudy (BLEU) score
- **E.** Perplexity

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Precision and recall) và C (Accuracy and F1 score): Bài toán xác định sản phẩm "Passed" (Đạt) hoặc "Failed" (Hỏng) dựa trên hình ảnh là một bài toán Phân loại nhị phân (Binary Classification) điển hình trong Computer Vision. . Accuracy (Độ chính xác): Đo lường tỷ lệ dự đoán đúng trên tổng số mẫu. Hữu ích khi dữ liệu cân bằng. . Precision (Độ chính xác của lớp Positive) & Recall (Độ phủ): Cực kỳ quan trọng trong sản xuất.  Precision: Trong số các sản phẩm model báo "Hỏng", bao nhiêu phần trăm thực sự hỏng? (Tránh vứt nhầm hàng tốt).  Recall: Trong số tất cả sản phẩm "Hỏng" thực tế, model phát hiện được bao nhiêu? (Tránh để lọt hàng lỗi ra thị trường). . F1 Score: Là trung bình điều hòa của Precision và Recall, giúp đánh giá hiệu năng tổng thể khi cần cân bằng giữa hai yếu tố trên hoặc khi dữ liệu bị mất cân bằng (Imbalanced Data - ví dụ hàng lỗi rất ít so với hàng tốt). Vì các đáp án còn lại đều thuộc về các lĩnh vực khác (Regression hoặc NLP), nên A và C là hai nhóm chỉ số duy nhất phù hợp. Tại sao không chọn B (RMSE và MAPE): Root Mean Square Error và Mean Absolute Percentage Error là các chỉ số dùng cho bài toán Hồi quy (Regression) - tức là dự đoán một con số cụ thể (ví dụ: dự đoán nhiệt độ, giá nhà), không dùng cho bài toán phân loại (Classification). Tại sao không chọn D (BLEU score): BLEU (Bilingual Evaluation Understudy) là chỉ số tiêu chuẩn dùng để đánh giá chất lượng của các hệ thống Dịch máy (Machine Translation) hoặc sinh văn bản, bằng cách so sánh văn bản máy tạo ra với văn bản mẫu của con người. Nó không liên quan đến xử lý ảnh. Tại sao không chọn E (Perplexity): Perplexity là chỉ số dùng để đánh giá các Mô hình ngôn ngữ (Language Models) (ví dụ: model dự đoán từ tiếp theo tốt đến đâu). Nó đo lường độ "bối rối" của model trước dữ liệu mới; giá trị càng thấp càng tốt. Nó không áp dụng cho bài toán phân loại ảnh.

---

## Question 23

An ML engineer needs to encrypt all data in transit when an ML training job runs. The ML engineer must ensure that encryption in transit is applied to processes that Amazon SageMaker uses during the training job. Which solution will meet these requirements?

- **A.** Encrypt communication between nodes for batch processing.
- **B.** Encrypt communication between nodes in a training cluster.
- **C.** Specify an AWS Key Management Service (AWS KMS) key during creation of the training job request.
- **D.** Specify an AWS Key Management Service (AWS KMS) key during creation of the SageMaker domain.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Encrypt communication between nodes): Trong quá trình huấn luyện phân tán (Distributed Training) sử dụng nhiều instance (nodes), các node này cần trao đổi dữ liệu liên tục (như tham số mô hình, gradients) với nhau. Để đảm bảo an toàn cho dữ liệu đang di chuyển (in transit) giữa các container trên các node khác nhau, Amazon SageMaker cung cấp tính năng Inter-container traffic encryption. Khi tạo training job, bạn cần bật cờ (flag) EnableInterContainerTrafficEncryption thành True. Điều này đảm bảo mọi giao tiếp mạng giữa các node trong cụm huấn luyện đều được mã hóa bằng giao thức TLS 1.2. Tại sao không chọn A (Batch processing): "Batch processing" thường ám chỉ tác vụ suy luận hàng loạt (Batch Transform) hoặc xử lý dữ liệu ETL, không phải là thuật ngữ chuyên môn dùng để mô tả giao tiếp nội bộ trong cụm "Training Job" (Huấn luyện). Hơn nữa, cơ chế mã hóa cho Batch Transform cũng tương tự nhưng ngữ cảnh câu hỏi đang nhấn mạnh vào "training job". Tại sao không chọn C (AWS KMS key for training job): Việc chỉ định AWS KMS key (VolumeKmsKeyId) khi tạo training job chủ yếu để mã hóa Dữ liệu tại chỗ (Data At Rest) trên các ổ đĩa EBS được gắn vào training instances và dữ liệu đầu ra trên S3 (OutputDataConfig). Nó không tự động bật tính năng mã hóa đường truyền mạng giữa các node. Tại sao không chọn D (AWS KMS key for SageMaker domain): Cấu hình KMS cho SageMaker Domain dùng để mã hóa dữ liệu lưu trữ trên ổ đĩa EFS của môi trường làm việc (SageMaker Studio/Notebooks). Nó hoàn toàn không liên quan đến môi trường tính toán tạm thời (ephemeral cluster) được khởi tạo riêng biệt để chạy training job.

---

## Question 24

An ML engineer needs to use metrics to assess the quality of a time-series forecasting model. Which metrics apply to this model? (Choose two.)

- **A.** Recall
- **B.** LogLoss
- **C.** Root mean square error (RMSE)
- **D.** InferenceLatency
- **E.** Average weighted quantile loss (wQL)

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (RMSE): Dự báo chuỗi thời gian (Time-series forecasting) về bản chất là một bài toán hồi quy (Regression) với yếu tố thời gian. RMSE (Root Mean Square Error) là thước đo tiêu chuẩn để đánh giá độ lệch giữa giá trị dự báo và giá trị thực tế. Nó đo lường độ lớn trung bình của sai số và đặc biệt "trừng phạt" nặng các sai số lớn (do bình phương sai số), giúp phát hiện các điểm dự báo sai lệch nghiêm trọng. Tại sao chọn E (Average weighted quantile loss - wQL): Trong các dịch vụ dự báo hiện đại của AWS (như Amazon Forecast hay thuật toán DeepAR), mô hình thường đưa ra dự báo theo xác suất (Probabilistic Forecast) thay vì một điểm đơn lẻ (Point Forecast). wQL được sử dụng để đánh giá độ chính xác của dự báo tại các phân vị cụ thể (ví dụ: P10, P50, P90). Nó đo lường mức độ sai lệch giữa phân phối dự đoán và thực tế, giúp đánh giá rủi ro tốt hơn (ví dụ: dự báo tồn kho quá nhiều hay quá ít). Tại sao không chọn A (Recall): Recall là chỉ số dùng cho bài toán Phân loại (Classification) để đo lường tỷ lệ các mẫu Positive thực tế được dự đoán đúng. Dự báo chuỗi thời gian là dự đoán giá trị liên tục (số lượng, doanh thu), không phải phân loại nhãn. Tại sao không chọn B (LogLoss): LogLoss (hay Cross-entropy Loss) là hàm mất mát dùng cho bài toán Phân loại, đặc biệt là để đánh giá độ tin cậy của xác suất dự đoán lớp (class probability). Nó không áp dụng cho dự báo giá trị số thực. Tại sao không chọn D (InferenceLatency): InferenceLatency (Độ trễ suy luận) là chỉ số về Hiệu năng vận hành (Operational Performance/Efficiency) - tức là model chạy nhanh hay chậm. Khi nói đến "quality of a model" trong ngữ cảnh Data Science, người ta thường ám chỉ độ chính xác (Accuracy/Error metrics) của dự đoán, chứ không phải tốc độ phản hồi.

---

## Question 25

A company runs Amazon SageMaker ML models that use accelerated instances. The models require real-time responses. Each model has different scaling requirements. The company must not allow a cold start for the models. Which solution will meet these requirements?

- **A.** Create a SageMaker Serverless Inference endpoint for each model. Use provisioned concurrency for the endpoints.
- **B.** Create a SageMaker Asynchronous Inference endpoint for each model. Create an auto scaling policy for each endpoint.
- **C.** Create a SageMaker endpoint. Create an inference component for each model. In the inference component settings, specify the newly created endpoint. Create an auto scaling policy for each inference component. Set the parameter for the minimum number of copies to at least 1.
- **D.** Create an Amazon S3 bucket. Store all the model artifacts in the S3 bucket. Create a SageMaker multi-model endpoint. Point the endpoint to the S3 bucket. Create an auto scaling policy for the endpoint. Set the parameter for the minimum number of copies to at least 1.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Inference Components): Đây là tính năng mới và mạnh mẽ nhất của SageMaker Real-time Inference, được thiết kế đặc biệt để giải quyết bài toán "nhiều model trên một endpoint" nhưng vẫn đảm bảo sự độc lập về tài nguyên. . Accelerated Instances & Cost Efficiency: Inference Components cho phép bạn triển khai nhiều model lên cùng một endpoint (chia sẻ instance GPU đắt tiền) để tối ưu chi phí, thay vì mỗi model một endpoint riêng. . Independent Scaling: Điểm cốt lõi là mỗi "Inference Component" có thể có chính sách Auto Scaling riêng biệt. Model A có thể scale lên 5 copies khi tải cao, trong khi Model B vẫn giữ 1 copy. . No Cold Start: Bằng cách đặt tham số "minimum number of copies" (số bản sao tối thiểu) là 1 (hoặc lớn hơn), bạn đảm bảo model luôn được tải sẵn trong bộ nhớ GPU/CPU và sẵn sàng phục vụ request ngay lập tức, loại bỏ hoàn toàn vấn đề cold start (độ trễ khi khởi động). Tại sao không chọn A (Serverless Inference): Serverless Inference hiện tại chưa hỗ trợ GPU (accelerated instances). Ngoài ra, mặc dù có Provisioned Concurrency để giảm cold start, nhưng nó không phù hợp với các workload yêu cầu GPU hiệu năng cao như đề bài gợi ý ("accelerated instances"). Tại sao không chọn B (Asynchronous Inference): Asynchronous Inference được thiết kế cho các request có thời gian xử lý lâu (long-running) hoặc payload lớn, không phải tối ưu cho "Real-time responses" (phản hồi tức thì) với độ trễ thấp nhất. Hơn nữa, Async Inference thường có cơ chế scale-to-zero, dẫn đến cold start nếu không cấu hình kỹ. Tại sao không chọn D (Multi-model Endpoint - MME): Multi-model Endpoint (MME) truyền thống hoạt động theo cơ chế "Lazy Loading": model chỉ được tải từ S3 vào bộ nhớ khi có request đầu tiên gọi đến nó. Điều này gây ra Cold Start rõ rệt cho các request đầu tiên. Mặc dù MME tiết kiệm chi phí, nhưng nó vi phạm yêu cầu nghiêm ngặt "must not allow a cold start". Ngoài ra, MME scale ở cấp độ Endpoint (Instance level), khó kiểm soát scaling chi tiết cho từng model riên...

---

## Question 26

Question 92


??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (MulticlassClassificationEvaluator): Đây là đoạn mã chính xác để đánh giá mô hình phân loại đa lớp (multi-class) trong Spark ML. . Đúng Class Evaluator: Bài toán nêu rõ đây là "three-class decision tree classifier" (phân loại 3 lớp), do đó bắt buộc phải sử dụng MulticlassClassificationEvaluator. . Đúng Cấu hình: Các tham số predictionCol="prediction" và labelCol="actual" khớp hoàn toàn với schema của DataFrame preds_df đã cho. Tham số metricName="accuracy" là hợp lệ để tính độ chính xác. . Đúng Phương thức: Quan trọng nhất, đoạn code gọi phương thức .evaluate(preds_df) trên đối tượng evaluator. Đây là bước thực thi tính toán metric dựa trên dữ liệu và trả về kết quả số thực (Double) cho biến accuracy. Tại sao không chọn A (Summarizer): Summarizer trong Spark ML (pyspark.ml.stat) thường được sử dụng để tính toán các thống kê mô tả (như mean, variance, count) cho các cột vector (Vector column summary statistics). Nó không phải là class dùng để đánh giá hiệu năng (evaluation metrics) của mô hình phân loại. Tại sao không chọn C (Missing .evaluate()): Mặc dù Option C khởi tạo đúng đối tượng MulticlassClassificationEvaluator, nhưng nó thiếu bước gọi hàm .evaluate(preds_df). Biến accuracy trong trường hợp này sẽ chỉ chứa đối tượng Evaluator (instance của class), chứ không phải là giá trị độ chính xác (số thực) mà đề bài yêu cầu "compute the accuracy". Tại sao không chọn D (BinaryClassificationEvaluator): BinaryClassificationEvaluator chỉ dành riêng cho bài toán phân loại nhị phân (2 lớp). Đề bài nêu rõ đây là bài toán 3 lớp (three-class), nên việc sử dụng Binary Evaluator là sai về mặt kỹ thuật. Hơn nữa, BinaryClassificationEvaluator mặc định hỗ trợ các metric như areaUnderROC hoặc areaUnderPR, chứ không hỗ trợ accuracy một cách trực tiếp như Multiclass Evaluator.

---

## Question 27

A company runs training jobs on Amazon SageMaker by using a compute optimized instance. Demand for training runs will remain constant for the next 55 weeks. The instance needs to run for 35 hours each week. The company needs to reduce its model training costs. Which solution will meet these requirements?

!!! warning "Select 3"

- **A.** Use a serverless endpoint with a provisioned concurrency of 35 hours for each week. Run the training on the endpoint.
- **B.** Use SageMaker Edge Manager for the training. Specify the instance requirement in the edge device configuration. Run the training.
- **C.** Use the heterogeneous cluster feature of SageMaker Training. Configure the instance_type, instance_count, and instance_groups arguments to run training jobs.
- **D.** Opt in to a SageMaker Savings Plan with a 1-year term and an All Upfront payment. Run a SageMaker Training job on the instance.

??? success "Reveal Answer"
    **Correct Answer: D,a**

    Tại sao chọn D (SageMaker Savings Plan): Bài toán đưa ra một nhu cầu sử dụng tài nguyên rất rõ ràng và ổn định: chạy training 35 giờ/tuần trong suốt 55 tuần (tương đương hơn 1 năm một chút). Đây là kịch bản hoàn hảo để sử dụng SageMaker Savings Plans. SageMaker Savings Plans cung cấp mức giá chiết khấu đáng kể (lên đến 64%) so với giá On-Demand để đổi lấy cam kết sử dụng một lượng tài nguyên nhất định (tính theo $/giờ) trong kỳ hạn 1 hoặc 3 năm. Với lựa chọn "1-year term" và thanh toán "All Upfront" (trả trước toàn bộ), công ty sẽ đạt được mức tiết kiệm chi phí tối đa cho khối lượng công việc đã được dự báo trước này. Tại sao không chọn A (Serverless Endpoint): Serverless Endpoint là dịch vụ dành cho Suy luận (Inference), tức là triển khai model để dự đoán. Bạn không thể chạy các công việc Huấn luyện (Training jobs) trên một Inference Endpoint. Đây là sự nhầm lẫn cơ bản về mục đích sử dụng dịch vụ. Tại sao không chọn B (SageMaker Edge Manager): SageMaker Edge Manager được thiết kế để quản lý, giám sát và vận hành các model ML trên các thiết bị biên (Edge devices) như robot, camera thông minh, v.v. Nó không phải là giải pháp để tối ưu hóa chi phí cho việc huấn luyện model trên đám mây (Cloud Training) bằng EC2 instance. Tại sao không chọn C (Heterogeneous cluster): Tính năng Heterogeneous cluster cho phép chạy một training job trên nhiều loại instance khác nhau (ví dụ: dùng CPU instance cho xử lý dữ liệu và GPU instance cho training) để tối ưu hóa hiệu năng. Tuy nhiên, đề bài chỉ đề cập đến việc sử dụng "a compute optimized instance" (một loại instance) và tập trung vào khía cạnh tài chính (reduce costs) cho một nhu cầu ổn định dài hạn. Việc thay đổi kiến trúc cluster phức tạp hơn và không đảm bảo giảm chi phí trực tiếp bằng việc cam kết Savings Plan.

---

## Question 28

A company deployed an ML model that uses the XGBoost algorithm to predict product failures. The model is hosted on an Amazon SageMaker endpoint and is trained on normal operating data. An AWS Lambda function provides the predictions to the company's application. An ML engineer must implement a solution that uses incoming live data to detect decreased model accuracy over time. Which solution will meet these requirements?

- **A.** Use Amazon CloudWatch to create a dashboard that monitors real-time inference data and model predictions. Use the dashboard to detect drift.
- **B.** Modify the Lambda function to calculate model drift by using real-time inference data and model predictions. Program the Lambda function to send alerts.
- **C.** Schedule a monitoring job in SageMaker Model Monitor. Use the job to detect drift by analyzing the live data against a baseline of the training data statistics and constraints.
- **D.** Schedule a monitoring job in SageMaker Debugger. Use the job to detect drift by analyzing the live data against a baseline of the training data statistics and constraints.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Model Monitor): Câu hỏi yêu cầu phát hiện sự suy giảm độ chính xác của model theo thời gian (decreased model accuracy over time) dựa trên dữ liệu thực tế (incoming live data). Đây chính là định nghĩa của việc giám sát Model Quality Drift và Data Quality Drift. Amazon SageMaker Model Monitor là dịch vụ chuyên dụng được thiết kế để giải quyết chính xác bài toán này. Quy trình chuẩn như sau: . Tạo một Baseline (đường cơ sở) từ thống kê của dữ liệu huấn luyện (Training data statistics & constraints). . Bật tính năng Data Capture trên Endpoint để lưu lại dữ liệu suy luận thực tế. . Lên lịch (Schedule) một monitoring job định kỳ. Job này sẽ tự động so sánh dữ liệu thực tế với Baseline. Nếu phát hiện sự sai lệch vượt quá ngưỡng cho phép (ví dụ: phân phối dữ liệu thay đổi), nó sẽ báo cáo drift và gửi cảnh báo qua CloudWatch. Tại sao không chọn A (CloudWatch Dashboard): Amazon CloudWatch Dashboards dùng để trực quan hóa các số liệu (metrics) như CPU, Memory, Latency hoặc các custom metrics đơn giản. Nó không có khả năng tự động thực hiện các phép tính thống kê phức tạp (như KS test, Chi-square test) để so sánh phân phối dữ liệu (distribution comparison) nhằm phát hiện drift một cách khoa học. Tại sao không chọn B (Lambda function): Việc sửa đổi Lambda function để tự tính toán drift là một giải pháp thủ công, phức tạp và không hiệu quả (Self-managed solution). Bạn sẽ phải tự viết code để lưu trữ trạng thái, thực hiện các phép toán thống kê và quản lý baseline, điều này đi ngược lại với thực tiễn tốt nhất là sử dụng các dịch vụ Managed Services có sẵn. Hơn nữa, tính toán drift thường là tác vụ batch (xử lý theo lô) định kỳ, không nên thực hiện trong thời gian thực (real-time) bên trong Lambda vì sẽ làm tăng độ trễ của ứng dụng. Tại sao không chọn D (SageMaker Debugger): SageMaker Debugger là công cụ dùng để gỡ lỗi và phân tích model trong quá trình huấn luyện (Training phase), ví dụ như phát hiện vanishing gradients, overfitting, hoặc giám sát việc sử...

---

## Question 29

A company has an ML model that uses historical transaction data to predict customer behavior. An ML engineer is optimizing the model in Amazon SageMaker to enhance the model's predictive accuracy. The ML engineer must examine the input data and the resulting predictions to identify trends that could skew the model's performance across different demographics. Which solution will provide this level of analysis?

- **A.** Use Amazon CloudWatch to monitor network metrics and CPU metrics for resource optimization during model training.
- **B.** Create AWS Glue DataBrew recipes to correct the data based on statistics from the model output.
- **C.** Use SageMaker Clarify to evaluate the model and training data for underlying patterns that might affect accuracy.
- **D.** Create AWS Lambda functions to automate data pre-processing and to ensure consistent quality of input data for the model.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Clarify): Yêu cầu cốt lõi của đề bài là "examine the input data and the resulting predictions" (kiểm tra dữ liệu đầu vào và kết quả dự đoán) để xác định các xu hướng gây sai lệch hiệu năng trên "different demographics" (các nhóm nhân khẩu học khác nhau). Đây chính là bài toán phát hiện Bias (Thiên kiến). Amazon SageMaker Clarify là công cụ chuyên dụng được tích hợp trong SageMaker để thực hiện nhiệm vụ này. Nó có khả năng: . Pre-training bias metrics: Phân tích dữ liệu trước khi huấn luyện để tìm sự mất cân bằng đại diện (ví dụ: dữ liệu về một nhóm tuổi quá ít). . Post-training bias metrics: Phân tích kết quả dự đoán sau khi huấn luyện để xem model có đối xử bất công với các nhóm cụ thể hay không (ví dụ: tỷ lệ từ chối vay vốn cao bất thường ở một nhóm dân tộc). . Explainability: Giải thích lý do tại sao model đưa ra dự đoán đó (Feature attribution). Tại sao không chọn A (Amazon CloudWatch): CloudWatch là dịch vụ giám sát hạ tầng và hiệu năng vận hành (Operational monitoring). Nó theo dõi CPU, RAM, Network I/O để biết "Server có khỏe không", chứ không thể phân tích nội dung dữ liệu để biết "Model có công bằng không". Tại sao không chọn B (AWS Glue DataBrew): AWS Glue DataBrew là công cụ visual data preparation dùng để làm sạch và chuẩn hóa dữ liệu thô (ETL). Mặc dù nó có thể hiển thị thống kê dữ liệu (Data profile), nhưng nó không có khả năng so sánh tương quan giữa Input và Model Output để đánh giá Bias của thuật toán ML như Clarify. Tại sao không chọn D (AWS Lambda): AWS Lambda là dịch vụ tính toán phi máy chủ (Serverless Compute) dùng để chạy code tùy ý. Để dùng Lambda giải quyết bài toán này, bạn sẽ phải tự viết toàn bộ thuật toán thống kê phức tạp để tính toán bias từ đầu (Self-managed code), rất tốn kém công sức và không tận dụng được các tính năng có sẵn của nền tảng AI/ML.

---

## Question 30

A company uses 10 Reserved Instances of accelerated instance types to serve the current version of an ML model. An ML engineer needs to deploy a new version of the model to an Amazon SageMaker real-time inference endpoint. The solution must use the original 10 instances to serve both versions of the model. The solution also must include one additional Reserved Instance that is available to use in the deployment process. The transition between versions must occur with no downtime or service interruptions. Which solution will meet these requirements?

- **A.** Configure a blue/green deployment with all-at-once traffic shifting.
- **B.** Configure a blue/green deployment with canary traffic shifting and a size of 10%.
- **C.** Configure a shadow test with a traffic sampling percentage of 10%.
- **D.** Configure a rolling deployment with a rolling batch size of 1.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Rolling deployment): Bài toán đặt ra ràng buộc rất khắt khe về tài nguyên: Đang có 10 Reserved Instances (RIs) và chỉ có thêm 1 RI dự phòng (Tổng năng lực tối đa là 11 instances tại một thời điểm). Rolling Deployment (Triển khai cuốn chiếu) là chiến lược duy nhất phù hợp trong trường hợp này. Với RollingBatchSize = 1, SageMaker sẽ thực hiện quy trình sau: . Khởi tạo 1 instance mới (sử dụng RI thứ 11) chạy phiên bản model mới. . Sau khi instance này sẵn sàng, nó sẽ định tuyến traffic vào đó và tắt 1 instance cũ đi (trả lại 1 slot RI). . Lặp lại quy trình này 10 lần cho đến khi toàn bộ fleet được cập nhật. Cách này đảm bảo số lượng instance hoạt động không bao giờ vượt quá 11, tận dụng đúng số lượng RIs đã mua mà vẫn đảm bảo không có thời gian chết (no downtime). Tại sao không chọn A và B (Blue/Green Deployment): Blue/Green Deployment (dù là all-at-once hay canary) hoạt động theo nguyên tắc tạo ra một môi trường mới (Green Fleet) hoàn toàn độc lập và song song với môi trường cũ (Blue Fleet) trước khi chuyển traffic. Với 10 instance đang chạy, Blue/Green sẽ yêu cầu khởi tạo thêm 10 instance mới nữa (Tổng cộng 20 instances) để sẵn sàng chuyển đổi. Do công ty chỉ có thêm 1 RI, việc provision thêm 10 instance sẽ dẫn đến việc phải dùng On- Demand instance (tốn kém) hoặc không đủ quota/capacity, vi phạm ràng buộc về việc sử dụng tài nguyên đã nêu. Tại sao không chọn C (Shadow test): Shadow Testing là kỹ thuật kiểm thử, không phải chiến lược triển khai thay thế (replacement strategy). Nó gửi bản sao của traffic sang một "Shadow variant" để so sánh hiệu năng mà không trả kết quả cho user. Việc này vừa không hoàn thành mục tiêu "deploy new version" để phục vụ user, vừa tiêu tốn tài nguyên gấp đôi (nếu shadow 100% traffic) hoặc phức tạp hóa hạ tầng không cần thiết.

---

## Question 31

An IoT company uses Amazon SageMaker to train and test an XGBoost model for object detection. ML engineers need to monitor performance metrics when they train the model with variants in hyperparameters. The ML engineers also need to send Short Message Service (SMS) text messages after training is complete. Which solution will meet these requirements?

- **A.** Use Amazon CloudWatch to monitor performance metrics. Use Amazon Simple Queue Service (Amazon SQS) for message delivery.
- **B.** Use Amazon CloudWatch to monitor performance metrics. Use Amazon Simple Notification Service (Amazon SNS) for message delivery.
- **C.** Use AWS CloudTrail to monitor performance metrics. Use Amazon Simple Queue Service (Amazon SQS) for message delivery.
- **D.** Use AWS CloudTrail to monitor performance metrics. Use Amazon Simple Notification Service (Amazon SNS) for message delivery.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (CloudWatch + SNS): . Monitor performance metrics: Amazon CloudWatch là dịch vụ giám sát trung tâm của AWS. Khi Amazon SageMaker huấn luyện model (như XGBoost), nó tự động đẩy các metrics về hiệu năng (như training error, validation accuracy) lên CloudWatch Metrics và ghi logs vào CloudWatch Logs. Kỹ sư ML có thể xem biểu đồ trực quan tại đây. . Send SMS: Amazon Simple Notification Service (Amazon SNS) là dịch vụ thông báo dạng Pub/Sub hỗ trợ đẩy tin nhắn đến nhiều loại endpoint khác nhau, bao gồm Email và SMS. Đây là giải pháp chuẩn để gửi thông báo văn bản tới người dùng khi một sự kiện (như "Training Completed") xảy ra. Tại sao không chọn A và C (Amazon SQS): Amazon SQS (Simple Queue Service) là dịch vụ hàng đợi (queue) dùng để phân tách (decouple) các thành phần ứng dụng (để ứng dụng khác đọc và xử lý sau). SQS không có chức năng gửi tin nhắn văn bản (SMS) trực tiếp đến số điện thoại của người dùng. Tại sao không chọn C và D (AWS CloudTrail): AWS CloudTrail là dịch vụ dùng để ghi lại lịch sử gọi API (Audit/Governance) nhằm trả lời câu hỏi "Ai đã làm gì, lúc nào?". Nó không ghi nhận hay hiển thị các chỉ số hiệu năng (metrics) của quá trình huấn luyện model (như độ chính xác hay loss function).

---

## Question 32

A company is working on an ML project that will include Amazon SageMaker notebook instances. An ML engineer must ensure that the SageMaker notebook instances do not allow root access. Which solution will prevent the deployment of notebook instances that allow root access?

- **A.** Use IAM condition keys to stop deployments of SageMaker notebook instances that allow root access.
- **B.** Use AWS Key Management Service (AWS KMS) keys to stop deployments of SageMaker notebook instances that allow root access.
- **C.** Monitor resource creation by using Amazon EventBridge events. Create an AWS Lambda function that deletes all deployed SageMaker notebook instances that allow root access.
- **D.** Monitor resource creation by using AWS CloudFormation events. Create an AWS Lambda function that deletes all deployed SageMaker notebook instances that allow root access.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (IAM condition keys): Đây là giải pháp phòng ngừa (preventive) hiệu quả nhất. AWS IAM cung cấp condition key cụ thể là sagemaker:RootAccess. Bằng cách tạo một IAM policy với quy tắc Deny cho hành động sagemaker:CreateNotebookInstance nếu sagemaker:RootAccess được đặt là Enabled, bạn có thể chặn đứng yêu cầu tạo instance ngay từ bước gọi API. Instance sẽ không bao giờ được khởi tạo, đảm bảo tuân thủ bảo mật tuyệt đối. Tại sao không chọn B (AWS KMS): AWS KMS (Key Management Service) dùng để quản lý khóa mã hóa dữ liệu (Encryption). Nó không có khả năng kiểm soát cấu hình hệ điều hành (như quyền Root) của instance. Tại sao không chọn C (EventBridge + Lambda): Đây là giải pháp khắc phục (reactive). Instance đã được tạo ra và tồn tại trong một khoảng thời gian ngắn với quyền root trước khi EventBridge kích hoạt Lambda để xóa nó. Trong khoảng thời gian đó, lỗ hổng bảo mật đã tồn tại. Đề bài yêu cầu "prevent the deployment" (ngăn chặn việc triển khai), tức là không cho phép nó được sinh ra. Tại sao không chọn D (CloudFormation events + Lambda): Tương tự như phương án C, đây là cách tiếp cận phản ứng sau sự việc. Ngoài ra, việc sử dụng CloudFormation events phức tạp hơn và không chặn được các trường hợp người dùng tạo instance thủ công qua Console hoặc CLI mà không dùng CloudFormation.

---

## Question 33

A company is using Amazon SageMaker to develop ML models. The company stores sensitive training data in an Amazon S3 bucket. The model training must have network isolation from the internet. Which solution will meet this requirement?

- **A.** Run the SageMaker training jobs in private subnets. Create a NAT gateway. Route traffic for training through the NAT gateway.
- **B.** Run the SageMaker training jobs in private subnets. Create an S3 gateway VPC endpoint. Route traffic for training through the S3 gateway VPC endpoint.
- **C.** Run the SageMaker training jobs in public subnets that have an attached security group. In the security group, use inbound rules to limit traffic from the internet. Encrypt SageMaker instance storage by using server-side encryption with AWS KMS keys (SSE-KMS).
- **D.** Encrypt traffic to Amazon S3 by using a bucket policy that includes a value of True for the aws:SecureTransport condition key. Use default at-rest encryption for Amazon S3. Encrypt SageMaker instance storage by using server-side encryption with AWS KMS keys (SSE-KMS).

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Private subnets + S3 VPC Endpoint): Để đạt được yêu cầu "network isolation from the internet" (cô lập mạng hoàn toàn khỏi internet), các SageMaker training jobs phải chạy trong Private Subnet (không có đường ra Internet Gateway). Tuy nhiên, SageMaker vẫn cần truy cập dữ liệu training nằm trên S3. S3 Gateway VPC Endpoint là giải pháp chuẩn để cho phép các tài nguyên trong Private Subnet truy cập S3 qua mạng nội bộ của AWS mà không cần đi qua internet công cộng (public internet). Đây là kiến trúc tối ưu cho bảo mật và cô lập mạng. Tại sao không chọn A (NAT gateway): NAT Gateway được thiết kế để cung cấp khả năng truy cập internet chiều đi (outbound) cho các tài nguyên trong Private Subnet (ví dụ: để tải gói tin, update phần mềm). Việc sử dụng NAT Gateway đồng nghĩa với việc mở kết nối ra internet, điều này vi phạm yêu cầu "network isolation from the internet" (cô lập khỏi internet) của đề bài. Tại sao không chọn C (Public subnets): Việc chạy training jobs trong Public Subnets yêu cầu tài nguyên phải có địa chỉ Public IP và Internet Gateway để giao tiếp. Dù có dùng Security Group để hạn chế, về mặt kiến trúc mạng, tài nguyên này vẫn nằm trên mạng công cộng, vi phạm hoàn toàn yêu cầu về cô lập mạng (network isolation). Tại sao không chọn D (Encryption/SecureTransport): Đáp án này chỉ tập trung vào bảo mật dữ liệu (mã hóa đường truyền và mã hóa lưu trữ) mà không giải quyết vấn đề về kiến trúc mạng. Việc bật aws:SecureTransport (HTTPS) hay mã hóa dữ liệu không ngăn chặn việc training jobs kết nối ra internet hoặc đảm bảo traffic đi qua đường truyền riêng tư.

---

## Question 34

A company needs an AWS solution that will automatically create versions of ML models as the models are created. Which solution will meet this requirement?

- **A.** Amazon Elastic Container Registry (Amazon ECR)
- **B.** Model packages from Amazon SageMaker Marketplace
- **C.** Amazon SageMaker ML Lineage Tracking
- **D.** Amazon SageMaker Model Registry

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (SageMaker Model Registry): Đây là dịch vụ được thiết kế chuyên biệt để quản lý vòng đời của mô hình. Khi bạn tạo một "Model Group" và đăng ký một mô hình mới vào nhóm đó, SageMaker Model Registry sẽ tự động đánh số phiên bản (Version 1, Version 2,...) cho mô hình đó. Nó cung cấp kho lưu trữ trung tâm để quản lý các phiên bản, trạng thái phê duyệt (Approved/Rejected) và metadata, đáp ứng chính xác yêu cầu đề bài. Tại sao không chọn A (Amazon ECR): Amazon Elastic Container Registry (ECR) là nơi lưu trữ các Docker Container Images (thường chứa code inference). Mặc dù container là một phần của quá trình triển khai, nhưng ECR không quản lý "phiên bản mô hình" (model artifacts + metrics + status) theo ngữ cảnh ML. Nó chỉ quản lý phiên bản của image (tag). Tại sao không chọn B (SageMaker Marketplace): Đây là một "chợ ứng dụng" để tìm kiếm, mua hoặc bán các mô hình và thuật toán từ bên thứ ba (third-party vendors), không phải là công cụ để quản lý phiên bản cho các mô hình nội bộ của công ty. Tại sao không chọn C (SageMaker ML Lineage Tracking): Dịch vụ này tập trung vào việc truy vết nguồn gốc (provenance) và mối quan hệ giữa các thành phần (Dữ liệu -> Training Job -> Model). Mặc dù nó lưu giữ lịch sử, nhưng chức năng chính của nó là để audit (kiểm toán) và visualize quy trình, không phải là cơ chế chính để đăng ký và đánh số phiên bản cho việc triển khai (deployment) như Model Registry.

---

## Question 35

A company needs to use Retrieval Augmented Generation (RAG) to supplement an open source large language model (LLM) that runs on Amazon Bedrock. The company's data for RAG is a set of documents in an Amazon S3 bucket. The documents consist of .csv files and .docx files. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Create a pipeline in Amazon SageMaker Pipelines to generate a new model. Call the new model from Amazon Bedrock to perform RAG queries.
- **B.** Convert the data into vectors. Store the data in an Amazon Neptune database. Connect the database to Amazon Bedrock. Call the Amazon Bedrock API to perform RAG queries.
- **C.** Fine-tune an existing LLM by using an AutoML job in Amazon SageMaker. Configure the S3 bucket as a data source for the AutoML job. Deploy the LLM to a SageMaker endpoint. Use the endpoint to perform RAG queries.
- **D.** Create a knowledge base for Amazon Bedrock. Configure a data source that references the S3 bucket. Use the Amazon Bedrock API to perform RAG queries.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Knowledge base for Amazon Bedrock): Đây là giải pháp "Managed RAG" (RAG được quản lý hoàn toàn) của AWS. Tính năng Knowledge Bases for Amazon Bedrock tự động hóa toàn bộ quy trình RAG: từ việc kết nối nguồn dữ liệu (S3), chia nhỏ văn bản (chunking), tạo vector (embedding), lưu trữ vào vector database và truy xuất (retrieval). Vì AWS xử lý mọi công đoạn phức tạp ở backend, đây là giải pháp có "LEAST operational overhead" (ít gánh nặng vận hành nhất). Tại sao không chọn A (SageMaker Pipelines/New model): Phương án này đề cập đến việc tạo hoặc train một model mới. RAG (Retrieval Augmented Generation) là kỹ thuật bổ sung dữ liệu ngoài vào prompt, không phải là quy trình training model mới. Hơn nữa, việc quản lý pipeline training rất tốn kém chi phí vận hành. Tại sao không chọn B (Manual Vectorization + Neptune): Mặc dù kiến trúc này khả thi về mặt kỹ thuật, nhưng nó yêu cầu bạn phải tự viết code để chuyển đổi dữ liệu sang vector, sau đó tự cấu hình và quản lý cơ sở dữ liệu Amazon Neptune. Việc tự quản lý (self-managed) các thành phần này tạo ra gánh nặng vận hành cao hơn nhiều so với giải pháp tích hợp sẵn (Option D). Tại sao không chọn C (Fine-tune + AutoML): Fine-tuning (tinh chỉnh) khác hoàn toàn với RAG. Fine-tuning là dạy model học dữ liệu mới để thay đổi trọng số (weights), trong khi RAG là tra cứu thông tin tại thời điểm chạy (runtime). Ngoài ra, Fine-tuning yêu cầu chuẩn bị dữ liệu phức tạp và tốn kém tài nguyên tính toán hơn nhiều.

---

## Question 36

A company plans to deploy an ML model for production inference on an Amazon SageMaker endpoint. The average inference payload size will vary from 100 MB to 300 MB. Inference requests must be processed in 60 minutes or less. Which SageMaker inference option will meet these requirements?

- **A.** Serverless inference
- **B.** Asynchronous inference
- **C.** Real-time inference

??? success "Reveal Answer"
    **Correct Answer: ?**

    Tại sao chọn B (Asynchronous inference): Đây là chế độ suy luận được thiết kế đặc biệt cho các request có payload lớn (lên đến 1 GB) và thời gian xử lý lâu (lên đến 1 giờ). o Đề bài yêu cầu xử lý payload từ 100 MB - 300 MB (vượt xa giới hạn của Real- time) và thời gian xử lý lên đến 60 phút. Asynchronous Inference hoạt động bằng cách đưa request vào hàng đợi (queue) và xử lý không đồng bộ, hoàn toàn phù hợp với các thông số này. Tại sao không chọn A (Serverless inference): Chế độ Serverless có giới hạn payload rất thấp (tối đa 4 MB cho request body) và giới hạn thời gian xử lý (timeout) chỉ là 60 giây. Không thể xử lý file 100 MB hay chạy trong 60 phút. Tại sao không chọn C (Real-time inference): Chế độ Real-time được tối ưu cho độ trễ thấp (mili giây). Nó có giới hạn payload là 6 MB và timeout mặc định là 60 giây. Nếu gửi 100 MB vào Real-time endpoint, request sẽ bị từ chối ngay lập tức (413 Request Entity Too Large). Tại sao không chọn D (Batch transform): Mặc dù Batch Transform xử lý được dữ liệu lớn, nhưng đề bài yêu cầu triển khai trên một SageMaker Endpoint ("deploy... on an Amazon SageMaker endpoint"). Batch Transform không sử dụng endpoint thường trực mà là chạy các jobs xử lý hàng loạt offline (khởi tạo, xử lý, rồi tắt). Chỉ có Real-time, Serverless, và Asynchronous mới là các lại hình triển khai Endpoint.

---

## Question 37

An ML engineer notices class imbalance in an image classification training job. What should the ML engineer do to resolve this issue?

- **A.** Reduce the size of the dataset.
- **B.** Transform some of the images in the dataset.
- **C.** Apply random oversampling on the dataset.
- **D.** Apply random data splitting on the dataset.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Random oversampling): Đây là kỹ thuật kinh điển để xử lý vấn đề mất cân bằng dữ liệu (Class Imbalance). Random Oversampling hoạt động bằng cách nhân bản ngẫu nhiên các mẫu dữ liệu thuộc lớp thiểu số (minority class) cho đến khi số lượng của nó cân bằng với lớp đa số (majority class). Điều này giúp mô hình học được các đặc trưng của lớp thiểu số tốt hơn thay vì bị thiên vị về phía lớp đa số. Tại sao không chọn A (Reduce the size): Việc giảm kích thước tập dữ liệu một cách chung chung (không nói rõ là giảm lớp đa số - Undersampling) sẽ làm mất mát thông tin quan trọng và có thể dẫn đến việc mô hình hoạt động kém (underfitting) mà không nhất thiết giải quyết được tỷ lệ mất cân bằng. Tại sao không chọn B (Transform images): "Transform" ám chỉ kỹ thuật Data Augmentation (xoay, cắt, lật ảnh). Mặc dù Augmentation thường được dùng kết hợp với Oversampling để tạo ra các biến thể mới cho lớp thiểu số (tránh overfitting), nhưng bản thân hành động "biến đổi một số ảnh" không trực tiếp giải quyết vấn đề về số lượng/tỷ lệ chênh lệch giữa các lớp nếu không được thực hiện với mục đích tăng số lượng mẫu thiểu số cụ thể. Option C là định nghĩa trực tiếp của giải pháp. Tại sao không chọn D (Random data splitting): Đây là bước chia dữ liệu thành các tập Train/Validation/Test. Việc chia ngẫu nhiên (Random splitting) thậm chí còn có thể làm vấn đề tồi tệ hơn nếu lớp thiểu số quá ít và không xuất hiện trong tập Validation/Test. Để xử lý imbalance khi chia dữ liệu, người ta dùng Stratified Splitting (chia theo tỷ lệ tầng), nhưng nó chỉ đảm bảo phân phối đều giữa các tập con chứ không sửa lỗi mất cân bằng trong chính dữ liệu training.

---

## Question 38

A company receives daily .csv files about customer interactions with its ML model. The company stores the files in Amazon S3 and uses the files to retrain the model. An ML engineer needs to implement a solution to mask credit card numbers in the files before the model is retrained. Which solution will meet this requirement with the LEAST development effort?

- **A.** Create a discovery job in Amazon Macie. Configure the job to find and mask sensitive data.
- **B.** Create Apache Spark code to run on an AWS Glue job. Use the Sensitive Data Detection functionality in AWS Glue to find and mask sensitive data.
- **C.** Create Apache Spark code to run on an AWS Glue job. Program the code to perform a regex operation to find and mask sensitive data.
- **D.** Create Apache Spark code to run on an Amazon EC2 instance. Program the code to perform an operation to find and mask sensitive data.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (AWS Glue Sensitive Data Detection): AWS Glue là dịch vụ ETL (Trích xuất, Chuyển đổi, Tải) không máy chủ (Serverless). Tính năng "Sensitive Data Detection" được tích hợp sẵn trong Glue cho phép tự động nhận diện các loại dữ liệu nhạy cảm (PII) như số thẻ tín dụng và thực hiện hành động thay thế (masking/redaction) ngay trong luồng xử lý dữ liệu. Vì đây là tính năng có sẵn (built- in transform), bạn chỉ cần cấu hình mà không cần viết code xử lý phức tạp, đáp ứng hoàn hảo yêu cầu "LEAST development effort" (ít nỗ lực phát triển nhất). Tại sao không chọn A (Amazon Macie): Amazon Macie là dịch vụ bảo mật và khám phá dữ liệu (Discovery & Classification). Macie quét S3 để phát hiện và báo cáo dữ liệu nhạy cảm, nhưng nó KHÔNG phải là công cụ ETL để thực hiện hành động biến đổi (masking/redacting) dữ liệu trực tiếp trong file để phục vụ quy trình training tiếp theo. Tại sao không chọn C (AWS Glue + Custom Regex): Mặc dù vẫn dùng AWS Glue, nhưng việc phải tự viết code Apache Spark và duy trì các biểu thức chính quy (Regex) để khớp đúng định dạng thẻ tín dụng đòi hỏi nỗ lực phát triển và kiểm thử cao hơn nhiều so với việc dùng tính năng có sẵn (Option B). Ngoài ra, Regex tự viết dễ bị sai sót (false negatives) so với thư viện chuẩn của AWS. Tại sao không chọn D (EC2 + Custom Spark): Đây là giải pháp "tự quản lý" (Self- managed). Bạn phải tự cài đặt Spark, quản lý hạ tầng EC2 (patching, scaling) và tự viết code xử lý. Đây là phương án tốn kém nỗ lực phát triển và vận hành nhất (High operational overhead).

---

## Question 39

A medical company is using AWS to build a tool to recommend treatments for patients. The company has obtained health records and self-reported textual information in English from patients. The company needs to use this information to gain insight about the patients. Which solution will meet this requirement with the LEAST development effort?

- **A.** Use Amazon SageMaker to build a recurrent neural network (RNN) to summarize the data.
- **B.** Use Amazon Comprehend Medical to summarize the data.
- **C.** Use Amazon Kendra to create a quick-search tool to query the data.
- **D.** Use the Amazon SageMaker Sequence-to-Sequence (seq2seq) algorithm to create a text summary from the data.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Amazon Comprehend Medical): Đây là dịch vụ AI chuyên dụng (purpose-built) dành cho lĩnh vực y tế (Healthcare). Nó có khả năng tự động trích xuất thông tin y khoa quan trọng (như tên thuốc, bệnh lý, liều lượng, quy trình điều trị) từ văn bản phi cấu trúc (ghi chú bệnh án) mà không cần train model. Vì đề bài yêu cầu "gain insight" từ hồ sơ sức khỏe với "LEAST development effort" (ít nỗ lực phát triển nhất), việc gọi một API có sẵn chuyên cho y tế là tối ưu nhất. Tại sao không chọn A (RNN with SageMaker): Việc xây dựng một mạng nơ-ron hồi quy (RNN) từ đầu đòi hỏi chuyên môn sâu về Data Science, chuẩn bị dữ liệu lớn, training, tuning và deployment. Đây là phương án tốn nhiều công sức nhất (High effort). Tại sao không chọn C (Amazon Kendra): Amazon Kendra là dịch vụ tìm kiếm doanh nghiệp (Enterprise Search), giúp tìm tài liệu dựa trên câu hỏi. Mặc dù nó hỗ trợ tìm kiếm, nhưng nhiệm vụ chính ở đây là "gain insight" (phân tích/hiểu sâu) nội dung y tế (trích xuất thực thể, mối quan hệ) chứ không phải chỉ là tìm ra file tài liệu nào chứa từ khóa. Tại sao không chọn D (Seq2seq algorithm): Tương tự như Option A, Seq2seq (Sequence-to-Sequence) là thuật toán tóm tắt văn bản chung chung. Bạn phải tự xử lý dữ liệu, train model và fine-tune để nó hiểu ngữ cảnh y khoa. Effort cao hơn rất nhiều so với dùng dịch vụ Managed AI như Comprehend Medical.

---

## Question 40

A company needs to extract entities from a PDF document to build a classifier model. Which solution will extract and store the entities in the LEAST amount of time?

- **A.** Use Amazon Comprehend to extract the entities. Store the output in Amazon S3.
- **B.** Use an open source AI optical character recognition (OCR) tool on Amazon SageMaker to extract the entities. Store the output in Amazon S3.
- **C.** Use Amazon Textract to extract the entities. Use Amazon Comprehend to convert the entities to text. Store the output in Amazon S3.
- **D.** Use Amazon Textract integrated with Amazon Augmented AI (Amazon A2I) to extract the entities. Store the output in Amazon S3.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Amazon Comprehend direct processing): Amazon Comprehend hiện đã hỗ trợ tính năng Intelligent Document Processing (IDP), cho phép xử lý trực tiếp các file PDF, Word và hình ảnh. Bạn không cần phải trích xuất văn bản (OCR) thủ công trước. Chỉ cần gọi API của Comprehend với input là file PDF, dịch vụ sẽ tự động thực hiện OCR (ngầm định) và trích xuất thực thể (Entities) trong một bước duy nhất. Đây là giải pháp tối ưu nhất về thời gian triển khai và độ phức tạp kiến trúc. Tại sao không chọn C (Textract + Comprehend): Mặc dù đây là một pattern hợp lệ (dùng Textract để OCR rồi đưa text vào Comprehend), nhưng nó yêu cầu bạn phải quản lý hai dịch vụ riêng biệt và viết code để nối (glue code) output của Textract vào input của Comprehend. Điều này tốn nhiều thời gian thiết lập hơn so với tính năng native của Option A. Ngoài ra, mô tả "Comprehend to convert the entities to text" trong đáp án này bị sai về mặt kỹ thuật (Comprehend nhận Text và trả về Entities, không phải ngược lại). Tại sao không chọn B (Open source OCR on SageMaker): Việc tự triển khai và quản lý một tool OCR mã nguồn mở trên SageMaker đòi hỏi nhiều công sức cài đặt, cấu hình môi trường và vận hành (Self-managed). Nó không thể nhanh và đơn giản bằng việc sử dụng dịch vụ Managed Service có sẵn. Tại sao không chọn D (Textract + A2I): Amazon A2I (Augmented AI) được dùng để thêm quy trình con người rà soát (Human Loop) vào workflow. Việc thêm con người vào quy trình sẽ làm tăng đáng kể thời gian xử lý, trái ngược hoàn toàn với yêu cầu "Least amount of time".

---

## Question 41

An ML engineer needs to merge and transform data from two sources to retrain an existing ML model. One data source consists of .csv files that are stored in an Amazon S3 bucket. Each .csv file consists of millions of records. The other data source is an Amazon Aurora DB cluster. The result of the merge process must be written to a second S3 bucket. The ML engineer needs to perform this merge-and-transform task every week. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Create a transient Amazon EMR cluster every week. Use the cluster to run an Apache Spark job to merge and transform the data.
- **B.** Create a weekly AWS Glue job that uses the Apache Spark engine. Use DynamicFrame native operations to merge and transform the data.
- **C.** Create an AWS Lambda function that runs Apache Spark code every week to merge and transform the data. Configure the Lambda function to connect to the initial S3 bucket and the DB cluster.
- **D.** Create an AWS Batch job that runs Apache Spark code on Amazon EC2 instances every week. Configure the Spark code to save the data from the EC2 instances to the second S3 bucket.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (AWS Glue): AWS Glue là dịch vụ ETL (Extract, Transform, Load) được quản lý hoàn toàn (Serverless). Nó được thiết kế chuyên biệt để xử lý khối lượng dữ liệu lớn (millions of records) với engine Apache Spark mà không cần bạn phải quản lý hạ tầng máy chủ. o Native Integrations: Glue có sẵn kết nối (Connectors) tới S3 và Amazon Aurora (JDBC), giúp việc đọc/ghi dữ liệu từ hai nguồn này cực kỳ đơn giản. o DynamicFrame: Là cấu trúc dữ liệu tối ưu riêng của Glue, giúp xử lý dữ liệu hỗn hợp và biến đổi schema linh hoạt hơn DataFrame chuẩn của Spark. o Operational Overhead: Vì là serverless, bạn chỉ cần viết script và đặt lịch (schedule), AWS lo toàn bộ việc cấp phát tài nguyên, scaling và patching. Đây là lựa chọn có gánh nặng vận hành thấp nhất. Tại sao không chọn A (Amazon EMR): Mặc dù EMR chạy tốt Spark, nhưng bạn vẫn phải cấu hình cụm (cluster configuration), chọn loại instance, quản lý bootstrap actions và phiên bản phần mềm. Dù là cụm tạm thời (transient), công sức thiết lập và quản lý (manage infrastructure) vẫn cao hơn nhiều so với Glue. Tại sao không chọn C (AWS Lambda): AWS Lambda có giới hạn thời gian chạy tối đa là 15 phút và giới hạn về bộ nhớ/lưu trữ tạm (ephemeral storage). Với đầu vào là "millions of records", việc xử lý dữ liệu và chạy Spark (vốn rất nặng) trên Lambda là không khả thi và rất dễ bị timeout hoặc lỗi out-of-memory. Tại sao không chọn D (AWS Batch): AWS Batch yêu cầu bạn phải đóng gói code vào Docker container, thiết lập môi trường tính toán (Compute Environments) và hàng đợi (Job Queues). Bạn phải quản lý định nghĩa công việc (Job Definitions) và đôi khi cả cấu hình EC2 bên dưới. Mức độ vận hành cao hơn hẳn so với Glue.

---

## Question 42

An ML engineer has deployed an Amazon SageMaker model to a serverless endpoint in production. The model is invoked by the InvokeEndpoint API operation. The model's latency in production is higher than the baseline latency in the test environment. The ML engineer thinks that the increase in latency is because of model startup time. What should the ML engineer do to confirm or deny this hypothesis?

- **A.** Schedule a SageMaker Model Monitor job. Observe metrics about model quality.
- **B.** Schedule a SageMaker Model Monitor job with Amazon CloudWatch metrics enabled.
- **C.** Enable Amazon CloudWatch metrics. Observe the ModelSetupTime metric in the SageMaker namespace.
- **D.** Enable Amazon CloudWatch metrics. Observe the ModelLoadingWaitTime metric in the SageMaker namespace.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (ModelSetupTime): o Đối với SageMaker Serverless Inference, metric ModelSetupTime được thiết kế đặc biệt để đo thời gian "Cold Start" (khởi động nguội). o Khoảng thời gian này bao gồm việc AWS cấp phát tài nguyên tính toán (compute resources), tải model artifact từ S3, và khởi động container. o Khi latency tăng cao đột ngột trong môi trường production (nơi traffic có thể không đều đặn gây ra cold start), việc quan sát ModelSetupTime sẽ xác nhận trực tiếp giả thuyết "model startup time" có phải là nguyên nhân hay không. Tại sao không chọn D (ModelLoadingWaitTime): o Metric ModelLoadingWaitTime là metric dành riêng cho Multi-Model Endpoints (MME) chạy trên các instance thông thường (Provisioned instances). Nó đo thời gian một request phải chờ để model được tải vào bộ nhớ khi model đó chưa có sẵn trên instance. o Mặc dù Serverless Inference cũng có cơ chế tải model tương tự, nhưng metric chính thức được AWS công bố cho Serverless Endpoint để đo toàn bộ quá trình khởi tạo là ModelSetupTime. Tại sao không chọn A (Model Monitor - Model Quality): o SageMaker Model Monitor dùng để giám sát chất lượng mô hình (Model Quality) hoặc trôi dạt dữ liệu (Data Drift) về mặt thống kê và toán học. Nó không dùng để đo lường các chỉ số hiệu năng hệ thống (latency, CPU, memory). Tại sao không chọn B (Model Monitor + CloudWatch): o Tương tự như A, việc bật Model Monitor không giải quyết vấn đề debug về latency hạ tầng. CloudWatch metrics (như ở đáp án C) đã có sẵn cho Endpoint mà không cần cấu hình thêm job Model Monitor phức tạp.

---

## Question 43

An ML engineer needs to ensure that a dataset complies with regulations for personally identifiable information (PII). The ML engineer will use the data to train an ML model on Amazon SageMaker instances. SageMaker must not use any of the PII. Which solution will meet these requirements in the MOST operationally efficient way?

- **A.** Use the Amazon Comprehend DetectPiiEntities API call to redact the PII from the data. Store the data in an Amazon S3 bucket. Access the S3 bucket from the SageMaker instances for model training.
- **B.** Use the Amazon Comprehend DetectPiiEntities API call to redact the PII from the data. Store the data in an Amazon Elastic File System (Amazon EFS) file system. Mount the EFS file system to the SageMaker instances for model training.
- **C.** Use AWS Glue DataBrew to cleanse the dataset of PII. Store the data in an Amazon Elastic File System (Amazon EFS) file system. Mount the EFS file system to the SageMaker instances for model training.
- **D.** Use Amazon Macie for automatic discovery of PII in the data. Remove the PII. Store the data in an Amazon S3 bucket. Mount the S3 bucket to the SageMaker instances for model training.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Comprehend + S3): o Amazon Comprehend DetectPiiEntities: Là dịch vụ chuyên biệt sử dụng NLP để phát hiện và xác định vị trí các thực thể PII (tên, địa chỉ, số thẻ...) trong văn bản. Nó cung cấp thông tin chính xác để thực hiện việc che giấu (redaction) dữ liệu trước khi training. o Amazon S3: Là chuẩn lưu trữ (de facto standard) cho dữ liệu training của SageMaker. S3 tích hợp natively với SageMaker (qua File Mode hoặc Pipe Mode), rẻ hơn EFS và dễ dàng quản lý vòng đời dữ liệu. o Operational Efficiency: Việc kết hợp khả năng phát hiện mạnh mẽ của Comprehend và lưu trữ chuẩn S3 mang lại quy trình mượt mà và ít tốn công vận hành nhất so với việc phải quản lý mount điểm EFS hay dùng Macie (chỉ discovery). Tại sao không chọn B (Comprehend + EFS): o Mặc dù phần xử lý PII giống A, nhưng việc sử dụng Amazon EFS làm kho lưu trữ chính cho training data thường phức tạp hơn S3. EFS cần cấu hình VPC, Mount Targets, và gắn (mount) vào instance. Trừ khi cần chia sẻ file hệ thống trực tiếp hoặc huấn luyện phân tán đặc thù, S3 luôn là lựa chọn mặc định và hiệu quả hơn cho SageMaker. Tại sao không chọn C (Glue DataBrew + EFS): o Glue DataBrew là công cụ trực quan để làm sạch dữ liệu, có thể xử lý PII. Tuy nhiên, việc kết hợp với EFS lại làm giảm tính hiệu quả vận hành (như lý do ở B). Ngoài ra, đối với dữ liệu văn bản phi cấu trúc cần NLP để nhận diện ngữ cảnh PII, Comprehend thường vượt trội hơn các quy tắc transformation cố định của DataBrew. Tại sao không chọn D (Macie + S3): o Amazon Macie chủ yếu là công cụ bảo mật và tuân thủ (Security & Compliance) dùng để quét và báo cáo dữ liệu nhạy cảm đang nằm yên trong S3. Nó không phải là công cụ tiền xử lý (preprocessing tool) để redact (xóa/che) dữ liệu và tạo ra dataset sạch mới cho training pipeline một cách trực tiếp như Comprehend. Macie thiên về "phát hiện rủi ro" hơn là "chuẩn bị dữ liệu".

---

## Question 44

A company must install a custom script on any newly created Amazon SageMaker notebook instances. Which solution will meet this requirement with the LEAST operational overhead?

- **A.** Create a lifecycle configuration script to install the custom script when a new SageMaker notebook is created. Attach the lifecycle configuration to every new SageMaker notebook as part of the creation steps.
- **B.** Create a custom Amazon Elastic Container Registry (Amazon ECR) image that contains the custom script. Push the ECR image to a Docker registry. Attach the Docker image to a SageMaker Studio domain. Select the kernel to run as part of the SageMaker notebook.
- **C.** Create a custom package index repository. Use AWS CodeArtifact to manage the installation of the custom script. Set up AWS PrivateLink endpoints to connect CodeArtifact to the SageMaker instance. Install the script.
- **D.** Store the custom script in Amazon S3. Create an AWS Lambda function to install the custom script on new SageMaker notebooks. Configure Amazon EventBridge to invoke the Lambda function when a new SageMaker notebook is initialized.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Lifecycle configuration): Đây là tính năng nguyên bản (native) của Amazon SageMaker Notebook Instances, được thiết kế chuyên biệt để tự động hóa việc chạy các script tùy chỉnh (shell scripts) tại hai thời điểm: khi tạo mới (OnCreate) hoặc khi khởi động lại (OnStart). Bạn chỉ cần upload script một lần và chọn nó khi tạo notebook. Đây là giải pháp đơn giản nhất, không cần quản lý thêm hạ tầng hay dịch vụ bên ngoài, đáp ứng hoàn hảo tiêu chí "LEAST operational overhead". Tại sao không chọn B (Custom ECR image): Việc tạo và duy trì một Docker Image tùy chỉnh (build, push lên ECR, versioning) chỉ để chạy một script cài đặt là quá phức tạp và tốn công sức (Overkill). Giải pháp này thường dùng khi bạn cần thay đổi sâu vào môi trường (OS, drivers) hoặc dùng cho SageMaker Studio/Training Jobs, không phải là cách tối ưu cho việc cài script đơn giản trên Notebook Instance. Tại sao không chọn C (AWS CodeArtifact): CodeArtifact là dịch vụ quản lý gói phụ thuộc (artifact/package repository như PyPI, Maven private). Nó dùng để lưu trữ thư viện, không phải là công cụ để thực thi script cấu hình hệ thống (bootstrapping) khi khởi tạo máy ảo. Tại sao không chọn D (Lambda + EventBridge): Đây là giải pháp "tự chế" (custom orchestration). Bạn phải thiết lập EventBridge để bắt sự kiện tạo notebook, kích hoạt Lambda, và Lambda phải tìm cách kết nối vào Notebook (thường qua SSM) để chạy lệnh. Kiến trúc này quá phức tạp, dễ lỗi và khó bảo trì so với tính năng Lifecycle Config có sẵn.

---

## Question 45

A company is building a real-time data processing pipeline for an ecommerce application. The application generates a high volume of clickstream data that must be ingested, processed, and visualized in near real time. The company needs a solution that supports SQL for data processing and Jupyter notebooks for interactive analysis. Which solution will meet these requirements?

- **A.** Use Amazon Data Firehose to ingest the data. Create an AWS Lambda function to process the data. Store the processed data in Amazon S3. Use Amazon QuickSight to visualize the data.
- **B.** Use Amazon Kinesis Data Streams to ingest the data. Use Amazon Data Firehose to transform the data. Use Amazon Athena to process the data. Use Amazon QuickSight to visualize the data.
- **C.** Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to ingest the data. Use AWS Glue with PySpark to process the data. Store the processed data in Amazon S3. Use Amazon QuickSight to visualize the data.
- **D.** Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to ingest the data. Use Amazon Managed Service for Apache Flink to process the data. Use the built-in Flink dashboard to visualize the data.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Amazon MSK + Managed Flink): o Real-time & High Volume: Amazon MSK (Kafka) là tiêu chuẩn công nghiệp cho việc ingesting (nạp) lượng dữ liệu clickstream khổng lồ với độ trễ thấp. o SQL & Interactive Analysis: Amazon Managed Service for Apache Flink (trước đây là Kinesis Data Analytics) cung cấp tính năng "Studio". Tính năng này cho phép bạn chạy SQL queries trực tiếp trên luồng dữ liệu (streaming data) theo thời gian thực. o Notebooks: Flink Studio cung cấp giao diện Notebook (dựa trên Apache Zeppelin, nhưng thường được đánh đồng với trải nghiệm "interactive notebook" trong các bài thi) để Data Scientist/Engineer có thể viết code, chạy SQL và xem kết quả trực quan (visualize) ngay lập tức trên dòng dữ liệu đang chạy mà không cần chờ lưu xuống đĩa. Đây là giải pháp tối ưu nhất cho yêu cầu "Interactive analysis" trên dữ liệu Streaming. Tại sao không chọn A (Firehose + Lambda): AWS Lambda là dịch vụ tính toán dựa trên sự kiện (Event-driven compute), sử dụng code (Python, Node.js...) chứ không phải SQL native cho việc xử lý dữ liệu (mặc dù có thể viết code để chạy SQL, nhưng không phải là công cụ "Supports SQL" theo nghĩa của đề bài). Hơn nữa, Lambda không cung cấp giao diện "Jupyter notebooks" để phân tích tương tác. Tại sao không chọn B (Athena): Amazon Athena là công cụ truy vấn tương tác cho dữ liệu đã lưu trữ (Data at Rest) trên S3. Nó không phải là công cụ xử lý luồng thời gian thực (Real-time Stream Processing). Độ trễ từ lúc dữ liệu vào Kinesis -> Firehose -> S3 -> Athena query là quá cao so với yêu cầu "Real-time processing". Tại sao không chọn C (Glue + PySpark): Mặc dù AWS Glue có hỗ trợ Streaming ETL và Jupyter Notebooks, nhưng Glue thường hoạt động theo cơ chế Micro-batch (của Spark Streaming) nên độ trễ thường cao hơn Flink (Native Streaming). Ngoài ra, Glue thường thiên về các job ETL (Trích xuất - Biến đổi - Tải) nặng nề hơn là việc "Interactive Analysis" (Phân tích tương tác) nhanh chóng trên luồng dữ liệu như Flink Studio.

---

## Question 46

A medical company needs to store clinical data. The data includes personally identifiable information (PII) and protected health information (PHI). An ML engineer needs to implement a solution to ensure that the PII and PHI are not used to train ML models. Which solution will meet these requirements?

- **A.** Store the clinical data in Amazon S3 buckets. Use AWS Glue DataBrew to mask the PII and PHI before the data is used for model training.
- **B.** Upload the clinical data to an Amazon Redshift database. Use built-in SQL stored procedures to automatically classify and mask the PII and PHI before the data is used for model training.
- **C.** Use Amazon Comprehend to detect and mask the PII before the data is used for model training. Use Amazon Comprehend Medical to detect and mask the PHI before the data is used for model training.
- **D.** Create an AWS Lambda function to encrypt the PII and PHI. Program the Lambda function to save the encrypted data to an Amazon S3 bucket for model training.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Comprehend + Comprehend Medical): o Đây là sự kết hợp của hai dịch vụ NLP (Xử lý ngôn ngữ tự nhiên) chuyên dụng nhất của AWS:  Amazon Comprehend: Giỏi việc phát hiện và làm ẩn các thông tin PII phổ thông (tên, địa chỉ, email).  Amazon Comprehend Medical: Được huấn luyện đặc biệt trên dữ liệu y tế để nhận diện chính xác PHI (Protected Health Information) như tên thuốc, bệnh lý, liều lượng, và mối liên hệ với bệnh nhân trong các văn bản lâm sàng (clinical text). o Việc sử dụng đúng công cụ chuyên ngành (Domain-specific) giúp đảm bảo độ chính xác cao nhất trong việc loại bỏ dữ liệu nhạy cảm mà không cần tự xây dựng model hay rule phức tạp. Tại sao không chọn A (AWS Glue DataBrew): Glue DataBrew là công cụ chuẩn bị dữ liệu trực quan, có thể nhận diện PII cơ bản dựa trên mẫu (pattern/regex). Tuy nhiên, nó thiếu khả năng hiểu ngữ cảnh y khoa sâu sắc như Comprehend Medical để phát hiện PHI trong các ghi chú lâm sàng phi cấu trúc. Tại sao không chọn B (Amazon Redshift): Amazon Redshift là kho dữ liệu (Data Warehouse) dùng để phân tích SQL. Nó không có khả năng NLP tích hợp sẵn để "đọc hiểu" văn bản và tự động phân loại/masking dữ liệu PHI/PII phức tạp. Việc viết thủ tục SQL (Stored Procedures) để làm việc này là không khả thi và kém hiệu quả. Tại sao không chọn D (Lambda + Encryption): o Thứ nhất, "Mã hóa" (Encryption) khác với "Làm ẩn/Che" (Masking/Redaction). Dữ liệu mã hóa thường không thể dùng để training (trừ khi giải mã), trong khi masking giữ lại cấu trúc câu để model có thể học ngữ cảnh. o Thứ hai, việc tự viết code Lambda để phát hiện PHI/PII là rủi ro cao và tốn kém thời gian (High operational overhead) so với việc gọi API có sẵn.

---

## Question 47

An ML engineer is developing a classification model. The ML engineer needs to use custom libraries in processing jobs, training jobs, and pipelines in Amazon SageMaker. Which solution will provide this functionality with the LEAST implementation effort?

- **A.** Manually install the libraries in the SageMaker containers.
- **B.** Build a custom Docker container that includes the required libraries. Host the container in Amazon Elastic Container Registry (Amazon ECR). Use the ECR image in the SageMaker jobs and pipelines.
- **C.** Create a SageMaker notebook instance to host the jobs. Create an AWS Lambda function to install the libraries on the notebook instance when the notebook instance starts. Configure the SageMaker jobs and pipelines to run on the notebook instance.
- **D.** Run code for the libraries externally on Amazon EC2 instances. Store the results in Amazon S3. Import the results into the SageMaker jobs and pipelines.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Custom Docker Container): Đây là phương pháp chuẩn (Best Practice) để quản lý các thư viện tùy chỉnh trong môi trường ML công nghiệp (ML Pipelines). o Tính nhất quán (Consistency): Bằng cách đóng gói thư viện vào Docker Image, bạn đảm bảo môi trường chạy Processing, Training và Pipeline là hoàn toàn giống nhau, tránh lỗi "works on my machine". o Hiệu năng: Thư viện được cài sẵn trong image, không tốn thời gian cài đặt lại mỗi khi job chạy (khác với việc pip install tại runtime). o Khả năng mở rộng: Dễ dàng chia sẻ và tái sử dụng image này qua ECR cho nhiều project khác nhau. Tại sao không chọn A (Manually install): "Cài đặt thủ công" (thường ám chỉ việc chạy lệnh pip install ngay trong code training hoặc script entrypoint) có nhiều nhược điểm: o Tăng thời gian khởi động job (Latency) vì phải tải và cài thư viện mỗi lần chạy. o Yêu cầu kết nối Internet (rủi ro bảo mật). o Dễ gặp lỗi version xung đột tại thời điểm chạy (Runtime errors). Tại sao không chọn C (Notebook Instance + Lambda): Đây là hiểu sai cơ bản về kiến trúc SageMaker. Các SageMaker Jobs (Training, Processing) chạy trên các cụm máy chủ tính toán (compute clusters) tạm thời, tách biệt hoàn toàn với Notebook Instance. Việc cài thư viện lên Notebook Instance không hề ảnh hưởng hay cung cấp thư viện cho môi trường chạy Job. Tại sao không chọn D (External EC2): Việc chạy code trên EC2 thủ công là đi ngược lại lợi ích của SageMaker (Managed Service). Bạn sẽ phải tự quản lý việc bật/tắt máy, scaling và chuyển dữ liệu, gây tốn kém công sức vận hành (High operational overhead) hơn rất nhiều.

---

## Question 48

An ML engineer is deploying a trained model to an Amazon SageMaker endpoint. The ML engineer needs to receive alerts when data quality issues occur in production. Which solution will meet this requirement?

- **A.** Configure an Amazon CloudWatch metric alarm and a corresponding action to send an Amazon Simple Notification Service (Amazon SNS) notification.
- **B.** Integrate the SageMaker endpoint with a SageMaker Clarify processing job. Configure an Amazon CloudWatch alarm to provide alerts.
- **C.** Configure a monitoring job in SageMaker Model Monitor. Integrate Model Monitor with Amazon CloudWatch to provide alerts.
- **D.** Configure a data flow in SageMaker Data Wrangler. Integrate Data Wrangler with Amazon CloudWatch to provide alerts.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Model Monitor): Đây là dịch vụ chuyên dụng để giám sát chất lượng dữ liệu (Data Quality) và sự trôi dạt (Data Drift/Concept Drift) cho các mô hình đã triển khai trên Production. o Cơ chế: Model Monitor tự động so sánh dữ liệu đầu vào thực tế (captured data) với một tập dữ liệu cơ sở (baseline statistics). Nếu phát hiện sự sai lệch (ví dụ: tỉ lệ null cao, sai kiểu dữ liệu, thay đổi phân phối), nó sẽ đẩy các metrics vi phạm lên Amazon CloudWatch. o Alerting: Từ CloudWatch, bạn có thể cấu hình Alarm để gửi thông báo (alerts) khi các metrics này vượt ngưỡng. Tại sao không chọn A (CloudWatch metric alarm only): CloudWatch Alarm cần một nguồn metrics đầu vào. Bản thân CloudWatch chỉ đo các chỉ số hạ tầng (CPU, Memory, Latency) chứ không thể tự "đọc" nội dung dữ liệu ML để biết chất lượng tốt hay xấu. Nó cần Model Monitor (Option C) làm bước trung gian để phân tích dữ liệu và gửi metrics. Tại sao không chọn B (SageMaker Clarify): SageMaker Clarify tập trung vào việc phát hiện thiên kiến (Bias) và giải thích mô hình (Explainability). Mặc dù Model Monitor có sử dụng Clarify ở backend cho tính năng Bias Drift, nhưng để giám sát chung về "Data Quality" (như schema validation, completeness), thuật ngữ chính xác và dịch vụ bao trùm nhất là Model Monitor. Tại sao không chọn D (SageMaker Data Wrangler): Data Wrangler là công cụ low- code để chuẩn bị và làm sạch dữ liệu (Data Prep) trước khi training. Nó không có chức năng giám sát (Monitoring) cho Endpoint đang chạy.

---

## Question 49

A company needs to use Amazon SageMaker to train a model on more than 300 GB of data. The training data is composed of files that are 200 MB in size. The data is stored in Amazon S3 Standard storage and feeds a dashboard tool. Which SageMaker training ingestion mechanism is the MOST cost-effective solution for this scenario?

- **A.** Amazon Elastic File System (Amazon EFS) file system
- **B.** Amazon FSx for Lustre file system
- **C.** Amazon S3 in fast file mode while using S3 Express One Zone
- **D.** Amazon S3 in fast file mode without using S3 Express One Zone

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (S3 Fast File Mode with S3 Standard): o Tối ưu chi phí: Dữ liệu hiện đang nằm trên S3 Standard (rẻ nhất cho lưu trữ nóng). Fast File Mode (FFM) cho phép container training truy cập dữ liệu trực tiếp dưới dạng file hệ thống (POSIX) mà không cần tải toàn bộ dữ liệu về ổ đĩa cục bộ (EBS) của instance. Điều này giúp loại bỏ thời gian chờ tải dữ liệu (startup time) và tiết kiệm chi phí dung lượng EBS. o Phù hợp với đặc thù file: Với kích thước file trung bình ~200 MB, FFM hoạt động rất hiệu quả (vì ít tốn chi phí overhead cho metadata requests so với hàng triệu file nhỏ). o Không tốn phí hạ tầng phụ: Không cần khởi tạo và trả tiền cho file system phụ trợ như FSx hay EFS. Tại sao không chọn A (Amazon EFS): Amazon EFS có chi phí lưu trữ cao hơn nhiều so với S3 Standard (khoảng gấp 10 lần). Ngoài ra, EFS thường được dùng khi cần chia sẻ trạng thái hoặc code giữa các instance, không phải là lựa chọn tối ưu về giá cho việc stream dữ liệu training tĩnh cỡ lớn (throughput cost cao). Tại sao không chọn B (Amazon FSx for Lustre): FSx for Lustre cung cấp hiệu năng cực cao (throughput lớn, latency thấp), giúp tăng tốc training. Tuy nhiên, nó yêu cầu bạn phải trả tiền cho một hệ thống file riêng biệt (dung lượng + throughput). Với yêu cầu "MOST cost-effective" (tiết kiệm nhất) và kích thước 300GB, chi phí tăng thêm của FSx thường không bù đắp được bằng việc giảm thời gian training so với giải pháp "free" là FFM. Tại sao không chọn C (S3 Express One Zone): S3 Express One Zone là lớp lưu trữ hiệu năng cao (single-AZ) với độ trễ cực thấp, nhưng giá lưu trữ của nó đắt hơn nhiều so với S3 Standard (khoảng gấp 7 lần). Việc di chuyển dữ liệu sang lớp này chỉ để training sẽ làm tăng đáng kể chi phí lưu trữ mà không cần thiết cho kịch bản này.

---

## Question 50

A company has an ML model that is deployed to an Amazon SageMaker endpoint for real- time inference. The company needs to deploy a new model. The company must compare the new model's performance to the currently deployed model's performance before shifting all traffic to the new model. Which solution will meet these requirements with the LEAST operational effort?

- **A.** Deploy the new model to a separate endpoint. Manually split traffic between the two endpoints.
- **B.** Deploy the new model to a separate endpoint. Use Amazon CloudFront to distribute traffic between the two endpoints.
- **C.** Deploy the new model as a shadow variant on the same endpoint as the current model. Route a portion of live traffic to the shadow model for evaluation.
- **D.** Use AWS Lambda functions with custom logic to route traffic between the current model and the new model.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Shadow Variant): o Shadow Deployment (Shadow Mode) là tính năng được SageMaker hỗ trợ sẵn, cho phép bạn triển khai mô hình mới (Shadow model) song song với mô hình hiện tại (Production model) trên cùng một Endpoint. o Nó sẽ tự động sao chép (mirror) traffic thực tế gửi tới Production model sang Shadow model để chạy thử nghiệm. Kết quả trả về cho user vẫn là của Production model, nhưng bạn sẽ thu thập được metrics (latency, error rate, prediction) của Shadow model để so sánh hiệu năng. o Đây là giải pháp có "LEAST operational effort" vì SageMaker lo toàn bộ việc điều phối traffic, logging và so sánh mà không ảnh hưởng đến người dùng cuối. Tại sao không chọn A (Separate endpoint + Manual split): Việc triển khai ra endpoint riêng và tự chia traffic thủ công (ở phía client/application code) đòi hỏi bạn phải sửa đổi code ứng dụng, quản lý logic cân bằng tải, và tự thu thập/so sánh metrics từ 2 endpoint khác nhau. Rủi ro và công sức vận hành cao hơn nhiều. Tại sao không chọn B (CloudFront): Amazon CloudFront là CDN (Content Delivery Network), thường dùng để phân phối nội dung tĩnh hoặc cache API. Mặc dù CloudFront Functions/Lambda@Edge có thể chia traffic, nhưng việc thiết lập nó để routing request tới 2 SageMaker Endpoints (vốn nằm trong VPC hoặc yêu cầu SigV4 signing phức tạp) là giải pháp rất cồng kềnh (High complexity) và không phải là pattern chuẩn cho ML Model A/B Testing. Tại sao không chọn D (Lambda routing): Tương tự như B, việc dựng một hàm Lambda đứng trước để làm "Router" đòi hỏi bạn phải viết code custom logic để chia traffic, xử lý retry, timeout và monitor. Đây là việc "reinventing the wheel" (phát minh lại bánh xe) khi SageMaker đã có sẵn tính năng này.

---

## Question 51

A company runs an ML model on Amazon SageMaker. The company uses an automatic process that makes API calls to create training jobs for the model. The company has new compliance rules that prohibit the collection of aggregated metadata from training jobs. Which solution will prevent SageMaker from collecting metadata from the training jobs?

- **A.** Opt out of metadata tracking for any training job that is submitted.
- **B.** Ensure that training jobs are running in a private subnet in a custom VPC.
- **C.** Encrypt the training data with an AWS Key Management Service (AWS KMS) customer managed key.
- **D.** Reconfigure the training jobs to use only AWS Nitro instances.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Opt out of metadata tracking): o AWS thu thập siêu dữ liệu (metadata) tổng hợp từ các dịch vụ AI/ML (như SageMaker) để cải thiện chất lượng dịch vụ. Để tuân thủ quy tắc "prohibit the collection of aggregated metadata", AWS cung cấp cơ chế Opt-out (thông qua AWS Organizations AI services opt-out policies). o Khi bạn chọn "Opt out", AWS sẽ ngừng lưu trữ hoặc sử dụng dữ liệu đào tạo và metadata của bạn cho mục đích cải thiện sản phẩm của họ. Đây là giải pháp trực tiếp nhất để đáp ứng yêu cầu về "compliance rules" liên quan đến việc thu thập metadata. Tại sao không chọn B (Private subnet): Chạy trong Private Subnet giúp cô lập kết nối mạng (Network Isolation) để job không truy cập Internet. Tuy nhiên, nó không ngăn cản SageMaker Control Plane (mặt phẳng quản lý của AWS) thu thập các metrics và metadata (như trạng thái job, thời gian chạy, lỗi) để báo cáo lại cho bạn trong Console hoặc CloudWatch. Tại sao không chọn C (KMS Encryption): Mã hóa dữ liệu (Encryption) bảo vệ tính bí mật của nội dung dữ liệu (Training Data), nhưng không che giấu metadata (như tên job, tham số hyperparameter, loại instance, thời gian chạy). AWS vẫn có thể nhìn thấy các thông tin này để quản lý tài nguyên. Tại sao không chọn D (Nitro instances): AWS Nitro Instances cung cấp sự cô lập phần cứng và bảo mật tốt hơn (Enclaves), nhưng chúng không có tính năng tự động chặn việc gửi metadata vận hành về cho AWS Control Plane.

---

## Question 52

Topic #: 1 Context: An ecommerce company is using Amazon SageMaker Clarify Foundation Model Evaluations (FMEval) to evaluate ML models. Task: Select the correct model evaluation task from the following list for each ecommerce use case. Each model evaluation task should be selected one time. Options: * Classification evaluation * Open-ended generation * Question answering * Text summarization Use Cases (Inputs): 1. Categorize customer reviews as positive, neutral, or negative sentiment. 2. Create concise product descriptions from complete manufacturer details. 3. Recommend products based on a user's browsing history. 4. Respond to specific customer queries about product features. Answer : Dưới đây là cặp ghép nối chính xác (Mapping): 1. Categorize customer reviews as positive, neutral, or negative sentiment. ➔ [Classification evaluation] 2. Create concise product descriptions from complete manufacturer details. ➔ [Text summarization] 3. Recommend products based on a user's browsing history. ➔ [Open-ended generation] 4. Respond to specific customer queries about product features. ➔ [Question answering] Explain: * Tại sao chọn Classification evaluation cho "Categorize customer reviews...": Yêu cầu ở đây là gán nhãn (labeling) cho văn bản vào các nhóm rời rạc đã định trước (Positive, Neutral, Negative). Trong thuật ngữ Machine Learning và NLP, việc xác định cảm xúc (Sentiment

!!! info "Matching"


??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn Classification evaluation cho "Categorize customer reviews...": Yêu cầu ở đây là gán nhãn (labeling) cho văn bản vào các nhóm rời rạc đã định trước (Positive, Neutral, Negative). Trong thuật ngữ Machine Learning và NLP, việc xác định cảm xúc (Sentiment Analysis) chính là bài toán Classification (Phân loại văn bản). FMEval đánh giá task này dựa trên độ chính xác của việc model gán đúng nhãn. Tại sao chọn Text summarization cho "Create concise product descriptions...": Từ khóa "concise" (ngắn gọn) và "from complete details" (từ chi tiết đầy đủ) mô tả chính xác quá trình tóm tắt văn bản. Task Text summarization đo lường khả năng của model trong việc chắt lọc thông tin quan trọng từ văn bản dài thành văn bản ngắn hơn mà vẫn giữ được ý nghĩa cốt lõi. Tại sao chọn Question answering cho "Respond to specific customer queries...": Hành động "Respond to queries" (Trả lời truy vấn) về tính năng sản phẩm là định nghĩa cơ bản của bài toán Question Answering (QA). Trong FMEval, task này đánh giá khả năng model trả lời chính xác câu hỏi dựa trên kiến thức đã học hoặc ngữ cảnh được cung cấp (RAG). Tại sao chọn Open-ended generation cho "Recommend products...": Đây là lựa chọn cuối cùng và cũng là task trừu tượng nhất. Trong ngữ cảnh của Foundation Models (GenAI), việc đưa ra gợi ý (recommendation) dựa trên lịch sử duyệt web thường được coi là một bài toán sinh văn bản tự do (text generation) dựa trên ngữ cảnh đầu vào (context). Không giống như classification (chọn 1 nhãn) hay QA (trả lời fact), việc gợi ý đòi hỏi model sáng tạo ra một danh sách hoặc đoạn văn bản thuyết phục người dùng, do đó nó phù hợp nhất với nhóm Open-ended generation.

---

## Question 53

A company wants to launch a new internal generative AI interface to answer user questions. The interface will be based on a popular open source large language model (LLM). Which combination of steps will deploy the interface with the LEAST operational overhead? (Choose two.)

- **A.** Use Amazon SageMaker JumpStart to deploy the LLM.
- **B.** Download the LLM as a .zip file. Deploy the LLM on a GPU-based Amazon EC2 instance.
- **C.** Create a frontend HTML interface that uses an Amazon API Gateway WebSocket API with AWS Lambda functions to handle the user interaction.
- **D.** Use Amazon QuickSight to create a UI to handle the user interaction.
- **E.** Use Amazon Lex to create a UI to handle the user interaction.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (SageMaker JumpStart): Để triển khai một mô hình mã nguồn mở (Open Source LLM) phổ biến với chi phí vận hành thấp nhất, SageMaker JumpStart là giải pháp tối ưu. Nó cung cấp một "Model Zoo" với các mô hình đã được đóng gói sẵn (như Llama, Falcon, Mistral). Bạn có thể triển khai chúng lên SageMaker Endpoint chỉ bằng vài cú click chuột (hoặc vài dòng code) mà không cần tự xây dựng Docker container hay lo lắng về việc tối ưu hóa model server. Tại sao chọn E (Amazon Lex): Để tạo giao diện tương tác người dùng (UI/Conversational Interface) với ít nỗ lực nhất, Amazon Lex là dịch vụ được quản lý hoàn toàn (fully managed) dành cho chatbot. Thay vì phải tự code và duy trì hệ thống WebSocket, API Gateway và Frontend (như Option C), Amazon Lex cung cấp sẵn khung sườn cho hội thoại, quản lý phiên (session management) và tích hợp dễ dàng với các kênh chat hoặc web client (thông qua Amazon Lex Web UI). Bạn chỉ cần cấu hình Lex để gọi Lambda, và Lambda sẽ gọi SageMaker Endpoint để lấy câu trả lời từ LLM. Tại sao không chọn B (EC2 manual deployment): Việc tự tải model và cài đặt trên EC2 yêu cầu bạn phải quản lý hệ điều hành, driver GPU (CUDA), bản vá bảo mật và tự xây dựng cơ chế auto-scaling. Đây là phương án có gánh nặng vận hành (Operational Overhead) cao nhất (Self-managed). Tại sao không chọn C (Custom Frontend + API Gateway + Lambda): Mặc dù đây là kiến trúc Serverless phổ biến, nhưng việc phải tự xây dựng (build) và duy trì mã nguồn cho Frontend HTML, cấu hình WebSocket API và logic Lambda để xử lý kết nối đòi hỏi nỗ lực phát triển và vận hành lớn hơn nhiều so với việc sử dụng dịch vụ Chatbot có sẵn như Lex. Tại sao không chọn D (Amazon QuickSight): Amazon QuickSight là công cụ Business Intelligence (BI) dùng để vẽ biểu đồ và phân tích dữ liệu. Mặc dù có tính năng Generative Q, nhưng nó không phải là nền tảng để host một giao diện chat tùy chỉnh cho một model LLM mã nguồn mở bất kỳ.

---

## Question 54

A company wants to build a real-time analytics application that uses streaming data from social media. An ML engineer must implement a solution that ingests and transforms 5 GB of data each minute. The solution also must load the data into a data store that supports fast queries for the real-time analytics. Which solution will meet these requirements?

- **A.** Use Amazon EventBridge to ingest the social media data. Use AWS Glue to transform the data. Store the transformed data in Amazon ElastiCache (Memcached).
- **B.** Use Amazon Simple Queue Service (Amazon SQS) to ingest the social media data. Use AWS Lambda to transform the data. Store the transformed data in Amazon S3.
- **C.** Use Amazon Simple Notification Service (Amazon SNS) to ingest the social media data. Use Amazon EMR to transform the data. Store the transformed data in Amazon RDS.
- **D.** Use Amazon Kinesis Data Streams to ingest the social media data. Use Amazon Managed Service for Apache Flink to transform the data. Store the transformed data in Amazon DynamoDB.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (Kinesis Data Streams + Managed Flink + DynamoDB): Đây là kiến trúc tiêu chuẩn (Standard Reference Architecture) cho các ứng dụng phân tích dữ liệu thời gian thực (Real-time Analytics) với lưu lượng lớn trên AWS. o Ingestion: Amazon Kinesis Data Streams được thiết kế chuyên biệt để xử lý dữ liệu streaming với thông lượng cao (high throughput). Với khối lượng 5 GB/phút (~85 MB/s), Kinesis có thể dễ dàng mở rộng bằng cách tăng số lượng Shard. o Transformation: Amazon Managed Service for Apache Flink là dịch vụ xử lý luồng (stream processing) có độ trễ cực thấp (sub-second latency), hỗ trợ stateful processing (xử lý có trạng thái) để thực hiện các phép biến đổi phức tạp trên cửa sổ thời gian (windowing). o Storage: Amazon DynamoDB là cơ sở dữ liệu NoSQL có khả năng chịu tải ghi cực lớn (high write throughput) và trả về kết quả truy vấn với độ trễ mili giây (millisecond latency), đáp ứng hoàn hảo yêu cầu "fast queries for real- time analytics". Tại sao không chọn A (EventBridge + Glue + ElastiCache): Amazon EventBridge là dịch vụ định tuyến sự kiện (Event Bus) cho kiến trúc hướng sự kiện, không phải là đường ống dẫn dữ liệu (Data Pipeline) cho khối lượng dữ liệu streaming lớn (5 GB/phút). Ngoài ra, ElastiCache (Memcached) là bộ nhớ đệm (caching) tạm thời, không phải là nơi lưu trữ bền vững chính (primary data store) cho ứng dụng analytics. Tại sao không chọn B (SQS + Lambda + S3): Amazon S3 là kho lưu trữ đối tượng (Object Storage), thường dùng cho Data Lake. Mặc dù S3 bền vững, nhưng độ trễ khi truy vấn dữ liệu từ S3 (ví dụ dùng Athena) thường tính bằng giây hoặc phút, không đáp ứng được yêu cầu "fast queries for real-time analytics" (thường cần ms). Ngoài ra, mô hình SQS + Lambda khó xử lý các bài toán phân tích luồng phức tạp (như sliding windows) so với Flink. Tại sao không chọn C (SNS + EMR + RDS): Amazon SNS là dịch vụ thông báo (Pub/Sub notifications), giới hạn kích thước payload (256KB) và không có khả năng lưu giữ/phát lại luồng dữ liệu (retentio...

---

## Question 55

A company stores training data as a .csv file in an Amazon S3 bucket. The company must encrypt the data and must control which applications have access to the encryption key. Which solution will meet these requirements?

- **A.** Create a new SSH access key. Use the AWS Encryption CLI with a reference to the new access key to encrypt the file.
- **B.** Create a new API key by using the Amazon API Gateway CreateApiKey API operation. Use the AWS CLI with a reference to the new API key to encrypt the file.
- **C.** Create a new IAM role. Attach a policy that allows the AWS Key Management Service (AWS KMS) GenerateDataKey action. Use the role to encrypt the file.
- **D.** Create a new AWS Key Management Service (AWS KMS) key. Use the AWS Encryption CLI with a reference to the new KMS key to encrypt the file.

??? success "Reveal Answer"
    **Correct Answer: D**

    Tại sao chọn D (AWS KMS + Encryption CLI): o AWS KMS (Key Management Service): Là dịch vụ chuyên biệt để tạo và quản lý các khóa mã hóa. Tính năng quan trọng nhất của KMS là Key Policy (Chính sách khóa), cho phép bạn định nghĩa chính xác "ai" (User, Role, Application) được phép sử dụng khóa này để mã hóa hoặc giải mã. Điều này đáp ứng trực tiếp yêu cầu "control which applications have access to the encryption key". o AWS Encryption CLI: Là công cụ dòng lệnh giúp mã hóa dữ liệu (Client-side encryption) một cách an toàn bằng cách tích hợp với KMS. Tại sao không chọn A (SSH access key): SSH Keys được dùng để xác thực quyền truy cập vào máy chủ (như EC2) qua giao thức SSH. Chúng không phải là khóa mật mã dùng để mã hóa dữ liệu (Data Encryption). Tại sao không chọn B (API Gateway API Key): API Keys trong API Gateway được dùng để định danh và kiểm soát hạn ngạch (throttling/quota) cho người gọi API. Chúng không có chức năng mã hóa dữ liệu. Tại sao không chọn C (IAM Role only): Mặc dù IAM Role giúp quản lý quyền truy cập, nhưng bản thân Role không phải là "Khóa mã hóa". Bạn cần phải tạo ra một khóa (Key) trong KMS trước, sau đó mới dùng IAM Role để cấp quyền sử dụng khóa đó. Việc chỉ tạo Role mà không có Key thì không thể thực hiện hành động mã hóa.

---

## Question 56

A company needs to perform feature engineering, aggregation, and data preparation. After the features are produced, the company must implement a solution on AWS to process and store the features. Which solution will meet these requirements?

- **A.** Use Amazon SageMaker Feature Processing to process and ingest the data. Use SageMaker Feature Store to manage and store the features.
- **B.** Use Amazon SageMaker Model Monitor to automatically ingest and transform the data. Create an Amazon S3 bucket to store the features in JSON format.
- **C.** Use Amazon Managed Service for Apache Flink to transform the data and to ingest the data directly into Amazon SageMaker Feature Store. Use Feature Store to manage and store the features.
- **D.** Use an Amazon SageMaker batch transform job to analyze, transform, and ingest the data. Create an Amazon DynamoDB table to store the features.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (SageMaker Feature Processing + Feature Store): o SageMaker Feature Store là kho lưu trữ trung tâm chuyên dụng (centralized repository) để lưu trữ, truy xuất và chia sẻ các đặc trưng (features) phục vụ cho ML. Nó hỗ trợ cả Online Store (độ trễ thấp cho inference) và Offline Store (cho training). o SageMaker Feature Processing là một khả năng tích hợp sẵn của Feature Store, cho phép bạn định nghĩa các quy trình chuyển đổi dữ liệu (thường sử dụng Apache Spark/PySpark) để thực hiện feature engineering và aggregation. Nó tự động tải (ingest) dữ liệu đã xử lý vào Feature Store. Đây là giải pháp trọn gói (end-to-end) chuẩn nhất trong hệ sinh thái SageMaker cho bài toán này. Tại sao không chọn B (Model Monitor + S3): o SageMaker Model Monitor được dùng để giám sát mô hình đã triển khai (deployed models) nhằm phát hiện data drift hoặc model drift. Nó không phải là công cụ ETL để thực hiện feature engineering hay aggregation cho dữ liệu thô ban đầu. o Lưu trữ JSON trên S3 thiếu các tính năng quản lý đặc trưng chuyên sâu (như time travel, feature serving low-latency) mà Feature Store cung cấp. Tại sao không chọn C (Managed Flink): o Mặc dù Amazon Managed Service for Apache Flink có thể xử lý dữ liệu streaming và đẩy vào Feature Store, nhưng nó thiên về xử lý luồng thời gian thực (Real-time Streaming). Đề bài đề cập đến quy trình "feature engineering, aggregation, and data preparation" một cách tổng quát (thường là batch processing). SageMaker Feature Processing được thiết kế chuyên biệt để gắn liền quy trình biến đổi này với Feature Store management, là đáp án chính xác hơn về mặt tính năng "native". Tại sao không chọn D (Batch Transform + DynamoDB): o SageMaker Batch Transform chủ yếu được dùng để chạy suy luận (inference) offline trên hàng loạt dữ liệu bằng một model đã train, không phải là công cụ chính để làm ETL/Feature Engineering. o Dùng DynamoDB trực tiếp đòi hỏi bạn tự xây dựng lại các tính năng quản lý feature (metadata, versioning) mà SageMaker Featu...

---

## Question 57

A company is developing a new online application to gather information from customers. An ML engineer has developed a new ML model that will determine a score for each customer. The model will use the score to determine which product to display to the customer. The ML engineer needs to minimize response-time latency for the model. How should the ML engineer deploy the application in Amazon SageMaker to meet these requirements?

- **A.** Configure batch transform.
- **B.** Configure a real-time inference endpoint.
- **C.** Configure a serverless inference endpoint.
- **D.** Configure an asynchronous inference endpoint.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Real-time inference endpoint): o Đây là tùy chọn triển khai SageMaker tối ưu nhất cho các ứng dụng yêu cầu độ trễ cực thấp (millisecond latency) và phản hồi tức thì (synchronous). o Trong kịch bản "online application", khi khách hàng đang chờ để xem sản phẩm nào được hiển thị, mô hình cần trả về kết quả ngay lập tức (sub- second). Real-time Endpoint duy trì các instance luôn chạy sẵn (persistent/warm instances), đảm bảo không có độ trễ khởi động (cold start), đáp ứng hoàn hảo yêu cầu "minimize response-time latency". Tại sao không chọn A (Batch transform): Batch Transform dùng để xử lý offline hàng loạt dữ liệu lớn (ví dụ: chạy dự đoán cho toàn bộ khách hàng vào ban đêm). Nó không hỗ trợ tương tác thời gian thực với người dùng đang online. Tại sao không chọn C (Serverless inference): Serverless Inference có thể gặp vấn đề "Cold Start" (thời gian khởi động nguội) nếu endpoint không được gọi trong một khoảng thời gian, gây ra độ trễ cao đột ngột cho request đầu tiên. Do đó, nó không phải là lựa chọn tốt nhất nếu mục tiêu tối thượng là "minimize response-time latency" một cách ổn định. Tại sao không chọn D (Asynchronous inference): Asynchronous Inference đưa request vào hàng đợi (queue) để xử lý sau. Nó phù hợp cho các tác vụ mất nhiều thời gian (vài phút) hoặc dữ liệu lớn, nhưng không phù hợp cho ứng dụng online cần hiển thị kết quả ngay lập tức cho người dùng.

---

## Question 58

A company is using Amazon EMR. The company has a large dataset in Amazon S3 that needs to be ingested into Amazon SageMaker Feature Store. The dataset contains historical data and real-time streaming data. The company must ensure that the Feature Store online store is updated with the most recent data as soon as the data becomes available. The company also must maintain a complete Feature Store offline store for batch processing. Which solution will meet these requirements?

- **A.** Use the PutRecord API in Feature Store Runtime to ingest all the data into the online store.
- **B.** Use the PutRecord API in Feature Store Runtime to ingest all the data into the offline store.
- **C.** Use the Feature Store Spark connector to ingest the data as Spark DataFrames with the online store and offline store enabled.
- **D.** Use the Feature Store Spark connector to ingest the data as Spark DataFrames with only the online store enabled.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (Spark connector + Both stores): o Amazon SageMaker Feature Store Spark Connector: Đây là công cụ được tối ưu hóa để làm việc với Amazon EMR và các job xử lý dữ liệu Spark. Nó cho phép nạp (ingest) khối lượng dữ liệu lớn từ Spark DataFrames vào Feature Store một cách hiệu quả mà không cần viết vòng lặp gọi API thủ công. o Requirements: Đề bài yêu cầu cập nhật "online store" ngay lập tức (real- time availability) VÀ duy trì "offline store" cho batch processing. Khi sử dụng Spark Connector và bật cờ (flag) cho cả hai store (OnlineStore=True, OfflineStore=True), Feature Store sẽ tự động đồng bộ dữ liệu vào cả hai nơi: Online (DynamoDB) cho độ trễ thấp và Offline (S3) cho lưu trữ lịch sử. Đây là giải pháp "một mũi tên trúng hai đích" chuẩn xác nhất cho ngữ cảnh EMR. Tại sao không chọn A (PutRecord API to Online): Dùng PutRecord API đơn lẻ trong vòng lặp (loop) để nạp một "large dataset" từ EMR là không hiệu quả về mặt hiệu năng (throughput thấp, latency cao do round-trip network). Ngoài ra, nếu chỉ ingest vào Online store mà không cấu hình tự động sync sang Offline store (hoặc không enable Offline store ngay từ đầu), bạn có thể mất dữ liệu lịch sử hoặc phải thực hiện thêm bước copy phức tạp. Tại sao không chọn B (PutRecord API to Offline): PutRecord không hỗ trợ ghi trực tiếp vào Offline store theo cách update real-time để phục vụ inference ngay lập tức. Offline Store thường có độ trễ (latency) khi dữ liệu xuất hiện trên S3 (do buffering). Hơn nữa, yêu cầu quan trọng là "online store is updated... as soon as available", việc ghi vào Offline store vi phạm điều này. Tại sao không chọn D (Spark connector + Only Online): Nếu chỉ bật Online store, bạn sẽ mất tính năng lưu trữ lịch sử (Historical data retention) trên S3 phục vụ cho training và batch processing sau này. Điều này vi phạm yêu cầu "maintain a complete Feature Store offline store".

---

## Question 59

An ML engineer needs to deploy four ML models in an Amazon SageMaker inference pipeline. The models were built with different frameworks. The ML engineer also needs to give clients the ability to use the invoke_endpoint call to perform inference for each model. Which solution will meet these requirements MOST cost-effectively?

- **A.** Create a SageMaker multi-model endpoint.
- **B.** Create a SageMaker multi-container endpoint.
- **C.** Create multiple SageMaker single-model endpoints.
- **D.** Run a SparkML job to generate multiple endpoints.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Multi-container endpoint): o Different Frameworks: Đề bài nêu rõ các mô hình được xây dựng bằng "different frameworks" (ví dụ: một cái là PyTorch, một cái là TensorFlow). Điều này đồng nghĩa với việc chúng cần các môi trường runtime và thư viện dependencies khác nhau, tức là cần các Container Image khác nhau. SageMaker Multi-Container Endpoint (MCE) cho phép bạn triển khai tối đa 15 container khác nhau trên cùng một Endpoint (và cùng một instance EC2). o Inference Pipeline: Tính năng MCE chính là nền tảng để xây dựng Serial Inference Pipeline (chuỗi xử lý tuần tự: Tiền xử lý -> Model A -> Hậu xử lý). o Cost-effective: Thay vì dựng 4 endpoint riêng biệt (tốn tiền cho 4 instance chạy liên tục), bạn gom cả 4 container này vào 1 endpoint duy nhất, chạy trên 1 instance (hoặc 1 cluster nhỏ), giúp tiết kiệm chi phí hạ tầng đáng kể. o Direct Invocation: Với Multi-Container Endpoint, khách hàng có thể invoke toàn bộ pipeline hoặc (tùy cấu hình) gọi trực tiếp đến một container cụ thể trong nhóm bằng cách sử dụng header TargetContainerHostname trong API invoke_endpoint. Tại sao không chọn A (Multi-model endpoint - MME): o MME được thiết kế để host hàng ngàn mô hình chia sẻ chung một Container (ví dụ: 1000 model XGBoost chạy trên 1 container XGBoost). o Vì các model trong đề bài dùng "different frameworks", chúng không thể dễ dàng chia sẻ chung một container (trừ khi dùng Triton Inference Server cấu hình phức tạp). MME không giải quyết vấn đề "khác biệt môi trường/framework" tốt bằng Multi-Container Endpoint. Tại sao không chọn C (Multiple single-model endpoints): o Đây là giải pháp tốn kém nhất. Bạn phải trả tiền cho ít nhất 4 instance chạy 24/7 (mỗi endpoint cần ít nhất 1 instance). So với việc gộp lại (Option B), chi phí sẽ cao gấp 4 lần. Tại sao không chọn D (SparkML job): o SparkML job dùng để xử lý dữ liệu (batch processing) hoặc training, không phải là cơ chế để tạo và hosting Real-time Inference Endpoint.

---

## Question 60

An ML engineer wants an Amazon SageMaker notebook to automatically stop running after 1 hour of idle time. How can the ML engineer accomplish this goal?

- **A.** Create a lifecycle configuration in SageMaker. Copy the auto-stop-idle script from GitHub to the Start Notebook section.
- **B.** Create a lifecycle configuration in SageMaker. Copy the auto-stop-idle script from GitHub to the Create Notebook section.
- **C.** Track the notebook's CPU metric by using Amazon CloudWatch Logs. Invoke an AWS Lambda function from CloudWatch Logs to shut down the notebook instance if CPU utilization becomes zero.
- **D.** Track the notebook's memory metric by using Amazon CloudWatch Logs. Invoke an AWS Lambda function from CloudWatch Logs to shut down the notebook instance if memory utilization becomes zero.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (Lifecycle config - Start Notebook): o Cơ chế hoạt động: Để tự động tắt Notebook khi không sử dụng (idle), AWS cung cấp một script mẫu (auto-stop-idle) chạy một tiến trình nền (cron job) để liên tục kiểm tra trạng thái của Jupyter Kernel. o Vị trí cấu hình: Tiến trình giám sát này cần được kích hoạt mỗi lần Notebook khởi động (kể cả sau khi Stop/Start lại). Do đó, script phải được đặt trong phần "Start Notebook" (On-Start) của Lifecycle Configuration. Tại sao không chọn B (Create Notebook section): Script trong phần "Create Notebook" (On-Create) chỉ chạy duy nhất một lần khi bạn tạo mới instance lần đầu tiên. Nếu bạn tắt (Stop) instance và bật lại vào ngày hôm sau, script giám sát sẽ không được chạy lại, dẫn đến tính năng tự động tắt bị vô hiệu hóa. Tại sao không chọn C (CloudWatch CPU metric): o Về mặt kỹ thuật, CPU Utilization của một instance đang chạy không bao giờ bằng 0 (do các tiến trình hệ điều hành nền). Việc đặt ngưỡng trigger dựa trên CPU thường không chính xác bằng việc kiểm tra trực tiếp trạng thái kết nối của Jupyter Kernel (như script ở đáp án A làm). o Triển khai giải pháp này phức tạp hơn nhiều (cần Lambda, Alarm, IAM) so với dùng Lifecycle Script có sẵn. Tại sao không chọn D (CloudWatch Memory metric): Tương tự như C, Memory Utilization không bao giờ về 0 khi máy đang chạy. Dùng RAM để xác định trạng thái "idle" là sai về mặt nguyên lý quản trị hệ thống.

---

## Question 61

A company wants to provide services to help other businesses label images. The company wants its labeling specialists to complete human labeling tasks on AWS. How should the company register the labeling specialists to receive tasks on AWS?

- **A.** Use AWS Data Exchange.
- **B.** Create and use an internal workforce in Amazon SageMaker Ground Truth.
- **C.** Create and use Amazon Mechanical Turk entities in an Amazon SageMaker human loop.
- **D.** Use the Amazon Mechanical Turk website.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Internal workforce): o Amazon SageMaker Ground Truth cung cấp 3 loại lực lượng lao động (workforce): . Public (Amazon Mechanical Turk): Cộng đồng ẩn danh toàn cầu. . Vendor: Các công ty cung cấp dịch vụ gán nhãn chuyên nghiệp (bên thứ 3). . Private (Internal): Nhân viên hoặc chuyên gia riêng của chính công ty bạn. o Đề bài nêu rõ công ty muốn sử dụng "its labeling specialists" (chuyên gia của chính họ) để thực hiện tác vụ. Do đó, việc tạo một Internal Workforce (Private Team) là giải pháp chính xác. Bạn có thể quản lý danh sách người dùng này thông qua Amazon Cognito hoặc OIDC IDP của riêng công ty. Tại sao không chọn A (AWS Data Exchange): Dịch vụ này dùng để tìm kiếm, đăng ký và trao đổi các bộ dữ liệu (datasets) từ bên thứ ba trên nền tảng AWS. Nó không có chức năng quản lý quy trình gán nhãn hay quản lý nhân sự gán nhãn. Tại sao không chọn C (Amazon Mechanical Turk entities): Đây là tùy chọn Public Workforce. Nếu chọn tùy chọn này, task của bạn sẽ được gửi cho cộng đồng Workers ẩn danh trên toàn thế giới (Crowdsourcing), không phải cho đội ngũ chuyên gia nội bộ của công ty. Tại sao không chọn D (Amazon Mechanical Turk website): Đây là trang web dành cho Requesters (người thuê) và Workers (người làm) của hệ thống Mechanical Turk công cộng. Nó không cung cấp giao diện để tích hợp và quản lý đội ngũ riêng (Private Team) trong quy trình training của SageMaker Ground Truth.

---

## Question 62

A company wants to use Amazon SageMaker to host an ML model that runs on CPU for real-time predictions. The model will have intermittent traffic during business hours and will have periods of no traffic after business hours. The company needs a solution that will serve inference requests in the most cost-effective manner. Which hosting option will meet these requirements?

- **A.** Deploy the model to a SageMaker real-time endpoint. Add a schedule-based auto scaling policy to handle traffic surges during business hours.
- **B.** Deploy the model to a SageMaker Serverless Inference endpoint. Configure increased provisioned concurrency during business hours.
- **C.** Deploy the model to a SageMaker Asynchronous Inference endpoint. Configure an auto scaling policy that scales in to zero outside business hours.
- **D.** Deploy the model to a SageMaker real-time endpoint. Create a scheduled AWS Lambda function that activates the endpoint during business hours only.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (Serverless Inference): o Cost-effective for Intermittent Traffic: SageMaker Serverless Inference là giải pháp lý tưởng cho các mô hình có lưu lượng truy cập không đều đặn (intermittent) hoặc có khoảng thời gian không hoạt động (idle). Bạn chỉ phải trả tiền cho thời gian tính toán (compute duration) khi có request xử lý và dung lượng bộ nhớ sử dụng. Khi không có traffic (sau giờ làm việc), chi phí là bằng 0 vì nó tự động scale về 0. o Provisioned Concurrency: Để đảm bảo độ trễ thấp (real-time) trong giờ cao điểm ("business hours"), bạn có thể cấu hình Provisioned Concurrency (Khả năng đồng thời được cung cấp trước) để giữ cho các hàm "ấm" (warm), tránh hiện tượng Cold Start. Đây là sự cân bằng tốt nhất giữa chi phí và hiệu năng. Tại sao không chọn A (Real-time endpoint): SageMaker Real-time Endpoint sử dụng các instance EC2 dành riêng (provisioned instances). Bạn phải trả tiền cho thời gian instance bật, bất kể có traffic hay không. Với lưu lượng "intermittent" (lúc có lúc không), bạn sẽ lãng phí tiền cho các khoảng thời gian instance chạy nhàn rỗi (idle time). Tại sao không chọn C (Asynchronous Inference): Async Inference được thiết kế cho các tác vụ xử lý lâu (long-running) hoặc payload lớn (lên đến 1GB), và mô hình hoạt động là không đồng bộ (trả về Job ID để poll kết quả sau). Nó không phù hợp với yêu cầu "real-time predictions" (phản hồi tức thì) như Serverless hoặc Real-time Endpoint. Tại sao không chọn D (Lambda activation): Việc dùng Lambda để "bật/tắt" endpoint thực chất là tạo và xóa endpoint hàng ngày. Quá trình tạo endpoint mới có thể mất vài phút đến hàng chục phút, gây gián đoạn dịch vụ vào đầu giờ làm việc. Ngoài ra, trong giờ làm việc, nếu dùng Real-time endpoint thì vẫn bị vấn đề chi phí cho thời gian nhàn rỗi như Option A.

---

## Question 63

An ML engineer needs to train a supervised deep learning model. The available dataset is a large number of unlabeled images that only employees should access. The ML engineer needs to implement a solution that labels the dataset with the highest possible accuracy. Which combination of steps should the ML engineer take to meet these requirements? (Choose two.)

- **A.** Use Amazon Rekognition to automatically label the dataset.
- **B.** Train the deep learning model directly on the raw data. Let the model infer the labels by itself.
- **C.** Use Amazon SageMaker Ground Truth to create an annotation job that specifies the labeling task and requirements.
- **D.** Set up workforce teams to access a private workforce to run and review the annotation job created by Amazon SageMaker Ground Truth.
- **E.** Use Amazon Mechanical Turk to complete the annotation job created by Amazon SageMaker Ground Truth.

??? success "Reveal Answer"
    **Correct Answer: C**

    Tại sao chọn C (SageMaker Ground Truth): o Để huấn luyện một mô hình học sâu có giám sát (supervised deep learning model), điều kiện tiên quyết là phải có dữ liệu được gán nhãn (labeled data). Dữ liệu hiện tại là "unlabeled images" (ảnh chưa gán nhãn). o Amazon SageMaker Ground Truth là dịch vụ chuyên biệt giúp xây dựng các bộ dữ liệu huấn luyện chính xác cao bằng cách kết hợp sức người (human labelers) và máy học (auto-labeling). Nó cung cấp giao diện và quy trình quản lý job gán nhãn một cách hệ thống. Tại sao chọn D (Private Workforce): o Yêu cầu bảo mật: Đề bài nêu rõ "dataset... only employees should access" (chỉ nhân viên mới được truy cập). Điều này loại bỏ hoàn toàn khả năng sử dụng lực lượng lao động công cộng (Public Workforce) như Amazon Mechanical Turk hay các nhà cung cấp bên thứ ba (Vendor Workforce). o Private Workforce cho phép bạn định nghĩa một nhóm người dùng cụ thể (nhân viên nội bộ) và cấp quyền truy cập an toàn cho họ để thực hiện task gán nhãn mà không để lộ dữ liệu ra bên ngoài. o Độ chính xác: Yêu cầu "highest possible accuracy" thường đạt được tốt nhất khi sử dụng chuyên gia nội bộ (Subject Matter Experts) hiểu rõ nghiệp vụ để gán nhãn và review thủ công (human-in-the-loop). Tại sao không chọn A (Amazon Rekognition): o Amazon Rekognition trả về các nhãn tổng quát (generic labels) dựa trên mô hình đã huấn luyện sẵn của AWS. Các nhãn này có thể không khớp với danh mục (classes) cụ thể mà bài toán của bạn yêu cầu. Ngoài ra, độ chính xác cho các dữ liệu đặc thù (domain-specific) sẽ không cao bằng việc con người gán nhãn trực tiếp. Tại sao không chọn B (Train on raw data): o Đề bài yêu cầu huấn luyện mô hình Supervised (Có giám sát). Định nghĩa của Supervised Learning là mô hình học từ các cặp (Input, Label). Việc dùng dữ liệu thô chưa gán nhãn (Raw data) để training trực tiếp thuộc về lĩnh vực Unsupervised Learning (Học không giám sát), sai với yêu cầu đề bài. Tại sao không chọn E (Mechanical Turk): o Sử dụng Amazon Mechanical Turk (Public crow...

---

## Question 64

A company is using an Amazon S3 bucket to collect data that will be used for ML workflows. The company needs to use AWS Glue DataBrew to clean and normalize the data. Which solution will meet these requirements?

- **A.** Create a DataBrew dataset by using the S3 path. Clean and normalize the data by using a DataBrew profile job.
- **B.** Create a DataBrew dataset by using the S3 path. Clean and normalize the data by using a DataBrew recipe job.
- **C.** Create a DataBrew dataset by using a Java Database Connectivity (JDBC) driver to connect to the S3 bucket. Clean and normalize the data by using a DataBrew profile job.
- **D.** Create a DataBrew dataset by using a Java Database Connectivity (JDBC) driver to connect to the S3 bucket. Clean and normalize the data by using a DataBrew recipe job.

??? success "Reveal Answer"
    **Correct Answer: B**

    Tại sao chọn B (S3 path + Recipe job): o DataBrew Dataset (S3 Path): AWS Glue DataBrew hỗ trợ kết nối trực tiếp (native) với Amazon S3. Bạn chỉ cần trỏ đến đường dẫn S3 (S3 path) để tạo Dataset mà không cần qua bất kỳ driver trung gian nào. o Recipe Job: Trong DataBrew, tập hợp các bước biến đổi dữ liệu (như làm sạch, chuẩn hóa, đổi tên cột, xử lý null...) được gọi là một "Recipe". Để áp dụng các bước này lên toàn bộ tập dữ liệu lớn và xuất kết quả ra, bạn phải chạy một Recipe Job. Đây chính xác là công cụ để thực hiện yêu cầu "clean and normalize the data". Tại sao không chọn A (Profile job): o DataBrew Profile Job dùng để chạy thống kê mô tả (descriptive statistics) về dữ liệu (như phân phối giá trị, độ tương quan, chất lượng dữ liệu). Nó chỉ tạo ra một bản báo cáo (Profile) về dữ liệu chứ không thực hiện việc biến đổi hay tạo ra dataset mới đã được làm sạch. Tại sao không chọn C và D (JDBC driver): o JDBC (Java Database Connectivity) là giao thức dùng để kết nối với các cơ sở dữ liệu quan hệ (như RDS, Redshift, SQL Server). Amazon S3 là dịch vụ lưu trữ đối tượng (Object Storage), không phải Database, nên không sử dụng JDBC driver để kết nối trong DataBrew. DataBrew kết nối S3 trực tiếp.

---

## Question 65

A company is developing a new ML model that uses the XGBoost algorithm. The company will train the model on data that is stored in an Amazon S3 bucket. The data is in a nested JSON format. An ML engineer needs to convert the JSON files into a tabular format. Which solution will meet this requirement with the LEAST operational overhead?

- **A.** Create an AWS Glue PySpark job that uses the Relationalize transform to convert the files.
- **B.** Write custom Scala code to convert the files. Use Amazon EMR Serverless to run the Scala code.
- **C.** Create an AWS Lambda function that uses a Python runtime and invokes the reduce() function to convert the files. Invoke the Lambda function.
- **D.** Create an Amazon Athena database that is based on the JSON files. Use the Athena flatten function to convert the data.

??? success "Reveal Answer"
    **Correct Answer: A**

    Tại sao chọn A (AWS Glue Relationalize): o AWS Glue là dịch vụ ETL serverless (không cần quản lý máy chủ), giúp giảm tối đa gánh nặng vận hành (Least operational overhead). o Relationalize Transform: Đây là một hàm chuyển đổi có sẵn và chuyên biệt trong thư viện AWS Glue. Nó được thiết kế để tự động làm phẳng (flatten) các cấu trúc dữ liệu lồng nhau phức tạp (nested JSON) thành dạng bảng (tabular/relational) gồm các cột và hàng. Bạn không cần phải viết code phức tạp để duyệt từng node trong JSON. o Đây là giải pháp "chuẩn sách giáo khoa" của AWS cho việc xử lý dữ liệu nested JSON trước khi đưa vào huấn luyện mô hình (như XGBoost yêu cầu dữ liệu bảng). Tại sao không chọn B (EMR Serverless + Custom Scala): o Mặc dù EMR Serverless giảm bớt việc quản lý server, nhưng việc phải viết code Scala tùy chỉnh để phân tích cú pháp và làm phẳng file JSON lồng nhau là một công việc tốn kém thời gian và công sức phát triển (High development overhead) so với việc gọi một hàm có sẵn trong Glue. Tại sao không chọn C (Lambda + Python reduce): o Sử dụng hàm reduce() để làm phẳng JSON thủ công là việc "phát minh lại bánh xe" (reinventing the wheel). Nó phức tạp, dễ lỗi và khó bảo trì. Ngoài ra, Lambda có giới hạn về thời gian chạy (15 phút) và bộ nhớ, có thể không xử lý tốt nếu file dữ liệu lớn. Tại sao không chọn D (Athena flatten): o Amazon Athena chủ yếu dùng để truy vấn (Query). Mặc dù SQL có thể hỗ trợ làm phẳng mảng (UNNEST/FLATTEN), nhưng việc định nghĩa schema cho JSON phức tạp và viết câu lệnh SQL để biến đổi toàn bộ dataset thành bảng phẳng thường rườm rà hơn so với Glue. Athena phù hợp để xem dữ liệu hơn là biến đổi và lưu trữ (ETL) cho training pipeline.

---

