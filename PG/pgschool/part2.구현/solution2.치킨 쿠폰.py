# 치킨 쿠폰

def solution(chicken):
    service_coupon = chicken // 10 # 10
    add_coupon = service_coupon + chicken % 10

    while add_coupon >= 10:
        order = add_coupon // 10
        service_coupon += order
        add_coupon = order + add_coupon % 10
    
    return service_coupon

print(solution(100))
print(solution(1081))