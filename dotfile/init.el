(require 'package)
(add-to-list 'package-archives
             '("marmalade" . "http://marmalade-repo.org/packages/") t)
(add-to-list 'package-archives
             '("melpa" . "http://melpa.milkbox.net/packages/") t)
(add-to-list 'load-path "~/.emacs.d/wangdian")
(package-initialize)
(when (not package-archive-contents)
  (package-refresh-contents))
;; Add in your own as you wish:
(defvar my-packages '(starter-kit
                      smart-operator
                      starter-kit-lisp
                      starter-kit-bindings
                      auto-complete
                      autopair
                      google-translate
                      go-mode
                      auctex
                      python-mode
                      yasnippet)
  "A list of packages to ensure are installed at launch.")

(dolist (p my-packages)
  (when (not (package-installed-p p))
    (package-install p)))
(server-start)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(blink-cursor-mode nil)
 '(custom-enabled-themes (quote (manoj-dark)))
 '(font-use-system-font t)
 '(next-screen-context-lines 0)
 '(show-paren-mode t)
 '(tool-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "DejaVu Sans Mono" :foundry "unknown" :slant normal :weight normal :height 240 :width normal))))
 '(mode-line ((t (:background "black" :foreground "Blue" :box 1 :height 0.9))))
 '(mode-line-buffer-id ((t (:background "black" :foreground "red" :weight bold :height 0.9)))))
(setq visible-bell nil)
(setq kill-ring-max 200)
(setq enable-recursive-minibuffers t)
(setq whitespace-style '(tabs trailing))
(setq confirm-kill-emacs 'yes-or-no-p)
(setq hippie-expand-try-functions-list
      '(
        yas/hippie-try-expand
        try-expand-dabbrev-visible
        try-expand-dabbrev
        try-expand-dabbrev-all-buffers
        try-expand-dabbrev-from-kill
        try-complete-file-name-partially
        try-complete-file-name
        try-expand-all-abbrevs
        try-expand-list
        try-expand-line
        try-complete-lisp-symbol-partially
        try-complete-lisp-symbol))
(global-set-key (kbd "C-;") 'comment-or-uncomment-region)
;;windows resizing
(global-set-key "\M-\C-]" 'enlarge-window-horizontally)
(global-set-key "\M-\C-[" 'shrink-window-horizontally)
(global-set-key (kbd "C-M-^") 'enlarge-window)
(global-set-key (kbd "C-x r i") 'string-insert-rectangle)
(global-set-key (kbd "C-c c") 'revert-buffer-with-coding-system )
;;windows operations
(global-set-key (kbd "ESC 4")
                (lambda ()
                  (interactive)
                  (kill-buffer)))
(global-set-key (kbd "ESC 1") 'delete-other-windows)
(global-set-key (kbd "ESC o") 'other-window)
;;toggle fullscreen
(defun toggle-fullscreen (&optional f)
  (interactive)
  (let ((current-value (frame-parameter nil 'fullscreen)))
    (set-frame-parameter nil 'fullscreen
             (if (equal 'fullboth current-value)
                 (if (boundp 'old-fullscreen) old-fullscreen nil)
               (progn (setq old-fullscreen current-value)
                  'fullboth)))))
(global-set-key [f11] 'toggle-fullscreen)
(global-set-key [f12] 'toggle-truncate-lines)
(global-set-key [(meta left)] 'backward-sexp)
(global-set-key [(meta right)] 'forward-sexp)
;;open disabled functions
(put 'narrow-to-region 'disabled nil)
(put 'upcase-region 'disabled nil)
(put 'downcase-region 'disabled nil)
;;macros
(global-set-key (kbd "C-0") 'kmacro-end-and-call-macro)
(global-set-key (kbd "M-8") 'kmacro-start-macro)
(global-set-key (kbd "M-9") 'kmacro-end-macro)
;;macro crations: variables with "," ahead are replace by
(defmacro m-this-or-that
  (func-name cmd-this cmd-that)
  `(defun ,func-name ()
     (interactive)
     (if mark-active
         (call-interactively ,cmd-this)
       (call-interactively ,cmd-that))))
(global-set-key "\C-w"
                'kill-word-or-region-backward)
(m-this-or-that
 kill-word-or-region-backward
 'kill-region
 'backward-kill-word)
(require 'iswitchb)
(require 'python-mode)
(require 'pony-mode)
;; (load "/home/wangdian/Downloads/nxhtml/autostart.el")
;; (require 'smart-operator)
(add-hook 'iswitchb-make-buflist-hook 'iswitchb-summaries-to-end)
(defun quick-tri-sansw3m ()
  "switch between three buffers"
  (interactive)
  (iswitchb-make-buflist nil)
  (if (or (string-match "\\*w3m\\*"
                        (buffer-name (current-buffer)))
          (string-match "\\*w3m\\*"
                        (buffer-name (other-buffer))))
      (dolist (elem (cdr iswitchb-buflist))
        (unless (string-match "\\*w3m\\*" elem)
          (switch-to-buffer elem)
          (return)))
    (switch-to-buffer (nth 1 iswitchb-buflist))))
(defun quick-bi-sansw3m ()
  "switch between buffers, except w3m buffers"
  (interactive)
  (iswitchb-make-buflist nil)
  (if (and (string-match "\\*w3m\\*"
                         (buffer-name (current-buffer)))
           (string-match "\\*w3m\\*"
                         (buffer-name (other-buffer))))
      (dolist (elem iswitchb-buflist)
        (unless (string-match "\\*w3m\\*" elem)
          (switch-to-buffer elem)
          (return)))
    (switch-to-buffer nil)))
(global-set-key (kbd "ESC 2") 'quick-bi-sansw3m)
(global-set-key (kbd "ESC 3") 'quick-tri-sansw3m)
(global-set-key (kbd "C-x f") 'find-file-at-point)
(global-set-key (kbd "ESC n")
        (lambda ()
          (interactive)
          (scroll-up 1)))
(global-set-key (kbd "ESC p")
        (lambda ()
          (interactive)
          (scroll-down 1)))
(global-set-key (kbd "ESC 5")
        (lambda ()
          (interactive)
          (kill-new (buffer-file-name (current-buffer)))
          (message  (buffer-file-name (current-buffer)))))
(fset 'yes-or-no-p 'y-or-n-p)
;;files backup
(setq make-backup-files t
      version-control t
      delete-old-versions t
      kept-new-versions 6
      kept-old-versions 2
      dired-kept-versions 1
      ;;      backup-directory-alist '(("." . "~/backup-dirs"))
      backup-by-copying t)
;;tab issues
(setq tab-width 4)
(setq-default indent-tabs-mode nil)
;;;;auto completion start
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "~/.emacs.d/ac-dict")
(ac-config-default)
(add-hook 'python-mode-hook
          '(lambda ()
             (local-set-key [(control tab)] 'completion-at-point)
             ;; (local-set-key "tab" 'completion-at-point)
             ))
(add-hook 'shell-mode-hook
          '(lambda ()
             (local-unset-key (kbd "ESC RET"))
             (local-set-key " " 'comint-magic-space)
             (local-set-key [(control f5)] 'shell-resync-dirs)))
(add-hook 'eshell-mode-hook
          '(lambda ()
             (local-set-key " " 'comint-magic-space)))
(defun spcorstrollup (&optional n)
  "selfinsert SPACE or scroll up"
  (interactive "p")
  (if buffer-read-only
      (scroll-up-command)
    (self-insert-command (or n 1))))
(add-hook 'text-mode-hook
          '(lambda ()
             ;; (ispell-change-dictionary "american" t)
             (local-set-key (kbd "SPC") 'spcorstrollup)))
(remove-hook 'text-mode-hook 'turn-on-auto-fill)
(remove-hook 'text-mode-hook 'turn-on-flyspell)
(add-hook 'before-save-hook 'delete-trailing-whitespace)
(setq default-major-mode 'text-mode)
(mapcar
 (lambda (setting)
   (setq auto-mode-alist
         (cons setting auto-mode-alist)))
   '(("\\.[Ff]90$" . f90-mode)
   ("\\.h\\'" . c-mode)
   ("\\.bash_aliases$" . sh-mode)
   ("[Mm]akefile"  . makefile-mode)))
;;;;yasnippet start
(yas-global-mode 1)
;;;;pymacs start
;; (require 'pymacs)
;; (autoload 'pymacs-apply "pymacs")
;; (autoload 'pymacs-call "pymacs")
;; (autoload 'pymacs-eval "pymacs" nil t)
;; (autoload 'pymacs-exec "pymacs" nil t)
;; (autoload 'pymacs-load "pymacs" nil t)
;; (autoload 'pymacs-autoload "pymacs")
;;;;rope start: no need right now
;; (setq ropemacs-enable-shortcuts nil)
;; (setq ropemacs-local-prefix "C-c C-p")
;; (setq ropemacs-enable-autoimport 't)
;; (setq ropemacs-autoimport-modules '("os" "socket"))
;; (pymacs-load "ropemacs" "rope-")
;;;; auctex start:
(add-hook 'LaTeX-mode-hook
          (lambda ()
            (setq TeX-auto-untabify t
                  TeX-engine 'xetex
                  TeX-show-compilation t)
            (TeX-global-PDF-mode t)
            (setq TeX-save-query nil)
            (setq TeX-view-program-list (quote (("xpdf" "xpdf %o"))))
            (setq TeX-view-program-selection (quote ((output-pdf "xpdf"))))
            (setq TeX-engine (quote xetex))
            (add-to-list 'TeX-command-list
                         '("XeLaTeX" "%`%l%(mode)%' %t" TeX-run-command t t :help "Run xelatex"))
            (turn-off-auto-fill)
            (LaTeX-math-mode)
            (turn-on-reftex)
            (linum-mode)
            (imenu-add-menubar-index)
            (setq TeX-command-default "XeLaTeX")
            (define-key LaTeX-mode-map
              (kbd "TAB") 'TeX-complete-symbol)))
(require 'lyric-mode)
(load "kidsdcvtobuffer")
(load "searchandvoice")
(global-set-key (kbd "C-c d") 'kid-sdcv-to-buffer)
;;search and pronounce
(global-set-key (kbd "C-c v") 'search-voice)
;;(require 'w3m-load)
;;;;experiment start
;;(require 'ipython)
;; (setq interpreter-mode-alist(cons '("python" . python-mode)
;;                              interpreter-mode-alist))
;; (setq py-python-command "python")
;; (autoload 'python-mode "python-mode" "Python editing mode." t)
;; (setq pymacs-python-command py-python-command)
;;(require 'pycomplete)
;; ("\\.py$" . python-mode)
;;;; experiment  end
;; (shell-quote-argument "foo > bar")
;;      => "foo\\ \\>\\ bar"
;;;;Help
;; c-h l view lossage
;;;;info tips
;;info menu in $PREFIX/info/dir
;; p previous node
;; l old node
;; r return from old node
;; u upper node
;; i idex topics
;;;;coding,details for c-h a coding
;;c-x return f/r
;;;;abbrev-mode
;;m-x abbrev-mode #auto expand for c-x a e
;;c-m f
;;c-x a e
;;c-m b
;;;;chmod root permission
;;e /sudo::/boot/grub/menu.list
;;;;regular expression
;;M-x replace-regexp \[[0-9:.]+\]$  ~~  [02:15:51.393]
;;egrep option 'regexp' file1 file2
;;-i ingore cases
;;[0-9A-Z_!.?] [^w] ^w
;;()多选结构 ()|() {n,m} range n-m
;;regrx is greedy. --.*?---  sometimes not greedy(grep -P)
;;;;search and replace
;; replace-
;; isearch-forward
;;;;bookmarks
;;c-x r m add a new item
;;c-x r b jump to some item
;; M-x list-bookmarks
;;;;calc
;;;;conditionals ref: info elisp 10.2
;; (when CONDITION A B C)   equivalent to (if CONDITION (progn A B C) nil)
;; (unless CONDITION A B C) equivalent to (if CONDITION nil A B C)
;;
;;;;view-mode c-x c-q toggle between read-only and not
;;python ide key-bindings
;;;; M-;<c-c #> comment,
;;gdb tips
;;file (some.f90) | break (line #) | print (variable) | run | continue
;;c-u M-! cmd insert output at point
;;emacs -batch -f batch-byte-compile filename.el
;; (setq browse-url-default-browser 'w3m-browse-url)
(add-to-list 'load-path (expand-file-name "/opt/sage/local/share/emacs"))
(require 'sage "sage")
(setq sage-command "/opt/sage/sage")
(require 'sage-view "sage-view")
(add-hook 'sage-startup-hook 'sage-view
          'auto-complete-mode)
;; You can use commands like
;; (add-hook 'sage-startup-hook 'sage-view
;; 'sage-view-disable-inline-output 'sage-view-disable-inline-plots)
;; to have some combination of features.  In future, the customize interface
;; will make this simpler... hint, hint!
(global-unset-key (kbd "C-\\"))
(desktop-save-mode t)
(desktop-load-default)
