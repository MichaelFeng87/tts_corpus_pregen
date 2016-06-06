将混乱的文本，拆分出30字左右的，一系列 句子，并 分词、注音，作为后面阶段 corpus 制造做准备。


过程：
1，找基本文本 a.txt
2，tr.py a.txt a_out.txt 生成合理的句子列表（每句30词左右）
3，tn.py a_out.txt PREFIX 生成一系列.trn 文件（和 thchs30 corpus 一致）
4，到tts_corpus_gen 里面从 a_out.txt 生成 PREFIX  .wav
