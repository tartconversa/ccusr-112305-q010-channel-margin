# 资料口径

金额单位为人民币，units 为整份成交组合数，parts 是可独立承担换货的部件。allocation_weight 供拆件归属，不能重复计算已经纳入组合的件数。调整事件 recognized_week 是资料进入周，经营归属仍取原成交周；跨渠道换货不产生新的付费订单，退货扣减原销售，陈列归属按费用单的 counter_channel。未过 maturity_week 的资料仅作暂估。
渠道退出仍受 campaign 的最低营业渠道数 min_active 约束，optional_stop 是有退出权的范围。incompatible 中每个组允许至多同时存在一个陈列版本。sales_hold 是该活动仍需按单据兑现的旧交付，pickup_days 是自提约定保留天数。转购区间是候选效果输入，不是既已发生的转购，对缺同类观察的方向仅供敏感性分析。

followups 记录各决议后分批收到的转购统计及完成交付的回单。实际费用与候选预计费用各自保留。

entitlements 记录还有效的销售权益，partial 为是否允许单件先行兑现。assumption_changes 表示营运发布接管渠道及认可数量，按同一商品移交版本更新，部分接受只承接确认部分。redemption_events 中 serial 是实物交付凭证的序号，只在可核实实物有效时认定履行。相同序号跨店录得不增加实际件数。
