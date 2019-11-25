# OpencvExample
OpencvExample for beginners with python  
URL:https://www.youtube.com/watch?v=3D7O_kZi8-o&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=14  

03：  
	利用摄像头读取画面，展示画面，获取画面的张宽，以及写画面。  
	摄像头读取画面是一针一针读取的，将这一帧一帧的画面放到一个循环中，连成视频。
	
	• 读取：cap=cv2.VedioCapture(0); 其中参数是可为摄像头编号，或者视频文件的路径    
	Ret,frame  =  Cap.read(),ret是布尔值，读取到返回ture， 读取到文件末尾返回False，frame是一帧图像。  
	• 写入：writer = cv.VideoWrite（path, fourcc, fps, (H, W)），fourcc是视频的格式，长用的fourcc=cv2.VideoWriter_fourcc(*'XVID')
	Writer.write(frame) 执行视频写入的操作  
	• 长宽，cap.get(cv2.CAP_PROP_FRAME_WIDTH) 返回视频的宽度  
	• 视频默认读取的是彩色信息，即三通到BGR，可以通过gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)将彩色转换为灰白。  
	• Cv2.waitkey(1):延迟1s进入下一帧 ，对于视频而言 0 表示暂停  
	• 0xFF==ord（‘q’） 用于获取从键盘输入字符的ASCLL码  
	• Cap.release() 释放读取  
	• Cv2.destroyAllWindows() 用于销毁cv2创建的窗口  
04：图片的读写  
	• 读取、显示：img = cv2.imread(path, inter) ，inter是读入图片格式的数字表达，  
		
	
	cv2.imshow('image',img)，第一个图片窗口的名字，第二个是显示的图片
	• 写：cv2.imwrite(path, img)
05:   
	opencv的绘图功能：在已有图片上绘制线条、箭头、多边形，字体等  
	
	Img = cv2.line(img, (0,0), (255,255), (B,G,R),thickness )，(0,0), (255,255)：左上角、右下角坐标  
	Img = cv2.arrowedLine(img, (0,255), (255,255),  (B,G,R)，thickness)  
	Img = cv2.rectangle(img, (0,255), (255,255),  (B,G,R)，thickness)  
	Img = cv2.circle(img, center,r,  (B,G,R), -1) -1 表示填充，其他为不填充  
	
	Font = cv2.FONT_HERSHEY_SIMPLEX  文字的样式
	Img = cv2.putText(img, text,  (文字中心坐标x,y)， font, size, (B, G, R), thickness，cv2.LINE_AA)
07：  
	为视频加上文字，是03、05的应用，在frame上添加文字即可。  
08：  
	鼠标事件，当点击鼠标左右键，执行不同的函数，展现不同的结果。  
	
	Cv2.setMouseCallback('image', click_event)  
	 click_event 是一个回调函数  
	defclick_event(event,x,y,flags,params):  
		ifevent==cv2.EVENT_LBUTTONDOWN:  
		cv2.circle(img,(x,y),3,(255,225,0),-1)  
		points.append((x,y))  
		iflen(points)>=2:  
		cv2.line(img,points[-2],points[-1],(128,128,128),5)  
		cv2.imshow('image',img)  
有固定的参数。  
09：  
	将鼠标事件同05结合  
10： 

	H, w, c = img.shape  获得图片的长、宽、通道数＜/br＞ 
	B, g, r = cv2.split(img) ＜/br＞ 
	Img = cv2.merge((b, g, r))＜/br＞ 
	
	Ball = img[x:x+a, y:y+b]  提取图中的物体
	Img[z:z+a, t:t+a] = ball 将提取到的物体复制到图片中其他位置
	
	Img = cv2.resize(img, (h,w) ) 重置大小
	
	Dst = cv2.add(img, img1)   将两张大小相同的图片叠加在一起，就是对应坐标相加。
	Dst = cv2.addWeight(img, 0.9, img1, 0.1)  按照比例进行融合，造成一种透明的感觉
11： 
	对图像进行逻辑运算，得到不同的效果
	
	bitAnd=cv2.bitwise_and(img2,img1)#全1才是1
	bitOr=cv2.bitwise_or(img2,img1)#有一个1就是1
	bitXor=cv2.bitwise_xor(img2,img1)#相同是0不同是1
	bitNot=cv2.bitwise_not(img2)#取反
