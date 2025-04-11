TITLE: Whisper CLI Usage and Options
DESCRIPTION: Comprehensive list of command-line arguments and options for the whisper-cli program, including audio processing parameters, output formats, and model configuration settings. The CLI supports features like multi-threading, language detection, translation, diarization, and various output formats including TXT, VTT, SRT, LRC, CSV, and JSON.

LANGUAGE: shell
CODE:
./build/bin/whisper-cli -h

usage: ./build-pkg/bin/whisper-cli [options] file0.wav file1.wav ...

options:
  -h,        --help              [default] show this help message and exit
  -t N,      --threads N         [4      ] number of threads to use during computation
  -p N,      --processors N      [1      ] number of processors to use during computation
  -ot N,     --offset-t N        [0      ] time offset in milliseconds
  -on N,     --offset-n N        [0      ] segment index offset
  -d  N,     --duration N        [0      ] duration of audio to process in milliseconds
  -mc N,     --max-context N     [-1     ] maximum number of text context tokens to store
  -ml N,     --max-len N         [0      ] maximum segment length in characters
  -sow,      --split-on-word     [false  ] split on word rather than on token
  -bo N,     --best-of N         [5      ] number of best candidates to keep
  -bs N,     --beam-size N       [5      ] beam size for beam search
  -ac N,     --audio-ctx N       [0      ] audio context size (0 - all)
  -wt N,     --word-thold N      [0.01   ] word timestamp probability threshold
  -et N,     --entropy-thold N   [2.40   ] entropy threshold for decoder fail
  -lpt N,    --logprob-thold N   [-1.00  ] log probability threshold for decoder fail
  -tp,       --temperature N     [0.00   ] The sampling temperature, between 0 and 1
  -tpi,      --temperature-inc N [0.20   ] The increment of temperature, between 0 and 1
  -debug,    --debug-mode        [false  ] enable debug mode (eg. dump log_mel)
  -tr,       --translate         [false  ] translate from source language to english
  -di,       --diarize           [false  ] stereo audio diarization
  -tdrz,     --tinydiarize       [false  ] enable tinydiarize (requires a tdrz model)
  -nf,       --no-fallback       [false  ] do not use temperature fallback while decoding
  -otxt,     --output-txt        [false  ] output result in a text file
  -ovtt,     --output-vtt        [false  ] output result in a vtt file
  -osrt,     --output-srt        [false  ] output result in a srt file
  -olrc,     --output-lrc        [false  ] output result in a lrc file
  -owts,     --output-words      [false  ] output script for generating karaoke video
  -fp,       --font-path         [/System/Library/Fonts/Supplemental/Courier New Bold.ttf] path to a monospace font for karaoke video
  -ocsv,     --output-csv        [false  ] output result in a CSV file
  -oj,       --output-json       [false  ] output result in a JSON file
  -ojf,      --output-json-full  [false  ] include more information in the JSON file
  -of FNAME, --output-file FNAME [       ] output file path (without file extension)
  -np,       --no-prints         [false  ] do not print anything other than the results
  -ps,       --print-special     [false  ] print special tokens
  -pc,       --print-colors      [false  ] print colors
  -pp,       --print-progress    [false  ] print progress
  -nt,       --no-timestamps     [false  ] do not print timestamps
  -l LANG,   --language LANG     [en     ] spoken language ('auto' for auto-detect)
  -dl,       --detect-language   [false  ] exit after automatically detecting language
             --prompt PROMPT     [       ] initial prompt (max n_text_ctx/2 tokens)
  -m FNAME,  --model FNAME       [models/ggml-base.en.bin] model path
  -f FNAME,  --file FNAME        [       ] input WAV file path
  -oved D,   --ov-e-device DNAME [CPU    ] the OpenVINO device used for encode inference
  -dtw MODEL --dtw MODEL         [       ] compute token-level timestamps
  -ls,       --log-score         [false  ] log best decoder scores of tokens
  -ng,       --no-gpu            [false  ] disable GPU
  -fa,       --flash-attn        [false  ] flash attention
  --suppress-regex REGEX         [       ] regular expression matching tokens to suppress
  --grammar GRAMMAR              [       ] GBNF grammar to guide decoding
  --grammar-rule RULE            [       ] top-level GBNF grammar rule name
  --grammar-penalty N            [100.0  ] scales down logits of nongrammar tokens

----------------------------------------

TITLE: Building whisper.cpp with BLAS CPU Support
DESCRIPTION: Configures and builds the project with CMake, enabling OpenBLAS support for CPU acceleration.

LANGUAGE: bash
CODE:
cmake -B build -DGGML_BLAS=1
cmake --build build -j --config Release

----------------------------------------

TITLE: Cloning the Whisper.cpp Repository
DESCRIPTION: This command clones the Whisper.cpp repository from GitHub to the local machine.

LANGUAGE: bash
CODE:
git clone https://github.com/ggml-org/whisper.cpp.git

----------------------------------------

TITLE: Running whisper-stream with Sliding Window and VAD
DESCRIPTION: Command to run whisper-stream in sliding window mode with Voice Activity Detection. Setting step to 0 enables the sliding window, while the -vth parameter controls the VAD threshold for speech detection.

LANGUAGE: bash
CODE:
./build/bin/whisper-stream -m ./models/ggml-base.en.bin -t 6 --step 0 --length 30000 -vth 0.6

----------------------------------------

TITLE: Generating Word-level Timestamps with whisper-cli
DESCRIPTION: Command-line example showing how to use the -ml 1 flag to generate word-level timestamps with whisper.cpp. The output shows a detailed breakdown of timestamps for each word in the transcription.

LANGUAGE: text
CODE:
$ ./build/bin/whisper-cli -m ./models/ggml-base.en.bin -f ./samples/jfk.wav -ml 1

whisper_model_load: loading model from './models/ggml-base.en.bin'
...
system_info: n_threads = 4 / 10 | AVX2 = 0 | AVX512 = 0 | NEON = 1 | FP16_VA = 1 | WASM_SIMD = 0 | BLAS = 1 |

main: processing './samples/jfk.wav' (176000 samples, 11.0 sec), 4 threads, 1 processors, lang = en, task = transcribe, timestamps = 1 ...

[00:00:00.000 --> 00:00:00.320]
[00:00:00.320 --> 00:00:00.370]   And
[00:00:00.370 --> 00:00:00.690]   so
[00:00:00.690 --> 00:00:00.850]   my
[00:00:00.850 --> 00:00:01.590]   fellow
[00:00:01.590 --> 00:00:02.850]   Americans
[00:00:02.850 --> 00:00:03.300]  ,
[00:00:03.300 --> 00:00:04.140]   ask
[00:00:04.140 --> 00:00:04.990]   not
[00:00:04.990 --> 00:00:05.410]   what
[00:00:05.410 --> 00:00:05.660]   your
[00:00:05.660 --> 00:00:06.260]   country
[00:00:06.260 --> 00:00:06.600]   can
[00:00:06.600 --> 00:00:06.840]   do
[00:00:06.840 --> 00:00:07.010]   for
[00:00:07.010 --> 00:00:08.170]   you
[00:00:08.170 --> 00:00:08.190]  ,
[00:00:08.190 --> 00:00:08.430]   ask
[00:00:08.430 --> 00:00:08.910]   what
[00:00:08.910 --> 00:00:09.040]   you
[00:00:09.040 --> 00:00:09.320]   can
[00:00:09.320 --> 00:00:09.440]   do
[00:00:09.440 --> 00:00:09.760]   for
[00:00:09.760 --> 00:00:10.020]   your
[00:00:10.020 --> 00:00:10.510]   country
[00:00:10.510 --> 00:00:11.000]  .

----------------------------------------

TITLE: Basic Transcription with Whisper in Ruby
DESCRIPTION: Demonstrates how to initialize a Whisper context with a model, configure transcription parameters, and transcribe an audio file. Parameters include language specification, time offsets, token limits, translation options, and formatting preferences.

LANGUAGE: ruby
CODE:
require "whisper"

whisper = Whisper::Context.new("base")

params = Whisper::Params.new(
  language: "en",
  offset: 10_000,
  duration: 60_000,
  max_text_tokens: 300,
  translate: true,
  print_timestamps: false,
  initial_prompt: "Initial prompt here."
)

whisper.transcribe("path/to/audio.wav", params) do |whole_text|
  puts whole_text
end

----------------------------------------

TITLE: Building whisper-stream with SDL2 Support
DESCRIPTION: Instructions for building the whisper-stream tool with SDL2 support for microphone capture. Includes package installation commands for different platforms and the necessary CMake commands.

LANGUAGE: bash
CODE:
# Install SDL2
# On Debian based linux distributions:
sudo apt-get install libsdl2-dev

# On Fedora Linux:
sudo dnf install SDL2 SDL2-devel

# Install SDL2 on Mac OS
brew install sdl2

cmake -B build -DWHISPER_SDL2=ON
cmake --build build --config Release

./build/bin/whisper-stream

----------------------------------------

TITLE: Generating Karaoke-style Videos with whisper.cpp
DESCRIPTION: Commands to generate karaoke-style videos where the currently pronounced word is highlighted. The example shows how to use the -owts flag to create a bash script that uses ffmpeg to produce the video.

LANGUAGE: bash
CODE:
./build/bin/whisper-cli -m ./models/ggml-base.en.bin -f ./samples/jfk.wav -owts
source ./samples/jfk.wav.wts
ffplay ./samples/jfk.wav.mp4

LANGUAGE: bash
CODE:
./build/bin/whisper-cli -m ./models/ggml-base.en.bin -f ./samples/mm0.wav -owts
source ./samples/mm0.wav.wts
ffplay ./samples/mm0.wav.mp4

LANGUAGE: bash
CODE:
./build/bin/whisper-cli -m ./models/ggml-base.en.bin -f ./samples/gb0.wav -owts
source ./samples/gb0.wav.wts
ffplay ./samples/gb0.wav.mp4

----------------------------------------

TITLE: Transcribing Audio with Whisper-CLI
DESCRIPTION: This command uses the built whisper-cli tool to transcribe an audio file (jfk.wav) using the Whisper model.

LANGUAGE: bash
CODE:
./build/bin/whisper-cli -f samples/jfk.wav

----------------------------------------

TITLE: Downloading Whisper Model in GGML Format
DESCRIPTION: This script downloads a Whisper model converted to GGML format. The example uses the 'base.en' model.

LANGUAGE: bash
CODE:
sh ./models/download-ggml-model.sh base.en

----------------------------------------

TITLE: Setting up Python Environment for OpenVINO (Linux/macOS)
DESCRIPTION: Creates a Python virtual environment and installs required dependencies for OpenVINO conversion on Linux and macOS.

LANGUAGE: bash
CODE:
cd models
python3 -m venv openvino_conv_env
source openvino_conv_env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-openvino.txt

----------------------------------------

TITLE: Initializing and Using WhisperCpp in Java
DESCRIPTION: This snippet demonstrates how to initialize WhisperCpp, load a model, transcribe audio, and retrieve the transcribed text segments. It includes error handling and resource cleanup.

LANGUAGE: java
CODE:
import io.github.ggerganov.whispercpp.WhisperCpp;

public class Example {

    public static void main(String[] args) {
        WhisperCpp whisper = new WhisperCpp();
        // By default, models are loaded from ~/.cache/whisper/ and are usually named "ggml-${name}.bin"
        // or you can provide the absolute path to the model file.
        long context = whisper.initContext("base.en");
        try {
            var whisperParams = whisper.getFullDefaultParams(WhisperSamplingStrategy.WHISPER_SAMPLING_GREEDY);
            // custom configuration if required
            whisperParams.temperature_inc = 0f;

            var samples = readAudio(); // divide each value by 32767.0f
            whisper.fullTranscribe(whisperParams, samples);

            int segmentCount = whisper.getTextSegmentCount(context);
            for (int i = 0; i < segmentCount; i++) {
                String text = whisper.getTextSegment(context, i);
                System.out.println(segment.getText());
            }
        } finally {
             whisper.freeContext(context);
        }
     }
}

----------------------------------------

TITLE: Using Docker for Model Download and Transcription
DESCRIPTION: Demonstrates how to use Docker to download a model and transcribe an audio file using whisper.cpp.

LANGUAGE: bash
CODE:
docker run -it --rm \
  -v path/to/models:/models \
  whisper.cpp:main "./models/download-ggml-model.sh base /models"

docker run -it --rm \
  -v path/to/models:/models \
  -v path/to/audios:/audios \
  whisper.cpp:main "./main -m /models/ggml-base.bin -f /audios/jfk.wav"

----------------------------------------

TITLE: Using Whisper XCFramework in Swift Projects
DESCRIPTION: Example of how to integrate the pre-built Whisper XCFramework into Swift projects using Swift Package Manager. This allows using the whisper.cpp library in iOS, visionOS, tvOS, and macOS applications without compiling from source.

LANGUAGE: swift
CODE:
// swift-tools-version: 5.10
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "Whisper",
    targets: [
        .executableTarget(
            name: "Whisper",
            dependencies: [
                "WhisperFramework"
            ]),
        .binaryTarget(
            name: "WhisperFramework",
            url: "https://github.com/ggml-org/whisper.cpp/releases/download/v1.7.5/whisper-v1.7.5-xcframework.zip",
            checksum: "c7faeb328620d6012e130f3d705c51a6ea6c995605f2df50f6e1ad68c59c6c4a"
        )
    ]
)

----------------------------------------

TITLE: Building Whisper.cpp Project with CMake
DESCRIPTION: These commands build the Whisper.cpp project using CMake, creating a build directory and compiling the project in Release configuration.

LANGUAGE: bash
CODE:
cmake -B build
cmake --build build --config Release

----------------------------------------

TITLE: Converting Audio to 16-bit WAV Format
DESCRIPTION: This ffmpeg command converts an input audio file to a 16-bit WAV format compatible with the whisper-cli tool.

LANGUAGE: bash
CODE:
ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav

----------------------------------------

TITLE: Using Pre-converted Whisper Models in Ruby
DESCRIPTION: Shows how to use pre-converted Whisper models, which are downloaded automatically on first use and then cached. Includes methods for accessing cached models, clearing the cache, and listing available pre-converted models.

LANGUAGE: ruby
CODE:
base_en = Whisper::Model.pre_converted_models["base.en"]
whisper = Whisper::Context.new(base_en)

LANGUAGE: ruby
CODE:
Whisper::Model.pre_converted_models["base"].clear_cache

LANGUAGE: ruby
CODE:
whisper = Whisper::Context.new("base.en")

LANGUAGE: ruby
CODE:
puts Whisper::Model.pre_converted_models.keys
# tiny
# tiny.en
# tiny-q5_1
# tiny.en-q5_1
# tiny-q8_0
# base
# base.en
# base-q5_1
# base.en-q5_1
# base-q8_0
#   :
#   :

----------------------------------------

TITLE: Using Segment Callbacks in Whisper Ruby
DESCRIPTION: Demonstrates how to register a callback that is triggered on each new segment during transcription. The callback receives segment information including text, timestamps, and speaker change indicators.

LANGUAGE: ruby
CODE:
# Add hook before calling #transcribe
params.on_new_segment do |segment|
  line = "[%{st} --> %{ed}] %{text}" % {
    st: format_time(segment.start_time),
    ed: format_time(segment.end_time),
    text: segment.text
  }
  line << " (speaker turned)" if segment.speaker_next_turn?
  puts line
end

whisper.transcribe("path/to/audio.wav", params)

----------------------------------------

TITLE: Running Basic Real-Time Transcription with whisper-stream
DESCRIPTION: Command to run the whisper-stream tool for real-time audio transcription from the microphone with a fixed step interval. This samples audio every 500ms and processes 5-second chunks using 8 threads.

LANGUAGE: bash
CODE:
./build/bin/whisper-stream -m ./models/ggml-base.en.bin -t 8 --step 500 --length 5000

----------------------------------------

TITLE: Downloading the Whisper Base Model
DESCRIPTION: Command to download the English base model for Whisper, which is required for transcription.

LANGUAGE: shell
CODE:
./models/download-ggml-model.sh base.en

----------------------------------------

TITLE: Converting PyTorch Models to ggml Format
DESCRIPTION: Bash script demonstrating how to convert a PyTorch Whisper model to ggml format using the convert-pt-to-ggml.py script. The process includes creating a directory, running the conversion script, and moving the output file.

LANGUAGE: bash
CODE:
mkdir models/whisper-medium
python models/convert-pt-to-ggml.py ~/.cache/whisper/medium.pt ~/path/to/repo/whisper/ ./models/whisper-medium
mv ./models/whisper-medium/ggml-model.bin models/ggml-medium.bin
rmdir models/whisper-medium

----------------------------------------

TITLE: Downloading ggml Models with download-ggml-model.sh
DESCRIPTION: Example of downloading a pre-converted ggml model using the download-ggml-model.sh script. The command downloads the base.en model and outputs information about how to use it.

LANGUAGE: text
CODE:
$ ./download-ggml-model.sh base.en
Downloading ggml model base.en ...
models/ggml-base.en.bin          100%[=============================================>] 141.11M  5.41MB/s    in 22s
Done! Model 'base.en' saved in 'models/ggml-base.en.bin'
You can now use it like this:

  $ ./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav

----------------------------------------

TITLE: Defining Build Options for whisper.cpp
DESCRIPTION: Defines the available build options for the project, including general settings, debug options, sanitizers, and third-party library integrations. These options control the build behavior and feature set of whisper.cpp.

LANGUAGE: CMake
CODE:
#
# option list
#

# general
option(WHISPER_CCACHE "whisper: use ccache if available" ON)

# debug
option(WHISPER_ALL_WARNINGS           "whisper: enable all compiler warnings"                   ON)
option(WHISPER_ALL_WARNINGS_3RD_PARTY "whisper: enable all compiler warnings in 3rd party libs" OFF)

# build
option(WHISPER_FATAL_WARNINGS  "whisper: enable -Werror flag"               OFF)
option(WHISPER_USE_SYSTEM_GGML "whisper: use system-installed GGML library" OFF)

# sanitizers
option(WHISPER_SANITIZE_THREAD    "whisper: enable thread sanitizer"    OFF)
option(WHISPER_SANITIZE_ADDRESS   "whisper: enable address sanitizer"   OFF)
option(WHISPER_SANITIZE_UNDEFINED "whisper: enable undefined sanitizer" OFF)

# extra artifacts
option(WHISPER_BUILD_TESTS    "whisper: build tests"          ${WHISPER_STANDALONE})
option(WHISPER_BUILD_EXAMPLES "whisper: build examples"       ${WHISPER_STANDALONE})
option(WHISPER_BUILD_SERVER   "whisper: build server example" ${WHISPER_STANDALONE})

# 3rd party libs
option(WHISPER_CURL "whisper: use libcurl to download model from an URL" OFF)
option(WHISPER_SDL2 "whisper: support for libSDL2" OFF)

if (CMAKE_SYSTEM_NAME MATCHES "Linux")
    option(WHISPER_FFMPEG "whisper: support building and linking with ffmpeg libs (avcodec, swresample, ...)" OFF)
endif()

option(WHISPER_COREML                "whisper: enable Core ML framework"  OFF)
option(WHISPER_COREML_ALLOW_FALLBACK "whisper: allow non-CoreML fallback" OFF)
option(WHISPER_OPENVINO              "whisper: support for OpenVINO"      OFF)

----------------------------------------

TITLE: Building and Running Voice-Controlled Chess in Bash
DESCRIPTION: Commands for building the wchess project from source using CMake and running it with a Whisper model. The resulting program displays a chess board interface in the terminal and accepts voice commands for moves.

LANGUAGE: bash
CODE:
mkdir build && cd build
cmake -DWHISPER_SDL2=1 ..
make -j

./bin/wchess -m ../models/ggml-base.en.bin

Move: start

a b c d e f g h
r n b q k b n r 8
p p p p p p p p 7
. * . * . * . * 6
* . * . * . * . 5
. * . * . * . * 4
* . * . * . * . 3
P P P P P P P P 2
R N B Q K B N R 1

White's turn
[(l)isten/(p)ause/(q)uit]: 

----------------------------------------

TITLE: Loading Custom Whisper Models in Ruby
DESCRIPTION: Demonstrates how to use local model files and remotely hosted models in the Whisper context. Supports loading from local paths or remote URLs.

LANGUAGE: ruby
CODE:
whisper = Whisper::Context.new("path/to/your/model.bin")

LANGUAGE: ruby
CODE:
whisper = Whisper::Context.new("https://example.net/uri/of/your/model.bin")
# Or
whisper = Whisper::Context.new(URI("https://example.net/uri/of/your/model.bin"))

----------------------------------------

TITLE: Building Whisper.wasm with Emscripten
DESCRIPTION: This snippet shows how to clone the whisper.cpp repository, create a build directory, and compile the project using Emscripten for WebAssembly output. It uses CMake for build configuration.

LANGUAGE: bash
CODE:
# build using Emscripten
git clone https://github.com/ggml-org/whisper.cpp
cd whisper.cpp
mkdir build-em && cd build-em
emcmake cmake ..
make -j

----------------------------------------

TITLE: Running Whisper.cpp Node.js Addon Example
DESCRIPTION: Command to run the example Node.js script that uses the compiled Whisper.cpp addon. It demonstrates how to pass language, model path, and input file path as command-line arguments.

LANGUAGE: shell
CODE:
cd examples/addon.node

node index.js --language='language' --model='model-path' --fname_inp='file-path'

----------------------------------------

TITLE: Accessing Whisper Model Information in Ruby
DESCRIPTION: Shows how to retrieve detailed information about the loaded Whisper model, including vocabulary size, context dimensions, network architecture parameters, and model type.

LANGUAGE: ruby
CODE:
whisper = Whisper::Context.new("base")
model = whisper.model

model.n_vocab # => 51864
model.n_audio_ctx # => 1500
model.n_audio_state # => 512
model.n_audio_head # => 8
model.n_audio_layer # => 6
model.n_text_ctx # => 448
model.n_text_state # => 512
model.n_text_head # => 8
model.n_text_layer # => 6
model.n_mels # => 80
model.ftype # => 1
model.type # => "base"

----------------------------------------

TITLE: Configuring WebAssembly Build Target for Whisper.cpp using CMake
DESCRIPTION: This CMake script configures the compilation of the Whisper speech recognition library to WebAssembly. It defines the target executable, links the Whisper library, and sets up Emscripten-specific link flags for thread support, memory management, and module export. The script also includes an optional configuration to embed the WASM binary directly in the JavaScript file for simpler deployment.

LANGUAGE: cmake
CODE:
set(TARGET libwhisper)

add_executable(${TARGET}
    emscripten.cpp
    )

target_link_libraries(${TARGET} PRIVATE
    whisper
    )

unset(EXTRA_FLAGS)

if (WHISPER_WASM_SINGLE_FILE)
    set(EXTRA_FLAGS "-s SINGLE_FILE=1")
    message(STATUS "Embedding WASM inside whisper.js")

    add_custom_command(
        TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_BINARY_DIR}/bin/libwhisper.js
        ${CMAKE_CURRENT_SOURCE_DIR}/whisper.js
        )

    add_custom_command(
        TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_BINARY_DIR}/bin/libwhisper.worker.js
        ${CMAKE_CURRENT_SOURCE_DIR}/libwhisper.worker.js
        )
endif()

set_target_properties(${TARGET} PROPERTIES LINK_FLAGS " \
    --bind \
    -s MODULARIZE=1 \
    -s EXPORT_NAME=\"'whisper_factory'\" \
    -s FORCE_FILESYSTEM=1 \
    -s USE_PTHREADS=1 \
    -s PTHREAD_POOL_SIZE=8 \
    -s ALLOW_MEMORY_GROWTH=1 \
    ${EXTRA_FLAGS} \
    ")

----------------------------------------

TITLE: Generating Core ML Model for Whisper
DESCRIPTION: This script generates a Core ML model for the 'base.en' Whisper model, which can be used for accelerated inference on Apple Silicon devices.

LANGUAGE: bash
CODE:
./models/generate-coreml-model.sh base.en

----------------------------------------

TITLE: Building and Running Real-time Audio Input Example
DESCRIPTION: Configures, builds, and runs the real-time audio input example using SDL2.

LANGUAGE: bash
CODE:
cmake -B build -DWHISPER_SDL2=ON
cmake --build build --config Release
./build/bin/whisper-stream -m ./models/ggml-base.en.bin -t 8 --step 500 --length 5000

----------------------------------------

TITLE: Speaker Segmentation using tinydiarize in whisper.cpp
DESCRIPTION: Example of using tinydiarize for speaker segmentation in whisper.cpp. It demonstrates how to download a compatible model and run it with the -tdrz flag, which adds speaker turn annotations to the transcription.

LANGUAGE: python
CODE:
# download a tinydiarize compatible model
./models/download-ggml-model.sh small.en-tdrz

# run as usual, adding the "-tdrz" command-line argument
./build/bin/whisper-cli -f ./samples/a13.wav -m ./models/ggml-small.en-tdrz.bin -tdrz
...
main: processing './samples/a13.wav' (480000 samples, 30.0 sec), 4 threads, 1 processors, lang = en, task = transcribe, tdrz = 1, timestamps = 1 ...
...
[00:00:00.000 --> 00:00:03.800]   Okay Houston, we've had a problem here. [SPEAKER_TURN]
[00:00:03.800 --> 00:00:06.200]   This is Houston. Say again please. [SPEAKER_TURN]
[00:00:06.200 --> 00:00:08.260]   Uh Houston we've had a problem.
[00:00:08.260 --> 00:00:11.320]   We've had a main beam up on a volt. [SPEAKER_TURN]
[00:00:11.320 --> 00:00:13.820]   Roger main beam interval. [SPEAKER_TURN]
[00:00:13.820 --> 00:00:15.100]   Uh uh [SPEAKER_TURN]
[00:00:15.100 --> 00:00:18.020]   So okay stand, by thirteen we're looking at it. [SPEAKER_TURN]
[00:00:18.020 --> 00:00:25.740]   Okay uh right now uh Houston the uh voltage is uh is looking good um.
[00:00:27.620 --> 00:00:29.940]   And we had a a pretty large bank or so.

----------------------------------------

TITLE: Compiling Whisper.cpp Node.js Addon with cmake-js
DESCRIPTION: Command to compile the Whisper.cpp Node.js addon using cmake-js. It specifies the target name as 'addon.node' and sets the build type to 'Release'.

LANGUAGE: shell
CODE:
npx cmake-js compile -T addon.node -B Release

----------------------------------------

TITLE: Running the Whisper Benchmarking Tool with a Small English Model
DESCRIPTION: This command demonstrates how to run the whisper-bench tool on the small.en model using 4 threads. The output shows detailed model information and performance metrics, including load time, encoding time per layer, and total execution time. The benchmark results can be submitted to a GitHub issue for comparison.

LANGUAGE: bash
CODE:
# run the bench too on the small.en model using 4 threads
$ ./build/bin/whisper-bench -m ./models/ggml-small.en.bin -t 4

whisper_model_load: loading model from './models/ggml-small.en.bin'
whisper_model_load: n_vocab       = 51864
whisper_model_load: n_audio_ctx   = 1500
whisper_model_load: n_audio_state = 768
whisper_model_load: n_audio_head  = 12
whisper_model_load: n_audio_layer = 12
whisper_model_load: n_text_ctx    = 448
whisper_model_load: n_text_state  = 768
whisper_model_load: n_text_head   = 12
whisper_model_load: n_text_layer  = 12
whisper_model_load: n_mels        = 80
whisper_model_load: f16           = 1
whisper_model_load: type          = 3
whisper_model_load: mem_required  = 1048.00 MB
whisper_model_load: adding 1607 extra tokens
whisper_model_load: ggml ctx size = 533.05 MB
whisper_model_load: memory size =    68.48 MB 
whisper_model_load: model size  =   464.44 MB

whisper_print_timings:     load time =   240.82 ms
whisper_print_timings:      mel time =     0.00 ms
whisper_print_timings:   sample time =     0.00 ms
whisper_print_timings:   encode time =  1062.21 ms / 88.52 ms per layer
whisper_print_timings:   decode time =     0.00 ms / 0.00 ms per layer
whisper_print_timings:    total time =  1303.04 ms

