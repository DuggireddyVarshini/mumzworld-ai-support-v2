RESPONSES = {
    "refund_request": {
        "en": "Refund is available within 30 days if the product is unused.",
        "ar": "يمكنك استرجاع المبلغ خلال 30 يوم إذا لم يتم استخدام المنتج."
    },

    "delay_issue": {
        "en": "Your order may be delayed. Please share your order ID.",
        "ar": "قد يكون طلبك متأخراً. يرجى مشاركة رقم الطلب."
    },

    "product_issue": {
        "en": "We can replace or refund damaged items.",
        "ar": "يمكننا استبدال أو استرجاع المنتجات التالفة."
    },

    "order_status": {
        "en": "Please provide your order ID to track status.",
        "ar": "يرجى تزويدنا برقم الطلب لتتبع الحالة."
    },

    "shipping_info": {
        "en": "We ship across GCC and international regions.",
        "ar": "نحن نشحن داخل دول الخليج وخارجها."
    },

    "policy_query": {
        "en": "Our policies include 30-day returns and refunds.",
        "ar": "سياساتنا تشمل الإرجاع والاسترجاع خلال 30 يوم."
    },

    "unknown": {
        "en": "I need more details to help you.",
        "ar": "أحتاج إلى مزيد من التفاصيل لمساعدتك."
    }
}


def generate_response(intent):
    return RESPONSES.get(intent, RESPONSES["unknown"])