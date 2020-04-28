##### 1. cuda Tensor转numpy
```python
## one:
outputs = outputs.cpu().numpy()

## two:
outputs = outputs.to('cpu').numpy()
```

##### 2. 打印出网络结构和参数个数
###### 低级版本：summary（pip install summary）
```python
from torchsummary import summary

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)
    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
    

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

summary(model, (1, 28, 28)) （C, H, W）
print("parameters_count: {}".format(count_parameters(model)))
print(model)
```
###### 高级版本：summaryX（pip install summaryX）
```python

from torchsummaryX import summary

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)
    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


model = Net()
inputs = torch.zeros((1, 1, 28, 28))
summary(model,inputs)
print("parameters_count: {}".format(count_parameters(model)))
print(model)



class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
    # def __init__(self):
        super(LSTM,self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.LSTM_1 = nn.LSTM(input_size=input_size, hidden_size=self.hidden_size, num_layers=self.num_layers)
        self.fc = nn.Sequential(nn.Linear(self.hidden_size, 2), nn.Sigmoid())
    def initHidden(self, batchsize):
        self.hidden = [(autograd.Variable(torch.zeros(1, batchsize, hidden_dim)),
                        autograd.Variable(torch.zeros(1, batchsize, hidden_dim))) 
                        for hidden_dim in [32]]
    def forward(self, input):
        self.initHidden(input.size()[1])
        output_1, self.hidden[0] = self.LSTM_1(input, self.hidden[0])
        output = self.fc(output_1[-1])
        return output
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


model = LSTM(15, 32, 1)
inputs = torch.zeros((24, 32, 15))
summary(model,inputs)
print("parameters_count: {}".format(count_parameters(model)))
print(model)
```
#####  3. 保存、加载模型和打印网络结构和参数
###### 保存并加载模型：
```python
## 保存模型
## One：保存和加载 网络结构和权重参数
path = ./models/model.pkl
#  保存网络结构和权重参数
torch.save(model,  path)  
# 加载网络结构和权重参数
model = torch.load(path)

## Two：只保存权重参数
path = ./models/model.pkl
#  保存模型参数
torch.save(mode.state_dict(), './models/model.pkl')
# 加模型参数
model = net()
model.load_state_dict(torch.load(path))
```
###### 加载模型并打印结构和模型：
```python
print(model) # 打印网络结构

# 打印每层网络参数的形状
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())
    
# 打印每层网络的权重
for weight in model.named_parameters():
    print(weight)
```