system_info: n_threads = 4 | AVX2 = 0 | AVX512 = 0 | NEON = 1 | FP16_VA = 1 | WASM_SIMD = 0 | BLAS = 1 | 

If you wish, you can submit these results here:

  https://github.com/ggml-org/whisper.cpp/issues/89

Please include the following information:

  - CPU model
  - Operating system
  - Compiler

----------------------------------------

TITLE: Building whisper.cpp with NVIDIA GPU Support
DESCRIPTION: Configures and builds the project with CMake, enabling CUDA support for NVIDIA GPUs.

LANGUAGE: bash
CODE:
cmake -B build -DGGML_CUDA=1
cmake --build build -j --config Release

----------------------------------------

TITLE: Converting Hugging Face Fine-tuned Models to ggml Format
DESCRIPTION: Bash script showing how to convert Hugging Face fine-tuned Whisper models to ggml format. The process includes cloning necessary repositories, downloading the model, and running the conversion script.

LANGUAGE: bash
CODE:
git clone https://github.com/openai/whisper
git clone https://github.com/ggml-org/whisper.cpp

# clone HF fine-tuned model (this is just an example)
git clone https://huggingface.co/openai/whisper-medium

# convert the model to ggml
python3 ./whisper.cpp/models/convert-h5-to-ggml.py ./whisper-medium/ ./whisper .

----------------------------------------

TITLE: Controlling Text Segment Length in Transcription
DESCRIPTION: Demonstrates how to limit the length of generated text segments during transcription.

LANGUAGE: bash
CODE:
./build/bin/whisper-cli -m ./models/ggml-base.en.bin -f ./samples/jfk.wav -ml 16

----------------------------------------

TITLE: Sample Output of Whisper.cpp Node.js Test Run
DESCRIPTION: Example output showing the model loading process, system information, and transcription results from running the test script. Includes detailed timing metrics for different processing stages.

LANGUAGE: text
CODE:
$ node --experimental-wasm-threads --experimental-wasm-simd ../tests/test-whisper.js

whisper_model_load: loading model from 'whisper.bin'
whisper_model_load: n_vocab       = 51864
whisper_model_load: n_audio_ctx   = 1500
whisper_model_load: n_audio_state = 512
whisper_model_load: n_audio_head  = 8
whisper_model_load: n_audio_layer = 6
whisper_model_load: n_text_ctx    = 448
whisper_model_load: n_text_state  = 512
whisper_model_load: n_text_head   = 8
whisper_model_load: n_text_layer  = 6
whisper_model_load: n_mels        = 80
whisper_model_load: f16           = 1
whisper_model_load: type          = 2
whisper_model_load: adding 1607 extra tokens
whisper_model_load: mem_required  =  506.00 MB
whisper_model_load: ggml ctx size =  140.60 MB
whisper_model_load: memory size   =   22.83 MB
whisper_model_load: model size    =  140.54 MB

system_info: n_threads = 8 / 10 | AVX = 0 | AVX2 = 0 | AVX512 = 0 | NEON = 0 | F16C = 0 | FP16_VA = 0 | WASM_SIMD = 1 | BLAS = 0 |

operator(): processing 176000 samples, 11.0 sec, 8 threads, 1 processors, lang = en, task = transcribe ...

[00:00:00.000 --> 00:00:11.000]   And so my fellow Americans, ask not what your country can do for you, ask what you can do for your country.

whisper_print_timings:     load time =   162.37 ms
whisper_print_timings:      mel time =   183.70 ms
whisper_print_timings:   sample time =     4.27 ms
whisper_print_timings:   encode time =  8582.63 ms / 1430.44 ms per layer
whisper_print_timings:   decode time =   436.16 ms / 72.69 ms per layer
whisper_print_timings:    total time =  9370.90 ms

----------------------------------------

TITLE: Building whisper.cpp with FFmpeg Support (Linux)
DESCRIPTION: Configures and builds the project with CMake, enabling FFmpeg integration for additional audio format support on Linux.

LANGUAGE: bash
CODE:
cmake -B build -D WHISPER_FFMPEG=yes
cmake --build build

----------------------------------------

TITLE: Building whisper.cpp with Vulkan GPU Support
DESCRIPTION: Configures and builds the project with CMake, enabling Vulkan support for cross-vendor GPU acceleration.

LANGUAGE: bash
CODE:
cmake -B build -DGGML_VULKAN=1
cmake --build build -j --config Release

----------------------------------------

TITLE: Configuring and Building Whisper Server with CMake
DESCRIPTION: Sets up the whisper-server target by defining source files, including dependencies, linking libraries, and handling platform-specific requirements. The configuration links the common, json_cpp, and whisper libraries, adds threading support, and includes Windows-specific socket libraries when building on Windows.

LANGUAGE: CMake
CODE:
set(TARGET whisper-server)
add_executable(${TARGET} server.cpp httplib.h)

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE common json_cpp whisper ${CMAKE_THREAD_LIBS_INIT})

if (WIN32)
    target_link_libraries(${TARGET} PRIVATE ws2_32)
endif()

install(TARGETS ${TARGET} RUNTIME)

----------------------------------------

TITLE: Running Transcription with Confidence Color-coding
DESCRIPTION: Executes the whisper-cli with color-coded confidence output for transcribed text.

LANGUAGE: bash
CODE:
./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/gb0.wav --print-colors

----------------------------------------

TITLE: Building whisper.cpp with OpenVINO Support
DESCRIPTION: Configures and builds the project with CMake, enabling OpenVINO support.

LANGUAGE: bash
CODE:
cmake -B build -DWHISPER_OPENVINO=1
cmake --build build -j --config Release

----------------------------------------

TITLE: Whisper Server Model Loading API Request
DESCRIPTION: cURL command example for loading a new model file into the server.

LANGUAGE: bash
CODE:
curl 127.0.0.1:8080/load \
-H "Content-Type: multipart/form-data" \
-F model="<path-to-model-file>"

----------------------------------------

TITLE: Building Whisper Command with SDL2 Dependencies
DESCRIPTION: Instructions for building the whisper-command tool with SDL2 library dependencies across different operating systems including Debian, Fedora, and MacOS.

LANGUAGE: bash
CODE:
# Install SDL2
# On Debian based linux distributions:
sudo apt-get install libsdl2-dev

# On Fedora Linux:
sudo dnf install SDL2 SDL2-devel

# Install SDL2 on Mac OS
brew install sdl2

cmake -B build -DWHISPER_SDL2=ON
cmake --build build --config Release

----------------------------------------

TITLE: Building Whisper.cpp with Core ML Support
DESCRIPTION: These commands build Whisper.cpp with Core ML support enabled, allowing for accelerated inference on Apple Silicon devices.

LANGUAGE: bash
CODE:
cmake -B build -DWHISPER_COREML=1
cmake --build build -j --config Release

----------------------------------------

TITLE: Creating Video Comparisons of Different Whisper Models
DESCRIPTION: Commands to generate a video that compares the transcription quality of different whisper.cpp models on the same audio input. Uses a dedicated script and ffmpeg to produce a side-by-side comparison.

LANGUAGE: bash
CODE:
./scripts/bench-wts.sh samples/jfk.wav
ffplay ./samples/jfk.wav.all.mp4

----------------------------------------

TITLE: Building and Running whisper-talk-llama with SDL2
DESCRIPTION: Instructions for installing SDL2 dependencies, building the whisper-talk-llama executable, and running it with specific command line arguments for Whisper and LLaMA models.

LANGUAGE: bash
CODE:
# Install SDL2
# On Debian based linux distributions:
sudo apt-get install libsdl2-dev

# On Fedora Linux:
sudo dnf install SDL2 SDL2-devel

# Install SDL2 on Mac OS
brew install sdl2

# Build the "whisper-talk-llama" executable
cmake -B build -S . -DWHISPER_SDL2=ON
cmake --build build --config Release

# Run it
./build/bin/whisper-talk-llama -mw ./models/ggml-small.en.bin -ml ../llama.cpp/models/llama-13b/ggml-model-q4_0.gguf -p "Georgi" -t 8

----------------------------------------

TITLE: Running Whisper Command with Default Settings
DESCRIPTION: Commands for running the voice assistant with default arguments and small model. Includes specific optimization parameters for Raspberry Pi deployment.

LANGUAGE: bash
CODE:
# Run with default arguments and small model
./whisper-command -m ./models/ggml-small.en.bin -t 8

# On Raspberry Pi, use tiny or base models + "-ac 768" for better performance
./whisper-command -m ./models/ggml-tiny.en.bin -ac 768 -t 3 -c 0

----------------------------------------

TITLE: Whisper Server Command Line Options
DESCRIPTION: Comprehensive list of command-line arguments for configuring the whisper.cpp server, including threading, processing, model, and server options.

LANGUAGE: plaintext
CODE:
./build/bin/whisper-server -h

usage: ./build/bin/whisper-server [options]

options:
  -h,        --help              [default] show this help message and exit
  -t N,      --threads N         [4      ] number of threads to use during computation
  -p N,      --processors N      [1      ] number of processors to use during computation
  -ot N,     --offset-t N        [0      ] time offset in milliseconds
  -on N,     --offset-n N        [0      ] segment index offset
  -d  N,     --duration N        [0      ] duration of audio to process in milliseconds
  -mc N,     --max-context N     [-1     ] maximum number of text context tokens to store
  -ml N,     --max-len N         [0      ] maximum segment length in characters
  -sow,      --split-on-word     [false  ] split on word rather than on token
  -bo N,     --best-of N         [2      ] number of best candidates to keep
  -bs N,     --beam-size N       [-1     ] beam size for beam search
  -wt N,     --word-thold N      [0.01   ] word timestamp probability threshold
  -et N,     --entropy-thold N   [2.40   ] entropy threshold for decoder fail
  -lpt N,    --logprob-thold N   [-1.00  ] log probability threshold for decoder fail
  -debug,    --debug-mode        [false  ] enable debug mode (eg. dump log_mel)
  -tr,       --translate         [false  ] translate from source language to english
  -di,       --diarize           [false  ] stereo audio diarization
  -tdrz,     --tinydiarize       [false  ] enable tinydiarize (requires a tdrz model)
  -nf,       --no-fallback       [false  ] do not use temperature fallback while decoding
  -ps,       --print-special     [false  ] print special tokens
  -pc,       --print-colors      [false  ] print colors
  -pr,       --print-realtime    [false  ] print output in realtime
  -pp,       --print-progress    [false  ] print progress
  -nt,       --no-timestamps     [false  ] do not print timestamps
  -l LANG,   --language LANG     [en     ] spoken language ('auto' for auto-detect)
  -dl,       --detect-language   [false  ] exit after automatically detecting language
             --prompt PROMPT     [       ] initial prompt
  -m FNAME,  --model FNAME       [models/ggml-base.en.bin] model path
  -oved D,   --ov-e-device DNAME [CPU    ] the OpenVINO device used for encode inference
  --host HOST,                   [127.0.0.1] Hostname/ip-adress for the server
  --port PORT,                   [8080   ] Port number for the server
  --convert,                     [false  ] Convert audio to WAV, requires ffmpeg on the server

----------------------------------------

TITLE: Building and Testing Whisper.cpp Java Bindings
DESCRIPTION: This bash script demonstrates how to clone the whisper.cpp repository, navigate to the Java bindings directory, and run the Gradle build process for testing the Java bindings.

LANGUAGE: bash
CODE:
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp/bindings/java

./gradlew build

----------------------------------------

TITLE: Quantizing Whisper Model
DESCRIPTION: This command quantizes a Whisper model using the Q5_0 method, which reduces model size and can improve inference speed.

LANGUAGE: bash
CODE:
./build/bin/quantize models/ggml-base.en.bin models/ggml-base.en-q5_0.bin q5_0

----------------------------------------

TITLE: GGML Backend Configuration Options
DESCRIPTION: Defines CMake options for various hardware acceleration backends and their settings, including CUDA, Metal, Vulkan, OpenCL, and others. Each option controls specific features and behaviors of the respective backend.

LANGUAGE: cmake
CODE:
option(GGML_ACCELERATE "ggml: enable Accelerate framework" ON)
option(GGML_BLAS "ggml: use BLAS" ${GGML_BLAS_DEFAULT})
set(GGML_BLAS_VENDOR ${GGML_BLAS_VENDOR_DEFAULT} CACHE STRING "ggml: BLAS library vendor")
option(GGML_LLAMAFILE "ggml: use LLAMAFILE" ${GGML_LLAMAFILE_DEFAULT})

----------------------------------------

TITLE: Downloading LibriSpeech Audio Files
DESCRIPTION: Command to download the necessary audio files from the LibriSpeech project for testing purposes.

LANGUAGE: bash
CODE:
$ make get-audio

----------------------------------------

TITLE: Running whisper-talk-llama with Session Support
DESCRIPTION: Example command for running whisper-talk-llama with session management enabled, which allows for maintaining conversation context across multiple interactions by saving and loading model state.

LANGUAGE: bash
CODE:
./build/bin/whisper-talk-llama --session ./my-session-file -mw ./models/ggml-small.en.bin -ml ../llama.cpp/models/llama-13b/ggml-model-q4_0.gguf -p "Georgi" -t 8

----------------------------------------

TITLE: Building whisper.cpp from the Project Root Directory
DESCRIPTION: Commands to compile the whisper-cli executable and download a model in ggml format. These steps are prerequisites for running the LibriSpeech tests.

LANGUAGE: bash
CODE:
$ # Execute the commands below in the project root dir.
$ cmake -B build
$ cmake --build build --config Release
$ ./models/download-ggml-model.sh tiny

----------------------------------------

TITLE: Starting a Local HTTP Server for Whisper.wasm
DESCRIPTION: This snippet demonstrates how to start a local HTTP server using Python to serve the Whisper.wasm example. It also provides the URL to access the example in a web browser.

LANGUAGE: console
CODE:
python3 examples/server.py

----------------------------------------

TITLE: Checking GPU Device Information
DESCRIPTION: Command to verify GPU device installation and configuration using clinfo

LANGUAGE: bash
CODE:
sudo apt install clinfo
sudo clinfo -l

----------------------------------------

TITLE: Running CI Locally for whisper.cpp
DESCRIPTION: Commands to execute the full CI process locally on your machine, with options for CPU-only build and CUDA support. Creates temporary directories for results and mounts, then runs the CI script.

LANGUAGE: bash
CODE:
mkdir tmp

# CPU-only build
bash ./ci/run.sh ./tmp/results ./tmp/mnt

# with CUDA support
GG_BUILD_CUDA=1 bash ./ci/run.sh ./tmp/results ./tmp/mnt

----------------------------------------

TITLE: Building Whisper.cpp with BLAS Support for POWER Architectures
DESCRIPTION: These commands build Whisper.cpp with BLAS support, which is optimized for POWER architectures running Linux.

LANGUAGE: bash
CODE:
cmake -B build -DGGML_BLAS=1
cmake --build build --config Release

----------------------------------------

TITLE: Building whisper.cpp with SYCL Support
DESCRIPTION: Commands for building whisper.cpp with SYCL support using CMake

LANGUAGE: bash
CODE:
mkdir -p build
cd build
source /opt/intel/oneapi/setvars.sh

#for FP16
#cmake .. -DWHISPER_SYCL=ON -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx -DWHISPER_SYCL_F16=ON 

#for FP32
cmake .. -DWHISPER_SYCL=ON -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx

#build example/main only
#cmake --build . --config Release --target main

#build all binary
cmake --build . --config Release -v

----------------------------------------

TITLE: Building whisper.cpp with Ascend NPU Support
DESCRIPTION: Configures and builds the project with CMake, enabling CANN support for Ascend NPU acceleration.

LANGUAGE: bash
CODE:
cmake -B build -DGGML_CANN=1
cmake --build build -j --config Release

----------------------------------------

TITLE: Running Benchmarks with Python Script in whisper.cpp
DESCRIPTION: Command to run the bench.py script for benchmarking whisper.cpp performance across different models and configurations. The script outputs a CSV file with benchmark results.

LANGUAGE: bash
CODE:
python3 scripts/bench.py -f samples/jfk.wav -t 2,4,8 -p 1,2

----------------------------------------

TITLE: Building the Whisper XCFramework for iOS
DESCRIPTION: Command to build the whisper.xcframework which is required for the Objective-C application to function. This framework needs to be built before using the application.

LANGUAGE: bash
CODE:
./build-xcframework.sh

----------------------------------------

TITLE: Building whisper.cpp WebAssembly Benchmark with Emscripten
DESCRIPTION: This snippet shows the commands to clone the whisper.cpp repository, create a build directory, and compile the project using Emscripten for WebAssembly. It requires Emscripten v3.1.2 to be installed.

LANGUAGE: bash
CODE:
# build using Emscripten (v3.1.2)
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
mkdir build-em && cd build-em
emcmake cmake ..
make -j

----------------------------------------

TITLE: Installing Python Dependencies for Core ML Model Creation
DESCRIPTION: This command installs the necessary Python packages to generate a Core ML model for use with Whisper.cpp on Apple Silicon devices.

LANGUAGE: bash
CODE:
pip install ane_transformers
pip install openai-whisper
pip install coremltools

----------------------------------------

TITLE: Starting a Local HTTP Server for Testing
DESCRIPTION: Command to start a Python-based HTTP server that hosts the WebAssembly application for local testing. This makes the stream.wasm demo accessible via a browser.

LANGUAGE: console
CODE:
python3 examples/server.py

----------------------------------------

TITLE: Whisper Server Inference API Request
DESCRIPTION: cURL command example for making an inference request to the server with a WAV file upload and processing parameters.

LANGUAGE: bash
CODE:
curl 127.0.0.1:8080/inference \
-H "Content-Type: multipart/form-data" \
-F file="@<file-path>" \
-F temperature="0.0" \
-F temperature_inc="0.2" \
-F response_format="json"

----------------------------------------

TITLE: Building the command.wasm Voice Assistant with Emscripten
DESCRIPTION: Build instructions for compiling the WebAssembly version of the command voice assistant using Emscripten v3.1.2. This process creates the necessary WebAssembly files that will run in the browser.

LANGUAGE: bash
CODE:
# build using Emscripten (v3.1.2)
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
mkdir build-em && cd build-em
emcmake cmake ..
make -j libcommand

----------------------------------------

TITLE: Building stream.wasm with Emscripten
DESCRIPTION: Commands to clone the whisper.cpp repository, create a build directory, and compile the project using Emscripten v3.1.2. This builds the WebAssembly version of the real-time transcription tool.

LANGUAGE: bash
CODE:
# build using Emscripten (v3.1.2)
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
mkdir build-em && cd build-em
emcmake cmake ..
make -j

----------------------------------------

TITLE: Building and Testing Whisper.cpp Go Bindings
DESCRIPTION: Commands for cloning the repository and running tests for the Go bindings. This process compiles a static library and downloads a model file for testing.

LANGUAGE: bash
CODE:
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp/bindings/go
make test

----------------------------------------

TITLE: Building whisper.cpp Stream Tool
DESCRIPTION: Commands to clone the whisper.cpp repository and build the stream tool needed for the plugin.

LANGUAGE: shell
CODE:
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make stream

----------------------------------------

TITLE: Configuring CPU Backend Variants with Architecture-Specific Flags in CMake
DESCRIPTION: This CMake function configures CPU backend variants for the GGML library. It manages architecture-specific source files, compilation flags, and feature detection. The function handles setting up dynamic loading capabilities, manages special cases for Emscripten compilation, and includes error handling for incompatible build options.

LANGUAGE: CMake
CODE:
list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p1x4_qsi4c32p4vlx4_1x4vl_sme2_sdot.c)
            set(PRIVATE_ARCH_FLAGS "${PRIVATE_ARCH_FLAGS}+sve+sve2")
        endif()

        set_source_files_properties(${GGML_KLEIDIAI_SOURCES} PROPERTIES COMPILE_OPTIONS "${PRIVATE_ARCH_FLAGS}")
        list(APPEND GGML_CPU_SOURCES ${GGML_KLEIDIAI_SOURCES})
    endif()

    message(STATUS "Adding CPU backend variant ${GGML_CPU_NAME}: ${ARCH_FLAGS} ${ARCH_DEFINITIONS}")
    target_sources(${GGML_CPU_NAME} PRIVATE ${GGML_CPU_SOURCES})
    target_compile_options(${GGML_CPU_NAME} PRIVATE ${ARCH_FLAGS})
    target_compile_definitions(${GGML_CPU_NAME} PRIVATE ${ARCH_DEFINITIONS})

    if (GGML_BACKEND_DL)
        if (GGML_NATIVE)
            # the feature check relies on ARCH_DEFINITIONS, but it is not set with GGML_NATIVE
            message(FATAL_ERROR "GGML_NATIVE is not compatible with GGML_BACKEND_DL, consider using GGML_CPU_ALL_VARIANTS")
        endif()

        # The feature detection code is compiled as a separate target so that
        # it can be built without the architecture flags
        # Since multiple variants of the CPU backend may be included in the same
        # build, using set_source_files_properties() to set the arch flags is not possible
        set(GGML_CPU_FEATS_NAME ${GGML_CPU_NAME}-feats)
        add_library(${GGML_CPU_FEATS_NAME} OBJECT ggml-cpu/cpu-feats-x86.cpp)
        target_include_directories(${GGML_CPU_FEATS_NAME} PRIVATE . .. ../include)
        target_compile_definitions(${GGML_CPU_FEATS_NAME} PRIVATE ${ARCH_DEFINITIONS})
        target_compile_definitions(${GGML_CPU_FEATS_NAME} PRIVATE GGML_BACKEND_DL GGML_BACKEND_BUILD GGML_BACKEND_SHARED)
        set_target_properties(${GGML_CPU_FEATS_NAME} PROPERTIES POSITION_INDEPENDENT_CODE ON)
        target_link_libraries(${GGML_CPU_NAME} PRIVATE ${GGML_CPU_FEATS_NAME})
    endif()

    if (EMSCRIPTEN)
        set_target_properties(${GGML_CPU_NAME} PROPERTIES COMPILE_FLAGS "-msimd128")
    endif()
endfunction()

----------------------------------------

TITLE: Downloading a Whisper Model
DESCRIPTION: Command to download the base English model required for speech recognition. The model is necessary for the application to perform transcription.

LANGUAGE: bash
CODE:
./models/download-ggml-model.sh base.en

----------------------------------------

TITLE: Sample GPU Device Output
DESCRIPTION: Example output showing detected Intel GPU devices

LANGUAGE: plaintext
CODE:
Platform #0: Intel(R) OpenCL Graphics
 `-- Device #0: Intel(R) Arc(TM) A770 Graphics


Platform #0: Intel(R) OpenCL HD Graphics
 `-- Device #0: Intel(R) Iris(R) Xe Graphics [0x9a49]

----------------------------------------

TITLE: Converting Distilled Whisper Models to ggml Format
DESCRIPTION: Bash script demonstrating how to convert distilled Whisper models from Hugging Face to ggml format. The process includes cloning repositories, downloading the models, and running conversion scripts for two different model sizes.

LANGUAGE: bash
CODE:
# clone OpenAI whisper and whisper.cpp
git clone https://github.com/openai/whisper
git clone https://github.com/ggml-org/whisper.cpp

# get the models
cd whisper.cpp/models
git clone https://huggingface.co/distil-whisper/distil-medium.en
git clone https://huggingface.co/distil-whisper/distil-large-v2

# convert to ggml
python3 ./convert-h5-to-ggml.py ./distil-medium.en/ ../../whisper .
mv ggml-model.bin ggml-medium.en-distil.bin

python3 ./convert-h5-to-ggml.py ./distil-large-v2/ ../../whisper .
mv ggml-model.bin ggml-large-v2-distil.bin

----------------------------------------

TITLE: Generating OpenVINO Encoder Model
DESCRIPTION: Converts a Whisper model to OpenVINO format using a Python script.

LANGUAGE: bash
CODE:
python convert-whisper-to-openvino.py --model base.en

----------------------------------------

TITLE: Running the Whisper Stream Tool
DESCRIPTION: Command to run the stream tool with suggested parameters for real-time transcription. The step parameter can be increased on slower machines.

LANGUAGE: shell
CODE:
./stream -t 8 -m models/ggml-base.en.bin --step 350 --length 10000 -f /tmp/whisper.nvim 2> /dev/null

----------------------------------------

TITLE: Building Main whisper Library
DESCRIPTION: Defines and configures the main whisper library target with version properties, includes, dependencies, and platform-specific settings. Integrates with optional components like CoreML, OpenVINO, and MKL based on build configuration.

LANGUAGE: cmake
CODE:
add_library(whisper
            ../include/whisper.h
            whisper-arch.h
            whisper.cpp
            )

# Set the version numbers
set_target_properties(whisper PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION ${SOVERSION}
)

target_include_directories(whisper PUBLIC . ../include)
target_compile_features   (whisper PUBLIC cxx_std_11) # don't bump

if (CMAKE_CXX_BYTE_ORDER STREQUAL "BIG_ENDIAN")
    set(WHISPER_EXTRA_FLAGS ${WHISPER_EXTRA_FLAGS} -DWHISPER_BIG_ENDIAN)
endif()

if (WHISPER_EXTRA_FLAGS)
    target_compile_options(whisper PRIVATE ${WHISPER_EXTRA_FLAGS})
endif()

target_link_libraries(whisper PUBLIC ggml)

if (WHISPER_COREML)
    target_link_libraries(whisper PRIVATE whisper.coreml)
endif()

if (WHISPER_OPENVINO)
    target_link_libraries(whisper PRIVATE whisper.openvino)
endif()

if (WHISPER_MKL)
    target_link_libraries(whisper PRIVATE MKL::MKL)
endif()

if (BUILD_SHARED_LIBS)
    set_target_properties(whisper PROPERTIES POSITION_INDEPENDENT_CODE ON)
    target_compile_definitions(whisper PRIVATE WHISPER_SHARED WHISPER_BUILD)
endif()

----------------------------------------

TITLE: Configuring Model and Sample Paths in WhisperService.java
DESCRIPTION: Modify the modelFilePath and sampleFilePath variables in the WhisperService.java file to specify the locations of the chosen whisper model and audio sample file.

LANGUAGE: Java
CODE:
// In WhisperService.java
String modelFilePath = "path/to/your/model/file";
String sampleFilePath = "path/to/your/sample/audio/file";

----------------------------------------

TITLE: Basic Usage of Whisper.cpp Go Bindings
DESCRIPTION: Demonstrates the most basic usage pattern for the Go bindings, including loading a model, processing audio samples, and retrieving transcription segments.

LANGUAGE: go
CODE:
import (
	"github.com/ggerganov/whisper.cpp/bindings/go/pkg/whisper"
)

func main() {
	var modelpath string // Path to the model
	var samples []float32 // Samples to process

	// Load the model
	model, err := whisper.New(modelpath)
	if err != nil {
		panic(err)
	}
	defer model.Close()

	// Process samples
	context, err := model.NewContext()
	if err != nil {
		panic(err)
	}
	if err := context.Process(samples, nil, nil, nil); err != nil {
		return err
	}

	// Print out the results
	for {
		segment, err := context.NextSegment()
		if err != nil {
			break
		}
		fmt.Printf("[%6s->%6s] %s\n", segment.Start, segment.End, segment.Text)
	}
}

----------------------------------------

