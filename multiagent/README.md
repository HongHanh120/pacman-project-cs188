Câu 1
Hàm evaluationFunction là hàm đánh giá những nước đi của Pacman và trả về điểm số của trạng thái trò chơi. Hàm evaluationFuntion được tính dựa trên khoảng cách nhỏ nhất giữa food và Pacman, khoảng cách nhỏ nhất của con ma gần nhất với Pacman nhất, xét các vị trí lân cận con ma của Pacman  và điểm của trạng thái đó.

Câu 2
Đầu tiên trong hàm getAction, lấy ra số lượng con ma tại mỗi trạng thái của trò chơi và trả về hành động tốt nhất mà Pacman có thể đạt được dựa vào hàm maximize.
Sau đó viết một hàm maximize. Với hàm maximize này, trước tiên kiểm tra trạng thái của trò chơi nếu thua hay thắng thì trả về số điểm tại trạng thái đó. Nếu không tạo tất cả các hành động Pacman có thể đi và tìm maxValue của các hành động qua việc so sánh với tempValue là giá trị các hành động của con ma thông qua hàm minimize. Nếu depth > 1 thì trả về các giá trị maxValue, và không thì trả lại hành động tốt nhất mà Pacman có thể thực hiện.
Cuối cùng, viết một hàm minimize để tính giá trị minValue. Trước tiên cũng kiểm tra trạng thái của trò chơi nếu thua hay thắng thì trả về số điểm tại vị trí đó. Nếu không khởi tạo tất cả các hành động có thể đi của các con agent. So sánh giá trị minValue khi mà cây hiện tại đã quét đủ agent xung quanh mà độ sâu chưa đạt thì sử dụng hàm maximize để tạo độ sâu mới với những hành động tiếp theo của Pacman. Độ sâu đã đạt mức yêu cầu thì trả lại điểm lại vị trí. Nếu chưa quét đủ agent xung quanh thì tăng agentIndex + 1 và áp dụng đệ quy cho hàm minimize và tìm giá trị minValue.

Câu 3
Tương tự câu 2 nhưng mình sẽ khởi tạo thêm 2 biến alpha và beta. Tại mỗi hàm maximize nếu maxValue mỗi state lớn hơn beta thì chấm dứt và trả lại giá trị maxValue. Nếu không cập nhật alpha nếu maxValue lớn hơn alpha hiện tại.
Tương tự với hàm minimize thì nếu giá trị minValue nh hơn alpha thì trả lại giá trịỏ minValue đó nếu không cập nhật beta nếu giá trị minValue đó nhỏ hơn beta.

Câu 4
Tương tự câu 2 nhưng với hàm expectimax thì ta sẽ trả về trung bình điểm số của các trạng thái xung quanh các con agent.

Câu 5
Hàm bettervaluationFunction được tính dựa trên hàm tuyến tính
Điểm tại trạng thái hiện t + 1/khoảng cách giữa Pacman và food gần nhất - 1/khoảng cách giữa Pacman và con ma gần nhất - trạng thái hoạt động của Pacman khi ở lân cận con ma - số thức ăn khi Pacman ăn vào thì con ma sẽ bị vô hiệu hóa. Khi khoảng cách giữa Pacman và thức ăn càng nhỏ thì điểm càng cao và ngược lại. Tương tự khoảng cách nhỏ nhất giữa Pacman và con ma càng lớn thì số điểm càng cao.