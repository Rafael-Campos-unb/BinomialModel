SELECT idade, principio_ativo,quantidade_vendida, ano 
FROM `basedosdados.br_anvisa_medicamentos_industrializados.microdados`
WHERE ano = 2020 AND sigla_uf = 'DF' AND principio_ativo = 'AZITROMICINA DI-HIDRATADA' AND idade IS NOT NULL AND idade < 100
ORDER BY quantidade_vendida DESC;

SELECT idade, principio_ativo,quantidade_vendida, ano 
FROM `basedosdados.br_anvisa_medicamentos_industrializados.microdados`
WHERE ano = 2020 AND sigla_uf = 'DF' AND principio_ativo = 'AZITROMICINA DI-HIDRATADA'
ORDER BY idade DESC;


SELECT idade, principio_ativo,quantidade_vendida, ano 
FROM `basedosdados.br_anvisa_medicamentos_industrializados.microdados`
WHERE ano = 2020 AND sigla_uf = 'DF' AND principio_ativo = 'CLONAZEPAM' AND idade IS NOT NULL
ORDER BY quantidade_vendida DESC;