TITLE: Using Low-level API with Ruby Arrays in Whisper
DESCRIPTION: Shows how to use the low-level API (#full and #full_parallel) with Ruby arrays as audio samples. This gives more flexibility but may be slower than the recommended file-based transcription method.

LANGUAGE: ruby
CODE:
require "whisper"
require "wavefile"

reader = WaveFile::Reader.new("path/to/audio.wav", WaveFile::Format.new(:mono, :float, 16000))
samples = reader.enum_for(:each_buffer).map(&:samples).flatten

whisper = Whisper::Context.new("base")
whisper
  .full(Whisper::Params.new, samples)
  .each_segment do |segment|
    puts segment.text
  end

----------------------------------------

TITLE: Setting up OpenVINO Environment (Linux)
DESCRIPTION: Sources the OpenVINO setup script to configure the environment on Linux.

LANGUAGE: bash
CODE:
source /path/to/l_openvino_toolkit_ubuntu22_2023.0.0.10926.b4452d56304_x86_64/setupvars.sh

----------------------------------------

TITLE: Compiling Whisper.cpp Node.js Addon with Custom CMake Path
DESCRIPTION: Example command showing how to compile the addon while specifying a custom CMake path using the '-c' option in cmake-js.

LANGUAGE: shell
CODE:
npx cmake-js compile -c 'xxx/cmake' -T addon.node -B Release

----------------------------------------

TITLE: Configuring Whisper-Talk-Llama Build with SDL2 in CMake
DESCRIPTION: Sets up the build configuration for the whisper-talk-llama executable. It includes necessary source files, links required libraries, and sets compiler options. The build is conditional on WHISPER_SDL2 being enabled and includes special handling for Windows platforms.

LANGUAGE: CMake
CODE:
if (WHISPER_SDL2)
    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)

    set(TARGET whisper-talk-llama)
    add_executable(${TARGET} talk-llama.cpp
        llama.cpp
        llama-adapter.cpp
        llama-arch.cpp
        llama-batch.cpp
        llama-chat.cpp
        llama-context.cpp
        llama-cparams.cpp
        llama-grammar.cpp
        llama-hparams.cpp
        llama-impl.cpp
        llama-kv-cache.cpp
        llama-mmap.cpp
        llama-model-loader.cpp
        llama-model.cpp
        llama-quant.cpp
        llama-sampling.cpp
        llama-vocab.cpp
        unicode.cpp
        unicode-data.cpp)
    target_include_directories(${TARGET} PRIVATE ${SDL2_INCLUDE_DIRS})

    target_link_libraries(${TARGET} PRIVATE common common-sdl whisper ${SDL2_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT})

    if(WIN32)
        # It requires Windows 8.1 or later for PrefetchVirtualMemory
        target_compile_definitions(${TARGET} PRIVATE -D_WIN32_WINNT=0x0602)
    endif()

    include(DefaultTargetOptions)
endif ()

----------------------------------------

TITLE: Running the command.wasm Example with a Local HTTP Server
DESCRIPTION: Commands to start a Python-based HTTP server that hosts the WebAssembly example. This allows testing the voice assistant in a browser on the local machine.

LANGUAGE: console
CODE:
python3 examples/server.py

----------------------------------------

TITLE: Downloading and Converting Audio Samples in Makefile for whisper.cpp
DESCRIPTION: This Makefile snippet defines a 'samples' target that downloads various public audio files and converts them to 16-bit WAV format using ffmpeg. It includes samples from different sources such as OSR, Common Voice, and specific YouTube videos.

LANGUAGE: Makefile
CODE:
samples:
	@echo "Downloading samples..."
	@mkdir -p samples
	whisper.cpp/wget -q --show-progress https://github.com/ggerganov/whisper.cpp/raw/master/samples/jfk.wav -O samples/jfk.wav
	whisper.cpp/wget -q --show-progress https://github.com/ggerganov/whisper.cpp/raw/master/samples/gb0.wav -O samples/gb0.wav
	whisper.cpp/wget -q --show-progress https://github.com/ggerganov/whisper.cpp/raw/master/samples/gb1.wav -O samples/gb1.wav
	whisper.cpp/wget -q --show-progress https://github.com/ggerganov/whisper.cpp/raw/master/samples/hp0.wav -O samples/hp0.wav
	whisper.cpp/wget -q --show-progress https://github.com/ggerganov/whisper.cpp/raw/master/samples/output-001.wav -O samples/output-001.wav
	ffmpeg -i https://www.youtube.com/watch?v=HYuCa0Regx8 -ar 16000 -ac 1 -c:a pcm_s16le samples/test-001.wav
	ffmpeg -i https://www.youtube.com/watch?v=PXi3Mv6KMzY -ar 16000 -ac 1 -c:a pcm_s16le samples/test-002.wav
	ffmpeg -i https://www.youtube.com/watch?v=b-r5BM0lJpQ -ar 16000 -ac 1 -c:a pcm_s16le samples/test-003.wav
	@echo "Done"

----------------------------------------

TITLE: Compiling Language Server for Whisper.cpp
DESCRIPTION: Command to compile the language server for Whisper.cpp transcription integration.

LANGUAGE: bash
CODE:
make lsp

----------------------------------------

TITLE: Copying Whisper.wasm Files to a Web Server
DESCRIPTION: This snippet shows the commands to copy the necessary Whisper.wasm files to a web server's HTTP path. It includes the WebAssembly file and the worker JavaScript file.

