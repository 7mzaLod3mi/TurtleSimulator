Duvardan Kaçan Kaplumbağa

Proje Hakkında

Bu proje, ROS 2 ve Python kullanılarak geliştirilmiştir. Kaplumbağa, duvarlara yaklaştığında yönünü değiştirerek hareket etmeye devam eder.

Kullanılan Teknolojiler

- ROS 2 Humble
- Python
- rclpy
- geometry_msgs
- turtlesim

Özellikler

- Kaplumbağanın konumu `/turtle1/pose` konusundan alınır.
- Hareket komutları `/turtle1/cmd_vel` konusuna gönderilir.
- X ve Y koordinatları her saniye terminale yazdırılır.
- Duvarlara yaklaşınca kaplumbağanın yönü değiştirilir.
- Hareket hızı ve sınır değerleri parametrelerle ayarlanabilir.

Çalıştırma

Önce turtlesim simülasyonunu başlatın:

bash
ros2 run turtlesim turtlesim_node


Ardından yeni bir terminalde kontrol düğümünü çalıştırın:

bash
source ~/ros2_ws/install/setup.bash
ros2 run turtle_duvar_py turtle_duvar_node


Geliştirici

Hamza Lodami
