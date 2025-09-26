# GPS-free Real-time UAV Orthophoto Mapping via Terrain Constraint Monocular SLAM
***
![UAV_Orthophoto](https://github.com/YFS90/Real-time-orthophoto/blob/main/Img/GIF.gif)
Unmanned Aerial Vehicles (UAVs) play an increasingly vital role in civilian and military applications, where timely and accurate mapping is essential. However, conventional mapping pipelines typically depend on GPS, IMU, or computationally intensive Structure-from-Motion (SfM) techniques, limiting their applicability for real-time use in GPS-free environments.
To overcome these limitations, we introduce GROMS, a novel framework for real-time orthophoto generation from UAV imagery without requiring GPS or IMU data. GROMS integrates UAV–satellite image alignment, terrain-constrained monocular SLAM, and an efficient orthophoto generation strategy, enabling scalable, accurate, and low-latency mapping in complex, GPS-free scenarios.

## UAV Orthophotos 

![UAV_Orthophoto](https://github.com/YFS90/Real-time-orthophoto/blob/main/Img/uav_real-time_orthophoto.png)

## Demonstration videos

<table>
      <tr>
		<td colspan="2"><img src="https://github.com/YFS90/Real-time-orthophoto/blob/main/Img/Set_z.png" ></td>
	    <td colspan="2"><img src="https://github.com/YFS90/Real-time-orthophoto/blob/main/Img/Set_f.png" ></td>
	    <td colspan="2"><img src="https://github.com/YFS90/Real-time-orthophoto/blob/main/Img/Set_k.png" ></td>
	    <td colspan="2"><img src="https://github.com/YFS90/Real-time-orthophoto/blob/main/Img/Set_o.png" ></td> 
        <td colspan="2"><img src="https://github.com/YFS90/Real-time-orthophoto/blob/main/Img/Set_p.png" ></td>
	    <td colspan="2"><img src="https://github.com/YFS90/Real-time-orthophoto/blob/main/Img/Set_s.png" ></td> 
      </tr >
      <tr >
		<td><a href="https://www.bilibili.com/video/BV1Hbnhz4E6k/">bilibili</a></td>
	    <td><a href="https://www.youtube.com/watch?v=hIa6UpgjXLA/">YouTube</a></td>
	    <td><a href="https://www.bilibili.com/video/BV1w4nhzZEUb/">bilibili</a></td>
	    <td><a href="https://www.youtube.com/watch?v=kUrFVJ2w_P4">YouTube</a></td>
        <td><a href="https://www.bilibili.com/video/BV1wbnhz4EJL/">bilibili</a></td>
	    <td><a href="https://www.youtube.com/watch?v=yPT6AwQHLp8/">YouTube</a></td>
        <td><a href="https://www.bilibili.com/video/BV1AsnhzFE93/">bilibili</a></td>
	    <td><a href="https://www.youtube.com/watch?v=dDPBcCD0aDM/">YouTube</a></td>
        <td><a href="https://www.bilibili.com/video/BV1A4nhzZEAX/">bilibili</a></td>
	    <td><a href="https://www.youtube.com/watch?v=mbo58fBPGZQ/">YouTube</a></td>
        <td><a href="https://www.bilibili.com/video/BV1w4nhzZEeP/">bilibili</a></td>
	    <td><a href="https://www.youtube.com/watch?v=0GROtfs2gqw/)">YouTube</a></td>
	</tr>     
</table>

***

## Datasets📦

NUP DroneMap – Publicly available at [link](https://pan.baidu.com/s/1Lx0UYDlX08CFI6uA1b19EQ), extraction code: m33s. The dataset includes UAV-captured images along with corresponding satellite imagery of the same areas. Thanks to [Map2DFusion](https://github.com/zdzhaoyong/Map2DFusion) for open-sourcing the UAV imagery.

XD-Lab DroneMap – Available upon request: yaofushan123@163.com

⚠️ Usage restriction: Both datasets are provided for academic research purposes only.