LANGUAGE: console
CODE:
# copy the produced page to your HTTP path
cp bin/whisper.wasm/*    /path/to/html/
cp bin/libmain.worker.js /path/to/html/

----------------------------------------

TITLE: Running whisper.cpp with SYCL
DESCRIPTION: Command to run whisper.cpp with SYCL using specific GPU device

LANGUAGE: bash
CODE:
GGML_SYCL_DEVICE=0 ./build/bin/main -m models/ggml-base.en.bin -f samples/jfk.wav

----------------------------------------

TITLE: Configuring GGML CPU Backend with CMake
DESCRIPTION: CMake function to configure GGML CPU backend variants with architecture-specific optimizations. Handles platform detection, compiler flags, dependencies like OpenMP and Accelerate framework, and sets up CPU-specific source files.

LANGUAGE: cmake
CODE:
function(ggml_add_cpu_backend_variant_impl tag_name)
    if (tag_name)
        set(GGML_CPU_NAME ggml-cpu-${tag_name})
    else()
        set(GGML_CPU_NAME ggml-cpu)
    endif()

    ggml_add_backend_library(${GGML_CPU_NAME})

    list (APPEND GGML_CPU_SOURCES
        ggml-cpu/ggml-cpu.c
        ggml-cpu/ggml-cpu.cpp
        ggml-cpu/ggml-cpu-aarch64.cpp
        ggml-cpu/ggml-cpu-aarch64.h
        ggml-cpu/ggml-cpu-hbm.cpp
        ggml-cpu/ggml-cpu-hbm.h
        ggml-cpu/ggml-cpu-quants.c
        ggml-cpu/ggml-cpu-quants.h
        ggml-cpu/ggml-cpu-traits.cpp
        ggml-cpu/ggml-cpu-traits.h
        ggml-cpu/amx/amx.cpp
        ggml-cpu/amx/amx.h
        ggml-cpu/amx/mmq.cpp
        ggml-cpu/amx/mmq.h
        ggml-cpu/ggml-cpu-impl.h
        ggml-cpu/common.h
        ggml-cpu/binary-ops.h
        ggml-cpu/binary-ops.cpp
        ggml-cpu/unary-ops.h
        ggml-cpu/unary-ops.cpp
        ggml-cpu/simd-mappings.h
        ggml-cpu/vec.h
        ggml-cpu/vec.cpp
        ggml-cpu/ops.h
        ggml-cpu/ops.cpp
        )

    target_compile_features(${GGML_CPU_NAME} PRIVATE c_std_11 cxx_std_17)
    target_include_directories(${GGML_CPU_NAME} PRIVATE . ggml-cpu)

    if (APPLE AND GGML_ACCELERATE)
        find_library(ACCELERATE_FRAMEWORK Accelerate)
        if (ACCELERATE_FRAMEWORK)
            message(STATUS "Accelerate framework found")

            target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_ACCELERATE)
            target_compile_definitions(${GGML_CPU_NAME} PRIVATE ACCELERATE_NEW_LAPACK)
            target_compile_definitions(${GGML_CPU_NAME} PRIVATE ACCELERATE_LAPACK_ILP64)

            target_link_libraries(${GGML_CPU_NAME} PRIVATE ${ACCELERATE_FRAMEWORK})
        else()
            message(WARNING "Accelerate framework not found")
        endif()
    endif()

    if (GGML_OPENMP)
        find_package(OpenMP)
        if (OpenMP_FOUND)
            target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_OPENMP)

            target_link_libraries(${GGML_CPU_NAME} PRIVATE OpenMP::OpenMP_C OpenMP::OpenMP_CXX)
        else()
            message(WARNING "OpenMP not found")
        endif()
    endif()

    if (GGML_LLAMAFILE)
        target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_LLAMAFILE)

        list(APPEND GGML_CPU_SOURCES
                    ggml-cpu/llamafile/sgemm.cpp
                    ggml-cpu/llamafile/sgemm.h)
    endif()

    if (GGML_CPU_HBM)
        find_library(memkind memkind REQUIRED)

        message(STATUS "Using memkind for CPU HBM")

        target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_CPU_HBM)

        target_link_libraries(${GGML_CPU_NAME} PUBLIC memkind)
    endif()

    if (CMAKE_OSX_ARCHITECTURES      STREQUAL "arm64" OR
        CMAKE_GENERATOR_PLATFORM_LWR STREQUAL "arm64" OR
        (NOT CMAKE_OSX_ARCHITECTURES AND NOT CMAKE_GENERATOR_PLATFORM_LWR AND
            CMAKE_SYSTEM_PROCESSOR MATCHES "^(aarch64|arm.*|ARM64)$"))

        message(STATUS "ARM detected")

        if (MSVC AND NOT CMAKE_C_COMPILER_ID STREQUAL "Clang")
            message(FATAL_ERROR "MSVC is not supported for ARM, use clang")
        else()
            check_cxx_compiler_flag(-mfp16-format=ieee GGML_COMPILER_SUPPORTS_FP16_FORMAT_I3E)
            if (NOT "${GGML_COMPILER_SUPPORTS_FP16_FORMAT_I3E}" STREQUAL "")
                list(APPEND ARCH_FLAGS -mfp16-format=ieee)
            endif()

            if (GGML_NATIVE)
                execute_process(
                    COMMAND ${CMAKE_C_COMPILER} -mcpu=native -E -v -
                    INPUT_FILE "/dev/null"
                    OUTPUT_QUIET
                    ERROR_VARIABLE ARM_MCPU
                    RESULT_VARIABLE ARM_MCPU_RESULT
                )
                if (NOT ARM_MCPU_RESULT)
                    string(REGEX MATCH "-mcpu=[^ ']+" ARM_MCPU_FLAG "${ARM_MCPU}")
                endif()
                if ("${ARM_MCPU_FLAG}" STREQUAL "")
                    set(ARM_MCPU_FLAG -mcpu=native)
                    message(STATUS "ARM -mcpu not found, -mcpu=native will be used")
                endif()

                include(CheckCXXSourceRuns)

                function(check_arm_feature tag code)
                    set(CMAKE_REQUIRED_FLAGS_SAVE ${CMAKE_REQUIRED_FLAGS})
                    set(CMAKE_REQUIRED_FLAGS "${ARM_MCPU_FLAG}+${tag}")
                    check_cxx_source_runs("${code}" GGML_MACHINE_SUPPORTS_${tag})
                    if (GGML_MACHINE_SUPPORTS_${tag})
                        set(ARM_MCPU_FLAG_FIX "${ARM_MCPU_FLAG_FIX}+${tag}" PARENT_SCOPE)
                    else()
                        set(CMAKE_REQUIRED_FLAGS "${ARM_MCPU_FLAG}+no${tag}")
                        check_cxx_source_compiles("int main() { return 0; }" GGML_MACHINE_SUPPORTS_no${tag})
                        if (GGML_MACHINE_SUPPORTS_no${tag})
                            set(ARM_MCPU_FLAG_FIX "${ARM_MCPU_FLAG_FIX}+no${tag}" PARENT_SCOPE)
                        endif()
                    endif()
                    set(CMAKE_REQUIRED_FLAGS ${CMAKE_REQUIRED_FLAGS_SAVE})
                endfunction()

                check_arm_feature(dotprod "#include <arm_neon.h>\nint main() { int8x16_t _a, _b; volatile int32x4_t _s = vdotq_s32(_s, _a, _b); return 0; }")
                check_arm_feature(i8mm    "#include <arm_neon.h>\nint main() { int8x16_t _a, _b; volatile int32x4_t _s = vmmlaq_s32(_s, _a, _b); return 0; }")
                check_arm_feature(sve     "#include <arm_sve.h>\nint main()  { svfloat32_t _a, _b; volatile svfloat32_t _c = svadd_f32_z(svptrue_b8(), _a, _b); return 0; }")
                check_arm_feature(sme     "#include <arm_sme.h>\n__arm_locally_streaming int main() { __asm__ volatile(\"smstart; smstop;\"); return 0; }")

                list(APPEND ARCH_FLAGS "${ARM_MCPU_FLAG}${ARM_MCPU_FLAG_FIX}")
            else()
                if (GGML_CPU_ARM_ARCH)
                    list(APPEND ARCH_FLAGS -march=${GGML_CPU_ARM_ARCH})
                endif()
            endif()

            if (CMAKE_HOST_SYSTEM_NAME STREQUAL "Windows")
                set(FEAT_INPUT_FILE "NUL")
            else()
                set(FEAT_INPUT_FILE "/dev/null")
            endif()

            execute_process(
                COMMAND ${CMAKE_C_COMPILER} ${ARCH_FLAGS} -dM -E -
                INPUT_FILE ${FEAT_INPUT_FILE}
                OUTPUT_VARIABLE ARM_FEATURE
                RESULT_VARIABLE ARM_FEATURE_RESULT
            )
            if (ARM_FEATURE_RESULT)
                message(WARNING "Failed to get ARM features")
            else()
                foreach(feature DOTPROD SVE MATMUL_INT8 FMA FP16_VECTOR_ARITHMETIC SME)
                    string(FIND "${ARM_FEATURE}" "__ARM_FEATURE_${feature} 1" feature_pos)
                    if (NOT ${feature_pos} EQUAL -1)
                        message(STATUS "ARM feature ${feature} enabled")
                    endif()
                endforeach()
            endif()
        endif()
    elseif (CMAKE_OSX_ARCHITECTURES STREQUAL "x86_64" OR CMAKE_GENERATOR_PLATFORM_LWR MATCHES "^(x86_64|i686|amd64|x64|win32)$" OR
            (NOT CMAKE_OSX_ARCHITECTURES AND NOT CMAKE_GENERATOR_PLATFORM_LWR AND
            CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|i686|AMD64|amd64)$"))

        message(STATUS "x86 detected")

        if (MSVC)
            if (GGML_NATIVE)
                include(ggml-cpu/cmake/FindSIMD.cmake)
            endif ()
            if (GGML_AVX512)
                list(APPEND ARCH_FLAGS /arch:AVX512)
                list(APPEND ARCH_DEFINITIONS GGML_AVX512)
                if (GGML_AVX512_VBMI)
                    list(APPEND ARCH_DEFINITIONS __AVX512VBMI__)
                    if (CMAKE_C_COMPILER_ID STREQUAL "Clang")
                        list(APPEND ARCH_FLAGS -mavx512vbmi)
                    endif()
                endif()
                if (GGML_AVX512_VNNI)
                    list(APPEND ARCH_DEFINITIONS __AVX512VNNI__ GGML_AVX512_VNNI)
                    if (CMAKE_C_COMPILER_ID STREQUAL "Clang")
                        list(APPEND ARCH_FLAGS -mavx512vnni)
                    endif()
                endif()
                if (GGML_AVX512_BF16)
                    list(APPEND ARCH_DEFINITIONS __AVX512BF16__ GGML_AVX512_BF16)
                    if (CMAKE_C_COMPILER_ID STREQUAL "Clang")
                        list(APPEND ARCH_FLAGS -mavx512bf16)
                    endif()
                endif()
                if (GGML_AMX_TILE)
                    list(APPEND ARCH_DEFINITIONS __AMX_TILE__ GGML_AMX_TILE)
                endif()
                if (GGML_AMX_INT8)
                    list(APPEND ARCH_DEFINITIONS __AMX_INT8__ GGML_AMX_INT8)
                endif()
                if (GGML_AMX_BF16)
                    list(APPEND ARCH_DEFINITIONS __AMX_BF16__ GGML_AMX_BF16)
                endif()
            elseif (GGML_AVX2)
                list(APPEND ARCH_FLAGS /arch:AVX2)
                list(APPEND ARCH_DEFINITIONS GGML_AVX2 GGML_FMA GGML_F16C)
            elseif (GGML_AVX)
                list(APPEND ARCH_FLAGS /arch:AVX)
                list(APPEND ARCH_DEFINITIONS GGML_AVX)
            else ()
                list(APPEND ARCH_FLAGS /arch:SSE4.2)
                list(APPEND ARCH_DEFINITIONS GGML_SSE42)
            endif()
            if (GGML_AVX_VNNI)
                list(APPEND ARCH_DEFINITIONS __AVXVNNI__ GGML_AVX_VNNI)
            endif()
            if (GGML_BMI2)

----------------------------------------

TITLE: Building Whisper.cpp XCFramework in Bash
DESCRIPTION: Command to build the whisper.cpp XCFramework, which is required for the SwiftUI app. This should be run from the whisper.cpp project root.

LANGUAGE: bash
CODE:
$ ./build-xcframework.sh

----------------------------------------

TITLE: Benchmarking Whisper Models on V100 GPU with Flash Attention Enabled
DESCRIPTION: Runs performance tests on various Whisper models (tiny through large-v3-turbo) on V100 GPU with CUDA, using 8 threads and with flash attention enabled. Shows encoding, decoding, batch processing, and prompt processing times.

LANGUAGE: bash
CODE:
WHISPER_CUDA=1 make -j && ./scripts/bench-all.sh 8 1 1

----------------------------------------

TITLE: Creating a Dummy Core ML Model Directory
DESCRIPTION: Command to create a dummy model directory if you don't want to convert a Core ML model. This allows the application to run without requiring Core ML conversion.

LANGUAGE: bash
CODE:
mkdir models/ggml-base.en-encoder.mlmodelc

----------------------------------------

TITLE: Setting Up Python Environment for WER Calculation
DESCRIPTION: Commands to install the required Python dependencies for computing Word Error Rate (WER) scores when evaluating speech recognition accuracy.

LANGUAGE: bash
CODE:
$ pip install -r requirements.txt

----------------------------------------

TITLE: Running the Benchmark Test
DESCRIPTION: Command to execute the benchmark evaluation of whisper.cpp against the LibriSpeech dataset.

LANGUAGE: bash
CODE:
$ make

----------------------------------------

TITLE: Configuring Whisper Stream Target with SDL2 in CMake
DESCRIPTION: This CMake snippet conditionally builds the whisper-stream executable when SDL2 support is enabled. It sets up the target using stream.cpp as the source file, includes default target options, links necessary libraries including SDL components, and configures installation parameters.

LANGUAGE: cmake
CODE:
if (WHISPER_SDL2)
    set(TARGET whisper-stream)
    add_executable(${TARGET} stream.cpp)

    include(DefaultTargetOptions)

    target_link_libraries(${TARGET} PRIVATE common common-sdl whisper ${CMAKE_THREAD_LIBS_INIT})

    install(TARGETS ${TARGET} RUNTIME)
endif ()

----------------------------------------

TITLE: Configuring Instruction Set Specific Options
DESCRIPTION: Sets options for CPU-specific instruction set optimizations including AVX, AVX2, BMI2, AVX512, and various other architecture-specific features.

LANGUAGE: CMake
CODE:
# instruction set specific
if (GGML_NATIVE OR NOT GGML_NATIVE_DEFAULT)
    set(INS_ENB OFF)
else()
    set(INS_ENB ON)
endif()

message(DEBUG "GGML_NATIVE         : ${GGML_NATIVE}")
message(DEBUG "GGML_NATIVE_DEFAULT : ${GGML_NATIVE_DEFAULT}")
message(DEBUG "INS_ENB             : ${INS_ENB}")

option(GGML_CPU_HBM          "ggml: use memkind for CPU HBM" OFF)
option(GGML_CPU_AARCH64      "ggml: use runtime weight conversion of Q4_0 to Q4_X_X" ON)
option(GGML_CPU_KLEIDIAI     "ggml: use KleidiAI optimized kernels if applicable" OFF)
option(GGML_AVX              "ggml: enable AVX"              ${INS_ENB})
option(GGML_AVX_VNNI         "ggml: enable AVX-VNNI"         OFF)
option(GGML_AVX2             "ggml: enable AVX2"             ${INS_ENB})
option(GGML_BMI2             "ggml: enable BMI2"             ${INS_ENB})
option(GGML_AVX512           "ggml: enable AVX512F"          OFF)
option(GGML_AVX512_VBMI      "ggml: enable AVX512-VBMI"      OFF)
option(GGML_AVX512_VNNI      "ggml: enable AVX512-VNNI"      OFF)
option(GGML_AVX512_BF16      "ggml: enable AVX512-BF16"      OFF)
if (NOT MSVC)
    # in MSVC F16C and FMA is implied with AVX2/AVX512
    option(GGML_FMA          "ggml: enable FMA"              ${INS_ENB})
    option(GGML_F16C         "ggml: enable F16C"             ${INS_ENB})
    # MSVC does not seem to support AMX
    option(GGML_AMX_TILE     "ggml: enable AMX-TILE"         OFF)
    option(GGML_AMX_INT8     "ggml: enable AMX-INT8"         OFF)
    option(GGML_AMX_BF16     "ggml: enable AMX-BF16"         OFF)
endif()
option(GGML_LASX             "ggml: enable lasx"             ON)
option(GGML_LSX              "ggml: enable lsx"              ON)
option(GGML_RVV              "ggml: enable rvv"              ON)
option(GGML_RV_ZFH           "ggml: enable riscv zfh"        OFF)
option(GGML_VXE              "ggml: enable vxe"              ON)

----------------------------------------

TITLE: Setting Up Virtual Environment for Dependencies
DESCRIPTION: Optional commands for setting up a Python virtual environment before installing the required dependencies.

LANGUAGE: bash
CODE:
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt

----------------------------------------

TITLE: Copying WebAssembly Files for Deployment
DESCRIPTION: These commands copy the necessary WebAssembly and JavaScript files to a specified HTTP path for deployment on a different server. This step is required when not using the local Python server.

LANGUAGE: bash
CODE:
# copy the produced page to your HTTP path
cp bin/bench.wasm/*       /path/to/html/
cp bin/libbench.worker.js /path/to/html/

----------------------------------------

TITLE: Building Examples for Whisper.cpp Go Bindings
DESCRIPTION: Command to build example applications that demonstrate the Go bindings functionality.

LANGUAGE: bash
CODE:
make examples

----------------------------------------

TITLE: Downloading Model Files for Whisper.cpp
DESCRIPTION: Command to download all available models using the go-model-download utility, placing them in a models directory.

LANGUAGE: bash
CODE:
./build/go-model-download -out models

----------------------------------------

TITLE: Building and Testing Whisper.cpp Node.js Package
DESCRIPTION: Commands for setting up, building, and testing the Whisper.cpp Node.js integration. Includes steps for loading emscripten, cloning the repo, downloading the model, preparing audio samples, and building/testing the package.

LANGUAGE: bash
CODE:
# load emscripten
source /path/to/emsdk/emsdk_env.sh

# clone repo
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp

# grab base.en model
./models/download-ggml-model.sh base.en

# prepare PCM sample for testing
ffmpeg -i samples/jfk.wav -f f32le -acodec pcm_f32le samples/jfk.pcmf32

# build
mkdir build-em && cd build-em
emcmake cmake .. && make -j

# run test
node ../tests/test-whisper.js

# For Node.js versions prior to v16.4.0, experimental features need to be enabled:
node --experimental-wasm-threads --experimental-wasm-simd ../tests/test-whisper.js

# publish npm package
make publish-npm

----------------------------------------

TITLE: Installation Configuration for whisper.cpp
DESCRIPTION: Sets up the installation process for the whisper library, including package configuration files, version information, and pkg-config. Configures paths for header, library, and binary files.

LANGUAGE: CMake
CODE:
#
# install
#

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

set(WHISPER_BUILD_NUMBER        ${BUILD_NUMBER})
set(WHISPER_BUILD_COMMIT        ${BUILD_COMMIT})
set(WHISPER_INSTALL_VERSION     ${CMAKE_PROJECT_VERSION})

set(WHISPER_INCLUDE_INSTALL_DIR ${CMAKE_INSTALL_INCLUDEDIR} CACHE PATH "Location of header  files")
set(WHISPER_LIB_INSTALL_DIR     ${CMAKE_INSTALL_LIBDIR}     CACHE PATH "Location of library files")
set(WHISPER_BIN_INSTALL_DIR     ${CMAKE_INSTALL_BINDIR}     CACHE PATH "Location of binary  files")

get_directory_property(WHISPER_TRANSIENT_DEFINES COMPILE_DEFINITIONS)

set_target_properties(whisper PROPERTIES PUBLIC_HEADER ${CMAKE_CURRENT_SOURCE_DIR}/include/whisper.h)
install(TARGETS whisper LIBRARY PUBLIC_HEADER)

configure_package_config_file(
        ${CMAKE_CURRENT_SOURCE_DIR}/cmake/whisper-config.cmake.in
        ${CMAKE_CURRENT_BINARY_DIR}/whisper-config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/whisper
    PATH_VARS
    WHISPER_INCLUDE_INSTALL_DIR
    WHISPER_LIB_INSTALL_DIR
    WHISPER_BIN_INSTALL_DIR )

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/whisper-version.cmake
    VERSION ${WHISPER_INSTALL_VERSION}
    COMPATIBILITY SameMajorVersion)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/whisper-config.cmake
              ${CMAKE_CURRENT_BINARY_DIR}/whisper-version.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/whisper)

configure_file(cmake/whisper.pc.in
        "${CMAKE_CURRENT_BINARY_DIR}/whisper.pc"
        @ONLY)

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/whisper.pc"
        DESTINATION lib/pkgconfig)

----------------------------------------

TITLE: Configuring Whisper.cpp Directory Path in Vim
DESCRIPTION: Vim configuration snippet for setting the Whisper.cpp directory path using path expansion.

LANGUAGE: vim
CODE:
let g:whisper_dir = expand("~/whisper.cpp/")

----------------------------------------

TITLE: Adding User to GPU Groups in Linux
DESCRIPTION: Commands to add current user to render and video groups for GPU access permissions

LANGUAGE: bash
CODE:
sudo usermod -aG render username
sudo usermod -aG video username

----------------------------------------

TITLE: Building whisper.coreml Library
DESCRIPTION: Defines and configures the whisper.coreml library when CoreML integration is enabled. Sets up source files, include directories, framework dependencies, and Objective-C configuration options.

LANGUAGE: cmake
CODE:
if (WHISPER_COREML)
    set(TARGET whisper.coreml)

    add_library(${TARGET}
        coreml/whisper-encoder.h
        coreml/whisper-encoder.mm
        coreml/whisper-encoder-impl.h
        coreml/whisper-encoder-impl.m
        )

    include(DefaultTargetOptions)

    target_include_directories(${TARGET} PUBLIC
        .
        )

    target_link_libraries(${TARGET} PRIVATE ${FOUNDATION_FRAMEWORK} ${COREML_FRAMEWORK})

    set_target_properties(${TARGET} PROPERTIES
        COMPILE_FLAGS "-fobjc-arc"
        XCODE_ATTRIBUTE_CLANG_ENABLE_OBJC_ARC YES
        )
    set_target_properties(${TARGET} PROPERTIES FOLDER "libs")
endif()

----------------------------------------

TITLE: Setting up OpenVINO Environment (Windows)
DESCRIPTION: Runs the OpenVINO setup script to configure the environment on Windows.

LANGUAGE: powershell
CODE:
C:\Path\To\w_openvino_toolkit_windows_2023.0.0.10926.b4452d56304_x86_64\setupvars.bat

----------------------------------------

TITLE: Creating and Configuring the ggml-hip Backend Library
DESCRIPTION: Adds the ggml-hip backend library and configures compilation definitions based on various feature flags. Sets up language handling for source files based on whether hipcc is being used.

LANGUAGE: CMake
CODE:
ggml_add_backend_library(ggml-hip
                         ${GGML_HEADERS_ROCM}
                         ${GGML_SOURCES_ROCM}
                        )

# TODO: do not use CUDA definitions for HIP
if (NOT GGML_BACKEND_DL)
    target_compile_definitions(ggml PUBLIC GGML_USE_CUDA)
endif()

add_compile_definitions(GGML_USE_HIP)

if (GGML_HIP_UMA)
    add_compile_definitions(GGML_HIP_UMA)
endif()

if (GGML_CUDA_FORCE_MMQ)
    add_compile_definitions(GGML_CUDA_FORCE_MMQ)
endif()

if (GGML_CUDA_FORCE_CUBLAS)
    add_compile_definitions(GGML_CUDA_FORCE_CUBLAS)
endif()

if (GGML_CUDA_NO_PEER_COPY)
    add_compile_definitions(GGML_CUDA_NO_PEER_COPY)
endif()

if (GGML_HIP_GRAPHS)
    add_compile_definitions(GGML_HIP_GRAPHS)
endif()

if (GGML_HIP_NO_VMM)
    add_compile_definitions(GGML_HIP_NO_VMM)
endif()

if (GGML_HIP_ROCWMMA_FATTN)
    add_compile_definitions(GGML_HIP_ROCWMMA_FATTN)
endif()

if (NOT GGML_CUDA_FA)
    add_compile_definitions(GGML_CUDA_NO_FA)
endif()

if (CXX_IS_HIPCC)
    set_source_files_properties(${GGML_SOURCES_ROCM} PROPERTIES LANGUAGE CXX)
    target_link_libraries(ggml-hip PRIVATE hip::device)
else()
    set_source_files_properties(${GGML_SOURCES_ROCM} PROPERTIES LANGUAGE HIP)
endif()

if (GGML_STATIC)
    message(FATAL_ERROR "Static linking not supported for HIP/ROCm")
endif()

target_link_libraries(ggml-hip PRIVATE ggml-base hip::host roc::rocblas roc::hipblas)

----------------------------------------

TITLE: Setting up Python Environment for OpenVINO (Windows)
DESCRIPTION: Creates a Python virtual environment and installs required dependencies for OpenVINO conversion on Windows.

LANGUAGE: powershell
CODE:
cd models
python -m venv openvino_conv_env
openvino_conv_env\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements-openvino.txt

----------------------------------------

TITLE: Accessing Whisper Log in Vim
DESCRIPTION: Vim command to open the Whisper log buffer for viewing plugin activity and debugging information.

LANGUAGE: vim
CODE:
:e whisper_log

----------------------------------------

TITLE: Displaying Binary Filename Changes Table in Markdown
DESCRIPTION: A markdown table showing the mapping between old and new binary filenames for the whisper.cpp project. This table helps users update their scripts and workflows to use the new binary names.

LANGUAGE: markdown
CODE:
| Old Filename | New Filename |
| ---- | ---- |
| main | whisper-cli |
| bench | whisper-bench |
| stream | whisper-stream |
| command | whisper-command |
| server | whisper-server |
| talk-llama | whisper-talk-llama |

----------------------------------------

TITLE: Configuring CoreML Integration
DESCRIPTION: Sets up CoreML framework integration when WHISPER_COREML is enabled. Finds necessary frameworks, configures compiler flags, and adds optional fallback support if requested.

LANGUAGE: cmake
CODE:
if (WHISPER_COREML)
    find_library(FOUNDATION_FRAMEWORK Foundation)
    find_library(COREML_FRAMEWORK CoreML)

    if (COREML_FRAMEWORK)
        message(STATUS "CoreML framework found")

        set(WHISPER_EXTRA_FLAGS ${WHISPER_EXTRA_FLAGS} -DWHISPER_USE_COREML)
    else()
        message(FATAL_ERROR "CoreML framework not found")
    endif()

    if (WHISPER_COREML_ALLOW_FALLBACK)
        set(WHISPER_EXTRA_FLAGS ${WHISPER_EXTRA_FLAGS} -DWHISPER_COREML_ALLOW_FALLBACK)
    endif()
endif()

----------------------------------------

TITLE: Setting up oneAPI Environment for SYCL in llama.cpp
DESCRIPTION: Commands to source the Intel oneAPI environment variables required for SYCL execution.

LANGUAGE: bash
CODE:
source /opt/intel/oneapi/setvars.sh

----------------------------------------

TITLE: Configuring GGML BLAS Backend with Located Dependencies
DESCRIPTION: Sets up the ggml-blas target with the detected BLAS libraries and include directories. Also detects and configures Intel MKL if present in the include paths.

LANGUAGE: CMake
CODE:
    message(STATUS "BLAS found, Includes: ${BLAS_INCLUDE_DIRS}")

    target_compile_options(ggml-blas PRIVATE ${BLAS_LINKER_FLAGS})

    if (${BLAS_INCLUDE_DIRS} MATCHES "mkl" AND (${GGML_BLAS_VENDOR} MATCHES "Generic" OR ${GGML_BLAS_VENDOR} MATCHES "Intel"))
        add_compile_definitions(GGML_BLAS_USE_MKL)
    endif()

    target_link_libraries     (ggml-blas PRIVATE ${BLAS_LIBRARIES})
    target_include_directories(ggml-blas PRIVATE ${BLAS_INCLUDE_DIRS})

----------------------------------------

TITLE: Setting Platform-Specific Default Options
DESCRIPTION: Configures platform-specific default options for Apple devices (enabling Metal and BLAS) versus other platforms. Also handles cross-compilation and reproducible build settings.

LANGUAGE: CMake
CODE:
if (APPLE)
    set(GGML_METAL_DEFAULT ON)
    set(GGML_BLAS_DEFAULT ON)
    set(GGML_BLAS_VENDOR_DEFAULT "Apple")
else()
    set(GGML_METAL_DEFAULT OFF)
    set(GGML_BLAS_DEFAULT OFF)
    set(GGML_BLAS_VENDOR_DEFAULT "Generic")
endif()

if (CMAKE_CROSSCOMPILING OR DEFINED ENV{SOURCE_DATE_EPOCH})
    message(STATUS "Setting GGML_NATIVE_DEFAULT to OFF")
    set(GGML_NATIVE_DEFAULT OFF)
else()
    set(GGML_NATIVE_DEFAULT ON)
endif()

# defaults
if (NOT GGML_LLAMAFILE_DEFAULT)
    set(GGML_LLAMAFILE_DEFAULT OFF)
endif()

if (NOT GGML_CUDA_GRAPHS_DEFAULT)
    set(GGML_CUDA_GRAPHS_DEFAULT OFF)
endif()

----------------------------------------

TITLE: Running memcpy Benchmark on M1 Pro
DESCRIPTION: This snippet shows the command to run the memcpy benchmark and its results, demonstrating memory bandwidth scaling with multiple threads.

LANGUAGE: shell
CODE:
make -j && ./scripts/bench-all.sh 8

----------------------------------------

TITLE: Defining GGML Backend Library Addition Function in CMake
DESCRIPTION: Creates a function 'ggml_add_backend_library' to add backend libraries to the GGML project. It handles both dynamic and static linking scenarios and sets up necessary compiler definitions and dependencies.

LANGUAGE: CMake
CODE:
function(ggml_add_backend_library backend)
    if (GGML_BACKEND_DL)
        add_library(${backend} MODULE ${ARGN})
        # write the shared library to the output directory
        set_target_properties(${backend} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
        target_compile_definitions(${backend} PRIVATE GGML_BACKEND_DL)
        add_dependencies(ggml ${backend})
    else()
        add_library(${backend} ${ARGN})
        target_link_libraries(ggml PUBLIC ${backend})
        install(TARGETS ${backend} LIBRARY)
    endif()

    target_link_libraries(${backend} PRIVATE ggml-base)
    target_include_directories(${backend} PRIVATE ..)

    if (${BUILD_SHARED_LIBS})
        target_compile_definitions(${backend} PRIVATE GGML_BACKEND_BUILD)
        target_compile_definitions(${backend} PUBLIC  GGML_BACKEND_SHARED)
    endif()

    if(NOT GGML_AVAILABLE_BACKENDS)
        set(GGML_AVAILABLE_BACKENDS "${backend}"
            CACHE INTERNAL "List of backends for cmake package")
    else()
        list(FIND GGML_AVAILABLE_BACKENDS "${backend}" has_backend)
        if(has_backend EQUAL -1)
            set(GGML_AVAILABLE_BACKENDS "${GGML_AVAILABLE_BACKENDS};${backend}"
                CACHE INTERNAL "List of backends for cmake package")
        endif()
    endif()
endfunction()

----------------------------------------

TITLE: Processing Transcription Segments in Ruby Whisper
DESCRIPTION: Shows how to iterate through transcription segments after calling transcribe, including formatting timestamps and handling segment metadata. Demonstrates how to extract transcript text, time markers, and speaker turn indicators.

LANGUAGE: ruby
CODE:
def format_time(time_ms)
  sec, decimal_part = time_ms.divmod(1000)
  min, sec = sec.divmod(60)
  hour, min = min.divmod(60)
  "%02d:%02d:%02d.%03d" % [hour, min, sec, decimal_part]
end

whisper
  .transcribe("path/to/audio.wav", params)
  .each_segment.with_index do |segment, index|
    line = "[%{nth}: %{st} --> %{ed}] %{text}" % {
      nth: index + 1,
      st: format_time(segment.start_time),
      ed: format_time(segment.end_time),
      text: segment.text
    }
    line << " (speaker turned)" if segment.speaker_next_turn?
    puts line
  end

----------------------------------------

TITLE: AI Assistant Dialog Template
DESCRIPTION: A structured dialog template where {0} represents the user, {1} represents the AI assistant name, {2} represents time, {3} represents year, and {4} represents dialog separator. The template includes basic conversation examples with short, concise responses.

LANGUAGE: text
CODE:
{0}{4} Hello, {1}!
{1}{4} Hello {0}! How may I help you today?
{0}{4} What time is it?
{1}{4} It is {2} o'clock.
{0}{4} What year is it?
{1}{4} We are in {3}.
{0}{4} What is a cat?
{1}{4} A cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae.
{0}{4} Name a color.
{1}{4} Blue
{0}{4}

----------------------------------------

TITLE: Configuring Logging for Whisper Ruby
DESCRIPTION: Demonstrates how to set up custom logging callbacks for the Whisper library. Shows how to handle different log levels (none, info, warn, error, debug) and customize log output format.

LANGUAGE: ruby
CODE:
prefix = "[MyApp] "
log_callback = ->(level, buffer, user_data) {
  case level
  when Whisper::LOG_LEVEL_NONE
    puts "#{user_data}none: #{buffer}"
  when Whisper::LOG_LEVEL_INFO
    puts "#{user_data}info: #{buffer}"
  when Whisper::LOG_LEVEL_WARN
    puts "#{user_data}warn: #{buffer}"
  when Whisper::LOG_LEVEL_ERROR
    puts "#{user_data}error: #{buffer}"
  when Whisper::LOG_LEVEL_DEBUG
    puts "#{user_data}debug: #{buffer}"
  when Whisper::LOG_LEVEL_CONT
    puts "#{user_data}same to previous: #{buffer}"
  end
}
Whisper.log_set log_callback, prefix

LANGUAGE: ruby
CODE:
Whisper.log_set ->(level, buffer, user_data) {
  # do nothing
}, nil
Whisper::Context.new("base")

----------------------------------------

TITLE: Setting Emscripten Link Flags for WebAssembly Build
DESCRIPTION: Configures the Emscripten linker flags for the whisper.wasm build. These settings enable threading, configure memory limits, enable filesystem access, and export specific runtime methods for JavaScript interoperability.

LANGUAGE: cmake
CODE:
set_target_properties(${TARGET} PROPERTIES LINK_FLAGS " \
    --bind \
    -s USE_PTHREADS=1 \
    -s PTHREAD_POOL_SIZE_STRICT=0 \
    -s INITIAL_MEMORY=512MB \
    -s MAXIMUM_MEMORY=2000MB \
    -s ALLOW_MEMORY_GROWTH=1 \
    -s FORCE_FILESYSTEM=1 \
    -s EXPORTED_RUNTIME_METHODS=\"['print', 'printErr', 'ccall', 'cwrap']\" \
    ${EXTRA_FLAGS} \
    ")

----------------------------------------

TITLE: Configuring GGML Library Targets in CMake
DESCRIPTION: Sets up include directories, compiler features, and linking options for the GGML library targets. It handles platform-specific settings and shared library configurations.

LANGUAGE: CMake
CODE:
foreach (target ggml-base ggml)
    target_include_directories(${target} PUBLIC    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include> $<INSTALL_INTERFACE:include>)
    target_compile_features   (${target} PRIVATE c_std_11 cxx_std_17) # don't bump
endforeach()

target_link_libraries(ggml-base PRIVATE Threads::Threads)

find_library(MATH_LIBRARY m)
if (MATH_LIBRARY)
    if (NOT WIN32 OR NOT DEFINED ENV{ONEAPI_ROOT})
        target_link_libraries(ggml-base PRIVATE m)
    endif()
endif()

if (CMAKE_SYSTEM_NAME MATCHES "Android")
    target_link_libraries(ggml-base PRIVATE dl)
endif()

if(CMAKE_SYSTEM_NAME MATCHES "visionOS")
    target_compile_definitions(ggml-base PUBLIC _DARWIN_C_SOURCE)
endif()

if (BUILD_SHARED_LIBS)
    foreach (target ggml-base ggml)
        set_target_properties(${target} PROPERTIES POSITION_INDEPENDENT_CODE ON)
        target_compile_definitions(${target} PRIVATE GGML_BUILD)
        target_compile_definitions(${target} PUBLIC  GGML_SHARED)
    endforeach()
endif()

----------------------------------------

TITLE: Defining GGML Backend Addition Function in CMake
DESCRIPTION: Creates a function 'ggml_add_backend' to add specific backends to the GGML project. It handles subdirectory inclusion and compiler definitions based on the backend type.

LANGUAGE: CMake
CODE:
function(ggml_add_backend backend)
    string(TOUPPER "GGML_${backend}" backend_id)
    if (${backend_id})
        string(TOLOWER "ggml-${backend}" backend_target)
        add_subdirectory(${backend_target})
        message(STATUS "Including ${backend} backend")
        if (NOT GGML_BACKEND_DL)
            string(TOUPPER "GGML_USE_${backend}" backend_use)
            target_compile_definitions(ggml PUBLIC ${backend_use})
        endif()
    endif()
endfunction()

----------------------------------------

TITLE: Configuring FFmpeg Dependency in CMake
DESCRIPTION: This block handles finding and configuring FFmpeg libraries when WHISPER_FFMPEG is enabled. It checks for required components, displays information about found libraries, and adds the necessary include directories and compile definitions.

LANGUAGE: CMake
CODE:
if (WHISPER_FFMPEG)
    # As of cmake 3.27, there is no official cmake support for FindFFmpeg.
    # Consequnelty we added a FindFFmpeg.cmake script the cmake subfolder:
    # whisper.cpp does not need the full ffmpeg libs, just AVFORMAT AVCODEC AVUTIL SWRESAMPLE
    # libswresample  performs highly optimized audio resampling, rematrixing and sample format conversion operations
    # libavcodec provides a generic encoding/decoding framework and contains multiple decoders and encoders for audio, video and subtitle streams, and several bitstream filters.
    # libavformat provides a generic framework for multiplexing and demultiplexing (muxing and demuxing) audio, video and subtitle streams.
    find_package(FFmpeg REQUIRED)

    if (NOT ${FFMPEG_FOUND})
        message(FATAL_ERROR "Cannot find ffmpeg libs/headers")
    endif()

    message(STATUS "Found ffmpeg libs:       ${FFMPEG_LIBRARIES}")
    message(STATUS "Found ffmpeg headers in: ${FFMPEG_INCLUDE_DIRS}")
    message(STATUS "ffmpeg definitions:      ${FFMPEG_DEFINITIONS}")
    message(STATUS "Found avformat           ${AVFORMAT_VERSION}")

    include_directories(${FFMPEG_INCLUDE_DIRS})
    add_compile_definitions(WHISPER_FFMPEG)

    list(APPEND COMMON_EXTRA_LIBS ${FFMPEG_LIBRARIES})

    set(COMMON_SOURCES_FFMPEG ffmpeg-transcode.cpp)
endif()

----------------------------------------

TITLE: Deploying to a Custom HTTP Server
DESCRIPTION: Instructions for copying the necessary WebAssembly and JavaScript worker files to a custom HTTP server path. This allows the stream.wasm application to be hosted on any web server.

LANGUAGE: bash
CODE:
# copy the produced page to your HTTP path
cp bin/stream.wasm/*       /path/to/html/
cp bin/libstream.worker.js /path/to/html/

----------------------------------------

TITLE: Running Whisper Command in Guided Mode
DESCRIPTION: Commands for running the voice assistant in guided mode with predefined command lists. Includes performance optimization settings for Raspberry Pi.

LANGUAGE: bash
CODE:
# Run in guided mode, the list of allowed commands is in commands.txt
./whisper-command -m ./models/ggml-base.en.bin -cmd ./examples/command/commands.txt

# On Raspberry Pi, in guided mode you can use "-ac 128" for extra performance
./whisper-command -m ./models/ggml-tiny.en.bin -cmd ./examples/command/commands.txt -ac 128 -t 3 -c 0

----------------------------------------

TITLE: Example SYCL Device Listing Output in llama.cpp
DESCRIPTION: Sample output from the ls-sycl-device tool showing detected devices with their compute capabilities, work group sizes, and memory details.

LANGUAGE: bash
CODE:
found 4 SYCL devices:
  Device 0: Intel(R) Arc(TM) A770 Graphics,	compute capability 1.3,
    max compute_units 512,	max work group size 1024,	max sub group size 32,	global mem size 16225243136
  Device 1: Intel(R) FPGA Emulation Device,	compute capability 1.2,
    max compute_units 24,	max work group size 67108864,	max sub group size 64,	global mem size 67065057280
  Device 2: 13th Gen Intel(R) Core(TM) i7-13700K,	compute capability 3.0,
    max compute_units 24,	max work group size 8192,	max sub group size 64,	global mem size 67065057280
  Device 3: Intel(R) Arc(TM) A770 Graphics,	compute capability 3.0,
    max compute_units 512,	max work group size 1024,	max sub group size 32,	global mem size 16225243136

----------------------------------------

TITLE: Defining CPU Backend Variant Addition Function in CMake
DESCRIPTION: Creates a function 'ggml_add_cpu_backend_variant' to add CPU-specific backend variants with different instruction set optimizations. It sets up compiler flags for various CPU features.

LANGUAGE: CMake
CODE:
function(ggml_add_cpu_backend_variant tag_name)
    set(GGML_CPU_TAG_NAME ${tag_name})
    # other: OPENMP LLAMAFILE CPU_HBM
    foreach (feat NATIVE
                  AVX AVX2 BMI2 AVX_VNNI FMA F16C
                  AVX512 AVX512_VBMI AVX512_VNNI AVX512_BF16
                  AMX_TILE AMX_INT8 AMX_BF16)
        set(GGML_${feat} OFF)
    endforeach()

    foreach (feat ${ARGN})
        set(GGML_${feat} ON)
    endforeach()

    ggml_add_cpu_backend_variant_impl(${tag_name})
endfunction()

----------------------------------------

TITLE: Configuring MUSA Architectures and Source Files in CMake
DESCRIPTION: Sets up MUSA architectures, gathers MUSA-specific header and source files, and configures compilation flags for MUSA sources. It also handles conditional compilation based on GGML_CUDA_FA_ALL_QUANTS.

LANGUAGE: CMake
CODE:
if (MUSAToolkit_FOUND)
    message(STATUS "MUSA Toolkit found")

    if (NOT DEFINED MUSA_ARCHITECTURES)
        set(MUSA_ARCHITECTURES "21;22;31")
    endif()
    message(STATUS "Using MUSA architectures: ${MUSA_ARCHITECTURES}")

    file(GLOB   GGML_HEADERS_MUSA "../ggml-cuda/*.cuh")
    list(APPEND GGML_HEADERS_MUSA "../../include/ggml-cuda.h")

    file(GLOB   GGML_SOURCES_MUSA "../ggml-cuda/*.cu")
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-mma*.cu")
    list(APPEND GGML_SOURCES_MUSA ${SRCS})
    file(GLOB   SRCS "../ggml-cuda/template-instances/mmq*.cu")
    list(APPEND GGML_SOURCES_MUSA ${SRCS})

    if (GGML_CUDA_FA_ALL_QUANTS)
        file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*.cu")
        list(APPEND GGML_SOURCES_MUSA ${SRCS})
        add_compile_definitions(GGML_CUDA_FA_ALL_QUANTS)
    else()
        file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*q4_0-q4_0.cu")
        list(APPEND GGML_SOURCES_MUSA ${SRCS})
        file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*q8_0-q8_0.cu")
        list(APPEND GGML_SOURCES_MUSA ${SRCS})
        file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*f16-f16.cu")
        list(APPEND GGML_SOURCES_MUSA ${SRCS})
    endif()

    set_source_files_properties(${GGML_SOURCES_MUSA} PROPERTIES LANGUAGE CXX)
    foreach(SOURCE ${GGML_SOURCES_MUSA})
        set(COMPILE_FLAGS "-fsigned-char -x musa -mtgpu")
        foreach(ARCH ${MUSA_ARCHITECTURES})
            set(COMPILE_FLAGS "${COMPILE_FLAGS} --cuda-gpu-arch=mp_${ARCH}")
        endforeach()
        set_property(SOURCE ${SOURCE} PROPERTY COMPILE_FLAGS ${COMPILE_FLAGS})
    endforeach()

----------------------------------------

TITLE: Defining Common Library Target in CMake
DESCRIPTION: This snippet defines the 'common' library target with its source files. It includes conditionally added FFmpeg source files and sets target properties and dependencies.

LANGUAGE: CMake
CODE:
add_library(${TARGET} STATIC
    common.h
    common.cpp
    common-ggml.h
    common-ggml.cpp
    common-whisper.h
    common-whisper.cpp
    grammar-parser.h
    grammar-parser.cpp
    ${COMMON_SOURCES_FFMPEG}
    )

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE whisper ${COMMON_EXTRA_LIBS} ${CMAKE_DL_LIBS})

set_target_properties(${TARGET} PROPERTIES POSITION_INDEPENDENT_CODE ON)
set_target_properties(${TARGET} PROPERTIES FOLDER "libs")

----------------------------------------

TITLE: Benchmarking Whisper Models on M4 Max with Flash Attention Disabled
DESCRIPTION: Runs performance tests on various Whisper models (tiny through large-v2) on M4 Max with METAL, using 1 thread and with flash attention disabled. Shows encoding, decoding, batch processing, and prompt processing times.

LANGUAGE: bash
CODE:
make -j && ./scripts/bench-all.sh 1 1 0

----------------------------------------

TITLE: Configuring OpenVINO Integration
DESCRIPTION: Finds the OpenVINO package when WHISPER_OPENVINO is enabled. This integrates the OpenVINO runtime for potential acceleration of whisper models.

LANGUAGE: cmake
CODE:
if (WHISPER_OPENVINO)
    find_package(OpenVINO REQUIRED COMPONENTS Runtime)
endif()

----------------------------------------

TITLE: Adding Various GGML Backends in CMake
DESCRIPTION: Adds multiple backend options to the GGML project, including BLAS, CUDA, HIP, Metal, and others. Each backend is conditionally added based on project configuration.

LANGUAGE: CMake
CODE:
ggml_add_backend(BLAS)
ggml_add_backend(CANN)
ggml_add_backend(CUDA)
ggml_add_backend(HIP)
ggml_add_backend(Kompute)
ggml_add_backend(METAL)
ggml_add_backend(MUSA)
ggml_add_backend(RPC)
ggml_add_backend(SYCL)
ggml_add_backend(Vulkan)
ggml_add_backend(OpenCL)

----------------------------------------

TITLE: Configuring Whisper CLI Build in CMake
DESCRIPTION: Defines and configures the whisper-cli executable target with necessary dependencies including common libraries, whisper core, FFmpeg, and threading support. Sets up build options and installation rules for the CLI application.

LANGUAGE: cmake
CODE:
set(TARGET whisper-cli)
add_executable(${TARGET} cli.cpp)

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE common whisper ${FFMPEG_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT})

install(TARGETS ${TARGET} RUNTIME)

----------------------------------------

TITLE: Adding MUSA Backend Library and Setting Compile Definitions in CMake
DESCRIPTION: Adds the MUSA backend library, sets various compile definitions for CUDA-like features, and links necessary MUSA libraries. It also handles different compilation options based on project settings.

LANGUAGE: CMake
CODE:
ggml_add_backend_library(ggml-musa
                         ${GGML_HEADERS_MUSA}
                         ${GGML_SOURCES_MUSA}
                        )

# TODO: do not use CUDA definitions for MUSA
target_compile_definitions(ggml PUBLIC GGML_USE_CUDA)

add_compile_definitions(GGML_USE_MUSA)
add_compile_definitions(GGML_CUDA_PEER_MAX_BATCH_SIZE=${GGML_CUDA_PEER_MAX_BATCH_SIZE})

if (GGML_CUDA_FORCE_MMQ)
    add_compile_definitions(GGML_CUDA_FORCE_MMQ)
endif()

if (GGML_CUDA_FORCE_CUBLAS)
    add_compile_definitions(GGML_CUDA_FORCE_CUBLAS)
endif()

if (GGML_CUDA_NO_VMM)
    add_compile_definitions(GGML_CUDA_NO_VMM)
endif()

if (NOT GGML_CUDA_FA)
    add_compile_definitions(GGML_CUDA_NO_FA)
endif()

if (GGML_CUDA_F16 OR GGML_CUDA_DMMV_F16)
    add_compile_definitions(GGML_CUDA_F16)
endif()

if (GGML_CUDA_NO_PEER_COPY)
    add_compile_definitions(GGML_CUDA_NO_PEER_COPY)
endif()

if (GGML_STATIC)
    target_link_libraries(ggml-musa PRIVATE MUSA::musart_static MUSA::mublas_static)
else()
    target_link_libraries(ggml-musa PRIVATE MUSA::musart MUSA::mublas)
endif()

if (GGML_CUDA_NO_VMM)
    # No VMM requested, no need to link directly with the musa driver lib (libmusa.so)
else()
    target_link_libraries(ggml-musa PRIVATE MUSA::musa_driver)
endif()
else()
    message(FATAL_ERROR "MUSA Toolkit not found")
endif()

----------------------------------------

TITLE: Including CUDA Source Files in CMake
DESCRIPTION: Gathers CUDA source files (.cu) and header files (.cuh) for inclusion in the GGML CUDA library build.

LANGUAGE: CMake
CODE:
file(GLOB   GGML_HEADERS_CUDA "*.cuh")
list(APPEND GGML_HEADERS_CUDA "../../include/ggml-cuda.h")

file(GLOB   GGML_SOURCES_CUDA "*.cu")
file(GLOB   SRCS "template-instances/fattn-mma*.cu")
list(APPEND GGML_SOURCES_CUDA ${SRCS})
file(GLOB   SRCS "template-instances/mmq*.cu")
list(APPEND GGML_SOURCES_CUDA ${SRCS})

----------------------------------------

TITLE: Whisper Model Inference Benchmarks (FA=0)
DESCRIPTION: Inference performance measurements for different Whisper models with forced alignment disabled, showing encoding, decoding, batch processing and post-processing times

LANGUAGE: text
CODE:
|      CPU | Config |         Model |  Th |  FA |    Enc. |    Dec. |    Bch5 |      PP |  Commit |
|      --- |    --- |           --- | --- | --- |     --- |     --- |     --- |     --- |     --- |
| M2 ULTRA |  METAL |          tiny |   1 |   0 |    8.74 |    1.20 |    0.36 |    0.01 | ad4e350 |
[...truncated for brevity...]

----------------------------------------

TITLE: Collecting GGML Source and Header Files for HIP/ROCm
DESCRIPTION: Gathers the necessary source and header files for the HIP backend implementation, including template instances for different quantization methods depending on build options.

LANGUAGE: CMake
CODE:
file(GLOB   GGML_HEADERS_ROCM "../ggml-cuda/*.cuh")
list(APPEND GGML_HEADERS_ROCM "../../include/ggml-cuda.h")

file(GLOB   GGML_SOURCES_ROCM "../ggml-cuda/*.cu")
file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-mma*.cu")
list(APPEND GGML_SOURCES_ROCM ${SRCS})
file(GLOB   SRCS "../ggml-cuda/template-instances/mmq*.cu")
list(APPEND GGML_SOURCES_ROCM ${SRCS})

if (GGML_CUDA_FA_ALL_QUANTS)
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*.cu")
    list(APPEND GGML_SOURCES_ROCM ${SRCS})
    add_compile_definitions(GGML_CUDA_FA_ALL_QUANTS)
else()
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*q4_0-q4_0.cu")
    list(APPEND GGML_SOURCES_ROCM ${SRCS})
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*q8_0-q8_0.cu")
    list(APPEND GGML_SOURCES_ROCM ${SRCS})
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*f16-f16.cu")
    list(APPEND GGML_SOURCES_ROCM ${SRCS})
endif()

----------------------------------------

TITLE: Configuring GGML Base and Core Libraries in CMake
DESCRIPTION: Sets up the main GGML library targets 'ggml-base' and 'ggml', including source files and compiler options. It also handles platform-specific linking and shared library settings.

LANGUAGE: CMake
CODE:
add_library(ggml-base
            ../include/ggml.h
            ../include/ggml-alloc.h
            ../include/ggml-backend.h
            ../include/ggml-cpp.h
            ../include/ggml-opt.h
            ../include/gguf.h
            ggml.c
            ggml-alloc.c
            ggml-backend.cpp
            ggml-opt.cpp
            ggml-threading.cpp
            ggml-threading.h
            ggml-quants.c
            ggml-quants.h
            gguf.cpp)

target_include_directories(ggml-base PRIVATE .)
if (GGML_BACKEND_DL)
    target_compile_definitions(ggml-base PUBLIC GGML_BACKEND_DL)
endif()

add_library(ggml
            ggml-backend-reg.cpp)

target_link_libraries(ggml PUBLIC ggml-base)

if (CMAKE_SYSTEM_NAME MATCHES "Linux")
    target_link_libraries(ggml PRIVATE dl stdc++fs)
endif()

----------------------------------------

TITLE: Configuring Emscripten and Shared Library Settings for whisper.cpp
DESCRIPTION: Handles special configuration for Emscripten WebAssembly builds and sets the default behavior for shared libraries based on the platform. Includes pthread and stack size settings for WebAssembly.

LANGUAGE: CMake
CODE:
if (EMSCRIPTEN)
    set(BUILD_SHARED_LIBS_DEFAULT OFF)

    option(WHISPER_WASM_SINGLE_FILE "whisper: embed WASM inside the generated whisper.js" ON)

    # TODO: without these, we get the following error:
    #       wasm-ld: error: --shared-memory is disallowed by whisper.cpp.o because it was not compiled with 'atomics' or 'bulk-memory' features.
    set(CMAKE_C_FLAGS   "${CMAKE_C_FLAGS}   -pthread")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -s TOTAL_STACK=5242880")
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -s TOTAL_STACK=5242880")

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-deprecated")
else()
    if (MINGW)
        set(BUILD_SHARED_LIBS_DEFAULT OFF)
    else()
        set(BUILD_SHARED_LIBS_DEFAULT ON)
    endif()
endif()

option(BUILD_SHARED_LIBS "build shared libraries" ${BUILD_SHARED_LIBS_DEFAULT})

----------------------------------------

TITLE: Configuring SDL2-enabled Whisper CLI Build
DESCRIPTION: Configures the build settings for the whisper command line interface executable when SDL2 support is enabled. Links required libraries including common, SDL components, and whisper core library, and sets up installation rules.

LANGUAGE: cmake
CODE:
if (WHISPER_SDL2)
    set(TARGET whisper-command)
    add_executable(${TARGET} command.cpp)

    include(DefaultTargetOptions)

    target_link_libraries(${TARGET} PRIVATE common common-sdl whisper ${CMAKE_THREAD_LIBS_INIT})

    install(TARGETS ${TARGET} RUNTIME)
endif ()

----------------------------------------

TITLE: Adding GGML Metal Backend Library in CMake
DESCRIPTION: Adds the ggml-metal backend library to the project and links it with the required frameworks.

LANGUAGE: CMake
CODE:
ggml_add_backend_library(ggml-metal
                         ggml-metal.m
                        )

target_link_libraries(ggml-metal PRIVATE
                      ${FOUNDATION_LIBRARY}
                      ${METAL_FRAMEWORK}
                      ${METALKIT_FRAMEWORK}
                      )

----------------------------------------

TITLE: Whisper Model Inference Benchmarks (FA=1)
DESCRIPTION: Inference performance measurements for different Whisper models with forced alignment enabled, showing encoding, decoding, batch processing and post-processing times

LANGUAGE: text
CODE:
|      CPU | Config |         Model |  Th |  FA |    Enc. |    Dec. |    Bch5 |      PP |  Commit |
|      --- |    --- |           --- | --- | --- |     --- |     --- |     --- |     --- |     --- |
| M2 ULTRA |  METAL |          tiny |   1 |   1 |    7.82 |    1.31 |    0.35 |    0.01 | ad4e350 |
[...truncated for brevity...]

----------------------------------------

TITLE: Configuring SDL2-based Streaming Target in CMake
DESCRIPTION: Sets up a conditional build target named 'lsp' when the WHISPER_SDL2 flag is enabled. The target is built from lsp.cpp and linked against several dependencies including common, json_cpp, common-sdl, whisper, and threading libraries.

LANGUAGE: CMake
CODE:
if (WHISPER_SDL2)
    # stream
    set(TARGET lsp)
    add_executable(${TARGET} lsp.cpp)

    include(DefaultTargetOptions)

    target_link_libraries(${TARGET} PRIVATE common json_cpp common-sdl whisper ${CMAKE_THREAD_LIBS_INIT})
endif ()

----------------------------------------

TITLE: Configuring CMake Project for Whisper.cpp Android Library
DESCRIPTION: Sets up the CMake project for Whisper.cpp, including C++ standard, source files, and library directories. It also finds the Android log library and defines a function to build the shared library with specific compiler options.

LANGUAGE: CMake
CODE:
cmake_minimum_required(VERSION 3.10)

project(whisper.cpp)

set(CMAKE_CXX_STANDARD 17)
set(WHISPER_LIB_DIR ${CMAKE_SOURCE_DIR}/../../../../../../../)

set(SOURCE_FILES
    ${WHISPER_LIB_DIR}/ggml/src/ggml.c
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu.c
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu-aarch64.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu-traits.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu-quants.c
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/unary-ops.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/binary-ops.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/vec.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ops.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-alloc.c
    ${WHISPER_LIB_DIR}/ggml/src/ggml-backend.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-backend-reg.cpp
    ${WHISPER_LIB_DIR}/ggml/src/ggml-quants.c
    ${WHISPER_LIB_DIR}/ggml/src/ggml-threading.cpp
    ${WHISPER_LIB_DIR}/src/whisper.cpp
    ${CMAKE_SOURCE_DIR}/jni.c
    )

find_library(LOG_LIB log)

function(build_library target_name)
    add_library(
        ${target_name}
        SHARED
        ${SOURCE_FILES}
    )

    target_link_libraries(${target_name} ${LOG_LIB} android)
    target_compile_definitions(${target_name} PUBLIC GGML_USE_CPU)

    if (${target_name} STREQUAL "whisper_v8fp16_va")
        target_compile_options(${target_name} PRIVATE -march=armv8.2-a+fp16)
    elseif (${target_name} STREQUAL "whisper_vfpv4")
        target_compile_options(${target_name} PRIVATE -mfpu=neon-vfpv4)
    endif ()

    if (NOT ${CMAKE_BUILD_TYPE} STREQUAL "Debug")

        target_compile_options(${target_name} PRIVATE -O3)
        target_compile_options(${target_name} PRIVATE -fvisibility=hidden -fvisibility-inlines-hidden)
        target_compile_options(${target_name} PRIVATE -ffunction-sections -fdata-sections)

        #target_link_options(${target_name} PRIVATE -Wl,--gc-sections)
        #target_link_options(${target_name} PRIVATE -Wl,--exclude-libs,ALL)
        #target_link_options(${target_name} PRIVATE -flto)
    endif ()
endfunction()

----------------------------------------

TITLE: Building Tests and Examples for whisper.cpp
DESCRIPTION: Conditional configuration for building tests and examples based on the build options. This section includes CTest for testing and adds the tests and examples subdirectories if enabled.

LANGUAGE: CMake
CODE:
#
# programs, examples and tests
#

if (WHISPER_BUILD_TESTS AND NOT CMAKE_JS_VERSION)
    include(CTest)
    add_subdirectory(tests)
endif ()

if (WHISPER_BUILD_EXAMPLES)
    add_subdirectory(examples)
endif()

----------------------------------------

TITLE: Setting Up OpenCL Target Library in CMake
DESCRIPTION: Creates and configures the ggml-opencl backend library, linking it with OpenCL libraries and including necessary directories.

LANGUAGE: CMake
CODE:
set(TARGET_NAME ggml-opencl)

ggml_add_backend_library(${TARGET_NAME}
                         ggml-opencl.cpp
                         ../../include/ggml-opencl.h)
target_link_libraries(${TARGET_NAME} PRIVATE ${OpenCL_LIBRARIES})
target_include_directories(${TARGET_NAME} PRIVATE ${OpenCL_INCLUDE_DIRS})

----------------------------------------

TITLE: Detecting ROCm Path in CMake
DESCRIPTION: Sets up the ROCM_PATH variable by checking environment variables and common installation locations. This is essential for finding ROCm libraries and tools.

LANGUAGE: CMake
CODE:
if (NOT EXISTS $ENV{ROCM_PATH})
    if (NOT EXISTS /opt/rocm)
        set(ROCM_PATH /usr)
    else()
        set(ROCM_PATH /opt/rocm)
    endif()
else()
    set(ROCM_PATH $ENV{ROCM_PATH})
endif()

list(APPEND CMAKE_PREFIX_PATH  ${ROCM_PATH})
list(APPEND CMAKE_PREFIX_PATH "${ROCM_PATH}/lib64/cmake")

----------------------------------------

TITLE: Running Multi-threaded Memcpy Benchmark on M4 Max
DESCRIPTION: Executes a benchmark to measure memory copy performance on M4 Max with 8 threads, showing memory bandwidth in GB/s for different thread counts.

LANGUAGE: bash
CODE:
make -j && ./scripts/bench-all.sh 8

----------------------------------------

TITLE: Embedding Metal Library in GGML using Assembly in CMake
DESCRIPTION: Creates an assembly file that embeds the Metal shader code directly into the library, allowing for standalone operation without external shader files.

LANGUAGE: CMake
CODE:
set(METALLIB_COMMON "${CMAKE_CURRENT_SOURCE_DIR}/../ggml-common.h")
if (GGML_METAL_EMBED_LIBRARY)
    enable_language(ASM)

    add_compile_definitions(GGML_METAL_EMBED_LIBRARY)

    set(METALLIB_SOURCE "${CMAKE_CURRENT_SOURCE_DIR}/ggml-metal.metal")
    set(METALLIB_IMPL   "${CMAKE_CURRENT_SOURCE_DIR}/ggml-metal-impl.h")

    file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/autogenerated")

    # merge ggml-common.h and ggml-metal.metal into a single file
    set(METALLIB_EMBED_ASM        "${CMAKE_BINARY_DIR}/autogenerated/ggml-metal-embed.s")
    set(METALLIB_SOURCE_EMBED     "${CMAKE_BINARY_DIR}/autogenerated/ggml-metal-embed.metal")
    set(METALLIB_SOURCE_EMBED_TMP "${CMAKE_BINARY_DIR}/autogenerated/ggml-metal-embed.metal.tmp")

    add_custom_command(
        OUTPUT ${METALLIB_EMBED_ASM}
        COMMAND echo "Embedding Metal library"
        COMMAND sed -e '/__embed_ggml-common.h__/r         ${METALLIB_COMMON}' -e '/__embed_ggml-common.h__/d'         < ${METALLIB_SOURCE}           > ${METALLIB_SOURCE_EMBED_TMP}
        COMMAND sed -e '/\#include \"ggml-metal-impl.h\"/r ${METALLIB_IMPL}'   -e '/\#include \"ggml-metal-impl.h\"/d' < ${METALLIB_SOURCE_EMBED_TMP} > ${METALLIB_SOURCE_EMBED}
        COMMAND echo ".section __DATA,__ggml_metallib"          >  ${METALLIB_EMBED_ASM}
        COMMAND echo ".globl _ggml_metallib_start"              >> ${METALLIB_EMBED_ASM}
        COMMAND echo "_ggml_metallib_start:"                    >> ${METALLIB_EMBED_ASM}
        COMMAND echo ".incbin \\\"${METALLIB_SOURCE_EMBED}\\\"" >> ${METALLIB_EMBED_ASM}
        COMMAND echo ".globl _ggml_metallib_end"                >> ${METALLIB_EMBED_ASM}
        COMMAND echo "_ggml_metallib_end:"                      >> ${METALLIB_EMBED_ASM}
        DEPENDS ../ggml-common.h ggml-metal.metal ggml-metal-impl.h
        COMMENT "Generate assembly for embedded Metal library"
    )

    target_sources(ggml-metal PRIVATE ${METALLIB_EMBED_ASM})

----------------------------------------

TITLE: Configuring Platform-specific Subdirectories in CMake
DESCRIPTION: This conditional block adds different subdirectories to the build based on the platform (Emscripten, Node.js, or native). It also handles optional dependencies like SDL2 and SYCL.

LANGUAGE: CMake
CODE:
if (EMSCRIPTEN)
    add_subdirectory(whisper.wasm)
    add_subdirectory(stream.wasm)
    add_subdirectory(command.wasm)
    add_subdirectory(bench.wasm)
elseif(CMAKE_JS_VERSION)
    add_subdirectory(addon.node)
else()
    add_subdirectory(cli)
    add_subdirectory(bench)
    add_subdirectory(server)
    add_subdirectory(quantize)
    if (WHISPER_SDL2)
        add_subdirectory(stream)
        add_subdirectory(command)
        add_subdirectory(talk-llama)
        add_subdirectory(lsp)
        if (GGML_SYCL)
            add_subdirectory(sycl)
        endif()
    endif (WHISPER_SDL2)

    add_subdirectory(deprecation-warning)
endif()

----------------------------------------

TITLE: Compiler Cache Configuration in CMake
DESCRIPTION: Sets up ccache or sccache for faster compilation by caching build artifacts. Includes special handling for SYCL on Windows.

LANGUAGE: cmake
CODE:
if (GGML_CCACHE AND NOT CMAKE_C_COMPILER_LAUNCHER AND NOT CMAKE_CXX_COMPILER_LAUNCHER)
    find_program(GGML_CCACHE_FOUND ccache)
    find_program(GGML_SCCACHE_FOUND sccache)

    if (GGML_CCACHE_FOUND OR GGML_SCCACHE_FOUND)
        if(GGML_CCACHE_FOUND)
            set(GGML_CCACHE_VARIANT ccache)
        else()
            set(GGML_CCACHE_VARIANT sccache)
        endif()
        if (GGML_SYCL AND GGML_CCACHE_FOUND AND WIN32)
            set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "ccache compiler_type=icl")
        else ()
            set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${GGML_CCACHE_VARIANT}")
        endif ()
        set(ENV{CCACHE_SLOPPINESS} time_macros)
        message(STATUS "${GGML_CCACHE_VARIANT} found, compilation results will be cached. Disable with GGML_CCACHE=OFF.")
    endif ()
endif()

----------------------------------------

TITLE: Configuring Apple Accelerate BLAS
DESCRIPTION: Sets compiler definitions for using Apple's Accelerate framework with LAPACK. This configures the GGML BLAS backend to use Apple's optimized BLAS implementation.

LANGUAGE: CMake
CODE:
    if (${GGML_BLAS_VENDOR} MATCHES "Apple")
        add_compile_definitions(ACCELERATE_NEW_LAPACK)
        add_compile_definitions(ACCELERATE_LAPACK_ILP64)
        add_compile_definitions(GGML_BLAS_USE_ACCELERATE)

----------------------------------------

TITLE: Configuring Standard Model Tests
DESCRIPTION: Defines test cases for various Whisper model sizes (tiny through large) with both general and English-specific variants. Each test uses the JFK sample WAV file and specifies appropriate test labels.

LANGUAGE: cmake
CODE:
set(TEST_TARGET test-whisper-cli-tiny)
add_test(NAME ${TEST_TARGET}
    COMMAND $<TARGET_FILE:whisper-cli>
    -m ${PROJECT_SOURCE_DIR}/models/for-tests-ggml-tiny.bin -l fr
    -f ${PROJECT_SOURCE_DIR}/samples/jfk.wav)
set_tests_properties(${TEST_TARGET} PROPERTIES LABELS "tiny;gh")

set(TEST_TARGET test-whisper-cli-tiny.en)
add_test(NAME ${TEST_TARGET}
    COMMAND $<TARGET_FILE:whisper-cli>
    -m ${PROJECT_SOURCE_DIR}/models/for-tests-ggml-tiny.en.bin
    -f ${PROJECT_SOURCE_DIR}/samples/jfk.wav)
set_tests_properties(${TEST_TARGET} PROPERTIES LABELS "tiny;en")

----------------------------------------

TITLE: Running Whisper Model Inference Benchmark on M1 Pro (With Flash Attention)
DESCRIPTION: This snippet shows the command to run the Whisper model inference benchmark with flash attention enabled and its results for different model sizes.

LANGUAGE: shell
CODE:
make -j && ./scripts/bench-all.sh 1 1 1

----------------------------------------

TITLE: Configuring CUDA Architecture Selection in CMake
DESCRIPTION: Sets up CUDA architecture selection based on various conditions, including native GPU support and specific CUDA features.

LANGUAGE: CMake
CODE:
if (NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
    if (GGML_NATIVE AND CUDAToolkit_VERSION VERSION_GREATER_EQUAL "11.6" AND CMAKE_VERSION VERSION_GREATER_EQUAL "3.24")
        set(CMAKE_CUDA_ARCHITECTURES "native")
    elseif(GGML_CUDA_F16 OR GGML_CUDA_DMMV_F16)
        set(CMAKE_CUDA_ARCHITECTURES "60;61;70;75;80")
    else()
        set(CMAKE_CUDA_ARCHITECTURES "50;61;70;75;80")
    endif()
endif()

----------------------------------------

TITLE: Configuring Neovim Key Mappings
DESCRIPTION: Vim configuration for adding keyboard shortcuts that activate speech-to-text in different editor modes (insert, normal, and visual). The mappings run the whisper.nvim script and insert the transcribed text at the cursor.

LANGUAGE: vim
CODE:
inoremap <C-G>  <C-O>:!whisper.nvim<CR><C-O>:let @a = system("cat /tmp/whisper.nvim \| tail -n 1 \| xargs -0 \| tr -d '\\n' \| sed -e 's/^[[:space:]]*//'"><CR><C-R>a
nnoremap <C-G>       :!whisper.nvim<CR>:let @a = system("cat /tmp/whisper.nvim \| tail -n 1 \| xargs -0 \| tr -d '\\n' \| sed -e 's/^[[:space:]]*//'"><CR>"ap
vnoremap <C-G> c<C-O>:!whisper.nvim<CR><C-O>:let @a = system("cat /tmp/whisper.nvim \| tail -n 1 \| xargs -0 \| tr -d '\\n' \| sed -e 's/^[[:space:]]*//'"><CR><C-R>a

----------------------------------------

TITLE: Configuring Vulkan Shader Generation in CMake
DESCRIPTION: Sets up custom commands to generate Vulkan shaders using a custom tool (vulkan-shaders-gen). Handles both native and cross-compilation scenarios.

LANGUAGE: CMake
CODE:
set (_ggml_vk_host_suffix $<IF:$<STREQUAL:${CMAKE_HOST_SYSTEM_NAME},Windows>,.exe,>)
set (_ggml_vk_genshaders_cmd ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/vulkan-shaders-gen${_ggml_vk_host_suffix})
set (_ggml_vk_header     ${CMAKE_CURRENT_BINARY_DIR}/ggml-vulkan-shaders.hpp)
set (_ggml_vk_source     ${CMAKE_CURRENT_BINARY_DIR}/ggml-vulkan-shaders.cpp)
set (_ggml_vk_input_dir  ${CMAKE_CURRENT_SOURCE_DIR}/vulkan-shaders)
set (_ggml_vk_output_dir ${CMAKE_CURRENT_BINARY_DIR}/vulkan-shaders.spv)

file(GLOB _ggml_vk_shader_deps "${_ggml_vk_input_dir}/*.comp")
set (_ggml_vk_shader_deps ${_ggml_vk_shader_deps} vulkan-shaders-gen)

if (CMAKE_CROSSCOMPILING)
    set(_ggml_vk_shader_deps ${_ggml_vk_shader_deps} vulkan-shaders-gen-build vulkan-shaders-gen-install)
endif()

add_custom_command(
    OUTPUT ${_ggml_vk_header}
            ${_ggml_vk_source}

    COMMAND ${_ggml_vk_genshaders_cmd}
        --glslc      ${Vulkan_GLSLC_EXECUTABLE}
        --input-dir  ${_ggml_vk_input_dir}
        --output-dir ${_ggml_vk_output_dir}
        --target-hpp ${_ggml_vk_header}
        --target-cpp ${_ggml_vk_source}
        --no-clean

    DEPENDS ${_ggml_vk_shader_deps}
    COMMENT "Generate vulkan shaders"
)

----------------------------------------

TITLE: Configuring GGML BLAS Backend Library
DESCRIPTION: Creates a BLAS backend library for GGML when BLAS is found. This adds the ggml-blas.cpp source file to compile as a backend library for GGML.

LANGUAGE: CMake
CODE:
if (BLAS_FOUND)
    message(STATUS "BLAS found, Libraries: ${BLAS_LIBRARIES}")

    ggml_add_backend_library(ggml-blas
                             ggml-blas.cpp
                            )

----------------------------------------

TITLE: Configuring FFmpeg MP3 Support Test
DESCRIPTION: Adds an additional test case for MP3 format support when FFmpeg is enabled, using the tiny English model and JFK MP3 sample file.

LANGUAGE: cmake
CODE:
if (WHISPER_FFMPEG)
    set(TEST_TARGET test-whisper-cli-tiny-mp3)
    # Check with reviewers: any way to check the output transcription via ctest (diff, ...)?
    add_test(NAME ${TEST_TARGET}
      COMMAND $<TARGET_FILE:whisper-cli>
      -m ${PROJECT_SOURCE_DIR}/models/for-tests-ggml-tiny.en.bin
      -f ${PROJECT_SOURCE_DIR}/samples/jfk.mp3)
    set_tests_properties(${TEST_TARGET} PROPERTIES LABELS "tiny;mp3")
endif()

----------------------------------------

TITLE: Running Whisper.cpp Speech Recognition on Audio Sample
DESCRIPTION: Command to run speech recognition on an audio file using a specified model, demonstrating basic usage of the compiled example.

LANGUAGE: bash
CODE:
./build/go-whisper -model models/ggml-tiny.en.bin samples/jfk.wav

----------------------------------------

TITLE: Running Matrix Multiplication Benchmark on M1 Pro
DESCRIPTION: This snippet shows the command to run the ggml_mul_mat benchmark with 1 thread and its results for various matrix sizes and quantization types.

LANGUAGE: shell
CODE:
make -j && ./scripts/bench-all.sh 1 0 0

----------------------------------------

TITLE: Initializing CMake Project Configuration
DESCRIPTION: Sets up basic CMake project configuration including minimum version, project name, and C++ standard. Defines the base project structure and source file paths.

LANGUAGE: cmake
CODE:
cmake_minimum_required(VERSION 3.10)

project(whisper.cpp)

set(CMAKE_CXX_STANDARD 17)
set(WHISPER_LIB_DIR ${CMAKE_SOURCE_DIR}/../../../../../../..)

# Path to external GGML, otherwise uses the copy in whisper.cpp.
option(GGML_HOME "whisper: Path to external GGML source" OFF)

set(
    SOURCE_FILES
    ${WHISPER_LIB_DIR}/src/whisper.cpp
    ${CMAKE_SOURCE_DIR}/jni.c
    )

----------------------------------------

TITLE: Finding BLAS Include Directories with PkgConfig
DESCRIPTION: Uses pkg-config to locate BLAS include directories when they're not provided by FindBLAS.cmake. This is a workaround for a known issue in CMake's BLAS detection.

LANGUAGE: CMake
CODE:
    elseif ("${BLAS_INCLUDE_DIRS}" STREQUAL "")
        # BLAS_INCLUDE_DIRS is missing in FindBLAS.cmake.
        # see https://gitlab.kitware.com/cmake/cmake/-/issues/20268
        find_package(PkgConfig REQUIRED)
        if (${GGML_BLAS_VENDOR} MATCHES "Generic")
            pkg_check_modules(DepBLAS blas)
        elseif (${GGML_BLAS_VENDOR} MATCHES "OpenBLAS")
            # As of openblas v0.3.22, the 64-bit is named openblas64.pc
            pkg_check_modules(DepBLAS openblas64)
            if (NOT DepBLAS_FOUND)
                pkg_check_modules(DepBLAS openblas)
            endif()
        elseif (${GGML_BLAS_VENDOR} MATCHES "FLAME")
            add_compile_definitions(GGML_BLAS_USE_BLIS)
            pkg_check_modules(DepBLAS blis)
        elseif (${GGML_BLAS_VENDOR} MATCHES "ATLAS")
            pkg_check_modules(DepBLAS blas-atlas)
        elseif (${GGML_BLAS_VENDOR} MATCHES "FlexiBLAS")
            pkg_check_modules(DepBLAS flexiblas_api)
        elseif (${GGML_BLAS_VENDOR} MATCHES "Intel")
            add_compile_definitions(GGML_BLAS_USE_MKL)
            # all Intel* libraries share the same include path
            pkg_check_modules(DepBLAS mkl-sdl)
        elseif (${GGML_BLAS_VENDOR} MATCHES "NVHPC")
            # this doesn't provide pkg-config
            # suggest to assign BLAS_INCLUDE_DIRS on your own
            if ("${NVHPC_VERSION}" STREQUAL "")
                message(WARNING "Better to set NVHPC_VERSION")
            else()
                set(DepBLAS_FOUND ON)
                set(DepBLAS_INCLUDE_DIRS "/opt/nvidia/hpc_sdk/${CMAKE_SYSTEM_NAME}_${CMAKE_SYSTEM_PROCESSOR}/${NVHPC_VERSION}/math_libs/include")
            endif()
        endif()

----------------------------------------

TITLE: Finding BLAS Package with Vendor Specification
DESCRIPTION: Sets the BLAS vendor from GGML_BLAS_VENDOR variable and invokes CMake's find_package to locate the BLAS implementation.

LANGUAGE: CMake
CODE:
set(BLA_VENDOR ${GGML_BLAS_VENDOR})
find_package(BLAS)

----------------------------------------

TITLE: GGML Core Build Configuration
DESCRIPTION: Sets up core build requirements including C/C++ standards, threading support, and basic project structure. Configures compiler standards and finds required system dependencies.

LANGUAGE: cmake
CODE:
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED true)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED true)