12： 
	在窗口上添加一个滑动条，拖动滑块，改变变量的值，滑块和图片应该在同一个窗口上。
	Cv2.namedWindow('image')  创建一个命名窗口，图片和滑块通过指定窗口名字‘image’都显示到这个窗口上
	
	Cv2.createTrackbar(bar_name, window_name, min, max, callback_func)
	Pos = cv2.getTrackbarPos(bar_name, window_name)  获得滑块当前值	
	它可以用于改变图片中BGR的值从而显示不同的图片，或者在图片添加滑块的值为文字
13：   	
	介绍了HSV颜色空间，色调（H），饱和度（S），明度（V）。＜/br＞ 
	
	Hsv = cv.cvtColor(img, cv2.COLOR_BGR2HSV)  将图片转换到HSV颜色空间
	利用trackbar动态改变HSV的值
	本例中是做了一个mask掩膜，利用掩膜对图片进行逻辑操作，从而获得想要的图像，即结合11、12.
	Mask = cv2.inRange(hsv_img,low_array, high_array)
14:			
	对图片像素值进行截断，给定一个阈值，阈值一下一个值，阈值以上一个值，得到一个二值化图片	
	
	_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)#0or1 	
	_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#0to1,1to0 	
	_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)#小于127是原图像素值，大于部分全为127	
	_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#小于127全位0，大于部分为原图	
	_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)#小于127为原图，大于部分为0	
15：	
	在14中阈值是人为指定的，对于不同的图像，阈值不同，效果不同，为了得到一个较好 二值化图片。
	
	Th1 =dst = cv2.adaptiveThreshold(src, maxval, thresh_type, type, Block Size, C)	
	src： 输入图，只能输入单通道图像，通常来说为灰度图	
	dst： 输出图	
	maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值	
	thresh_type： 阈值的计算方法，包含以下2种类型：cv2.ADAPTIVE_THRESH_MEAN_C； cv2.ADAPTIVE_THRESH_GAUSSIAN_C.	
	type：二值化操作的类型，与固定阈值函数相同，包含以下5种类型： cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV.	
	Block Size： 图片中分块的大小	
	C ：阈值计算方法中的常数项	
	
本例结合了03。  

16：	
	将CV2读取的图片利用matplotlib.pyplot 来显示	
	Cv2.imread(path, agrs) 读取的颜色空间为 BGR， 	
	Plt,imshow(img, args) 展示的图片为RGB	
	需要使用 img = cv2.cvtColorimg, cv2.COLOR_BGR2RGB()  	

17: 
	对二值化图形进行腐蚀、扩张等操作，操作实质是对某个像素点的周围像素进行整合，需要一个“核”。
	
	_, mask = cv2.threshold(img, 220, 255, cv2THRESH_BINARY_INV.)  # 对图片进行二值化
	
	Kernel = np.ones((3,3), np.uint8)
	Dilation = cv2.dilate(mask, kernel, iterations = 2)
	erosion = cv2.erode(mask, kernel, iterations=1)
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # erosion +dilation
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # dilation + erosion
18:	  		
	对图片做平滑处理或模糊处理， 同样需要一个核，有二维卷积（平滑）、模糊、高斯滤波、中值滤波、双边滤波	
	
	Kernel =  np.ones((5, 5), np.float32) / 25  # divided by size ^ 2  	
	dst = cv2.filter2D(img, -1, kernel)  # smooth
	blur = cv2.blur(img, (5, 5))  # mean method	
	gblur = cv2.GaussianBlur(img, (5, 5), 0)  # 先计算卷积核的值，在去做操作	
	median = cv2.medianBlur(img, 5)  # use salt-pepper-noise.png to see result	
	bilatera = cv2.bilateralFilter(img, 9, 75, 75)  # preserve the border of img	
	
19：	  		
	求图像x、y轴上的梯度信息，从而可以实现物体的边缘检测	
	先将图片转化为灰度图后进行边缘检测，使用边缘检测算法时候，会出现负值，使用cv2.CV_64F数据类型处理负值，显示图片前，需要将负数取绝对值	
	求梯度方法如下：
	
	Laplacian算子：	
	Lap = cv2.Laplacian(img_gray, cv2.CV_64F， ksize = 3)	
	Lap = np.uint8(np.absolute(lap))	
	
	sobel算子：
	Sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
	sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
	sobel_x = np.uint8(np.absolute(sobel_x))
	sobel_y = np.uint8(np.absolute(sobel_y))
	
	Canny算子：
	
	canny = cv2.Canny(img, 100, 200)
	
	同时显示x和y的梯度
	sobelCombined = cv2.bitwise_or(sobel_x, sobel_y)
	
	
	
	
	
	
