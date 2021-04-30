SELECT Sum(ven.Quantidade) as QTotal, Sum(ven.Valor) as VTotal
,pro.Descricao
from Item_venda ven 
JOIN Produto pro
on pro.Codigo = ven.Cod_Produto
where ven.Valor > 550
Group by pro.Descricao
HAVING sum(ven.Valor) >=100