set(THREADS_PREFER_PTHREAD_FLAG ON)

find_package(Threads REQUIRED)

include(GNUInstallDirs)

----------------------------------------

TITLE: Configuring SDL2-dependent wchess Executable in CMake
DESCRIPTION: Conditional CMake block that creates and configures the wchess executable when SDL2 is enabled. Sets up target options and links necessary libraries including wchess-core, SDL components, and threading libraries.

LANGUAGE: cmake
CODE:
if (WHISPER_SDL2)
    set(TARGET wchess)
    add_executable(${TARGET} wchess.cmd.cpp)

    include(DefaultTargetOptions)

    target_link_libraries(${TARGET} PRIVATE wchess-core common-sdl ${CMAKE_THREAD_LIBS_INIT})
endif ()

----------------------------------------

TITLE: Linking CUDA Libraries in CMake
DESCRIPTION: Configures library linking for CUDA, including static and dynamic linking options for various CUDA libraries.

LANGUAGE: CMake
CODE:
if (GGML_STATIC)
    if (WIN32)
        target_link_libraries(ggml-cuda PRIVATE CUDA::cudart_static CUDA::cublas CUDA::cublasLt)
    else ()
        target_link_libraries(ggml-cuda PRIVATE  CUDA::cudart_static CUDA::cublas_static CUDA::cublasLt_static)
    endif()
