①python3 get_2chtext.py "url" "dir/output_file.txt"
でredditから英語のテキストを取得
②DeepLで翻訳
③猛虎弁になおして区切りに"|"をいれてtxtファイルに保存
④録画しつつ
python3 run_bouyomi.py "dir/input_text.txt"
でテキストを音声化
⑤python3 create_comment_image.py "input_text.txt" "dir"
でテキストのフレーム付き画像を作成
⑥python3 combine_material.py "dir" "input_file.mp4" "bgm.mp3" "bouyomi.mp3" "output_file.mp4"
で動画を作成
⑦動画をfilmeで編集、コメントのフレームを入れる