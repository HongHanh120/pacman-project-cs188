# Project 5: Classification

### Question 1 (4 points): Perceptron
##### Mô tả cách làm
> Dựa vào công thức đã cho trên trang [ai.berkeley]http://ai.berkeley.edu/classification.html, thay đổi hàm **train** trong file **perceptron.py**.
##### Kết quả
> Accuracy: 79%
> Passed: 4/4 points

### Question 2 (1 points): Perceptron Analysis
##### Mô tả cách làm
> Thay đổi hàm **findHighWeightFeatures** trong file **perceptron.py** để tìm ra tất cả các đặc trưng, sắp xếp và trả về list 100 đặc trưng quan trọng nhất. Chạy và trả lời kết quả tương ứng với trường hợp A hay B vào file **answer.py**.
##### Kết quả
> Answer: return 'a'
> Passed: 1/1 points

### Question 3 (6 points): MIRA
##### Mô tả cách làm
> Thay đổi hàm **TrainAndTune** trong file **mira.py** để trả về trọng số lớn nhất. Ngoài hàm **train** ra, bổ sung thêm các hàm **getAccuracyCWeight**, **getTau**, **getAccuracy**. Trong trường hợp guess != correctLabels sẽ cập nhập lại trọng số với biến **tau** được tính theo công thức đã cho trong câu hỏi và biến **C** là một ngưỡng để giới hạn biến **tau**.
##### Kết quả
> Accuracy: 82%
> Passed: 6/6 points

### Question 4 (6 points): Digit Feature Design
##### Mô tả cách làm
> Thay đổi hàm **EnhancedFeatureExtractorDigit** trong file **dataClassifier.py** để tính số lượng region trong features. Đầu tiên tạo features theo chiều ngang(horizontal) và chiều dọc(vertical) gồm các số 0 và 1. Sau đó viết một hàm **getNeighbors** lấy ra các điểm lân cận xung quanh (x, )y. Tìm số lượng các vùng trong features(1, 2, 3) và biến đổi thành binary features. Cuối cùng trả về features.
##### Kết quả
> Accuracy: 84%
> Passed: 6/6 points

### Question 5 (4 points): Behavioral Cloning
##### Mô tả cách làm
> Ý tưởng làm câu này giống với ý tưởng làm question 1. Ta thay đổi hàm **train** trong file **perceptron_pacman.py**
##### Kết quả
> Accuracy: 84%
> Passed: 4/4 points

### Question 6 (4 points): Pacman Feature Design
##### Mô tả cách làm
> Thay đổi hàm **EnhancedPacmanFeatures** trong file **dataClassifier.py** bằng cách thiết kế ra các features cho Pacman. Các features đã thiết kế cho Pacman:
- Food: khoảng cách nhỏ nhất từ vị trí của Pacman đến thức ăn gần nhất.
- stop: nếu hành động của Pacman là dừng thì features['stop'] = 1 còn ngược lại nhận giá trị 0.
- foodCount: số lượng thức ăn còn lại hiện tại ở trong state.
- ghost: khoảng cách vị trí của Pacman đến vị trí con ma gần nhất.
##### Kết quả
> Accuracy
- The ContestAgent: 90%
- The other 3 provided agents: 84%
> Passed: 4/4 points