else()
    target_link_libraries(ggml-cuda PRIVATE CUDA::cudart CUDA::cublas CUDA::cublasLt)
endif()

----------------------------------------

TITLE: Configuring GGML Source Files
DESCRIPTION: Conditionally adds GGML source files to the build if no external GGML path is specified. Includes core GGML functionality and CPU-specific implementations.

LANGUAGE: cmake
CODE:
if (NOT GGML_HOME)
    set(
        SOURCE_FILES
        ${SOURCE_FILES}
        ${WHISPER_LIB_DIR}/ggml/src/ggml.c
        ${WHISPER_LIB_DIR}/ggml/src/ggml-alloc.c
        ${WHISPER_LIB_DIR}/ggml/src/ggml-backend.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-backend-reg.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-quants.c
        ${WHISPER_LIB_DIR}/ggml/src/ggml-threading.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu.c
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu-aarch64.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu-hbm.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu-quants.c
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ggml-cpu-traits.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/unary-ops.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/binary-ops.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/vec.cpp
        ${WHISPER_LIB_DIR}/ggml/src/ggml-cpu/ops.cpp
        )
endif()

----------------------------------------

TITLE: Finding Required HIP Dependencies and Version Check
DESCRIPTION: Locates necessary HIP packages and checks for ROCwmma if enabled. Verifies that the installed ROCm/HIP version is at least 5.5, which is required for proper functionality.

LANGUAGE: CMake
CODE:
find_package(hip     REQUIRED)
find_package(hipblas REQUIRED)
find_package(rocblas REQUIRED)
if (GGML_HIP_ROCWMMA_FATTN)
    CHECK_INCLUDE_FILE_CXX("rocwmma/rocwmma.hpp" FOUND_ROCWMMA)
    if (NOT ${FOUND_ROCWMMA})
        message(FATAL_ERROR "rocwmma has not been found")
    endif()
endif()

if (${hip_VERSION} VERSION_LESS 5.5)
    message(FATAL_ERROR "At least ROCM/HIP V5.5 is required")
endif()

message(STATUS "HIP and hipBLAS found")

# Workaround old compilers
set(CMAKE_HIP_FLAGS "${CMAKE_HIP_FLAGS} --gpu-max-threads-per-block=1024")

----------------------------------------

TITLE: Handling BLAS Not Found Error
DESCRIPTION: Displays an error message when BLAS is not found, providing guidance on setting the correct BLAS vendor. This helps users troubleshoot BLAS configuration issues.

LANGUAGE: CMake
CODE:
else()
    message(ERROR "BLAS not found, please refer to "
                  "https://cmake.org/cmake/help/latest/module/FindBLAS.html#blas-lapack-vendors"
                  " to set correct GGML_BLAS_VENDOR")
endif()

----------------------------------------

TITLE: Configuring Build Defaults for Different Platforms
DESCRIPTION: Sets up default build options for different platforms, including Emscripten (WASM) and MinGW. Configures library prefix settings for Windows environments.

LANGUAGE: CMake
CODE:
if (EMSCRIPTEN)
    set(BUILD_SHARED_LIBS_DEFAULT OFF)

    option(GGML_WASM_SINGLE_FILE "ggml: embed WASM inside the generated ggml.js" ON)
else()
    if (MINGW)
        set(BUILD_SHARED_LIBS_DEFAULT OFF)
    else()
        set(BUILD_SHARED_LIBS_DEFAULT ON)
    endif()
endif()

# remove the lib prefix on win32 mingw
if (WIN32)
    set(CMAKE_STATIC_LIBRARY_PREFIX "")
    set(CMAKE_SHARED_LIBRARY_PREFIX "")
    set(CMAKE_SHARED_MODULE_PREFIX  "")
endif()

option(BUILD_SHARED_LIBS "ggml: build shared libraries" ${BUILD_SHARED_LIBS_DEFAULT})
option(GGML_BACKEND_DL   "ggml: build backends as dynamic libraries (requires BUILD_SHARED_LIBS)" OFF)

----------------------------------------

TITLE: Initializing Vulkan Dependencies
DESCRIPTION: Sets up required Vulkan components and validates the presence of the GLSL compiler (glslc)

LANGUAGE: cmake
CODE:
find_package(Vulkan COMPONENTS glslc REQUIRED)
find_program(glslc_executable NAMES glslc HINTS Vulkan::glslc)

if (NOT glslc_executable)
    message(FATAL_ERROR "glslc not found")
endif()

----------------------------------------

TITLE: Configuring whisper.wasm Web Interface Files
DESCRIPTION: Sets up the whisper.wasm target and configures the HTML and JavaScript files needed for the web interface. The template files are copied to the output directory with variables replaced.

LANGUAGE: cmake
CODE:
set(TARGET whisper.wasm)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/index-tmpl.html  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/index.html @ONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/../helpers.js    ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/helpers.js @ONLY)

----------------------------------------

TITLE: Configuring GGML Kompute Backend Library
DESCRIPTION: Sets up the GGML Kompute backend library with necessary source files and dependencies

LANGUAGE: cmake
CODE:
ggml_add_backend_library(ggml-kompute
                         ggml-kompute.cpp
                         ../../include/ggml-kompute.h
                        )

target_link_libraries(ggml-kompute PRIVATE ggml-base kompute)
target_include_directories(ggml-kompute PRIVATE ${CMAKE_CURRENT_BINARY_DIR})

add_compile_definitions(VULKAN_HPP_DISPATCH_LOADER_DYNAMIC=1)

----------------------------------------

TITLE: Shader Compilation Configuration
DESCRIPTION: Configures the compilation of multiple GLSL compute shaders used for various operations in whisper.cpp

LANGUAGE: cmake
CODE:
compile_shader(SOURCES
    kompute-shaders/op_scale.comp
    kompute-shaders/op_scale_8.comp
    kompute-shaders/op_add.comp
    kompute-shaders/op_addrow.comp
    kompute-shaders/op_mul.comp
    kompute-shaders/op_silu.comp
    kompute-shaders/op_relu.comp
    kompute-shaders/op_gelu.comp
    kompute-shaders/op_softmax.comp
    kompute-shaders/op_norm.comp
    kompute-shaders/op_rmsnorm.comp
    kompute-shaders/op_diagmask.comp
    kompute-shaders/op_mul_mat_mat_f32.comp
    kompute-shaders/op_mul_mat_f16.comp
    kompute-shaders/op_mul_mat_q8_0.comp
    kompute-shaders/op_mul_mat_q4_0.comp
    kompute-shaders/op_mul_mat_q4_1.comp
    kompute-shaders/op_mul_mat_q4_k.comp
    kompute-shaders/op_mul_mat_q6_k.comp
    kompute-shaders/op_getrows_f32.comp
    kompute-shaders/op_getrows_f16.comp
    kompute-shaders/op_getrows_q4_0.comp
    kompute-shaders/op_getrows_q4_1.comp
    kompute-shaders/op_getrows_q6_k.comp
    kompute-shaders/op_rope_norm_f16.comp
    kompute-shaders/op_rope_norm_f32.comp
    kompute-shaders/op_rope_neox_f16.comp
    kompute-shaders/op_rope_neox_f32.comp
    kompute-shaders/op_cpy_f16_f16.comp
    kompute-shaders/op_cpy_f16_f32.comp
    kompute-shaders/op_cpy_f32_f16.comp
    kompute-shaders/op_cpy_f32_f32.comp
)

----------------------------------------

TITLE: Listing and Adding OpenCL Kernels in CMake
DESCRIPTION: Defines the list of OpenCL kernel files to be included in the build and applies the kernel addition function to each one.

LANGUAGE: CMake
CODE:
set(GGML_OPENCL_KERNELS
    ggml-opencl
    ggml-opencl_mm
    ggml-opencl_cvt
    ggml-opencl_gemv_noshuffle
    ggml-opencl_gemv_noshuffle_general
    ggml-opencl_mul_mat_Ab_Bi_8x4
    ggml-opencl_transpose_16
    ggml-opencl_transpose_32
    ggml-opencl_transpose_32_16
    ggml-opencl_im2col
)

foreach (K ${GGML_OPENCL_KERNELS})
    ggml_opencl_add_kernel(${K})
endforeach()

----------------------------------------

TITLE: Setting Project Configuration in CMake for whisper.cpp
DESCRIPTION: Configures the core project settings including version, build type, and compiler options for whisper.cpp. Sets the required CMake version and the default build type to Release if not specified.

LANGUAGE: CMake
CODE:
cmake_minimum_required(VERSION 3.5) # for add_link_options and implicit target directories.
project("whisper.cpp" C CXX)
project("whisper.cpp" VERSION 1.7.5)
include(CheckIncludeFileCXX)

set(SOVERSION 1)

#set(CMAKE_WARN_DEPRECATED YES)
set(CMAKE_WARN_UNUSED_CLI YES)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if (NOT XCODE AND NOT MSVC AND NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

----------------------------------------

TITLE: Setting up CANN Package Path and Run Mode in CMake
DESCRIPTION: This snippet sets up the CANN package path and defines a cache variable for the run mode. It allows switching between NPU and simulation modes.

LANGUAGE: CMake
CODE:
set(ASCEND_CANN_PACKAGE_PATH ${CANN_INSTALL_DIR})
set(RUN_MODE "npu" CACHE STRING "run mode: npu/sim")

----------------------------------------

TITLE: Copying Metal Files to Build Directory in CMake
DESCRIPTION: Copies necessary Metal shader files and headers to the build output directory so they can be accessed at runtime.

LANGUAGE: CMake
CODE:
# copy metal files to bin directory
configure_file(../ggml-common.h  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-common.h     COPYONLY)
configure_file(ggml-metal.metal  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-metal.metal  COPYONLY)
configure_file(ggml-metal-impl.h ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-metal-impl.h COPYONLY)

----------------------------------------

TITLE: Finding Required Dependencies for OpenCL Backend in CMake
DESCRIPTION: Finds the required packages OpenCL and Python3 for building the OpenCL backend of ggml.

LANGUAGE: CMake
CODE:
find_package(OpenCL REQUIRED)
find_package(Python3 REQUIRED)

----------------------------------------

TITLE: Ascend SOC Type Detection Function
DESCRIPTION: Function to automatically detect Ascend SOC type using npu-smi tool. Fails if detection is unsuccessful.

LANGUAGE: cmake
CODE:
function(detect_ascend_soc_type SOC_VERSION)
    execute_process(
        COMMAND bash -c "npu-smi info|awk -F' ' 'NF > 0 && NR==7 {print $3}'"
        OUTPUT_VARIABLE npu_info
        RESULT_VARIABLE npu_result
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    if("${npu_info}" STREQUAL "" OR ${npu_result})
        message(FATAL_ERROR "Auto-detech ascend soc type failed, please specify manually or check ascend device working normally.")
    endif()
    set(${SOC_VERSION} "Ascend${npu_info}" PARENT_SCOPE)
endfunction()

----------------------------------------

TITLE: Setting Up OpenCL Kernel Embedding in CMake
DESCRIPTION: Configures the build to embed OpenCL kernels into the binary rather than loading them at runtime when GGML_OPENCL_EMBED_KERNELS is set.

LANGUAGE: CMake
CODE:
if (GGML_OPENCL_EMBED_KERNELS)
    add_compile_definitions(GGML_OPENCL_EMBED_KERNELS)

    set(EMBED_KERNEL_SCRIPT "${CMAKE_CURRENT_SOURCE_DIR}/kernels/embed_kernel.py")
    file(MAKE_DIRECTORY     "${CMAKE_CURRENT_BINARY_DIR}/autogenerated")

    target_include_directories(${TARGET_NAME} PRIVATE "${CMAKE_CURRENT_BINARY_DIR}/autogenerated")
endif ()

----------------------------------------

TITLE: Configuring Module Paths and Project Structure for whisper.cpp
DESCRIPTION: Sets up the module paths and output directories for the build. Determines if this is a standalone build and configures JavaScript bindings if needed. This section handles setup for different build environments.

LANGUAGE: CMake
CODE:
# Add path to modules
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

if (CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    set(WHISPER_STANDALONE ON)

    include(git-vars)

    # configure project version
    configure_file(${CMAKE_SOURCE_DIR}/bindings/javascript/package-tmpl.json ${CMAKE_SOURCE_DIR}/bindings/javascript/package.json @ONLY)
else()
    set(WHISPER_STANDALONE OFF)
endif()

----------------------------------------

TITLE: Library Building Configuration for whisper.cpp
DESCRIPTION: Configures the build of the whisper library, either using a system-installed GGML library or building it from source. Adds the src directory to the build process.

LANGUAGE: CMake
CODE:
#
# build the library
#

if (NOT TARGET ggml)
    if (WHISPER_USE_SYSTEM_GGML)
        find_package(ggml REQUIRED)
        if (NOT ggml_FOUND)
            message(FATAL_ERROR "System-installed GGML library not found.")
        endif()
        add_library(ggml ALIAS ggml::ggml)
    else()
        add_subdirectory(ggml)
    endif()
    # ... otherwise assume ggml is added by a parent CMakeLists.txt
endif()
add_subdirectory(src)

----------------------------------------

TITLE: Emscripten Link Flags Configuration
DESCRIPTION: Sets up Emscripten-specific linking flags including thread pool size, memory limits, filesystem support, and exported runtime methods.

LANGUAGE: cmake
CODE:
set_target_properties(${TARGET} PROPERTIES LINK_FLAGS " \
    --bind \
    -s USE_PTHREADS=1 \
    -s PTHREAD_POOL_SIZE=8 \
    -s INITIAL_MEMORY=1024MB \
    -s TOTAL_MEMORY=1024MB \
    -s FORCE_FILESYSTEM=1 \
    -s EXPORTED_RUNTIME_METHODS=\"['print', 'printErr', 'ccall', 'cwrap']\" \
    ${EXTRA_FLAGS} \
    ")

----------------------------------------

TITLE: Configuring OpenCL Profiling in CMake
DESCRIPTION: Conditionally enables OpenCL profiling by adding a compile definition if GGML_OPENCL_PROFILING is set.

LANGUAGE: CMake
CODE:
if (GGML_OPENCL_PROFILING)
    message(STATUS "OpenCL profiling enabled (increases CPU overhead)")
    add_compile_definitions(GGML_OPENCL_PROFILING)
endif ()

----------------------------------------

TITLE: Finding Required Metal Libraries and Frameworks in CMake
DESCRIPTION: Finds the required Foundation, Metal, and MetalKit frameworks needed for Metal GPU acceleration in the GGML library.

LANGUAGE: CMake
CODE:
find_library(FOUNDATION_LIBRARY Foundation REQUIRED)
find_library(METAL_FRAMEWORK    Metal      REQUIRED)
find_library(METALKIT_FRAMEWORK MetalKit   REQUIRED)

message(STATUS "Metal framework found")

----------------------------------------

TITLE: Configuring OpenCL Compile Definitions in CMake
DESCRIPTION: Sets up standard compile definitions for the OpenCL backend, including SOA_Q and target version configurations.

LANGUAGE: CMake
CODE:
add_compile_definitions(GGML_OPENCL_SOA_Q)
add_compile_definitions(GGML_OPENCL_TARGET_VERSION=${GGML_OPENCL_TARGET_VERSION})

----------------------------------------

TITLE: GGML Dependency and Options Configuration for whisper.cpp
DESCRIPTION: Configures the GGML library dependency and overrides its options with whisper-specific ones. Includes a function to handle deprecated options and their transitions to new names.

LANGUAGE: CMake
CODE:
# Required for relocatable CMake package
include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/build-info.cmake)

# override ggml options
set(GGML_CCACHE             ${WHISPER_CCACHE})
set(GGML_SANITIZE_THREAD    ${WHISPER_SANITIZE_THREAD})
set(GGML_SANITIZE_ADDRESS   ${WHISPER_SANITIZE_ADDRESS})
set(GGML_SANITIZE_UNDEFINED ${WHISPER_SANITIZE_UNDEFINED})
set(GGML_ALL_WARNINGS       ${WHISPER_ALL_WARNINGS})
set(GGML_FATAL_WARNINGS     ${WHISPER_FATAL_WARNINGS})

# transition helpers
function (whisper_option_depr TYPE OLD NEW)
    if (${OLD})
        message(${TYPE} "${OLD} is deprecated and will be removed in the future.\nUse ${NEW} instead\n")
        set(${NEW} ON)
    endif()
endfunction()

whisper_option_depr(FATAL_ERROR WHISPER_CUBLAS              GGML_CUDA)
whisper_option_depr(WARNING     WHISPER_CUDA                GGML_CUDA)
whisper_option_depr(WARNING     WHISPER_KOMPUTE             GGML_KOMPUTE)
whisper_option_depr(WARNING     WHISPER_METAL               GGML_METAL)
whisper_option_depr(WARNING     WHISPER_METAL_EMBED_LIBRARY GGML_METAL_EMBED_LIBRARY)
whisper_option_depr(WARNING     WHISPER_NATIVE              GGML_NATIVE)
whisper_option_depr(WARNING     WHISPER_OPENMP              GGML_OPENMP)
whisper_option_depr(WARNING     WHISPER_RPC                 GGML_RPC)
whisper_option_depr(WARNING     WHISPER_SYCL                GGML_SYCL)
whisper_option_depr(WARNING     WHISPER_SYCL_F16            GGML_SYCL_F16)

----------------------------------------

TITLE: Running Whisper Model Inference Benchmark on M1 Pro (No Flash Attention)
DESCRIPTION: This snippet shows the command to run the Whisper model inference benchmark without flash attention and its results for different model sizes.

LANGUAGE: shell
CODE:
make -j && ./scripts/bench-all.sh 1 0 0

----------------------------------------

TITLE: Building Whisper.cpp Libraries for Different Android ABIs
DESCRIPTION: Creates multiple library targets based on the Android ABI. It builds the default 'whisper' target and additional targets for specific ARM architectures (arm64-v8a and armeabi-v7a) with optimized compiler options.

LANGUAGE: CMake
CODE:
build_library("whisper") # Default target

if (${ANDROID_ABI} STREQUAL "arm64-v8a")
    build_library("whisper_v8fp16_va")
elseif (${ANDROID_ABI} STREQUAL "armeabi-v7a")
    build_library("whisper_vfpv4")
endif ()

----------------------------------------

TITLE: Configuring Metal Compilation Options in CMake
DESCRIPTION: Sets compile definitions for Metal configurations including debug mode and BF16 support.

LANGUAGE: CMake
CODE:
if (GGML_METAL_NDEBUG)
    add_compile_definitions(GGML_METAL_NDEBUG)
endif()

if (GGML_METAL_USE_BF16)
    add_compile_definitions(GGML_METAL_USE_BF16)
endif()

----------------------------------------

TITLE: Configuring General Build Options
DESCRIPTION: Defines general build options for GGML, including static linking, native optimization, link-time optimization, and ccache usage.

LANGUAGE: CMake
CODE:
# general
option(GGML_STATIC "ggml: static link libraries"                     OFF)
option(GGML_NATIVE "ggml: optimize the build for the current system" ${GGML_NATIVE_DEFAULT})
option(GGML_LTO    "ggml: enable link time optimization"             OFF)
option(GGML_CCACHE "ggml: use ccache if available"                   ON)

----------------------------------------

TITLE: Compiling Metal Shaders with Custom Configuration in CMake
DESCRIPTION: Compiles Metal shaders with custom flags for debugging, optimization, and macOS version compatibility when not embedding the Metal library.

LANGUAGE: CMake
CODE:
else()
    if (GGML_METAL_SHADER_DEBUG)
        # custom command to do the following:
        #   xcrun -sdk macosx metal    -fno-fast-math -c ggml-metal.metal -o ggml-metal.air
        #   xcrun -sdk macosx metallib                   ggml-metal.air   -o default.metallib
        #
        # note: this is the only way I found to disable fast-math in Metal. it's ugly, but at least it works
        #       disabling fast math is needed in order to pass tests/test-backend-ops
        # note: adding -fno-inline fixes the tests when using MTL_SHADER_VALIDATION=1
        # note: unfortunately, we have to call it default.metallib instead of ggml.metallib
        #       ref: https://github.com/ggerganov/whisper.cpp/issues/1720
        set(XC_FLAGS -fno-fast-math -fno-inline -g)
    else()
        set(XC_FLAGS -O3)
    endif()

    # Append macOS metal versioning flags
    if (GGML_METAL_MACOSX_VERSION_MIN)
        message(STATUS "Adding  -mmacosx-version-min=${GGML_METAL_MACOSX_VERSION_MIN} flag to metal compilation")
        list   (APPEND XC_FLAGS -mmacosx-version-min=${GGML_METAL_MACOSX_VERSION_MIN})
    endif()

    if (GGML_METAL_STD)
        message(STATUS "Adding  -std=${GGML_METAL_STD} flag to metal compilation")
        list   (APPEND XC_FLAGS -std=${GGML_METAL_STD})
    endif()

    add_custom_command(
        OUTPUT ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/default.metallib
        COMMAND xcrun -sdk macosx metal ${XC_FLAGS} -c ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-metal.metal -o - |
            xcrun -sdk macosx metallib - -o ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/default.metallib
        COMMAND rm -f ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-common.h
        COMMAND rm -f ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-metal.metal
        DEPENDS ggml-metal.metal ${METALLIB_COMMON}
        COMMENT "Compiling Metal kernels"
        )

    # FIXME: only add to the ggml-metal target?
    add_custom_target(
        ggml-metal-lib ALL
        DEPENDS ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/default.metallib
        )
endif() # GGML_METAL_EMBED_LIBRARY

----------------------------------------

TITLE: Configuring Windows-specific Build Settings in CMake
DESCRIPTION: Sets up Windows-specific compiler definitions and export settings. Disables secure warnings and configures symbol exports for shared libraries on Windows platforms.

LANGUAGE: cmake
CODE:
# TODO: should not use this
if (WIN32)
    add_compile_definitions(_CRT_SECURE_NO_WARNINGS)

    if (BUILD_SHARED_LIBS)
        set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
    endif()
endif()

----------------------------------------

TITLE: Configuring Node.js Addon Target
DESCRIPTION: Sets up the basic configuration for the Node.js addon target, including NAPI version and compiler settings.

LANGUAGE: cmake
CODE:
set(TARGET addon.node)

# Base settings
#==================================================================
# env var supported by cmake-js
add_definitions(-DNAPI_VERSION=4)
include_directories(${CMAKE_JS_INC})
#==================================================================

add_library(${TARGET} SHARED ${CMAKE_JS_SRC} addon.cpp)
set_target_properties(${TARGET} PROPERTIES PREFIX "" SUFFIX ".node")

include(DefaultTargetOptions)

----------------------------------------

TITLE: Defining Library Build Function
DESCRIPTION: Creates a function to build the shared library with specific compiler and linker options. Handles different target architectures and optimization levels.

LANGUAGE: cmake
CODE:
function(build_library target_name)
    add_library(
        ${target_name}
        SHARED
        ${SOURCE_FILES}
    )

    target_compile_definitions(${target_name} PUBLIC GGML_USE_CPU)

    if (${target_name} STREQUAL "whisper_v8fp16_va")
        target_compile_options(${target_name} PRIVATE -march=armv8.2-a+fp16)
        set(GGML_COMPILE_OPTIONS                      -march=armv8.2-a+fp16)
    elseif (${target_name} STREQUAL "whisper_vfpv4")
        target_compile_options(${target_name} PRIVATE -mfpu=neon-vfpv4)
        set(GGML_COMPILE_OPTIONS                      -mfpu=neon-vfpv4)
    endif ()

    if (NOT ${CMAKE_BUILD_TYPE} STREQUAL "Debug")
        target_compile_options(${target_name} PRIVATE -O3)
        target_compile_options(${target_name} PRIVATE -fvisibility=hidden -fvisibility-inlines-hidden)
        target_compile_options(${target_name} PRIVATE -ffunction-sections -fdata-sections)

        target_link_options(${target_name} PRIVATE -Wl,--gc-sections)
        target_link_options(${target_name} PRIVATE -Wl,--exclude-libs,ALL)
        target_link_options(${target_name} PRIVATE -flto)
    endif ()

    if (GGML_HOME)
        include(FetchContent)
        FetchContent_Declare(ggml SOURCE_DIR ${GGML_HOME})
        FetchContent_MakeAvailable(ggml)

        target_compile_options(ggml PRIVATE ${GGML_COMPILE_OPTIONS})
        target_link_libraries(${target_name} ${LOG_LIB} android ggml)
    else()
        target_link_libraries(${target_name} ${LOG_LIB} android)
    endif()

endfunction()

----------------------------------------

TITLE: Configuring x86 Architecture Optimizations in CMake for GGML
DESCRIPTION: This snippet configures compiler flags and definitions for x86 architecture. It conditionally adds appropriate flags for various instruction set extensions like SSE4.2, F16C, FMA, BMI2, AVX, AVX2, AVX-VNNI, AVX512 and its variants, and AMX instructions based on build configuration.

LANGUAGE: CMake
CODE:
if (GGML_NATIVE)
    list(APPEND ARCH_FLAGS -march=native)
else ()
    list(APPEND ARCH_FLAGS -msse4.2)
    list(APPEND ARCH_DEFINITIONS GGML_SSE42)
    if (GGML_F16C)
        list(APPEND ARCH_FLAGS -mf16c)
        list(APPEND ARCH_DEFINITIONS GGML_F16C)
    endif()
    if (GGML_FMA)
        list(APPEND ARCH_FLAGS -mfma)
        list(APPEND ARCH_DEFINITIONS GGML_FMA)
    endif()
    if (GGML_BMI2)
        list(APPEND ARCH_FLAGS -mbmi2)
        list(APPEND ARCH_DEFINITIONS GGML_BMI2)
    endif()
    if (GGML_AVX)
        list(APPEND ARCH_FLAGS -mavx)
        list(APPEND ARCH_DEFINITIONS GGML_AVX)
    endif()
    if (GGML_AVX2)
        list(APPEND ARCH_FLAGS -mavx2)
        list(APPEND ARCH_DEFINITIONS GGML_AVX2)
    endif()
    if (GGML_AVX_VNNI)
        list(APPEND ARCH_FLAGS -mavxvnni)
        list(APPEND ARCH_DEFINITIONS GGML_AVX_VNNI)
    endif()
    if (GGML_AVX512)
        list(APPEND ARCH_FLAGS -mavx512f)
        list(APPEND ARCH_FLAGS -mavx512cd)
        list(APPEND ARCH_FLAGS -mavx512vl)
        list(APPEND ARCH_FLAGS -mavx512dq)
        list(APPEND ARCH_FLAGS -mavx512bw)
        list(APPEND ARCH_DEFINITIONS GGML_AVX512)
    endif()
    if (GGML_AVX512_VBMI)
        list(APPEND ARCH_FLAGS -mavx512vbmi)
        list(APPEND ARCH_DEFINITIONS GGML_AVX512_VBMI)
    endif()
    if (GGML_AVX512_VNNI)
        list(APPEND ARCH_FLAGS -mavx512vnni)
        list(APPEND ARCH_DEFINITIONS GGML_AVX512_VNNI)
    endif()
    if (GGML_AVX512_BF16)
        list(APPEND ARCH_FLAGS -mavx512bf16)
        list(APPEND ARCH_DEFINITIONS GGML_AVX512_BF16)
    endif()
    if (GGML_AMX_TILE)
        list(APPEND ARCH_FLAGS -mamx-tile)
        list(APPEND ARCH_DEFINITIONS GGML_AMX_TILE)
    endif()
    if (GGML_AMX_INT8)
        list(APPEND ARCH_FLAGS -mamx-int8)
        list(APPEND ARCH_DEFINITIONS GGML_AMX_INT8)
    endif()
    if (GGML_AMX_BF16)
        list(APPEND ARCH_FLAGS -mamx-bf16)
        list(APPEND ARCH_DEFINITIONS GGML_AMX_BF16)
    endif()
endif()

----------------------------------------

TITLE: Configuring SDL2 Dependency in CMake
DESCRIPTION: This code block handles finding and configuring the SDL2 library when WHISPER_SDL2 is enabled. It outputs the found include directories and libraries to the build log.

LANGUAGE: CMake
CODE:
if (WHISPER_SDL2)
    # SDL2
    find_package(SDL2 REQUIRED)

    string(STRIP "${SDL2_LIBRARIES}" SDL2_LIBRARIES)

    message(STATUS "SDL2_INCLUDE_DIRS = ${SDL2_INCLUDE_DIRS}")
    message(STATUS "SDL2_LIBRARIES    = ${SDL2_LIBRARIES}")
endif()

----------------------------------------

TITLE: Benchmarking Whisper Models on V100 GPU with Flash Attention Disabled
DESCRIPTION: Runs performance tests on various Whisper models (tiny through large-v3-turbo) on V100 GPU with CUDA, using 8 threads and with flash attention disabled. Shows encoding, decoding, batch processing, and prompt processing times.

LANGUAGE: bash
CODE:
WHISPER_CUDA=1 make -j && ./scripts/bench-all.sh 8 1 0

----------------------------------------

TITLE: Setting Up Compiler Warning Flags for Multiple Languages
DESCRIPTION: Configures compiler warning flags for C and C++ separately when WHISPER_ALL_WARNINGS is enabled. Includes different sets of flags for each language and handles platform-specific differences between MSVC and other compilers.

LANGUAGE: cmake
CODE:
if (WHISPER_ALL_WARNINGS)
    if (NOT MSVC)
        list(APPEND WARNING_FLAGS -Wall -Wextra -Wpedantic -Wcast-qual -Wno-unused-function)
        list(APPEND C_FLAGS       -Wshadow -Wstrict-prototypes -Wpointer-arith -Wmissing-prototypes
                                  -Werror=implicit-int -Werror=implicit-function-declaration)
        list(APPEND CXX_FLAGS     -Wmissing-declarations -Wmissing-noreturn)

        list(APPEND C_FLAGS   ${WARNING_FLAGS})
        list(APPEND CXX_FLAGS ${WARNING_FLAGS})

        add_compile_options("$<$<COMPILE_LANGUAGE:C>:${C_FLAGS}>"
                            "$<$<COMPILE_LANGUAGE:CXX>:${CXX_FLAGS}>")
    else()
        # todo : msvc
        set(C_FLAGS   "")
        set(CXX_FLAGS "")
    endif()
endif()

----------------------------------------

TITLE: Including Node Addon API Headers
DESCRIPTION: Executes Node.js to find the node-addon-api include directory and configures it for the target. Handles string manipulation to clean up the path output.

LANGUAGE: cmake
CODE:
# Include N-API wrappers
#==================================================================
execute_process(COMMAND node -p "require('node-addon-api').include"
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        OUTPUT_VARIABLE NODE_ADDON_API_DIR
        )
string(REPLACE "\n" "" NODE_ADDON_API_DIR ${NODE_ADDON_API_DIR})
string(REPLACE "\"" "" NODE_ADDON_API_DIR ${NODE_ADDON_API_DIR})
target_include_directories(${TARGET} PRIVATE ${NODE_ADDON_API_DIR})
#==================================================================

----------------------------------------

TITLE: Configuring CPU and Platform-Specific Options
DESCRIPTION: Sets options for CPU architecture variants, ARM architecture settings, PowerPC CPU type, and Windows version.

LANGUAGE: CMake
CODE:
option(GGML_CPU_ALL_VARIANTS "ggml: build all variants of the CPU backend (requires GGML_BACKEND_DL)" OFF)
set(GGML_CPU_ARM_ARCH        "" CACHE STRING "ggml: CPU architecture for ARM")
set(GGML_CPU_POWERPC_CPUTYPE "" CACHE STRING "ggml: CPU type for PowerPC")


if (WIN32)
    set(GGML_WIN_VER "0x602" CACHE STRING   "ggml: Windows version")
endif()

# ggml core
set(GGML_SCHED_MAX_COPIES  "4" CACHE STRING "ggml: max input copies for pipeline parallelism")
option(GGML_CPU                             "ggml: enable CPU backend"                        ON)

----------------------------------------

TITLE: Configuring PowerPC Architecture Optimizations in CMake for GGML
DESCRIPTION: This snippet detects PowerPC processors and configures appropriate compiler flags. It determines the PowerPC generation (POWER9, POWER10) by reading system information and sets specific optimization flags based on the detected processor.

LANGUAGE: CMake
CODE:
elseif ("${CMAKE_SYSTEM_PROCESSOR} " STREQUAL "ppc64le " OR "${CMAKE_SYSTEM_PROCESSOR} " STREQUAL "powerpc ")
    message(STATUS "PowerPC detected")
    if (GGML_NATIVE)
        if (${CMAKE_SYSTEM_PROCESSOR} MATCHES "ppc64")
            file(READ "/proc/cpuinfo" POWER10_M)
        elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "powerpc")
            execute_process(COMMAND bash -c "prtconf |grep 'Implementation' | head -n 1" OUTPUT_VARIABLE POWER10_M)
        endif()

        string(REGEX MATCHALL "POWER *([0-9]+)" MATCHED_STRING "${POWER10_M}")
        string(REGEX REPLACE "POWER *([0-9]+)" "\\1" EXTRACTED_NUMBER "${MATCHED_STRING}")

        if (EXTRACTED_NUMBER GREATER_EQUAL 10)
            list(APPEND ARCH_FLAGS -mcpu=power10 -mpowerpc64)
        elseif (EXTRACTED_NUMBER EQUAL 9)
            list(APPEND ARCH_FLAGS -mcpu=power9 -mpowerpc64)
        elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "ppc64le")
            list(APPEND ARCH_FLAGS -mcpu=powerpc64le -mtune=native)
        else()
            list(APPEND ARCH_FLAGS -mcpu=native -mtune=native -mpowerpc64)
        endif()
    else()
        if (GGML_CPU_POWERPC_CPUTYPE)
            list(APPEND ARCH_FLAGS -mcpu=${GGML_CPU_POWERPC_CPUTYPE})
        endif()
    endif()

