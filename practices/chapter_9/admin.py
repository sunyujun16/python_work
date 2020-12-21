from privilege import Admin  # 发现：调用的时候会自动执行users里面的第一级（无缩进）“调用函数”语句

admin = Admin("Sun", "Yujun", 26, "LiuYihan")

admin.privileges.show_privileges()