----------------------------------------

TITLE: Configuring RISC-V Architecture Optimizations in CMake for GGML
DESCRIPTION: This snippet sets up compiler flags for RISC-V processors. It specifically configures the vector extension (RVV) and half-precision floating-point extension (Zfh) flags when enabled in the build.

LANGUAGE: CMake
CODE:
elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "riscv64")
    message(STATUS "RISC-V detected")
    if (GGML_RVV)
        if (GGML_RV_ZFH)
            list(APPEND ARCH_FLAGS -march=rv64gcv_zfhmin -DGGML_RV_ZFH -mabi=lp64d)
        else()
            list(APPEND ARCH_FLAGS -march=rv64gcv -mabi=lp64d)
        endif()
    endif()

----------------------------------------

TITLE: Benchmarking Whisper Models on M4 Max with Flash Attention Enabled
DESCRIPTION: Runs performance tests on various Whisper models (tiny through large-v2) on M4 Max with METAL, using 1 thread and with flash attention enabled. Shows encoding, decoding, batch processing, and prompt processing times.

LANGUAGE: bash
CODE:
make -j && ./scripts/bench-all.sh 1 1 1

----------------------------------------

TITLE: Building whisper.openvino Library
DESCRIPTION: Defines and configures the whisper.openvino library component when OpenVINO integration is enabled. Sets up source files, include directories, and necessary compiler flags and dependencies.

LANGUAGE: cmake
CODE:
if (WHISPER_OPENVINO)
    set(TARGET whisper.openvino)

    add_library(${TARGET} OBJECT
        openvino/whisper-openvino-encoder.h
        openvino/whisper-openvino-encoder.cpp
        )

    target_include_directories(${TARGET} PUBLIC
        .
        )

    set_property(TARGET ${TARGET} PROPERTY POSITION_INDEPENDENT_CODE ON)
    set(WHISPER_EXTRA_FLAGS ${WHISPER_EXTRA_FLAGS} -DWHISPER_USE_OPENVINO)

    target_link_libraries(${TARGET} PRIVATE ggml openvino::runtime)
    set_target_properties(${TARGET} PROPERTIES FOLDER "libs")
endif()

----------------------------------------

TITLE: Linking Libraries and MSVC Configuration
DESCRIPTION: Links required libraries to the target and handles MSVC-specific configuration for generating node.lib when needed.

LANGUAGE: cmake
CODE:
target_link_libraries(${TARGET} ${CMAKE_JS_LIB} common whisper ${CMAKE_THREAD_LIBS_INIT})

if(MSVC AND CMAKE_JS_NODELIB_DEF AND CMAKE_JS_NODELIB_TARGET)
    # Generate node.lib
    execute_process(COMMAND ${CMAKE_AR} /def:${CMAKE_JS_NODELIB_DEF} /out:${CMAKE_JS_NODELIB_TARGET} ${CMAKE_STATIC_LINKER_FLAGS})
endif()

----------------------------------------

TITLE: Setting Emscripten Link Flags for WebAssembly in CMake
DESCRIPTION: Configures the Emscripten linker flags for the WebAssembly target. Enables threading, sets memory limits, configures filesystem support, and specifies exported JavaScript methods.

LANGUAGE: cmake
CODE:
set_target_properties(${TARGET} PROPERTIES LINK_FLAGS " \
    --bind \
    -s USE_PTHREADS=1 \
    -s PTHREAD_POOL_SIZE=8 \
    -s INITIAL_MEMORY=1024MB \
    -s TOTAL_MEMORY=1024MB \
    -s FORCE_FILESYSTEM=1 \
    -s EXPORTED_RUNTIME_METHODS=\"['print', 'printErr', 'ccall', 'cwrap']\" \
    ${EXTRA_FLAGS} \
    ")

----------------------------------------

TITLE: CANN Backend Library Configuration
DESCRIPTION: Configures CANN backend including platform checks, setting include directories, libraries, and compile definitions. Supports Linux on x86-64 and arm64 platforms.

LANGUAGE: cmake
CODE:
if (CANN_INSTALL_DIR)
    # Only Support Linux.
    if (NOT UNIX)
        message(FATAL_ERROR "CANN: CANN toolkit supports unix but not ${CMAKE_SYSTEM_NAME}")
    endif()

    # Supported platforms: x86-64, arm64
    if (CMAKE_SYSTEM_PROCESSOR STREQUAL "aarch64")
    elseif (CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64" OR CMAKE_SYSTEM_PROCESSOR STREQUAL "amd64")
    else()
        message(FATAL_ERROR "CANN: CANN toolkit supports x86-64 and arm64 but not ${CMAKE_SYSTEM_PROCESSOR}")
    endif()

    # Set header and libs
    set(CANN_INCLUDE_DIRS
        ${CANN_INSTALL_DIR}/include
        ${CANN_INSTALL_DIR}/include/aclnn
        ${CANN_INSTALL_DIR}/acllib/include
    )

    list(APPEND CANN_LIBRARIES
        ascendcl
        nnopbase
        opapi
        acl_op_compiler
    )

    file(GLOB GGML_SOURCES_CANN "*.cpp")

    ggml_add_backend_library(ggml-cann ${GGML_SOURCES_CANN})
    target_link_libraries(ggml-cann PRIVATE ${CANN_LIBRARIES})
    target_include_directories(ggml-cann PRIVATE ${CANN_INCLUDE_DIRS})
    target_link_directories(ggml-cann PRIVATE ${CANN_INSTALL_DIR}/lib64)

    target_compile_definitions(ggml-cann PRIVATE "-D${SOC_TYPE_COMPILE_OPTION}")

    message(STATUS "CANN: CANN_INCLUDE_DIRS =  ${CANN_INCLUDE_DIRS}")
    message(STATUS "CANN: CANN_LIBRARIES =  ${CANN_LIBRARIES}")
else()
    message(FATAL_ERROR "CANN: Can't find CANN_INSTALL_DIR, did you forget to source set_var.sh?")
endif()

----------------------------------------

TITLE: Defining and Configuring libbench Executable in CMake for WebAssembly Compilation
DESCRIPTION: Sets up the libbench executable target with its source file and links it to the whisper library. Configures build options and default target options.

LANGUAGE: cmake
CODE:
set(TARGET libbench)

add_executable(${TARGET}
    emscripten.cpp
    )

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE
    whisper
    )

----------------------------------------

TITLE: Configuring RPC Backend in CMake for GGML
DESCRIPTION: This CMake script configures the RPC backend for GGML. It adds the ggml-rpc library and links the ws2_32 library on Windows platforms.

LANGUAGE: CMake
CODE:
message(STATUS "Using RPC backend")

ggml_add_backend_library(ggml-rpc
                         ggml-rpc.cpp
                        )

if (WIN32)
    target_link_libraries(ggml-rpc PRIVATE ws2_32)
endif()

----------------------------------------

TITLE: Configuring Single-File WASM Option for Emscripten
DESCRIPTION: Adds an option to embed the WASM binary inside the JavaScript file as a single file. When enabled, it copies the built JavaScript file to the output directory and adds the necessary compile flags.

LANGUAGE: cmake
CODE:
unset(EXTRA_FLAGS)

if (WHISPER_WASM_SINGLE_FILE)
    set(EXTRA_FLAGS "-s SINGLE_FILE=1")
    message(STATUS "Embedding WASM inside main.js")

    add_custom_command(
        TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_BINARY_DIR}/bin/libmain.js
        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/whisper.wasm/main.js
        )
endif()

----------------------------------------

TITLE: Installing Dependencies for Whisper.cpp Node.js Addon
DESCRIPTION: Command to install the necessary dependencies for the Whisper.cpp Node.js addon using npm.

LANGUAGE: shell
CODE:
npm install

----------------------------------------

TITLE: Configuring and Building the whisper-bench Executable with CMake
DESCRIPTION: This CMake script defines the whisper-bench target, creates an executable from bench.cpp, applies default target options, links necessary libraries including whisper and thread libraries, and sets up installation rules for the target.

LANGUAGE: CMake
CODE:
set(TARGET whisper-bench)
add_executable(${TARGET} bench.cpp)

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE whisper ${CMAKE_THREAD_LIBS_INIT})

install(TARGETS ${TARGET} RUNTIME)

----------------------------------------

TITLE: Configuring Sanitizer Options in CMake
DESCRIPTION: Sets up compiler and linker flags for thread, address and undefined behavior sanitizers when not using MSVC compiler.

LANGUAGE: cmake
CODE:
if (NOT MSVC)
    if (GGML_SANITIZE_THREAD)
        add_compile_options(-fsanitize=thread)
        link_libraries     (-fsanitize=thread)
    endif()

    if (GGML_SANITIZE_ADDRESS)
        add_compile_options(-fsanitize=address -fno-omit-frame-pointer)
        link_libraries     (-fsanitize=address)
    endif()

    if (GGML_SANITIZE_UNDEFINED)
        add_compile_options(-fsanitize=undefined)
        link_libraries     (-fsanitize=undefined)
    endif()
endif()

----------------------------------------

TITLE: Configuring HIP Compiler Settings in CMake
DESCRIPTION: Detects whether hipcc is being used as the C++ compiler and sets up appropriate HIP language support. Handles platform-specific differences between Windows and Linux.

LANGUAGE: CMake
CODE:
# CMake on Windows doesn't support the HIP language yet
if (WIN32)
    set(CXX_IS_HIPCC TRUE)
else()
    string(REGEX MATCH "hipcc(\.bat)?$" CXX_IS_HIPCC "${CMAKE_CXX_COMPILER}")
endif()

if (CXX_IS_HIPCC)
    if (LINUX)
        if (NOT ${CMAKE_CXX_COMPILER_ID} MATCHES "Clang")
            message(WARNING "Only LLVM is supported for HIP, hint: CXX=/opt/rocm/llvm/bin/clang++")
        endif()

        message(WARNING "Setting hipcc as the C++ compiler is legacy behavior."
                " Prefer setting the HIP compiler directly. See README for details.")
    endif()
else()
    # Forward AMDGPU_TARGETS to CMAKE_HIP_ARCHITECTURES.
    if (AMDGPU_TARGETS AND NOT CMAKE_HIP_ARCHITECTURES)
        set(CMAKE_HIP_ARCHITECTURES ${AMDGPU_TARGETS})
    endif()
    cmake_minimum_required(VERSION 3.21)
    enable_language(HIP)
endif()

----------------------------------------

TITLE: Configuring Emscripten JavaScript Build and NPM Publishing in CMake
DESCRIPTION: Configures the JavaScript build process for Emscripten compilation, adding the javascript subdirectory and setting up NPM package publishing. Creates a custom command to publish the package to NPM when specified dependencies are updated.

LANGUAGE: cmake
CODE:
if (EMSCRIPTEN)
    add_subdirectory(javascript)

    add_custom_command(
        OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/javascript/publish.log
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/javascript/whisper.js
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/javascript/libwhisper.worker.js
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/javascript/package.json
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/javascript
        COMMAND npm publish
        COMMAND touch publish.log
        COMMENT "Publishing npm module v${PROJECT_VERSION}"
        VERBATIM
        )

    add_custom_target(publish-npm
        DEPENDS javascript/publish.log
        )
endif()

----------------------------------------

TITLE: Warning Configuration in CMake
DESCRIPTION: Configures compiler warning flags for different compilers including GCC, Clang and MSVC. Enables various warning levels and treats warnings as errors when specified.

LANGUAGE: cmake
CODE:
if (GGML_ALL_WARNINGS)
    if (NOT MSVC)
        list(APPEND WARNING_FLAGS -Wall -Wextra -Wpedantic -Wcast-qual -Wno-unused-function)
        list(APPEND C_FLAGS       -Wshadow -Wstrict-prototypes -Wpointer-arith -Wmissing-prototypes
                                  -Werror=implicit-int -Werror=implicit-function-declaration)
        list(APPEND CXX_FLAGS     -Wmissing-declarations -Wmissing-noreturn)

        list(APPEND C_FLAGS   ${WARNING_FLAGS})
        list(APPEND CXX_FLAGS ${WARNING_FLAGS})

        ggml_get_flags(${CMAKE_CXX_COMPILER_ID} ${CMAKE_CXX_COMPILER_VERSION})

        add_compile_options("$<$<COMPILE_LANGUAGE:C>:${C_FLAGS};${GF_C_FLAGS}>"
                            "$<$<COMPILE_LANGUAGE:CXX>:${CXX_FLAGS};${GF_CXX_FLAGS}>")
    else()
        # todo : msvc
        set(C_FLAGS   "")
        set(CXX_FLAGS "")
    endif()
endif()

----------------------------------------

TITLE: Configuring GGML CMake Project
DESCRIPTION: Sets up the basic CMake project configuration for GGML, including minimum CMake version, project name, build type settings, and output directories.

LANGUAGE: CMake
CODE:
cmake_minimum_required(VERSION 3.14) # for add_link_options and implicit target directories.
project("ggml" C CXX)
include(CheckIncludeFileCXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if (NOT XCODE AND NOT MSVC AND NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

if (CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    set(GGML_STANDALONE ON)

    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

    # configure project version
    # TODO
else()
    set(GGML_STANDALONE OFF)
endif()

----------------------------------------

TITLE: Configuring LoongArch64 Architecture Optimizations in CMake for GGML
DESCRIPTION: This snippet configures compiler flags for LoongArch64 processors. It sets the base architecture flag and conditionally adds LASX and LSX instruction set extensions if they are enabled in the build configuration.

LANGUAGE: CMake
CODE:
elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "loongarch64")
    message(STATUS "loongarch64 detected")

    list(APPEND ARCH_FLAGS -march=loongarch64)
    if (GGML_LASX)
        list(APPEND ARCH_FLAGS -mlasx)
    endif()
    if (GGML_LSX)
        list(APPEND ARCH_FLAGS -mlsx)
    endif()

----------------------------------------

TITLE: Fallback BLAS Include Directory Detection
DESCRIPTION: Attempts to find cblas.h from common locations when pkg-config fails to locate BLAS include directories. This is a last resort approach to find the necessary headers for compilation.

LANGUAGE: CMake
CODE:
        if (DepBLAS_FOUND)
            set(BLAS_INCLUDE_DIRS ${DepBLAS_INCLUDE_DIRS})
        else()
            message(WARNING "BLAS_INCLUDE_DIRS neither been provided nor been automatically"
            " detected by pkgconfig, trying to find cblas.h from possible paths...")
            find_path(BLAS_INCLUDE_DIRS
                NAMES cblas.h
                HINTS
                    /usr/include
                    /usr/local/include
                    /usr/include/openblas
                    /opt/homebrew/opt/openblas/include
                    /usr/local/opt/openblas/include
                    /usr/include/x86_64-linux-gnu/openblas/include
            )
        endif()

----------------------------------------

TITLE: Defining SDL2-dependent Common-SDL Library in CMake
DESCRIPTION: This conditional block creates a 'common-sdl' library target when SDL2 is enabled. It links with SDL2 libraries and sets appropriate target properties.

LANGUAGE: CMake
CODE:
if (WHISPER_SDL2)
    # common-sdl

    set(TARGET common-sdl)

    add_library(${TARGET} STATIC
        common-sdl.h
        common-sdl.cpp
        )

    include(DefaultTargetOptions)

    target_include_directories(${TARGET} PUBLIC  ${SDL2_INCLUDE_DIRS})
    target_link_libraries     (${TARGET} PRIVATE ${SDL2_LIBRARIES})

    set_target_properties(${TARGET} PROPERTIES POSITION_INDEPENDENT_CODE ON)
    set_target_properties(${TARGET} PROPERTIES FOLDER "libs")
endif()

----------------------------------------

TITLE: Detecting Host Compiler in CMake
DESCRIPTION: Function to detect the host C and C++ compilers, considering different system names and compiler options.

LANGUAGE: CMake
CODE:
function(detect_host_compiler)
    if (CMAKE_HOST_SYSTEM_NAME STREQUAL "Windows")
        find_program(HOST_C_COMPILER NAMES cl gcc clang NO_CMAKE_FIND_ROOT_PATH)
        find_program(HOST_CXX_COMPILER NAMES cl g++ clang++ NO_CMAKE_FIND_ROOT_PATH)
    else()
        find_program(HOST_C_COMPILER NAMES gcc clang NO_CMAKE_FIND_ROOT_PATH)
        find_program(HOST_CXX_COMPILER NAMES g++ clang++ NO_CMAKE_FIND_ROOT_PATH)
    endif()
    set(HOST_C_COMPILER "${HOST_C_COMPILER}" PARENT_SCOPE)
    set(HOST_CXX_COMPILER "${HOST_CXX_COMPILER}" PARENT_SCOPE)
endfunction()

----------------------------------------

TITLE: Configuring libcommand Target for WebAssembly in CMake
DESCRIPTION: Sets up the libcommand executable target that compiles the Whisper speech recognition library to WebAssembly. It defines source files, links required libraries, and configures compiler options.

LANGUAGE: cmake
CODE:
set(TARGET libcommand)

add_executable(${TARGET}
    emscripten.cpp
    )

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE
    common
    whisper
    )

----------------------------------------

TITLE: Building with CUDA Support for Whisper.cpp Go Bindings
DESCRIPTION: Command to build example applications with CUDA GPU acceleration support enabled.

LANGUAGE: bash
CODE:
GGML_CUDA=1 make examples

----------------------------------------

TITLE: Configuring Adreno-Optimized Kernels in CMake
DESCRIPTION: Conditionally enables optimized matrix multiplication kernels for Adreno GPUs if GGML_OPENCL_USE_ADRENO_KERNELS is set.

LANGUAGE: CMake
CODE:
if (GGML_OPENCL_USE_ADRENO_KERNELS)
    message(STATUS "OpenCL will use matmul kernels optimized for Adreno")
    add_compile_definitions(GGML_OPENCL_USE_ADRENO_KERNELS)
endif ()

----------------------------------------

TITLE: Configuring WebAssembly Single File Option for libbench
DESCRIPTION: Handles the WHISPER_WASM_SINGLE_FILE option which embeds the WebAssembly code directly in the JavaScript file. Adds a post-build command to copy the compiled JavaScript file to the output directory.

LANGUAGE: cmake
CODE:
unset(EXTRA_FLAGS)

if (WHISPER_WASM_SINGLE_FILE)
    set(EXTRA_FLAGS "-s SINGLE_FILE=1")
    message(STATUS "Embedding WASM inside bench.js")

    add_custom_command(
        TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_BINARY_DIR}/bin/libbench.js
        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/bench.wasm/bench.js
        )
endif()

----------------------------------------

TITLE: Configuring CUDA Compilation Flags in CMake
DESCRIPTION: Sets up CUDA-specific compilation flags, including fast math, compression mode, and warning levels.

LANGUAGE: CMake
CODE:
set(CUDA_FLAGS -use_fast_math)

if (CUDAToolkit_VERSION VERSION_GREATER_EQUAL "12.8")
    list(APPEND CUDA_FLAGS -compress-mode=${GGML_CUDA_COMPRESSION_MODE})
endif()

if (GGML_FATAL_WARNINGS)
    list(APPEND CUDA_FLAGS -Werror all-warnings)
endif()

target_compile_options(ggml-cuda PRIVATE "$<$<COMPILE_LANGUAGE:CUDA>:${CUDA_FLAGS}>")

----------------------------------------

TITLE: Configuring Vulkan Shader Generator in CMake for whisper.cpp
DESCRIPTION: This CMake snippet configures the build for a Vulkan shader generator. It includes thread support, adds conditional compilation definitions for Vulkan cooperative matrix features, sets up the build target, and specifies installation and linking options.

LANGUAGE: CMake
CODE:
find_package (Threads REQUIRED)

if (GGML_VULKAN_COOPMAT_GLSLC_SUPPORT)
    add_compile_definitions(GGML_VULKAN_COOPMAT_GLSLC_SUPPORT)
endif()
if (GGML_VULKAN_COOPMAT2_GLSLC_SUPPORT)
    add_compile_definitions(GGML_VULKAN_COOPMAT2_GLSLC_SUPPORT)
endif()
set(TARGET vulkan-shaders-gen)
add_executable(${TARGET} vulkan-shaders-gen.cpp)
install(TARGETS ${TARGET} RUNTIME)
target_compile_features(${TARGET} PRIVATE cxx_std_17)
target_link_libraries(vulkan-shaders-gen PUBLIC Threads::Threads)

----------------------------------------

TITLE: Configuring libmain Executable Target for Emscripten Compilation
DESCRIPTION: Sets up the 'libmain' target as an executable that compiles emscripten.cpp and links it with the whisper library. Includes default target options and defines the build specifications.

LANGUAGE: cmake
CODE:
set(TARGET libmain)

add_executable(${TARGET}
    emscripten.cpp
    )

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE
    whisper
    )

----------------------------------------

TITLE: Configuring Custom Inference Parameters
DESCRIPTION: Example of creating an evaluation configuration file to customize the Whisper model and inference parameters used during testing.

LANGUAGE: conf
CODE:
WHISPER_MODEL = large-v3-turbo
WHISPER_FLAGS = --no-prints --threads 8 --language en --output-txt

----------------------------------------

TITLE: Configuring Quantize Executable in CMake for Whisper.cpp
DESCRIPTION: This CMake snippet defines and configures the 'quantize' executable. It sets the target name, adds the executable, includes default target options, and links the necessary libraries including 'common', 'whisper', and threading libraries.

LANGUAGE: CMake
CODE:
set(TARGET quantize)
add_executable(${TARGET} quantize.cpp)

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE common whisper ${CMAKE_THREAD_LIBS_INIT})

----------------------------------------

TITLE: Configuring AMX Support for GGML Library in CMake
DESCRIPTION: This snippet checks for x86_64 architecture and GCC compiler version to enable AMX support. It sets up the necessary files, libraries, and compiler flags for AMX functionality.

LANGUAGE: CMake
CODE:
if (CMAKE_OSX_ARCHITECTURES STREQUAL "x86_64" OR CMAKE_GENERATOR_PLATFORM_LWR MATCHES "^(x86_64|i686|amd64|x64|win32)$" OR
        (NOT CMAKE_OSX_ARCHITECTURES AND NOT CMAKE_GENERATOR_PLATFORM_LWR AND
         CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|i686|AMD64)$") AND
        CMAKE_COMPILER_IS_GNUCC AND CMAKE_CXX_COMPILER_VERSION VERSION_GREATER 11.0)
    message(STATUS "Using AMX")

    file(GLOB   GGML_HEADERS_AMX "*.h")
    list(APPEND GGML_HEADERS_AMX "../../include/ggml-amx.h")

    file(GLOB   GGML_SOURCES_AMX "*.cpp")

    add_library(ggml-amx
                ${GGML_HEADERS_AMX}
                ${GGML_SOURCES_AMX})

    target_link_libraries(ggml-amx PRIVATE ggml-base)
    target_include_directories(ggml-amx PRIVATE . ..)

    # this is duplicated from the CPU backend, since the AMX backend also depends on the architecture flags
    # TODO: integrate AMX backend into the CPU backend
    if (MSVC)
        # instruction set detection for MSVC only
        if (GGML_NATIVE)
            # TODO: improve, should not reference files from the parent folder
            include(../ggml-cpu/cmake/FindSIMD.cmake)
        endif ()
        if (GGML_AVX512)
            list(APPEND ARCH_FLAGS /arch:AVX512)
            # MSVC has no compile-time flags enabling specific
            # AVX512 extensions, neither it defines the
            # macros corresponding to the extensions.
            # Do it manually.
            if (GGML_AVX512_VBMI)
                add_compile_definitions($<$<COMPILE_LANGUAGE:C>:__AVX512VBMI__>)
                add_compile_definitions($<$<COMPILE_LANGUAGE:CXX>:__AVX512VBMI__>)
            endif()
            if (GGML_AVX512_VNNI)
                add_compile_definitions($<$<COMPILE_LANGUAGE:C>:__AVX512VNNI__>)
                add_compile_definitions($<$<COMPILE_LANGUAGE:CXX>:__AVX512VNNI__>)
            endif()
            if (GGML_AVX512_BF16)
                add_compile_definitions($<$<COMPILE_LANGUAGE:C>:__AVX512BF16__>)
                add_compile_definitions($<$<COMPILE_LANGUAGE:CXX>:__AVX512BF16__>)
            endif()
            if (GGML_AMX_TILE)
                add_compile_definitions($<$<COMPILE_LANGUAGE:C>:__AMX_TILE__>)
                add_compile_definitions($<$<COMPILE_LANGUAGE:CXX>:__AMX_TILE__>)
            endif()
            if (GGML_AMX_INT8)
                add_compile_definitions($<$<COMPILE_LANGUAGE:C>:__AMX_INT8__>)
                add_compile_definitions($<$<COMPILE_LANGUAGE:CXX>:__AMX_INT8__>)
            endif()
            if (GGML_AMX_BF16)
                add_compile_definitions($<$<COMPILE_LANGUAGE:C>:__AMX_BF16__>)
                add_compile_definitions($<$<COMPILE_LANGUAGE:CXX>:__AMX_BF16__>)
            endif()
        elseif (GGML_AVX2)
            list(APPEND ARCH_FLAGS /arch:AVX2)
        elseif (GGML_AVX)
            list(APPEND ARCH_FLAGS /arch:AVX)
        endif()
    else()
        if (GGML_NATIVE)
            list(APPEND ARCH_FLAGS -march=native)
        endif()
        if (GGML_F16C)
            list(APPEND ARCH_FLAGS -mf16c)
        endif()
        if (GGML_FMA)
            list(APPEND ARCH_FLAGS -mfma)
        endif()
        if (GGML_AVX)
            list(APPEND ARCH_FLAGS -mavx)
        endif()
        if (GGML_AVX2)
            list(APPEND ARCH_FLAGS -mavx2)
        endif()
        if (GGML_AVX512)
            list(APPEND ARCH_FLAGS -mavx512f)
            list(APPEND ARCH_FLAGS -mavx512dq)
            list(APPEND ARCH_FLAGS -mavx512bw)
        endif()
        if (GGML_AVX512_VBMI)
            list(APPEND ARCH_FLAGS -mavx512vbmi)
        endif()
        if (GGML_AVX512_VNNI)
            list(APPEND ARCH_FLAGS -mavx512vnni)
        endif()
        if (GGML_AVX512_BF16)
            list(APPEND ARCH_FLAGS -mavx512bf16)
        endif()
        if (GGML_AMX_TILE)
            list(APPEND ARCH_FLAGS -mamx-tile)
        endif()
        if (GGML_AMX_INT8)
            list(APPEND ARCH_FLAGS -mamx-int8)
        endif()
        if (GGML_AMX_BF16)
            list(APPEND ARCH_FLAGS -mamx-bf16)
        endif()
    endif()

    target_compile_options(ggml-amx PRIVATE ${ARCH_FLAGS})
else()
    set(GGML_AMX OFF PARENT_SCOPE)
    message(WARNING "AMX requires x86 and gcc version > 11.0. Turning off GGML_AMX.")
endif()

----------------------------------------

TITLE: Setting Include Directories for Whisper.cpp Build
DESCRIPTION: Specifies the include directories for the Whisper.cpp library build, including the main library directory, source files, and GGML-related headers.

LANGUAGE: CMake
CODE:
include_directories(${WHISPER_LIB_DIR})
include_directories(${WHISPER_LIB_DIR}/src)
include_directories(${WHISPER_LIB_DIR}/include)
include_directories(${WHISPER_LIB_DIR}/ggml/include)
include_directories(${WHISPER_LIB_DIR}/ggml/src)
include_directories(${WHISPER_LIB_DIR}/ggml/src/ggml-cpu)

----------------------------------------

TITLE: Creating Ascend NPU Kernel Library in CMake
DESCRIPTION: This snippet uses the ascendc_library command to create a static library named 'ascendc_kernels' from the previously collected source files.

LANGUAGE: CMake
CODE:
ascendc_library(ascendc_kernels STATIC
    ${SRC_FILES}
)

----------------------------------------

TITLE: Configuring libstream Target
DESCRIPTION: Sets up the libstream executable target with Whisper library dependency and basic build configuration.

LANGUAGE: cmake
CODE:
set(TARGET libstream)

add_executable(${TARGET}
    emscripten.cpp
    )

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE
    whisper
    )

----------------------------------------

TITLE: Configuring Vim Plugin for Whisper.cpp
DESCRIPTION: Vim configuration snippet for setting up the Whisper.cpp plugin, including path configuration and keybindings for transcription commands.

LANGUAGE: vim
CODE:
let g:whisper_dir = "~/whisper.cpp"
" Start listening for commands when Ctrl - g is pressed in normal mode
nnoremap <C-G> call whisper#requestCommands()<CR>
" Start unguided transcription when Ctrl - g is pressed in insert mode
inoremap <C-G> <Cmd>call whisper#doTranscription()<CR>

----------------------------------------

TITLE: Installing the Whisper.nvim Script
DESCRIPTION: Commands to copy the whisper.nvim script to a directory in your PATH and make it executable.

LANGUAGE: shell
CODE:
cp examples/whisper.nvim/whisper.nvim ~/bin/
chmod u+x ~/bin/whisper.nvim

----------------------------------------

TITLE: Defining CMake Executables for Whisper.cpp
DESCRIPTION: This CMake snippet defines multiple executable targets for the Whisper.cpp project. It includes mandatory targets 'main' and 'bench', and conditional targets 'stream' and 'command' that are only built if SDL2 is enabled.

LANGUAGE: CMake
CODE:
add_executable(main ./deprecation-warning.cpp)
add_executable(bench ./deprecation-warning.cpp)
if (WHISPER_SDL2)
    add_executable(stream ./deprecation-warning.cpp)
    add_executable(command ./deprecation-warning.cpp)
endif()

----------------------------------------

TITLE: CANN Installation Directory Detection
DESCRIPTION: Checks for CANN installation directory using environment variables CANN_INSTALL_DIR or ASCEND_TOOLKIT_HOME.

LANGUAGE: cmake
CODE:
if ("cann${CANN_INSTALL_DIR}" STREQUAL "cann" AND DEFINED ENV{ASCEND_TOOLKIT_HOME})
    set(CANN_INSTALL_DIR $ENV{ASCEND_TOOLKIT_HOME})
    message(STATUS "CANN: updated CANN_INSTALL_DIR from ASCEND_TOOLKIT_HOME=$ENV{ASCEND_TOOLKIT_HOME}")
endif()

----------------------------------------

TITLE: Setting Compilation Definitions for Ascend NPU Kernels in CMake
DESCRIPTION: This snippet sets compilation definitions for the Ascend NPU kernels. It includes a status message about the compilation settings and uses ascendc_compile_definitions to set private compile definitions.

LANGUAGE: CMake
CODE:
message(STATUS "CANN: compile ascend kernels witch SOC_TYPE:${SOC_TYPE}, SOC_VERSION:${SOC_VERSION}, compile macro:-D${SOC_TYPE_COMPILE_OPTION}.")
ascendc_compile_definitions(ascendc_kernels PRIVATE "-D${SOC_TYPE_COMPILE_OPTION}")
# ascendc_compile_definitions(ascendc_kernels PRIVATE -DASCENDC_DUMP)

----------------------------------------

TITLE: Configuring SYCL Device Lister Executable in CMake
DESCRIPTION: Defines CMake build instructions for the ls-sycl-device utility, which likely lists available SYCL-compatible devices. The executable requires the common and whisper libraries, threading support, and C++17 features.

LANGUAGE: CMake
CODE:
#  MIT license
#  Copyright (C) 2024 Intel Corporation
#  SPDX-License-Identifier: MIT

set(TARGET ls-sycl-device)
add_executable(${TARGET} ls-sycl-device.cpp)
install(TARGETS ${TARGET} RUNTIME)
target_link_libraries(${TARGET} PRIVATE common whisper ${CMAKE_THREAD_LIBS_INIT})
target_compile_features(${TARGET} PRIVATE cxx_std_17)

----------------------------------------

TITLE: Defining Custom Whisper Commands in Vim
DESCRIPTION: Example of defining custom spoken commands for the Whisper.cpp Vim plugin, demonstrating integration with other plugins.

LANGUAGE: vim
CODE:
let g:whisper_user_commands = {"gen": "llama#doLlamaGen"}

----------------------------------------

TITLE: Setting Up Project Include Directories in CMake
DESCRIPTION: This code adds the current source directory to the include path for all targets.

LANGUAGE: CMake
CODE:
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

----------------------------------------

TITLE: Configuring Debug and Sanitizer Options
DESCRIPTION: Sets options for debugging, warnings, and sanitizers including thread, address, and undefined behavior sanitizers.

LANGUAGE: CMake
CODE:
# debug
option(GGML_ALL_WARNINGS           "ggml: enable all compiler warnings"                   ON)
option(GGML_ALL_WARNINGS_3RD_PARTY "ggml: enable all compiler warnings in 3rd party libs" OFF)
option(GGML_GPROF                  "ggml: enable gprof"                                   OFF)

# build
option(GGML_FATAL_WARNINGS    "ggml: enable -Werror flag"    OFF)

# sanitizers
option(GGML_SANITIZE_THREAD    "ggml: enable thread sanitizer"    OFF)
option(GGML_SANITIZE_ADDRESS   "ggml: enable address sanitizer"   OFF)
option(GGML_SANITIZE_UNDEFINED "ggml: enable undefined sanitizer" OFF)

----------------------------------------

TITLE: Configuring Build Targets and Include Directories
DESCRIPTION: Sets up architecture-specific build targets and configures include directories for the project. Handles different Android ABIs and includes necessary header paths.

LANGUAGE: cmake
CODE:
if (${ANDROID_ABI} STREQUAL "arm64-v8a")
    build_library("whisper_v8fp16_va")
elseif (${ANDROID_ABI} STREQUAL "armeabi-v7a")
    build_library("whisper_vfpv4")
endif ()

build_library("whisper") # Default target

include_directories(${WHISPER_LIB_DIR})
include_directories(${WHISPER_LIB_DIR}/src)
include_directories(${WHISPER_LIB_DIR}/include)
include_directories(${WHISPER_LIB_DIR}/ggml/include)
include_directories(${WHISPER_LIB_DIR}/ggml/src)
include_directories(${WHISPER_LIB_DIR}/ggml/src/ggml-cpu)

----------------------------------------

TITLE: GGML Installation and Package Configuration
DESCRIPTION: Configures installation targets, public headers, and CMake package generation. Sets up version information based on git commit data and creates necessary package configuration files.

LANGUAGE: cmake
CODE:
set(GGML_PUBLIC_HEADERS
    include/ggml.h
    include/ggml-cpu.h
    include/ggml-alloc.h
    include/ggml-backend.h
    include/ggml-blas.h
    include/ggml-cann.h
    include/ggml-cpp.h
    include/ggml-cuda.h
    include/ggml-kompute.h
    include/ggml-opt.h
    include/ggml-metal.h
    include/ggml-rpc.h
    include/ggml-sycl.h
    include/ggml-vulkan.h
    include/gguf.h)

----------------------------------------

TITLE: Defining wchess-core Static Library in CMake
DESCRIPTION: Creates a static library target called wchess-core with four source files: WChess.cpp, WChess.h, Chessboard.cpp, and Chessboard.h.

LANGUAGE: cmake
CODE:
add_library(wchess-core STATIC
    WChess.cpp
    WChess.h
    Chessboard.cpp
    Chessboard.h
)

----------------------------------------

TITLE: Adding JSON Library Target in CMake
DESCRIPTION: This snippet adds a header-only 'json_cpp' interface library and sets up its include directories.

LANGUAGE: CMake
CODE:
add_library(json_cpp INTERFACE)
target_include_directories(json_cpp INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

----------------------------------------

TITLE: Configuring Single File WASM Output in CMake
DESCRIPTION: Handles the optional embedding of WASM code into a single JavaScript file. When WHISPER_WASM_SINGLE_FILE is enabled, it sets appropriate flags and copies the output file to the correct destination.

LANGUAGE: cmake
CODE:
unset(EXTRA_FLAGS)

if (WHISPER_WASM_SINGLE_FILE)
    set(EXTRA_FLAGS "-s SINGLE_FILE=1")
    message(STATUS "Embedding WASM inside command.js")

    add_custom_command(
        TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_BINARY_DIR}/bin/libcommand.js
        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/command.wasm/command.js
        )
endif()

----------------------------------------

TITLE: Locating CANN Compiler CMake Directory in CMake
DESCRIPTION: This snippet checks for the existence of the ascendc_kernel_cmake directory in different possible locations within the CANN package. It sets the ASCENDC_CMAKE_DIR variable accordingly.

LANGUAGE: CMake
CODE:
if(EXISTS ${ASCEND_CANN_PACKAGE_PATH}/compiler/tikcpp/ascendc_kernel_cmake)
    set(ASCENDC_CMAKE_DIR ${ASCEND_CANN_PACKAGE_PATH}/compiler/tikcpp/ascendc_kernel_cmake)
elseif(EXISTS ${ASCEND_CANN_PACKAGE_PATH}/ascendc_devkit/tikcpp/samples/cmake)
    set(ASCENDC_CMAKE_DIR ${ASCEND_CANN_PACKAGE_PATH}/ascendc_devkit/tikcpp/samples/cmake)
else()
    message(FATAL_ERROR "ascendc_kernel_cmake does not exist, please check whether the compiler package is installed.")
endif()
include(${ASCENDC_CMAKE_DIR}/ascendc.cmake)

----------------------------------------

TITLE: Configuring command.wasm Target in CMake
DESCRIPTION: Sets up the command.wasm target and copies necessary web interface files (HTML and JavaScript) to the output directory using the configure_file command.

LANGUAGE: cmake
CODE:
set(TARGET command.wasm)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/index-tmpl.html  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/index.html @ONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/../helpers.js    ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/helpers.js @ONLY)

----------------------------------------

TITLE: Finding Thread Dependencies in CMake
DESCRIPTION: This snippet finds and includes the Threads package which is required for the whisper.cpp project.

LANGUAGE: CMake
CODE:
find_package(Threads REQUIRED)

----------------------------------------

TITLE: Configuring IBM s390x Architecture Optimizations in CMake for GGML
DESCRIPTION: This snippet detects IBM s390x processors and configures appropriate compiler flags. It reads the system information to identify the machine type (z15, z16) and sets specific optimization flags based on the detected processor model, including vector extension support.

LANGUAGE: CMake
CODE:
elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "s390x")
    message(STATUS "s390x detected")
    file(READ "/proc/cpuinfo" CPUINFO_CONTENTS)
    string(REGEX REPLACE "machine[ \t\r\n]*=[ \t\r\n]*([0-9]+)" "\\1" S390X_M ${CPUINFO_CONTENTS})

    # TODO: Separation to determine activation of VX/VXE/VXE2
    if (${S390X_M} MATCHES "8561|8562")
        message(STATUS "z15 target")
        list(APPEND ARCH_FLAGS -march=z15 -mtune=z15)
    elseif (${S390X_M} MATCHES "3931")
        message(STATUS "z16 target")
        list(APPEND ARCH_FLAGS -march=z16 -mtune=z16)
    else()
        message(STATUS "Unknown target")
        message(WARNING "Unknown target. If you are compiling for z14 and earlier, you might have to add -DGGML_VXE=OFF.")
        list(APPEND ARCH_FLAGS -march=native -mtune=native)
    endif()

    if (GGML_VXE)
        list(APPEND ARCH_FLAGS -mvx -mzvector)
    endif()

----------------------------------------

TITLE: Updating Windows DLL for Whisper.cpp Java Bindings
DESCRIPTION: This Windows command copies the updated whisper.dll file to the appropriate location in the Java project's resources directory for Windows x86-64 platforms.

LANGUAGE: bash
CODE:
copy /y ..\..\build\bin\Release\whisper.dll build\generated\resources\main\win32-x86-64\whisper.dll

----------------------------------------

TITLE: Configuring Core Library and Platform-Specific Targets in CMake
DESCRIPTION: This CMake snippet sets up the wchess project build. It adds the core library subdirectory, sets its folder property, and then conditionally includes either a WebAssembly or command-line target based on whether Emscripten is being used.

LANGUAGE: CMake
CODE:
add_subdirectory(libwchess)
set_target_properties(wchess-core PROPERTIES FOLDER "libs")

if (EMSCRIPTEN)
    add_subdirectory(wchess.wasm)
    set_target_properties(wchess.wasm PROPERTIES FOLDER "libs")
else()
    add_subdirectory(wchess.cmd)
    set_target_properties(wchess PROPERTIES FOLDER "libs")
endif()

----------------------------------------

TITLE: Configuring WebAssembly Chess Target in CMake
DESCRIPTION: Sets up the main executable target for the WebAssembly chess application, including source files and linked libraries. It also configures compilation flags and post-build steps for file management.

LANGUAGE: CMake
CODE:
set(TARGET wchess.wasm)

add_executable(${TARGET}
    wchess.wasm.cpp
    )

include(DefaultTargetOptions)

target_link_libraries(${TARGET} PRIVATE
    common
    wchess-core
    )

unset(EXTRA_FLAGS)

if (WHISPER_WASM_SINGLE_FILE)
    set(EXTRA_FLAGS "-s SINGLE_FILE=1")
    message(STATUS "Embedding WASM inside chess.js")

    add_custom_command(
        TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_BINARY_DIR}/bin/${TARGET}.js
        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/js/chess.js
        )
endif()

set_target_properties(${TARGET} PROPERTIES LINK_FLAGS " \
    --bind \
    -s USE_PTHREADS=1 \
    -s PTHREAD_POOL_SIZE=8 \
    -s INITIAL_MEMORY=1024MB \
    -s TOTAL_MEMORY=1024MB \
    -s FORCE_FILESYSTEM=1 \
    -s EXPORTED_RUNTIME_METHODS=\"['print', 'printErr', 'ccall', 'cwrap']\" \
    ${EXTRA_FLAGS} \
    ")


add_custom_command(
        TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
        ${CMAKE_CURRENT_SOURCE_DIR}/chessboardjs-1.0.0
        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/
        COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_CURRENT_SOURCE_DIR}/jquery-3.7.1.min.js
        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/js/
    )

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/index-tmpl.html  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/index.html @ONLY)
configure_file(${CMAKE_SOURCE_DIR}/examples/helpers.js    ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/js/helpers.js @ONLY)

----------------------------------------

TITLE: Setting MUSA Path and Compilers in CMake
DESCRIPTION: Determines the MUSA installation path and sets the C and C++ compilers to use MUSA's clang. It also appends the MUSA cmake modules path.

LANGUAGE: CMake
CODE:
if (NOT EXISTS $ENV{MUSA_PATH})
    if (NOT EXISTS /opt/musa)
        set(MUSA_PATH /usr/local/musa)
    else()
        set(MUSA_PATH /opt/musa)
    endif()
else()
    set(MUSA_PATH $ENV{MUSA_PATH})
endif()

set(CMAKE_C_COMPILER "${MUSA_PATH}/bin/clang")
set(CMAKE_C_EXTENSIONS OFF)
set(CMAKE_CXX_COMPILER "${MUSA_PATH}/bin/clang++")
set(CMAKE_CXX_EXTENSIONS OFF)

list(APPEND CMAKE_MODULE_PATH "${MUSA_PATH}/cmake")

find_package(MUSAToolkit)

----------------------------------------

TITLE: Configuring KleidiAI Integration for ARM Acceleration in CMake for GGML
DESCRIPTION: This snippet sets up KleidiAI integration for ARM architecture acceleration. It fetches the KleidiAI library from GitHub, configures include paths, and selectively includes optimized kernels based on the available ARM instruction set extensions like dotprod, i8mm, and SME.

LANGUAGE: CMake
CODE:
if (GGML_CPU_AARCH64)
    target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_CPU_AARCH64)
endif()

if (GGML_CPU_KLEIDIAI)
    message(STATUS "Using KleidiAI optimized kernels if applicable")

    # Disable the KleidiAI tests
    set(KLEIDIAI_BUILD_TESTS  OFF)

    # Fetch KleidiAI sources:
    include(FetchContent)
    set(KLEIDIAI_COMMIT_TAG "v1.5.0")
    set(KLEIDIAI_DOWNLOAD_URL "https://github.com/ARM-software/kleidiai/archive/refs/tags/${KLEIDIAI_COMMIT_TAG}.tar.gz")
    set(KLEIDIAI_ARCHIVE_MD5  "ea22e1aefb800e9bc8c74d91633cc58e")

    if (POLICY CMP0135)
        cmake_policy(SET CMP0135 NEW)
    endif()

    FetchContent_Declare(KleidiAI_Download
        URL ${KLEIDIAI_DOWNLOAD_URL}
        DOWNLOAD_EXTRACT_TIMESTAMP NEW
        URL_HASH MD5=${KLEIDIAI_ARCHIVE_MD5})

    FetchContent_MakeAvailable(KleidiAI_Download)
    FetchContent_GetProperties(KleidiAI_Download
        SOURCE_DIR  KLEIDIAI_SRC
        POPULATED   KLEIDIAI_POPULATED)

    if (NOT KLEIDIAI_POPULATED)
        message(FATAL_ERROR "KleidiAI source downloaded failed.")
    endif()

    add_compile_definitions(GGML_USE_CPU_KLEIDIAI)

    # Remove kleidiai target after fetching it
    if (TARGET kleidiai)
        set_target_properties(kleidiai PROPERTIES EXCLUDE_FROM_ALL TRUE)
    endif()

    list(APPEND GGML_CPU_SOURCES
        ggml-cpu/kleidiai/kleidiai.cpp
        ggml-cpu/kleidiai/kernels.cpp
        ggml-cpu/kleidiai/kleidiai.h
        ggml-cpu/kleidiai/kernels.h
        )

    # KleidiAI
    include_directories(
        ${KLEIDIAI_SRC}/
        ${KLEIDIAI_SRC}/kai/
        ${KLEIDIAI_SRC}/kai/ukernels/
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/)

    set(ARCH_FLAGS_TEMP "${ARCH_FLAGS}")
    if (NOT ARCH_FLAGS_TEMP)
        string(REGEX MATCH "-march=[^ ]+" ARCH_FLAGS_TEMP "${CMAKE_C_FLAGS}")
    endif()
    string(FIND "${ARCH_FLAGS_TEMP}" "+dotprod" DOTPROD_ENABLED)
    string(FIND "${ARCH_FLAGS_TEMP}" "+i8mm" I8MM_ENABLED)
    string(FIND "${ARCH_FLAGS_TEMP}" "+sme" SME_ENABLED)

    set(PRIVATE_ARCH_FLAGS ${ARCH_FLAGS})

    list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_lhs_quant_pack_qsi8d32p_f32.c)
    list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_rhs_pack_nxk_qsi4c32ps1s0scalef16_qsu4c32s16s0_neon.c)
    list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_lhs_quant_pack_qsi8d32p_f32_neon.c)
    list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_rhs_pack_nxk_qsi4c32pscalef16_qsu4c32s16s0.c)

    if (NOT DOTPROD_ENABLED MATCHES -1)
        list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p1x8_qsi4c32p4x8_1x4x32_neon_dotprod.c)
        list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p1x4_qsi4c32p4x4_1x4_neon_dotprod.c)
        list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p4x4_qsi4c32p4x4_16x4_neon_dotprod.c)
    endif()

    if (NOT I8MM_ENABLED MATCHES -1)
        list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p4x8_qsi4c32p4x8_16x4_neon_i8mm.c)
    endif()

    if (NOT SME_ENABLED MATCHES -1)
        list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p1vlx4_qsi4c32p4vlx4_1vlx4vl_sme2_mopa.c)
    endif()

----------------------------------------

TITLE: Stream WASM Resource Configuration
DESCRIPTION: Configures the stream.wasm target and sets up file copying for HTML template and helper JavaScript files.

LANGUAGE: cmake
CODE:
set(TARGET stream.wasm)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/index-tmpl.html  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/index.html @ONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/../helpers.js    ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/helpers.js @ONLY)

----------------------------------------

TITLE: Linking Dependencies to wchess-core in CMake
DESCRIPTION: Links the wchess-core library with the whisper and common libraries as PUBLIC dependencies, making them available to targets that link with wchess-core.

LANGUAGE: cmake
CODE:
target_link_libraries(wchess-core
    PUBLIC
    whisper
    common
)

----------------------------------------

TITLE: Setting Include Directories for wchess-core in CMake
DESCRIPTION: Configures the include directories for the wchess-core library, making the current source directory available to targets that use this library.

LANGUAGE: cmake
CODE:
target_include_directories(wchess-core
    PUBLIC
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>"
)

----------------------------------------

TITLE: Installing Metal Shader Files in CMake
DESCRIPTION: Configures installation rules for Metal shader files when not embedding the Metal library, ensuring they're available at the installation location.

LANGUAGE: CMake
CODE:
if (NOT GGML_METAL_EMBED_LIBRARY)
    install(
        FILES src/ggml-metal/ggml-metal.metal
        PERMISSIONS
            OWNER_READ
            OWNER_WRITE
            GROUP_READ
            WORLD_READ
        DESTINATION ${CMAKE_INSTALL_BINDIR})

        install(
            FILES ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/default.metallib
            DESTINATION ${CMAKE_INSTALL_BINDIR}
        )
endif()

----------------------------------------

TITLE: WASM Single File Configuration
DESCRIPTION: Configures optional single-file WASM build mode and sets up post-build file copying.

LANGUAGE: cmake
CODE:
unset(EXTRA_FLAGS)

if (WHISPER_WASM_SINGLE_FILE)
    set(EXTRA_FLAGS "-s SINGLE_FILE=1")
    message(STATUS "Embedding WASM inside stream.js")

    add_custom_command(
        TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_BINARY_DIR}/bin/libstream.js
        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/stream.wasm/stream.js
        )
endif()

----------------------------------------

TITLE: Configuring the bench.wasm Web Interface
DESCRIPTION: Sets up the bench.wasm target and copies template HTML and helper JavaScript files to the runtime output directory. These files provide the web interface for the WebAssembly benchmark tool.

LANGUAGE: cmake
CODE:
set(TARGET bench.wasm)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/index-tmpl.html  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/index.html @ONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/../helpers.js    ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${TARGET}/helpers.js @ONLY)

----------------------------------------

TITLE: Python Package Dependencies
DESCRIPTION: Lists the required Python packages needed to work with whisper.cpp, including PyTorch, Core ML Tools, OpenAI Whisper, and ANE Transformers for Apple Neural Engine support.

LANGUAGE: plaintext
CODE:
torch
coremltools
openai-whisper
ane_transformers